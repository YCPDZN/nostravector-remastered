"""Gareth Williams (Project BC) in a suit: his black tank top becomes a charcoal suit jacket over a white shirt and a burgundy tie,
his bare upper arms become the jacket's sleeves, his white trousers become the suit's and his white trainers black leather shoes.
Every mesh is named, so the alignment darkening (alOutfit in index.html) darkens his suit and leaves his face, hair and hands alone.
Usage: python3 gareth_suit.py data/chGareth.js data/chGareth.js   (reads the GLB from the data/*.js file, writes it back)"""
import base64, json, struct, re, sys, numpy as np

src = open(sys.argv[1]).read(); b = base64.b64decode(re.search(r'textContent="([^"]+)"', src).group(1))
jl = struct.unpack('<I', b[12:16])[0]; J = json.loads(b[20:20 + jl]); bl = struct.unpack('<I', b[20 + jl:24 + jl])[0]
B = bytearray(b[28 + jl:28 + jl + bl]); N = J['nodes']
assert not any(m.get('name') == 'Suit jacket' for m in J['materials']), 'already suited'

def new_mat(name, rgb, rough=.6, metal=0.):
    J['materials'].append({'name': name, 'pbrMetallicRoughness': {'baseColorFactor': [*rgb, 1], 'roughnessFactor': rough, 'metallicFactor': metal}})
    return len(J['materials']) - 1
JACKET = new_mat('Suit jacket', [.035, .042, .06], .7)      # charcoal navy (linear)
TROUSERS = new_mat('Suit trousers', [.035, .042, .06], .72)
SHIRT = new_mat('Suit shirt', [.82, .83, .85], .8)
TIE = new_mat('Suit tie', [.16, .012, .02], .5)              # burgundy
SHOES = new_mat('Suit shoe leather', [.012, .009, .008], .3, .1)
SOLES = new_mat('Suit shoe sole', [.006, .005, .005], .9)
# skin and face parts keep their colour, but get names (and their own named copies of the material) so the darkening skips them
named_mats = {}
def keep_mat(mi, name):
    if (mi, name) not in named_mats:
        m = json.loads(json.dumps(J['materials'][mi])); m['name'] = name; J['materials'].append(m); named_mats[(mi, name)] = len(J['materials']) - 1
    return named_mats[(mi, name)]

def set_mesh(node, name, mat):
    n = N[node]; n['name'] = name; me = J['meshes'][n['mesh']]; me['name'] = name
    for p in me['primitives']: p['material'] = mat

# the head: everything under it is face, hair or eyes
def under(i):
    out = [i]
    for c in N[i].get('children', []): out += under(c)
    return out
head = next(i for i, n in enumerate(N) if n.get('name') == 'Head')
for i in under(head):
    if 'mesh' in N[i]:
        mi = J['meshes'][N[i]['mesh']]['primitives'][0].get('material', 0)
        nm = 'Face hair' if mi in (1, 2) else 'Face eye' if mi in (3, 4) else 'Face mouth' if mi == 7 else 'Face stubble' if mi == 8 else 'Face skin'
        set_mesh(i, nm, keep_mat(mi, nm))
# arms: upper arms are the sleeves, the lower parts his hands
for arm in ('LeftArm', 'RightArm'):
    a = next(i for i, n in enumerate(N) if n.get('name') == arm); meshes = [i for i in under(a) if 'mesh' in N[i]]
    set_mesh(meshes[0], 'Suit sleeve', JACKET); set_mesh(meshes[1], 'Hand palm', keep_mat(11, 'Hand palm skin'))
# the tank top: body and straps become the jacket, the bare chest at the collar the shirt
top = next(i for i, n in enumerate(N) if n.get('name') == 'Rigged Resistance tank top'); N[top]['name'] = 'Suit'
t = [i for i in under(top) if 'mesh' in N[i]]
set_mesh(t[0], 'Suit jacket body', JACKET); set_mesh(t[1], 'Suit jacket chest', JACKET); set_mesh(t[2], 'Suit shirt collar', SHIRT)
set_mesh(t[3], 'Suit jacket lapel', JACKET); set_mesh(t[4], 'Suit jacket lapel', JACKET)
# legs: trousers, shoes, soles and laces
for leg in ('LeftLeg', 'RightLeg'):
    l = next(i for i, n in enumerate(N) if n.get('name') == leg); m = [i for i in under(l) if 'mesh' in N[i]]
    set_mesh(m[0], 'Suit trousers', TROUSERS); set_mesh(m[1], 'Suit shoe', SHOES)
    for k in m[2:]: set_mesh(k, 'Suit shoe sole', SOLES)

