# usage: python3 haw_rig.py thomas_hawthorne.glb flat.glb HAWTHORNE_rigged.glb  (then base64 it into data/hawMirror.js)
# Thomas Hawthorne for the Sevirrus cutscene page: flatten his node tree (bake each part's offset into its vertices), scale him
# to 1.9 m like the cast, then give him the same 18-bone armature Sevirrus has (rig_glb.py's weighting, with his own joints).
import json, struct, re, sys, numpy as np, importlib.util
spec = importlib.util.spec_from_file_location('rg', __import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), 'rig_glb.py')); rg = importlib.util.module_from_spec(spec); spec.loader.exec_module(rg)
src, mid, dst = sys.argv[1:4]
b = open(src, 'rb').read(); jl = struct.unpack('<I', b[12:16])[0]; J = json.loads(b[20:20 + jl]); o = 20 + jl; bl = struct.unpack('<I', b[o:o + 4])[0]; BIN = bytearray(b[o + 8:o + 8 + bl])
K = 1.9 / 4.18
N = J['nodes']; meshNodes = []
def pos(acc):
    a = J['accessors'][acc]; bv = J['bufferViews'][a['bufferView']]; off = bv.get('byteOffset', 0) + a.get('byteOffset', 0)
    return np.frombuffer(bytes(BIN), dtype='<f4', count=a['count'] * 3, offset=off).reshape(-1, 3).astype(np.float64)
def walk(i, T, S):
    n = N[i]; t = np.array(n.get('translation', [0, 0, 0]), float); s = np.array(n.get('scale', [1, 1, 1]), float); T2 = T + S * t; S2 = S * s
    if 'mesh' in n: meshNodes.append((i, T2, S2))
    for c in n.get('children', []): walk(c, T2, S2)
walk(0, np.zeros(3), np.ones(3))
newMeshes = []
for i, T, S in meshNodes:
    m = json.loads(json.dumps(J['meshes'][N[i]['mesh']]))
    for p in m['primitives']:
        v = ((pos(p['attributes']['POSITION']) * S + T) * K).astype('<f4')
        while len(BIN) % 4: BIN.append(0)
        off = len(BIN); BIN.extend(v.tobytes()); J['bufferViews'].append({'buffer': 0, 'byteOffset': off, 'byteLength': v.nbytes, 'target': 34962})
        J['accessors'].append({'bufferView': len(J['bufferViews']) - 1, 'componentType': 5126, 'count': len(v), 'type': 'VEC3', 'min': v.min(0).tolist(), 'max': v.max(0).tolist()})
        p['attributes']['POSITION'] = len(J['accessors']) - 1
    J['meshes'].append(m); N[i]['mesh'] = len(J['meshes']) - 1
    for k in ('translation', 'scale', 'rotation'): N[i].pop(k, None)
for n in N: n.pop('children', None)
N[0]['children'] = [i for i, _, _ in meshNodes]
while len(BIN) % 4: BIN.append(0)
J['buffers'][0]['byteLength'] = len(BIN)
js = json.dumps(J, separators=(',', ':')).encode()
while len(js) % 4: js += b' '
open(mid, 'wb').write(struct.pack('<4sII', b'glTF', 2, 28 + len(js) + len(BIN)) + struct.pack('<I4s', len(js), b'JSON') + js + struct.pack('<I4s', len(BIN), b'BIN\x00') + bytes(BIN))
P = lambda x, y, z: tuple(np.round(np.array([x, y, z]) * K, 4))
rg.BONES = [
    ('Hips', None, P(0, 1.95, 0)), ('Spine', 'Hips', P(0, 2.1, 0)), ('Neck', 'Spine', P(0, 2.95, 0)), ('Head', 'Neck', P(0, 3.1, 0)),
    ('Eye_L', 'Head', None), ('Eye_R', 'Head', None),
    ('UpperArm_L', 'Spine', P(.55, 2.88, 0)), ('LowerArm_L', 'UpperArm_L', P(.68, 2.32, 0)), ('Hand_L', 'LowerArm_L', P(.70, 1.78, .03)),
    ('UpperArm_R', 'Spine', P(-.55, 2.88, 0)), ('LowerArm_R', 'UpperArm_R', P(-.68, 2.32, 0)), ('Hand_R', 'LowerArm_R', P(-.70, 1.78, .03)),
    ('UpperLeg_L', 'Hips', P(.26, 1.85, 0)), ('LowerLeg_L', 'UpperLeg_L', P(.28, 1.01, 0)), ('Foot_L', 'LowerLeg_L', P(.30, .30, 0)),
    ('UpperLeg_R', 'Hips', P(-.26, 1.85, 0)), ('LowerLeg_R', 'UpperLeg_R', P(-.28, 1.01, 0)), ('Foot_R', 'LowerLeg_R', P(-.30, .30, 0))]
geo = {}  # each part's centre, for the parts named by where they are
mb = open(mid, 'rb').read(); mjl = struct.unpack('<I', mb[12:16])[0]; MJ = json.loads(mb[20:20 + mjl]); mo = 20 + mjl; MBIN = mb[mo + 8:]
for n in MJ['nodes']:
    if 'mesh' in n:
        a = MJ['accessors'][MJ['meshes'][n['mesh']]['primitives'][0]['attributes']['POSITION']]; geo[n['name']] = (np.array(a['min']) + np.array(a['max'])) / 2
old = rg.bone_for
def bone_for(name, cx):
    s = 'L' if cx >= 0 else 'R'
    if re.match(r'^(Hair|Beard|Moustache|Cheek scar|Communications|Earpiece|Comms boom|Microphone)', name): return 'Head'
    if re.match(r'^(Bracer|Wrist|Elbow flex rib|L lowerArm cuff|R lowerArm cuff)', name): return 'LowerArm_' + s
    if re.match(r'^Bicep', name): return 'UpperArm_' + s
    if re.match(r'^Knuckle', name): return 'Hand_' + s
    if re.match(r'^Knee', name): return 'LowerLeg_' + s
    if re.match(r'^(Boot toe|Boot tread)', name): return 'Foot_' + s
    if re.match(r'^(Belt|Pouch|Utility belt)', name): return 'Hips'
    if re.match(r'^Armour fastener', name):
        c = geo.get(name, np.zeros(3)) / K; x, y = abs(c[0]), c[1]
        if y < 1.9: return ('UpperLeg_' if y > 1.0 else 'LowerLeg_') + s
        if x > .6: return ('UpperArm_' if y > 2.32 else 'LowerArm_') + s
        return 'Spine'
    return old(name, cx)
rg.bone_for = bone_for
rg.main(mid, dst)
