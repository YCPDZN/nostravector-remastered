"""Javek: take out the red optical sensor and the smoked lens (and their glints) and give him green eyes in both goggle rings.
usage: python3 javek_green_eyes.py JAVEK_Rigged.glb out.glb"""
import sys, json, struct, numpy as np
from collections import defaultdict
CT={5120:np.int8,5121:np.uint8,5122:np.int16,5123:np.uint16,5125:np.uint32,5126:np.float32}
NC={'SCALAR':1,'VEC2':2,'VEC3':3,'VEC4':4,'MAT4':16}
b=open(sys.argv[1],'rb').read(); jl=struct.unpack('<I',b[12:16])[0]; J=json.loads(b[20:20+jl]); o=20+jl; bl=struct.unpack('<I',b[o:o+4])[0]; BIN=bytearray(b[o+8:o+8+bl])
def acc(i):
    a=J['accessors'][i]; v=J['bufferViews'][a['bufferView']]; n=NC[a['type']]; dt=CT[a['componentType']]; it=np.dtype(dt).itemsize
    st=v.get('byteStride',0) or n*it; off=v.get('byteOffset',0)+a.get('byteOffset',0)
    raw=np.frombuffer(bytes(BIN),np.uint8,count=st*(a['count']-1)+n*it,offset=off)
    return np.lib.stride_tricks.as_strided(raw,(a['count'],n*it),(st,1)).copy().view(dt).reshape(a['count'],n)
def add(arr,typ,ct,target=None,minmax=False):
    global BIN
    while len(BIN)%4: BIN.append(0)
    data=np.ascontiguousarray(arr).tobytes(); bv={'buffer':0,'byteOffset':len(BIN),'byteLength':len(data)}
    if target: bv['target']=target
    J['bufferViews'].append(bv); BIN+=data
    a={'bufferView':len(J['bufferViews'])-1,'componentType':ct,'count':len(arr),'type':typ}
    if minmax: a['min']=arr.min(0).tolist(); a['max']=arr.max(0).tolist()
    J['accessors'].append(a); return len(J['accessors'])-1
mesh=J['meshes'][0]; P=mesh['primitives']; M=J['materials']
mid={m['name']:i for i,m in enumerate(M)}
def comps(p):
    X=acc(p['attributes']['POSITION']); I=acc(p['indices']).ravel(); n=len(X); par=list(range(n))
    def f(a):
        while par[a]!=a: par[a]=par[par[a]]; a=par[a]
        return a
    for t in I.reshape(-1,3): r=f(t[0]); par[f(t[1])]=r; par[f(t[2])]=f(r)
    seen={}
    for i,q in enumerate(map(tuple,np.round(X,4))):
        if q in seen: par[f(i)]=f(seen[q])
        else: seen[q]=i
    lab=np.array([f(i) for i in range(n)]); return X,I.reshape(-1,3),lab
def drop(p, test):  # remove the connected parts of a primitive whose centre passes test
    X,T,lab=comps(p); gone=set()
    for l in set(lab):
        c=X[lab==l].mean(0)
        if test(c): gone.add(l)
    keep=np.array([lab[t[0]] not in gone for t in T])
    p['indices']=add(T[keep].astype(np.uint32).ravel(),'SCALAR',5125,34963); return X[np.isin(lab,list(gone))]
eyeTest=lambda c: c[1]>1.68 and c[2]>.17
red=[p for p in P if p['material']==mid['red optical sensor']][0]; redV=drop(red,eyeTest)
lens=[p for p in P if p['material']==mid['smoked optical lens']][0]; lensX=acc(lens['attributes']['POSITION']); P.remove(lens)
glint=[p for p in P if p['material']==mid['ivory teeth and glints']][0]; drop(glint, lambda c: c[1]>1.7 and c[2]>.2)
# skin the new eyes like the old lens (its head joint)
J0=acc(red['attributes']['JOINTS_0']); W0=acc(red['attributes']['WEIGHTS_0']); X0=acc(red['attributes']['POSITION'])
k=np.argmin(np.abs(X0-redV.mean(0)).sum(1)); jnt=J0[k]; wt=W0[k]
def mat(name,rgb,emis=None,rough=.35,metal=0.):
    m={'name':name,'pbrMetallicRoughness':{'baseColorFactor':list(rgb)+[1],'metallicFactor':metal,'roughnessFactor':rough}}
    if emis: m['emissiveFactor']=list(emis)
    M.append(m); return len(M)-1
