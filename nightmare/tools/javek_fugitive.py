"""Javek, the companion: a fugitive. Goggles off, round glasses on over green eyes, black hood and cape.
usage: python3 javek_fugitive.py javek.glb (the green-eyed build from javek_green_eyes.py) out.glb"""
import sys, json, struct, numpy as np
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
mesh=J['meshes'][0]; P=mesh['primitives']; M=J['materials']; mname=lambda p: M[p['material']]['name']
JT=[J['nodes'][j]['name'] for j in J['skins'][0]['joints']]; jid=JT.index
def comps(p):
    X=acc(p['attributes']['POSITION']); I=acc(p['indices']).reshape(-1,3); n=len(X); par=list(range(n))
    def f(a):
        while par[a]!=a: par[a]=par[par[a]]; a=par[a]
        return a
    for t in I: r=f(t[0]); par[f(t[1])]=r; par[f(t[2])]=f(r)
    seen={}
    for i,q in enumerate(map(tuple,np.round(X,4))):
        if q in seen: par[f(i)]=f(seen[q])
        else: seen[q]=i
    return X,I,np.array([f(i) for i in range(n)])
def drop(p,test):
    X,T,lab=comps(p); gone={l for l in set(lab) if test(X[lab==l].mean(0),X[lab==l].max(0)-X[lab==l].min(0),(lab==l).sum())}
    keep=np.array([lab[t[0]] not in gone for t in T]); p['indices']=add(T[keep].astype(np.uint32).ravel(),'SCALAR',5125,34963); return len(gone)
# 1. off with the goggles (and the old green eyes, which were sized to them)
P[:]=[p for p in P if mname(p) not in ('eye white','green iris','pupil','eye glint')]
n=0
for p in P:
    nm=mname(p)
    if nm=='dark structural metal': n+=drop(p,lambda c,s,k: c[1]>1.68 and c[2]>.1)                      # goggle housings
    if nm=='polished metal edges': n+=drop(p,lambda c,s,k: c[1]>1.68 and c[2]>.12)                      # rims and bridge
    if nm=='weathered gunmetal': n+=drop(p,lambda c,s,k: (c[1]>1.62 and c[2]>.14 and k<=60) or (c[1]>1.7 and abs(c[0]+.189)<.02 and abs(c[2])<.03))  # rim bolts, strap buckle
    if nm=='brown leather': n+=drop(p,lambda c,s,k: c[1]>1.7)                                           # goggle strap
print('goggle parts removed',n)
# 2. materials
def mat(name,rgb,emis=None,rough=.4,metal=0.,alpha=None,double=False):
    m={'name':name,'pbrMetallicRoughness':{'baseColorFactor':list(rgb)+[alpha if alpha else 1],'metallicFactor':metal,'roughnessFactor':rough}}
    if emis: m['emissiveFactor']=list(emis)
    if alpha: m['alphaMode']='BLEND'
    if double: m['doubleSided']=True
    M.append(m); return len(M)-1
mS=mat('eye white',(.82,.84,.8),rough=.3); mI=mat('green iris',(.03,.42,.08),emis=(.02,.5,.08),rough=.25); mP=mat('pupil',(.004,.006,.005),rough=.2); mG=mat('eye glint',(1,1,1),emis=(1,1,1),rough=.1)
mF=mat('glasses frame',(.018,.018,.02),rough=.35,metal=.7); mL=mat('glasses lens',(.55,.75,.7),rough=.05,alpha=.16,double=True)
mC=mat('black hood and cape',(.011,.011,.013),rough=.92,double=True)
# 3. geometry helpers
def normals(V,F):
    N=np.zeros_like(V); fn=np.cross(V[F[:,1]]-V[F[:,0]],V[F[:,2]]-V[F[:,0]])
    for k in range(3): np.add.at(N,F[:,k],fn)
    return (N/(np.linalg.norm(N,axis=1,keepdims=True)+1e-12)).astype(np.float32)
def prim(V,F,m,J4,W4,Nn=None):
    V=np.asarray(V,np.float32); F=np.asarray(F,np.uint32); n=len(V)
    P.append({'attributes':{'POSITION':add(V,'VEC3',5126,34962,True),'NORMAL':add(Nn if Nn is not None else normals(V,F),'VEC3',5126,34962),
      'JOINTS_0':add(np.asarray(J4,np.uint16).reshape(n,4),'VEC4',5123,34962),'WEIGHTS_0':add(np.asarray(W4,np.float32).reshape(n,4),'VEC4',5126,34962)},'indices':add(F.ravel(),'SCALAR',5125,34963),'material':m})
