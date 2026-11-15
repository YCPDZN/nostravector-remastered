# keep only the bufferViews that something still points at (haw_rig.py leaves the original, unscaled positions behind)
import json, struct, sys
src, dst = sys.argv[1:3]
b = open(src, 'rb').read(); jl = struct.unpack('<I', b[12:16])[0]; J = json.loads(b[20:20 + jl]); o = 20 + jl; bl = struct.unpack('<I', b[o:o + 4])[0]; BIN = b[o + 8:o + 8 + bl]
used_acc = set()
def walk(x):
    if isinstance(x, dict):
        for k, v in x.items():
            if k in ('POSITION', 'NORMAL', 'TEXCOORD_0', 'TEXCOORD_1', 'COLOR_0', 'JOINTS_0', 'WEIGHTS_0', 'TANGENT', 'indices', 'inverseBindMatrices', 'input', 'output') and isinstance(v, int): used_acc.add(v)
            else: walk(v)
    elif isinstance(x, list):
        for v in x: walk(v)
for key in ('meshes', 'skins', 'animations'): walk(J.get(key, []))
used_bv = {J['accessors'][a]['bufferView'] for a in used_acc if 'bufferView' in J['accessors'][a]}
for im in J.get('images', []):
    if 'bufferView' in im: used_bv.add(im['bufferView'])
for a in J['accessors']:
    if 'sparse' in a: used_bv |= {a['sparse']['indices']['bufferView'], a['sparse']['values']['bufferView']}
nb = bytearray(); remap = {}
for i, bv in enumerate(J['bufferViews']):
    if i not in used_bv: continue
    while len(nb) % 4: nb.append(0)
    s = bv.get('byteOffset', 0); chunk = BIN[s:s + bv['byteLength']]
    remap[i] = len(remap); bv2 = dict(bv); bv2['byteOffset'] = len(nb); nb.extend(chunk); J['bufferViews'][i] = bv2
J['bufferViews'] = [J['bufferViews'][i] for i in sorted(remap)]
# accessors: drop the unused ones too, renumbering every reference
acc_map = {}; newacc = []
for i, a in enumerate(J['accessors']):
    if i in used_acc: acc_map[i] = len(newacc); a = dict(a); a['bufferView'] = remap[a['bufferView']] if 'bufferView' in a else None; a = {k: v for k, v in a.items() if v is not None}; newacc.append(a)
J['accessors'] = newacc
def fix(x):
    if isinstance(x, dict):
        for k, v in list(x.items()):
            if k in ('POSITION', 'NORMAL', 'TEXCOORD_0', 'TEXCOORD_1', 'COLOR_0', 'JOINTS_0', 'WEIGHTS_0', 'TANGENT', 'indices', 'inverseBindMatrices', 'input', 'output') and isinstance(v, int): x[k] = acc_map[v]
            else: fix(v)
    elif isinstance(x, list):
        for v in x: fix(v)
for key in ('meshes', 'skins', 'animations'): fix(J.get(key, []))
for im in J.get('images', []):
    if 'bufferView' in im: im['bufferView'] = remap[im['bufferView']]
while len(nb) % 4: nb.append(0)
J['buffers'] = [{'byteLength': len(nb)}]
js = json.dumps(J, separators=(',', ':')).encode()
while len(js) % 4: js += b' '
open(dst, 'wb').write(struct.pack('<4sII', b'glTF', 2, 28 + len(js) + len(nb)) + struct.pack('<I4s', len(js), b'JSON') + js + struct.pack('<I4s', len(nb), b'BIN\x00') + bytes(nb))
print(len(b), '->', 28 + len(js) + len(nb), 'bytes;', len(used_acc), 'accessors kept')