mS=mat('eye white',(.82,.84,.8),rough=.3); mI=mat('green iris',(.03,.42,.08),emis=(.02,.5,.08),rough=.25); mP=mat('pupil',(.004,.006,.005),rough=.2); mG=mat('eye glint',(1,1,1),emis=(1,1,1),rough=.1)
def cap(cx,cy,cz,R,th,scale,nr=10,ns=28,shift=(0,0)):  # front cap of a sphere centred at (cx,cy,cz-R*cos?)
    V=[];N=[];F=[]
    V.append([0,0,1]); 
    for i in range(1,nr+1):
        t=th*i/nr
        for j in range(ns):
            ph=2*np.pi*j/ns; V.append([np.sin(t)*np.cos(ph),np.sin(t)*np.sin(ph),np.cos(t)])
    V=np.array(V)
    # tilt the cap to look a little toward 'shift' (glint placement)
    if shift!=(0,0):
        ax,ay=shift; V=V+np.array([ax,ay,0]); V/=np.linalg.norm(V,axis=1,keepdims=True)
    for j in range(ns): F.append([0,1+j,1+(j+1)%ns])
    for i in range(nr-1):
        for j in range(ns):
            a=1+i*ns+j; b_=1+i*ns+(j+1)%ns; c=a+ns; d=b_+ns; F+= [[a,c,b_],[b_,c,d]]
    Nn=V.copy(); Pp=V*R*scale+np.array([cx,cy,cz])
    return Pp.astype(np.float32),Nn.astype(np.float32),np.array(F,np.uint32)
def prim(Pp,Nn,F,m):
    n=len(Pp); P.append({'attributes':{'POSITION':add(Pp,'VEC3',5126,34962,True),'NORMAL':add(Nn,'VEC3',5126,34962),'JOINTS_0':add(np.tile(jnt,(n,1)).astype(J0.dtype),'VEC4',5123 if J0.dtype==np.uint16 else 5121,34962),'WEIGHTS_0':add(np.tile(wt,(n,1)).astype(np.float32),'VEC4',5126,34962)},'indices':add(F.ravel(),'SCALAR',5125,34963),'material':m})
for V in (redV, lensX):
    lo,hi=V.min(0),V.max(0); c=(lo+hi)/2; r=(hi[0]-lo[0])/2*.97; front=hi[2]
    # an eyeball whose front sits where the lens did: sphere of radius R behind it, showing a cap of half-angle th
    th=np.radians(62); R=r/np.sin(th); cz=front-R
    look=(.0,-.04)  # a touch downward, toward whoever he's talking to
    prim(*cap(c[0],c[1],cz,R,th,1.0),mS)
    prim(*cap(c[0],c[1],cz,R,np.radians(30),1.006,shift=look),mI)
    prim(*cap(c[0],c[1],cz,R,np.radians(13),1.012,shift=look),mP)
    prim(*cap(c[0]-r*.32,c[1]+r*.34,cz,R,np.radians(5),1.018,nr=3,ns=12,shift=(-.38,.4)),mG)
# write
J['buffers'][0]['byteLength']=len(BIN)
js=json.dumps(J,separators=(',',':')).encode(); js+=b' '*((4-len(js)%4)%4)
while len(BIN)%4: BIN.append(0)
out=b'glTF'+struct.pack('<II',2,12+8+len(js)+8+len(BIN))+struct.pack('<I4s',len(js),b'JSON')+js+struct.pack('<I4s',len(BIN),b'BIN\x00')+bytes(BIN)
open(sys.argv[2],'wb').write(out); print('ok',len(out),'joint',jnt,wt)
