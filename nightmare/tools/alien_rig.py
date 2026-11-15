"""Rig the Catharsis alien (the thing aboard the Nostra): flatten its pivot groups and give it a real skeleton.

Bones: Hips, Spine, Neck, Head, Jaw, UpperArm/LowerArm/Hand (L/R), UpperLeg/LowerLeg/Foot (L/R), Tail1-5.
Long parts (the sinewed arms, digitigrade legs, abdomen, tail) are weighted per vertex and blend across each joint,
so they bend instead of splitting; small parts (claws, horns, scutes) follow one bone. The model faces +Z.
usage: python3 alien_rig.py in.glb out.glb
"""
import json, re, struct, sys
import numpy as np

def main(src, dst):
    data = open(src, "rb").read(); jl = struct.unpack("<I", data[12:16])[0]; gl = json.loads(data[20:20 + jl])
    bo = 20 + jl; bl = struct.unpack("<I", data[bo:bo + 4])[0]; binc = bytearray(data[bo + 8:bo + 8 + bl])
    N = gl["nodes"]
    def rd(ai, k=3):
        a = gl["accessors"][ai]; bv = gl["bufferViews"][a["bufferView"]]; o = bv.get("byteOffset", 0) + a.get("byteOffset", 0)
        return np.frombuffer(binc, "<f4", a["count"] * k, o).reshape(-1, k).astype(np.float64)
    def pad():
        while len(binc) % 4: binc.append(0)
    def view(raw, tgt=None):
        pad(); off = len(binc); binc.extend(raw); bv = {"buffer": 0, "byteOffset": off, "byteLength": len(raw)}
        if tgt: bv["target"] = tgt
        gl["bufferViews"].append(bv); return len(gl["bufferViews"]) - 1
    def acc(v, ct, n, t, **kw):
        a = {"bufferView": v, "componentType": ct, "count": n, "type": t}; a.update(kw); gl["accessors"].append(a); return len(gl["accessors"]) - 1

    # every mesh, with the group it hangs from and its offset in model space (the groups only translate)
    meshes = []
    def walk(i, off, grp):
        n = N[i]; o = off + np.array(n.get("translation", [0, 0, 0]), float)
        g = n["name"] if ("mesh" not in n and i != 0) else grp
        if "mesh" in n: meshes.append((i, o, g))
        for c in n.get("children", []): walk(c, o, g)
    walk(0, np.zeros(3), "body")

    # tail centre line, from the tail rings
    rings = []
    for i, o, g in meshes:
        m = re.match(r"^Tail ring (\d+)$", N[i]["name"])
        if m:
            v = rd(gl["meshes"][N[i]["mesh"]]["primitives"][0]["attributes"]["POSITION"]) + o
            rings.append((int(m.group(1)), (v.min(0) + v.max(0)) / 2))
    rings = [c for _, c in sorted(rings, key=lambda r: r[0])]
    tail_base = np.array([0, 1.98, -0.23])
    tp = [tail_base] + [rings[min(len(rings) - 1, k)] for k in (6, 13, 20, 27)]

    P = {"Hips": (0, 2.05, 0), "Spine": (0, 2.55, 0), "Neck": (0, 3.25, 0), "Head": (0, 3.45, 0), "Jaw": (0, 3.62, 0.05),
         "UpperArm_L": (-0.68, 3.14, 0), "LowerArm_L": (-0.74, 2.62, 0.04), "Hand_L": (-0.80, 2.10, 0.1),
         "UpperArm_R": (0.68, 3.14, 0), "LowerArm_R": (0.74, 2.62, 0.04), "Hand_R": (0.80, 2.10, 0.1),
         "UpperLeg_L": (-0.33, 1.87, 0), "LowerLeg_L": (-0.38, 1.20, 0.1), "Foot_L": (-0.38, 0.32, -0.02),
         "UpperLeg_R": (0.33, 1.87, 0), "LowerLeg_R": (0.38, 1.20, 0.1), "Foot_R": (0.38, 0.32, -0.02)}
    for k in range(5): P["Tail%d" % (k + 1)] = tuple(tp[k])
    PAR = {"Hips": None, "Spine": "Hips", "Neck": "Spine", "Head": "Neck", "Jaw": "Head",
           "UpperArm_L": "Spine", "LowerArm_L": "UpperArm_L", "Hand_L": "LowerArm_L", "UpperArm_R": "Spine", "LowerArm_R": "UpperArm_R", "Hand_R": "LowerArm_R",
           "UpperLeg_L": "Hips", "LowerLeg_L": "UpperLeg_L", "Foot_L": "LowerLeg_L", "UpperLeg_R": "Hips", "LowerLeg_R": "UpperLeg_R", "Foot_R": "LowerLeg_R",
           "Tail1": "Hips", "Tail2": "Tail1", "Tail3": "Tail2", "Tail4": "Tail3", "Tail5": "Tail4"}
    names = list(P); idx = {n: k for k, n in enumerate(names)}; piv = {n: np.array(P[n], float) for n in names}

    def chain(v, bones, D=0.08):  # weight along a chain of joints, by height (arms and legs hang down)
        ys = [piv[b][1] for b in bones[1:]]; j = np.zeros((len(v), 4), np.uint8); w = np.zeros((len(v), 4), np.float32)
        y = v[:, 1]; seg = np.zeros(len(v), int)
        for k, yy in enumerate(ys): seg = np.where(y < yy, k + 1, seg)
        j[:, 0] = [idx[bones[s]] for s in seg]; w[:, 0] = 1
        for k, yy in enumerate(ys):  # blend across each joint
            t = np.clip((yy + D - y) / (2 * D), 0, 1); near = np.abs(y - yy) < D
            a, b = idx[bones[k]], idx[bones[k + 1]]
            j[near, 0] = a; j[near, 1] = b; w[near, 0] = 1 - t[near]; w[near, 1] = t[near]
        return j, w

    def nearest(v, bones):  # weight between the two nearest joints of a chain (the tail)
        pts = np.array([piv[b] for b in bones]); d = np.linalg.norm(v[:, None, :] - pts[None], axis=2)
        o = np.argsort(d, 1)[:, :2]; d0 = np.take_along_axis(d, o[:, :1], 1)[:, 0]; d1 = np.take_along_axis(d, o[:, 1:2], 1)[:, 0]
        j = np.zeros((len(v), 4), np.uint8); w = np.zeros((len(v), 4), np.float32)
        j[:, 0] = [idx[bones[k]] for k in o[:, 0]]; j[:, 1] = [idx[bones[k]] for k in o[:, 1]]
        a = d1 / (d0 + d1 + 1e-9); w[:, 0] = a; w[:, 1] = 1 - a; return j, w

    report = {}
    root = N[0]; root["children"] = []
    for i, o, g in meshes:
        nd = N[i]; name = nd["name"]
        for pr in gl["meshes"][nd["mesh"]]["primitives"]:
            v = rd(pr["attributes"]["POSITION"]) + o; n = len(v)
            pa = acc(view(v.astype("<f4").tobytes(), 34962), 5126, n, "VEC3", min=[float(x) for x in v.min(0)], max=[float(x) for x in v.max(0)])
            pr["attributes"]["POSITION"] = pa
            s = "L" if g.startswith("left") else "R"
            if g in ("head", "eyes"): j = np.full((n, 4), idx["Head"], np.uint8) * 0 + idx["Head"]; w = np.zeros((n, 4), np.float32); w[:, 0] = 1; j[:, 1:] = 0; b = "Head"
            elif g == "jaw": j = np.zeros((n, 4), np.uint8); j[:, 0] = idx["Jaw"]; w = np.zeros((n, 4), np.float32); w[:, 0] = 1; b = "Jaw"
            elif g.endswith("Arm"): j, w = chain(v, ["UpperArm_" + s, "LowerArm_" + s, "Hand_" + s]); b = "Arm_" + s
            elif g.endswith("Leg"): j, w = chain(v, ["UpperLeg_" + s, "LowerLeg_" + s, "Foot_" + s], .1); b = "Leg_" + s
            elif g == "tail": j, w = nearest(v, ["Tail1", "Tail2", "Tail3", "Tail4", "Tail5"]); b = "Tail"
            else: j, w = chain(v, ["Hips", "Spine", "Neck"], .12); b = "Body"
            pr["attributes"]["JOINTS_0"] = acc(view(j.astype(np.uint8).tobytes(), 34962), 5121, n, "VEC4")
            pr["attributes"]["WEIGHTS_0"] = acc(view(w.astype("<f4").tobytes(), 34962), 5126, n, "VEC4")
        nd.pop("translation", None); nd.pop("children", None); nd["skin"] = 0; root["children"].append(i)
        report[b] = report.get(b, 0) + 1
    first = len(N)
    for n in names:
        p = PAR[n]; t = piv[n] - (piv[p] if p else 0); N.append({"name": n, "translation": [round(float(x), 6) for x in t]})
    for n in names:
        if PAR[n]: N[first + idx[PAR[n]]].setdefault("children", []).append(first + idx[n])
    root["children"].append(first + idx["Hips"])
    ibm = np.zeros((len(names), 16), np.float32)
    for k, n in enumerate(names): m = np.eye(4, dtype=np.float32); m[0:3, 3] = -piv[n]; ibm[k] = m.T.reshape(-1)
    gl["skins"] = [{"name": "Armature", "joints": [first + k for k in range(len(names))], "skeleton": first + idx["Hips"], "inverseBindMatrices": acc(view(ibm.tobytes()), 5126, len(names), "MAT4")}]
    gl["asset"]["generator"] = gl["asset"].get("generator", "") + " + rigged (Armature, %d bones)" % len(names)
    for k, n in enumerate(N[:first]):  # the old pivot groups are empty now
        if k != 0 and 'mesh' not in n: n.pop('children', None)
    pad(); gl["buffers"][0]["byteLength"] = len(binc)
    js = json.dumps(gl, separators=(",", ":")).encode()
    while len(js) % 4: js += b" "
    out = struct.pack("<4sII", b"glTF", 2, 28 + len(js) + len(binc)) + struct.pack("<I4s", len(js), b"JSON") + js + struct.pack("<I4s", len(binc), b"BIN\x00") + bytes(binc)
    open(dst, "wb").write(out)
    for b, c in sorted(report.items()): print(f"{b:8s} {c} parts")
    print(len(names), "bones")

if __name__ == "__main__": main(sys.argv[1], sys.argv[2])
