"""Give James Brown (Terra Imperia, cpJamesTI) the Pontifex Maximus's scythe: copies the Pontifex model's 'weapon' subtree
(meshes, materials, geometry) into James's empty 'weapon' node. Both come from the same articulated generator, so it sits in his hand.
usage: python3 james_scythe.py data/cpJamesTI.js pontifex_maximus.glb out.js"""
import sys, json, struct, base64, re
def parse(b): jl = struct.unpack('<I', b[12:16])[0]; J = json.loads(b[20:20 + jl]); o = 20 + jl; bl = struct.unpack('<I', b[o:o + 4])[0]; return J, bytearray(b[o + 8:o + 8 + bl])
src_js = open(sys.argv[1]).read(); A, ABIN = parse(base64.b64decode(re.search(r'textContent="([^"]+)"', src_js).group(1)))
B, BBIN = parse(open(sys.argv[2], 'rb').read())
for k in ('accessors', 'bufferViews', 'materials', 'meshes', 'nodes'): A.setdefault(k, [])
aw = [i for i, n in enumerate(A['nodes']) if n.get('name') == 'weapon'][0]; bw = [i for i, n in enumerate(B['nodes']) if n.get('name') == 'weapon'][0]
assert not A['nodes'][aw].get('children'), 'James already holds something'
bvmap, accmap, matmap, meshmap = {}, {}, {}, {}
def bv(i):
    if i in bvmap: return bvmap[i]
    v = dict(B['bufferViews'][i]); data = BBIN[v.get('byteOffset', 0):v.get('byteOffset', 0) + v['byteLength']]
    while len(ABIN) % 4: ABIN.append(0)
    v['byteOffset'] = len(ABIN); v['buffer'] = 0; ABIN.extend(data); A['bufferViews'].append(v); bvmap[i] = len(A['bufferViews']) - 1; return bvmap[i]
def acc(i):
    if i in accmap: return accmap[i]
    a = dict(B['accessors'][i]); a['bufferView'] = bv(a['bufferView']); A['accessors'].append(a); accmap[i] = len(A['accessors']) - 1; return accmap[i]
def mat(i):
    if i in matmap: return matmap[i]
    A['materials'].append(B['materials'][i]); matmap[i] = len(A['materials']) - 1; return matmap[i]
def mesh(i):
    if i in meshmap: return meshmap[i]
    m = json.loads(json.dumps(B['meshes'][i]))
    for p in m['primitives']:
        p['attributes'] = {k: acc(v) for k, v in p['attributes'].items()}
        if 'indices' in p: p['indices'] = acc(p['indices'])
        if 'material' in p: p['material'] = mat(p['material'])
    A['meshes'].append(m); meshmap[i] = len(A['meshes']) - 1; return meshmap[i]
def node(i):
    n = json.loads(json.dumps(B['nodes'][i])); kids = n.pop('children', [])
    if 'mesh' in n: n['mesh'] = mesh(n['mesh'])
    A['nodes'].append(n); me = len(A['nodes']) - 1; ch = [node(c) for c in kids]
    if ch: A['nodes'][me]['children'] = ch
    return me
A['nodes'][aw]['children'] = [node(c) for c in B['nodes'][bw].get('children', [])]
A['nodes'][aw]['translation'] = B['nodes'][bw].get('translation', A['nodes'][aw].get('translation'))
while len(ABIN) % 4: ABIN.append(0)
A['buffers'] = [{'byteLength': len(ABIN)}]
js = json.dumps(A, separators=(',', ':')).encode(); js += b' ' * ((4 - len(js) % 4) % 4)
glb = b'glTF' + struct.pack('<II', 2, 12 + 8 + len(js) + 8 + len(ABIN)) + struct.pack('<I4s', len(js), b'JSON') + js + struct.pack('<I4s', len(ABIN), b'BIN\x00') + bytes(ABIN)
open(sys.argv[3], 'w').write('document.getElementById("cpJamesTI").textContent="' + base64.b64encode(glb).decode() + '";\n')
print('weapon parts', len(A['nodes'][aw]['children']), 'size', len(glb))