# a tie, and a white shirt front for it to lie on, added under the torso (world -> torso space)
def mat4(n):
    M = np.eye(4); t = n.get('translation', [0, 0, 0]); r = n.get('rotation', [0, 0, 0, 1]); s = n.get('scale', [1, 1, 1]); x, y, z, w = r
    R = np.array([[1 - 2 * (y * y + z * z), 2 * (x * y - z * w), 2 * (x * z + y * w)], [2 * (x * y + z * w), 1 - 2 * (x * x + z * z), 2 * (y * z - x * w)], [2 * (x * z - y * w), 2 * (y * z + x * w), 1 - 2 * (x * x + y * y)]])
    M[:3, :3] = R * np.array(s); M[:3, 3] = t; return M
root = J['scenes'][0]['nodes'][0]; torso = next(i for i, n in enumerate(N) if n.get('name') == 'Torso')
inv = np.linalg.inv(mat4(N[root]) @ mat4(N[torso]))
def add(data, target):
    while len(B) % 4: B.append(0)
    J['bufferViews'].append({'buffer': 0, 'byteOffset': len(B), 'byteLength': len(data), 'target': target}); B.extend(data); return len(J['bufferViews']) - 1
def quad_mesh(name, mat, quads):  # quads: list of 4 world-space corners (counter-clockwise seen from the front), flat-shaded
    P, Nm, I = [], [], []
    for q in quads:
        q = np.array(q, float); w = (inv @ np.c_[q, np.ones(4)].T).T[:, :3]; nrm = np.cross(w[1] - w[0], w[2] - w[0]); nrm /= np.linalg.norm(nrm)
        k = len(P); P += w.tolist(); Nm += [nrm.tolist()] * 4; I += [k, k + 1, k + 2, k, k + 2, k + 3]
    P = np.array(P, np.float32); Nm = np.array(Nm, np.float32); I = np.array(I, np.uint16)
    acc = lambda bv, ct, cnt, ty, **kw: (J['accessors'].append({'bufferView': bv, 'componentType': ct, 'count': cnt, 'type': ty, **kw}), len(J['accessors']) - 1)[1]
    pa = acc(add(P.tobytes(), 34962), 5126, len(P), 'VEC3', min=P.min(0).tolist(), max=P.max(0).tolist())
    na = acc(add(Nm.tobytes(), 34962), 5126, len(Nm), 'VEC3'); ia = acc(add(I.tobytes(), 34963), 5123, len(I), 'SCALAR')
    J['meshes'].append({'name': name, 'primitives': [{'attributes': {'POSITION': pa, 'NORMAL': na}, 'indices': ia, 'material': mat}]})
    N.append({'name': name, 'mesh': len(J['meshes']) - 1}); N[torso].setdefault('children', []).append(len(N) - 1)
def box(x0, x1, y0, y1, z0, z1, taper=1.):  # a slab, its bottom edge narrowed by taper
    xb0, xb1 = (x0 + x1) / 2 + (x0 - x1) / 2 * taper, (x0 + x1) / 2 + (x1 - x0) / 2 * taper
    f = [[xb0, y0, z1], [xb1, y0, z1], [x1, y1, z1], [x0, y1, z1]]; bk = [[xb1, y0, z0], [xb0, y0, z0], [x0, y1, z0], [x1, y1, z0]]
    return [f, bk, [[xb0, y0, z0], [xb0, y0, z1], [x0, y1, z1], [x0, y1, z0]], [[xb1, y0, z1], [xb1, y0, z0], [x1, y1, z0], [x1, y1, z1]],
            [[x0, y1, z1], [x1, y1, z1], [x1, y1, z0], [x0, y1, z0]], [[xb0, y0, z0], [xb1, y0, z0], [xb1, y0, z1], [xb0, y0, z1]]]
# the jacket's chest sits at z ≈ 0.20 in front; the shirt is an open V of white down to the jacket's button line
quad_mesh('Suit shirt front', SHIRT, [[[-.005, 1.20, .203], [.005, 1.20, .203], [.12, 1.60, .195], [-.12, 1.60, .195]]])
quad_mesh('Suit tie', TIE, box(-.032, .032, 1.18, 1.58, .203, .214, taper=1.5) + box(-.04, .04, 1.55, 1.62, .2, .216))

J['buffers'] = [{'byteLength': len(B)}]
js = json.dumps(J, separators=(',', ':')).encode()
while len(js) % 4: js += b' '
while len(B) % 4: B.append(0)
out = struct.pack('<III', 0x46546C67, 2, 12 + 8 + len(js) + 8 + len(B)) + struct.pack('<II', len(js), 0x4E4F534A) + js + struct.pack('<II', len(B), 0x004E4942) + bytes(B)
open(sys.argv[2], 'w').write('document.getElementById("chGareth").textContent="' + base64.b64encode(out).decode() + '";\n'); print('wrote', len(out))
