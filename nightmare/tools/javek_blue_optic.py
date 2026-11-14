"""Ancient Javek: his optical sensor glows blue instead of red (the knee and boot lights keep their red).
usage: python3 javek_blue_optic.py JAVEK_Rigged.glb out.glb"""
import sys, json, struct, numpy as np
CT={5121:np.uint8,5123:np.uint16,5125:np.uint32,5126:np.float32}; NC={'SCALAR':1,'VEC3':3,'VEC4':4}
b=open(sys.argv[1],'rb').read(); jl=struct.unpack('<I',b[12:16])[0]; J=json.loads(b[20:20+jl]); o=20+jl; bl=struct.unpack('<I',b[o:o+4])[0]; BIN=bytearray(b[o+8:o+8+bl])
def acc(i):
    a=J['accessors'][i]; v=J['bufferViews'][a['bufferView']]; n=NC[a['type']]; dt=CT[a['componentType']]
    return np.frombuffer(bytes(BIN),dt,count=a['count']*n,offset=v.get('byteOffset',0)+a.get('byteOffset',0)).reshape(a['count'],n)
def addIdx(arr):
    global BIN
    while len(BIN)%4: BIN.append(0)
    d=arr.astype(np.uint32).tobytes(); J['bufferViews'].append({'buffer':0,'byteOffset':len(BIN),'byteLength':len(d),'target':34963}); BIN+=d
    J['accessors'].append({'bufferView':len(J['bufferViews'])-1,'componentType':5125,'count':len(arr),'type':'SCALAR'}); return len(J['accessors'])-1
M=J['materials']; red=[i for i,m in enumerate(M) if m['name']=='red optical sensor'][0]
P=J['meshes'][0]['primitives']; p=[q for q in P if q['material']==red][0]
X=acc(p['attributes']['POSITION']); T=acc(p['indices']).reshape(-1,3)
eye=(X[T][:,:,1].mean(1)>1.68)&(X[T][:,:,2].mean(1)>.17)  # the big optic on his face, not the small lights on his legs
M.append({'name':'blue optical sensor','pbrMetallicRoughness':{'baseColorFactor':[0.006,0.07,0.32,1],'metallicFactor':0,'roughnessFactor':0.25},'emissiveFactor':[0.06,0.38,1.0]})
p['indices']=addIdx(T[~eye].ravel()); P.append(dict(p, indices=addIdx(T[eye].ravel()), material=len(M)-1))
print('optic triangles', int(eye.sum()), 'left red', int((~eye).sum()))
J['buffers'][0]['byteLength']=len(BIN)
js=json.dumps(J,separators=(',',':')).encode(); js+=b' '*((4-len(js)%4)%4)
while len(BIN)%4: BIN.append(0)
open(sys.argv[2],'wb').write(b'glTF'+struct.pack('<II',2,28+len(js)+len(BIN))+struct.pack('<I4s',len(js),b'JSON')+js+struct.pack('<I4s',len(BIN),b'BIN\x00')+bytes(BIN))