head=lambda n:(np.tile([jid('head'),0,0,0],(n,1)),np.tile([1,0,0,0],(n,1)))
def grid(rows,cols,closed=False):
    F=[]
    for i in range(rows-1):
        for j in range(cols-(0 if closed else 1)):
            a=i*cols+j; b_=i*cols+(j+1)%cols; F+=[[a,a+cols,b_],[b_,a+cols,b_+cols]]
    return np.array(F)
def cap(c,R,th,s=1.,look=(0,0),nr=10,ns=28):
    V=[[0,0,1]]+[[np.sin(th*i/nr)*np.cos(2*np.pi*j/ns),np.sin(th*i/nr)*np.sin(2*np.pi*j/ns),np.cos(th*i/nr)] for i in range(1,nr+1) for j in range(ns)]
    V=np.array(V)+np.array([look[0],look[1],0]); V/=np.linalg.norm(V,axis=1,keepdims=True)
    F=[[0,1+j,1+(j+1)%ns] for j in range(ns)]
    for i in range(nr-1):
        for j in range(ns): a=1+i*ns+j; b_=1+i*ns+(j+1)%ns; F+=[[a,a+ns,b_],[b_,a+ns,b_+ns]]
    return V*R*s+np.array(c),np.array(F),V
def torus(c,R,r,nu=40,nv=10):
    V=[[c[0]+(R+r*np.cos(v))*np.cos(u),c[1]+(R+r*np.cos(v))*np.sin(u),c[2]+r*np.sin(v)] for u in np.linspace(0,2*np.pi,nu,endpoint=False) for v in np.linspace(0,2*np.pi,nv,endpoint=False)]
    F=[]
    for i in range(nu):
        for j in range(nv): a=i*nv+j; b_=i*nv+(j+1)%nv; c_=((i+1)%nu)*nv+j; d=((i+1)%nu)*nv+(j+1)%nv; F+=[[a,c_,b_],[b_,c_,d]]
    return np.array(V),np.array(F)
def tube(p0,p1,r,nv=8):
    p0=np.array(p0,float); p1=np.array(p1,float); d=p1-p0; d/=np.linalg.norm(d); u=np.cross(d,[0,1,0]); u/=np.linalg.norm(u); w=np.cross(d,u)
    V=[pp+r*(np.cos(a)*u+np.sin(a)*w) for pp in (p0,p1) for a in np.linspace(0,2*np.pi,nv,endpoint=False)]
    return np.array(V),grid(2,nv,True)
# 4. green eyes, a matching pair, behind round glasses
EY,EZF,ER=1.756,.188,.04
for sx in (-1,1):
    cx=.093*sx; th=np.radians(62); R=ER/np.sin(th); cz=EZF-R
    for (t,s,m,lk) in ((th,1,mS,(0,0)),(np.radians(30),1.008,mI,(0,-.05)),(np.radians(13),1.016,mP,(0,-.05)),(np.radians(5),1.024,mG,(-.35,.4))):
        V,F,Nn=cap((cx,EY,cz),R,t,s,lk,nr=3 if m==mG else 10,ns=12 if m==mG else 28); prim(V,F,m,*head(len(V)),Nn=Nn.astype(np.float32))
    V,F=torus((cx,EY,.206),.057,.0055); prim(V,F,mF,*head(len(V)))                              # rim
    V,F,Nn=cap((cx,EY,.206-.4),.4,np.arcsin(.056/.4),1.,nr=4,ns=28); prim(V,F,mL,*head(len(V)),Nn=Nn.astype(np.float32))  # lens
    V,F=tube((cx+.057*sx,EY+.008,.206),(.192*sx,1.772,.03),.0045); prim(V,F,mF,*head(len(V)))     # arm back to the ear
