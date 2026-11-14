"""Croxian Mascar, companion version: his helmet off, Orion's face under it (no beard, no cybernetic eye), Orion's short brushed
hair cut shorter and dyed black. Reads the two GLBs from their data/*.js files and writes the new GLB."""
import base64, json, struct, re, sys, numpy as np
def load(f):
    s = open(f).read(); b = base64.b64decode(re.search(r'textContent="([^"]+)"', s).group(1))
    jl = struct.unpack('<I', b[12:16])[0]; J = json.loads(b[20:20 + jl]); bl = struct.unpack('<I', b[20 + jl:24 + jl])[0]
    return J, bytearray(b[28 + jl:28 + jl + bl])
CJ, CB = load(sys.argv[1]); OJ, OB = load(sys.argv[2])
CN, ON = CJ['nodes'], OJ['nodes']
idx = lambda N, nm: [i for i, n in enumerate(N) if n.get('name') == nm][0]
HELMET = ['Helmet inner shell', 'Helmet cheek -1', 'Helmet cheek 1', 'Cyan eye -1', 'Cyan eye 1', 'Crown fin -1', 'Crown fin 1', 'Helmet circuit -1', 'Helmet circuit 1', 'Centre face shield', 'Mask centre light']
head = idx(CN, 'head'); drop = {idx(CN, n) for n in HELMET}
CN[head]['children'] = [c for c in CN[head]['children'] if c not in drop]
PARTS = ['Face', 'Jaw', 'Nose', 'Hair cap', 'Sideburn -1', 'Sideburn 1', 'Eye white -1', 'Iris -1', 'Pupil -1', 'Eye glint -1', 'Eyebrow -1', 'Eye white 1', 'Iris 1', 'Pupil 1', 'Eye glint 1', 'Eyebrow 1', 'Mouth neutral', 'Ear -1', 'Ear inner -1', 'Ear 1', 'Ear inner 1'] + [f'Short brushed hair {k}' for k in range(7)]
HAIR = lambda nm: nm.startswith('Short brushed hair') or nm.startswith('Sideburn') or nm == 'Hair cap' or nm.startswith('Eyebrow')
def acc_bytes(J, B, ai):
    a = J['accessors'][ai]; v = J['bufferViews'][a['bufferView']]; n = {'SCALAR': 1, 'VEC2': 2, 'VEC3': 3, 'VEC4': 4}[a['type']]
    sz = {5126: 4, 5125: 4, 5123: 2, 5121: 1}[a['componentType']]; off = v.get('byteOffset', 0) + a.get('byteOffset', 0)
    assert 'byteStride' not in v or v['byteStride'] == n * sz
    return a, bytes(B[off:off + a['count'] * n * sz])
def add_acc(a, data, target):
    while len(CB) % 4: CB.append(0)
    CJ['bufferViews'].append({'buffer': 0, 'byteOffset': len(CB), 'byteLength': len(data), **({'target': target} if target else {})}); CB.extend(data)
    na = {k: a[k] for k in ('componentType', 'count', 'type', 'min', 'max', 'normalized') if k in a}; na['bufferView'] = len(CJ['bufferViews']) - 1
    CJ['accessors'].append(na); return len(CJ['accessors']) - 1
mat_map = {}
def mat(oi, hair):
    k = (oi, hair)
    if k not in mat_map:
        m = json.loads(json.dumps(OJ['materials'][oi])); m['name'] = 'Croxian ' + m.get('name', 'part') + (' (black)' if hair else '')
        if hair: m.setdefault('pbrMetallicRoughness', {})['baseColorFactor'] = [0.035, 0.032, 0.03, 1]; m['pbrMetallicRoughness']['roughnessFactor'] = 0.85
        CJ['materials'].append(m); mat_map[k] = len(CJ['materials']) - 1
    return mat_map[k]
new_children = []
for nm in PARTS:
    on = ON[idx(ON, nm)]; me = OJ['meshes'][on['mesh']]; prims = []
    for p in me['primitives']:
        attrs = {}
        for an, ai in p['attributes'].items():
            a, d = acc_bytes(OJ, OB, ai)
            if an == 'POSITION' and nm.startswith('Short brushed hair'): # shorter: pressed down toward the scalp
                v = np.frombuffer(d, np.float32).reshape(-1, 3).copy(); base = 1.80; v[:, 1] = np.where(v[:, 1] > base, base + (v[:, 1] - base) * 0.6, v[:, 1]); v[:, [0, 2]] *= 0.98
                a = dict(a, min=v.min(0).tolist(), max=v.max(0).tolist()); d = v.astype(np.float32).tobytes()
            if an == 'POSITION' and nm.startswith('Sideburn'): # cropped sideburns
                v = np.frombuffer(d, np.float32).reshape(-1, 3).copy(); top = v[:, 1].max(); v[:, 1] = top - (top - v[:, 1]) * 0.55
                a = dict(a, min=v.min(0).tolist(), max=v.max(0).tolist()); d = v.astype(np.float32).tobytes()
            attrs[an] = add_acc(a, d, 34962)
        np_ = {'attributes': attrs, 'mode': p.get('mode', 4)}
        if 'indices' in p: a, d = acc_bytes(OJ, OB, p['indices']); np_['indices'] = add_acc(a, d, 34963)
        if 'material' in p: np_['material'] = mat(p['material'], HAIR(nm))
        prims.append(np_)
    CJ['meshes'].append({'name': 'Croxian ' + nm, 'primitives': prims}); CN.append({'name': 'Croxian ' + nm, 'mesh': len(CJ['meshes']) - 1}); new_children.append(len(CN) - 1)
S = 1.3 # Orion's head, scaled into the space where the helmet was: chin at the neck seal
CN.append({'name': 'Croxian bare head', 'translation': [0, -1.415 * S + 0.02, 0.02], 'scale': [S, S, S], 'children': new_children}); CN[head]['children'].append(len(CN) - 1)
CJ['buffers'] = [{'byteLength': len(CB)}]
js = json.dumps(CJ, separators=(',', ':')).encode()
while len(js) % 4: js += b' '
while len(CB) % 4: CB.append(0)
out = struct.pack('<III', 0x46546C67, 2, 12 + 8 + len(js) + 8 + len(CB)) + struct.pack('<II', len(js), 0x4E4F534A) + js + struct.pack('<II', len(CB), 0x004E4942) + bytes(CB)
open(sys.argv[3], 'wb').write(out); print('wrote', len(out))
