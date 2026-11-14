"""Build the playable Taredesiban (the wanderer's body), as an unskinned GLB like the other playable species.

Same body as build_taredesiban.py, regrouped for the wanderer's rig: everything on an arm hangs from a
`leftArm` / `rightArm` node at the shoulder, everything on a leg from `leftLeg` / `rightLeg` at the hip, and
the rest stays on the body. The armour textures are greyscale and the armour colour sits in the material,
so the creator can recolour skin, armour, inlays (the "rim") and beard like any other species.

usage: python3 build_sp_taredesiban.py out.glb   (keep build_taredesiban.py beside it)
"""
import io, json, struct, sys, os
import numpy as np
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_taredesiban as T

def grey_png(seed):
    g = np.random.default_rng(seed); S = 256; yy, xx = np.mgrid[0:S, 0:S] / S
    img = np.full((S, S), 186.0)
    for _ in range(14):
        cx, cy, r = g.random(), g.random(), 0.15 + g.random() * 0.35
        img[np.abs(np.hypot(xx - cx, yy - cy) - r) < 0.006] = 255
    for _ in range(6): img[np.abs(yy - g.random()) < 0.004] = 110
    img += g.normal(0, 3, img.shape)
    buf = io.BytesIO(); Image.fromarray(np.clip(np.stack([img] * 3, -1), 0, 255).astype(np.uint8)).save(buf, "PNG"); return buf.getvalue()
TEX = [grey_png(5), grey_png(9)]
ARMOUR = [0.036, 0.04, 0.1, 1]  # one colour for both armour materials (the creator tints them together)
for n, m in T.MATS:
    if n in ("Armour", "Armour plate"): m["pbrMetallicRoughness"]["baseColorFactor"] = ARMOUR

RENAME = {"Nose ridge": "Nose"}  # the game finds the head height from a mesh called "nose"
GROUP = {"leftArm": ("UpperArm_L", "LowerArm_L", "Hand_L"), "rightArm": ("UpperArm_R", "LowerArm_R", "Hand_R"),
         "leftLeg": ("UpperLeg_L", "LowerLeg_L", "Foot_L"), "rightLeg": ("UpperLeg_R", "LowerLeg_R", "Foot_R")}
PIVOT = {"leftArm": T.P["UpperArm_L"], "rightArm": T.P["UpperArm_R"], "leftLeg": T.P["UpperLeg_L"], "rightLeg": T.P["UpperLeg_R"]}
def group_of(bone):
    for g, bones in GROUP.items():
        if bone in bones: return g
    return None

def main(out):
    blob = bytearray(); views = []; accs = []
    def view(raw, target=None):
        while len(blob) % 4: blob.append(0)
        v = {"buffer": 0, "byteOffset": len(blob), "byteLength": len(raw)}
        if target: v["target"] = target
        blob.extend(raw); views.append(v); return len(views) - 1
    def acc(arr, ctype, typ, target=None, minmax=False):
        a = {"bufferView": view(arr.tobytes(), target), "componentType": ctype, "count": len(arr), "type": typ}
        if minmax: a["min"] = arr.min(0).tolist(); a["max"] = arr.max(0).tolist()
        accs.append(a); return len(accs) - 1
    meshes = []; nodes = [{"name": "TAREDESIBAN", "children": []}]
    groups = {}
    for g in GROUP:
        nodes.append({"name": g, "translation": [round(float(x), 6) for x in PIVOT[g]], "children": []}); groups[g] = len(nodes) - 1; nodes[0]["children"].append(len(nodes) - 1)
    for name, (V, UV, Tr), mat, bone, soft in T.parts:
        g = group_of(bone); V = V.astype(float) - (PIVOT[g] if g else 0)
        N = T.normals(V, Tr).astype(np.float32); V = V.astype(np.float32)
        prim = {"attributes": {"POSITION": acc(V, 5126, "VEC3", 34962, True), "NORMAL": acc(N, 5126, "VEC3", 34962), "TEXCOORD_0": acc(UV.astype(np.float32), 5126, "VEC2", 34962)},
                "indices": acc(Tr.astype(np.uint16).reshape(-1), 5123, "SCALAR", 34963), "material": T.MI[mat]}
        nm = RENAME.get(name, name)
        meshes.append({"name": nm, "primitives": [prim]}); nodes.append({"name": nm, "mesh": len(meshes) - 1})
        nodes[groups[g] if g else 0]["children"].append(len(nodes) - 1)
    images = [{"bufferView": view(png), "mimeType": "image/png"} for png in TEX]
    gl = {"asset": {"version": "2.0", "generator": "NOSTRAVECTOR playable Taredesiban builder"}, "scene": 0, "scenes": [{"nodes": [0]}], "nodes": nodes, "meshes": meshes,
          "materials": [dict(name=n, **m) for n, m in T.MATS], "samplers": [{"magFilter": 9729, "minFilter": 9987, "wrapS": 10497, "wrapT": 10497}],
          "images": images, "textures": [{"sampler": 0, "source": i} for i in range(len(images))], "accessors": accs, "bufferViews": views, "buffers": [{"byteLength": 0}]}
    while len(blob) % 4: blob.append(0)
    gl["buffers"][0]["byteLength"] = len(blob)
    js = json.dumps(gl, separators=(",", ":")).encode()
    while len(js) % 4: js += b" "
    out_b = struct.pack("<4sII", b"glTF", 2, 28 + len(js) + len(blob)) + struct.pack("<I4s", len(js), b"JSON") + js + struct.pack("<I4s", len(blob), b"BIN\x00") + bytes(blob)
    open(out, "wb").write(out_b); print(f"{len(T.parts)} parts, {len(out_b)//1024} KB")

if __name__ == "__main__":
    main(sys.argv[1])