V,F=tube((-.036,EY+.012,.209),(.036,EY+.012,.209),.0048); prim(V,F,mF,*head(len(V)))              # bridge
# 5. the hood: a cowl over the head, open at the face, the long ears out through the sides
HC=np.array([0,1.742,-.008]); A,Bh,C=.222,.226,.22
phis=np.radians(np.linspace(-58,90,26)); ths=np.radians(np.linspace(-180,180,73)); rows=[]
for ph in phis:
    row=[]
    for t in ths:
        x=A*np.cos(ph)*np.sin(t); y=Bh*np.sin(ph); z=C*np.cos(ph)*np.cos(t)
        if np.cos(t)>0: z*=1+.12*np.cos(ph)*np.cos(t)   # a little peak at the brow, as a hood has
        row.append(HC+[x,y,z])
    rows.append(row)
V=np.array(rows).reshape(-1,3); nr,nc=len(phis),len(ths); F=[]
open_=lambda i,j: abs(np.degrees(ths[j]))<(70 if np.degrees(phis[i])<4 else 70-(np.degrees(phis[i])-4)*1.2) and np.degrees(phis[i])<20   # the face opening, arched over the brow
for i in range(nr-1):
    for j in range(nc-1):
        if open_(i,j) or open_(i+1,j) or open_(i,j+1) or open_(i+1,j+1): continue
        a=i*nc+j; F+=[[a,a+nc,a+1],[a+1,a+nc,a+nc+1]]
# the hood's back runs down into a shawl over the shoulders
bot=rows[0]; shawl=[]; SR=8
for k in range(SR):
    v=k/(SR-1); row=[]
    for j,t in enumerate(ths):
        p0=np.array(bot[j]); rx,rz=.21+.12*v,.2+.04*v; tgt=np.array([rx*np.sin(t),1.548-.12*v,-.01+rz*np.cos(t)])
        row.append(p0*(1-v)+tgt*v if k else p0)
    shawl.append(row)
S=np.array(shawl).reshape(-1,3); base=len(V); V=np.vstack([V,S])
for i in range(SR-1):
    for j in range(nc-1):
        if abs(np.degrees(ths[j]))<74 or abs(np.degrees(ths[j+1]))<74: continue
        a=base+i*nc+j; F+=[[a,a+nc,a+1],[a+1,a+nc,a+nc+1]]
nH=nr*nc; Jh=np.zeros((len(V),4),int); Wh=np.zeros((len(V),4))
Jh[:,0]=jid('head'); Jh[:,1]=jid('chest'); Wh[:nH,0]=1
for i in range(SR):
    v=i/(SR-1); sl=slice(nH+i*nc,nH+(i+1)*nc); Wh[sl,0]=1-v; Wh[sl,1]=v
used=np.unique(np.array(F).ravel()); remap=-np.ones(len(V),int); remap[used]=np.arange(len(used))
prim(V[used],remap[np.array(F)],mC,Jh[used],Wh[used])
# 6. the cape: from the shoulders to the backs of the knees, falling in folds
CR,CC=22,41; al=np.linspace(-1.12,1.12,CC); V=[]; Jc=[]; Wc=[]
for i in range(CR):
    v=i/(CR-1); y=1.43-.98*v; rx=.31+.1*v; rz=.205+.075*v
    for a in al:
        fold=(.004+.016*v)*np.sin(a*9)
        V.append([rx*np.sin(a)*(1+.02*np.sin(a*9)*v),y,-.035-rz*np.cos(a)-fold])
        # chest at the shoulders, the spine at the waist, the hips below, so it follows him as he walks
        w=np.array([max(0,1-v/.45), max(0,1-abs(v-.45)/.35), max(0,(v-.4)/.6)]); w/=w.sum()
        Jc.append([jid('chest'),jid('spine'),jid('pelvis'),0]); Wc.append(list(w)+[0])
prim(np.array(V),grid(CR,CC),mC,Jc,Wc)
# write
J['buffers'][0]['byteLength']=len(BIN)
js=json.dumps(J,separators=(',',':')).encode(); js+=b' '*((4-len(js)%4)%4)
while len(BIN)%4: BIN.append(0)
out=b'glTF'+struct.pack('<II',2,12+8+len(js)+8+len(BIN))+struct.pack('<I4s',len(js),b'JSON')+js+struct.pack('<I4s',len(BIN),b'BIN\x00')+bytes(BIN)
open(sys.argv[2],'wb').write(out); print('ok',len(out))
