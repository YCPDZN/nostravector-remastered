"""Build a Taredesiban (blue-skinned humanoid in dark armour with teal inlays, flared pauldrons, a sheer cape) as a rigged GLB.

Residents only: the Taredesibans are not a playable race.

Same 18-bone armature and bone names as the rigged Sevirrus and Jakal models, so every pose
and animation works on all of them. Character faces +Z, units are metres.

usage: python3 build_taredesiban.py out.glb
"""
import io, json, struct, sys
import numpy as np
from PIL import Image

rng = np.random.default_rng(7)

# ---------------- skeleton ----------------
PIV = {
    "Hips": (0, 0.95, 0), "Spine": (0, 1.02, 0), "Neck": (0, 1.47, 0), "Head": (0, 1.56, 0),
    "Eye_L": (0.042, 1.70, 0.08), "Eye_R": (-0.042, 1.70, 0.08),
    "UpperArm_L": (0.25, 1.40, 0), "LowerArm_L": (0.28, 1.12, 0), "Hand_L": (0.30, 0.86, 0.02),
    "UpperArm_R": (-0.25, 1.40, 0), "LowerArm_R": (-0.28, 1.12, 0), "Hand_R": (-0.30, 0.86, 0.02),
    "UpperLeg_L": (0.11, 0.90, 0), "LowerLeg_L": (0.12, 0.50, 0.01), "Foot_L": (0.13, 0.11, 0),
    "UpperLeg_R": (-0.11, 0.90, 0), "LowerLeg_R": (-0.12, 0.50, 0.01), "Foot_R": (-0.13, 0.11, 0),
}
PARENT = {"Hips": None, "Spine": "Hips", "Neck": "Spine", "Head": "Neck", "Eye_L": "Head", "Eye_R": "Head",
          "UpperArm_L": "Spine", "LowerArm_L": "UpperArm_L", "Hand_L": "LowerArm_L",
          "UpperArm_R": "Spine", "LowerArm_R": "UpperArm_R", "Hand_R": "LowerArm_R",
          "UpperLeg_L": "Hips", "LowerLeg_L": "UpperLeg_L", "Foot_L": "LowerLeg_L",
          "UpperLeg_R": "Hips", "LowerLeg_R": "UpperLeg_R", "Foot_R": "LowerLeg_R"}
BONES = list(PIV.keys())
P = {k: np.array(v, float) for k, v in PIV.items()}

# ---------------- geometry helpers (all return verts, uvs, tris) ----------------
def rot_to(d):
    """rotation matrix taking +Y onto direction d"""
    d = d / np.linalg.norm(d); y = np.array([0, 1.0, 0]); v = np.cross(y, d); c = y @ d
    if np.linalg.norm(v) < 1e-9: return np.eye(3) if c > 0 else np.diag([1, -1, -1.0])
    k = np.array([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
    return np.eye(3) + k + k @ k * (1 / (1 + c))

def euler(x=0, y=0, z=0):
    cx, sx, cy, sy, cz, sz = np.cos(x), np.sin(x), np.cos(y), np.sin(y), np.cos(z), np.sin(z)
    return np.array([[1, 0, 0], [0, cx, -sx], [0, sx, cx]]) @ np.array([[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]]) @ np.array([[cz, -sz, 0], [sz, cz, 0], [0, 0, 1]])

def lathe(profile, n=24, sx=1.0, sz=1.0, uscale=1.0):
    prof = np.array(profile, float); m = len(prof)
    th = np.linspace(0, 2 * np.pi, n + 1)
    V = []; UV = []
    L = np.r_[0, np.cumsum(np.linalg.norm(np.diff(prof, axis=0), axis=1))]
    for i, (r, y) in enumerate(prof):
        for j, t in enumerate(th):
            V.append([r * np.cos(t) * sx, y, r * np.sin(t) * sz]); UV.append([j / n * uscale, L[i] / max(L[-1], 1e-6)])
    T = []
    for i in range(m - 1):
        for j in range(n):
            a, b = i * (n + 1) + j, i * (n + 1) + j + 1; c, d = a + n + 1, b + n + 1
            T += [[a, c, b], [b, c, d]]
    return np.array(V), np.array(UV), np.array(T)

def capsule(A, B, r, sx=1.0, sz=1.0, n=20):
    A, B = np.array(A, float), np.array(B, float); L = np.linalg.norm(B - A)
    prof = [(r * np.cos(a), r * np.sin(a)) for a in np.linspace(-np.pi / 2, 0, 7)] + [(r * np.cos(a), L + r * np.sin(a)) for a in np.linspace(0, np.pi / 2, 7)]
    V, UV, T = lathe(prof, n, sx, sz, uscale=2)
    return V @ rot_to(B - A).T + A, UV, T

def ellipsoid(c, radii, R=None, n=22, lat=(-np.pi / 2, np.pi / 2), rings=14):
    prof = [(np.cos(a), np.sin(a)) for a in np.linspace(lat[0], lat[1], rings)]
    V, UV, T = lathe(prof, n)
    V = V * np.array(radii)
    if R is not None: V = V @ R.T
    return V + np.array(c), UV, T

def cylinder(c, r, h, R=None, n=18, cap=True):
    prof = ([(0, -h / 2)] if cap else []) + [(r, -h / 2), (r, h / 2)] + ([(0, h / 2)] if cap else [])
    V, UV, T = lathe(prof, n)
    if R is not None: V = V @ R.T
    return V + np.array(c), UV, T

def torus(c, Rr, r, R=None, n=28, m=10, sz=1.0):
    V = []; UV = []
    for i in range(n + 1):
        u = 2 * np.pi * i / n
        for j in range(m + 1):
            v = 2 * np.pi * j / m
            V.append([(Rr + r * np.cos(v)) * np.cos(u), r * np.sin(v), (Rr + r * np.cos(v)) * np.sin(u) * sz]); UV.append([i / n * 4, j / m])
    T = []
    for i in range(n):
        for j in range(m):
            a = i * (m + 1) + j; b = a + 1; cc = a + m + 1; d = cc + 1
            T += [[a, b, cc], [b, d, cc]]
    V = np.array(V)
    if R is not None: V = V @ R.T
    return V + np.array(c), np.array(UV), np.array(T)

def box(c, size, R=None, bevel=0.0):
    sx, sy, sz = np.array(size) / 2
    faces = [((1, 0, 0), (0, 0, -1), (0, 1, 0)), ((-1, 0, 0), (0, 0, 1), (0, 1, 0)), ((0, 1, 0), (1, 0, 0), (0, 0, -1)),
             ((0, -1, 0), (1, 0, 0), (0, 0, 1)), ((0, 0, 1), (1, 0, 0), (0, 1, 0)), ((0, 0, -1), (-1, 0, 0), (0, 1, 0))]
    V = []; UV = []; T = []
    for nrm, u, v in faces:
        nrm, u, v = map(np.array, (nrm, u, v)); base = len(V)
        for a, b in [(-1, -1), (1, -1), (1, 1), (-1, 1)]:
            p = nrm * [sx, sy, sz] + u * a * [sx, sy, sz] + v * b * [sx, sy, sz]
            V.append(p); UV.append([(a + 1) / 2, (b + 1) / 2])
        T += [[base, base + 1, base + 2], [base, base + 2, base + 3]]
    V = np.array(V, float)
    if R is not None: V = V @ R.T
    return V + np.array(c), np.array(UV, float), np.array(T)

# ---------------- materials ----------------
def plate_png(seed, base, line):
    """dark armour plate: a fine engraved pattern of curves and panel lines"""
    g = np.random.default_rng(seed); S = 256
    yy, xx = np.mgrid[0:S, 0:S] / S
    img = np.zeros((S, S, 3)); img[:] = base
    for _ in range(14):                                    # engraved arcs
        cx, cy, r = g.random(), g.random(), 0.15 + g.random() * 0.35
        d = np.abs(np.hypot(xx - cx, yy - cy) - r)
        img[d < 0.006] = line
    for k in range(6):                                     # panel seams
        y = g.random(); img[np.abs(yy - y) < 0.004] = np.array(base) * 0.55
    img += g.normal(0, 3, img.shape)
    buf = io.BytesIO(); Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).save(buf, "PNG"); return buf.getvalue()

TEX = [plate_png(5, (34, 36, 62), (70, 88, 130)), plate_png(9, (52, 60, 96), (96, 120, 170))]
MATS = [
    ("Armour", dict(pbrMetallicRoughness=dict(baseColorTexture=dict(index=0), metallicFactor=0.85, roughnessFactor=0.32))),
    ("Armour plate", dict(pbrMetallicRoughness=dict(baseColorTexture=dict(index=1), metallicFactor=0.88, roughnessFactor=0.26))),
    ("Undersuit", dict(pbrMetallicRoughness=dict(baseColorFactor=[0.06, 0.065, 0.11, 1], metallicFactor=0.3, roughnessFactor=0.6))),
    ("Teal inlay", dict(emissiveFactor=[0.12, 0.95, 0.88], pbrMetallicRoughness=dict(baseColorFactor=[0.1, 0.8, 0.75, 1], metallicFactor=0.2, roughnessFactor=0.3))),
    ("Violet inlay", dict(emissiveFactor=[0.45, 0.3, 1.0], pbrMetallicRoughness=dict(baseColorFactor=[0.4, 0.3, 0.9, 1], roughnessFactor=0.3))),
    ("Skin", dict(pbrMetallicRoughness=dict(baseColorFactor=[0.36, 0.5, 0.74, 1], metallicFactor=0.05, roughnessFactor=0.5))),
    ("Skin shade", dict(pbrMetallicRoughness=dict(baseColorFactor=[0.26, 0.38, 0.6, 1], metallicFactor=0.05, roughnessFactor=0.55))),
    ("Beard", dict(pbrMetallicRoughness=dict(baseColorFactor=[0.07, 0.09, 0.14, 1], metallicFactor=0.0, roughnessFactor=0.9))),
    ("Eye", dict(emissiveFactor=[0.25, 0.04, 0.06], pbrMetallicRoughness=dict(baseColorFactor=[0.12, 0.02, 0.04, 1], metallicFactor=0.3, roughnessFactor=0.08))),
    ("Glint", dict(emissiveFactor=[0.8, 0.85, 0.9], pbrMetallicRoughness=dict(baseColorFactor=[1, 1, 1, 1]))),
    ("Dark", dict(pbrMetallicRoughness=dict(baseColorFactor=[0.03, 0.03, 0.05, 1], metallicFactor=0.2, roughnessFactor=0.55))),
    ("Cape", dict(alphaMode="BLEND", doubleSided=True, emissiveFactor=[0.02, 0.12, 0.12], pbrMetallicRoughness=dict(baseColorFactor=[0.55, 0.85, 0.9, 0.32], metallicFactor=0.0, roughnessFactor=0.35))),
]
MI = {n: i for i, (n, _) in enumerate(MATS)}

# ---------------- parts: (name, mesh, material, bone, soft) ----------------
parts = []
def add(name, mesh, mat, bone, soft=False): parts.append((name, mesh, mat, bone, soft))

for s, sg in (("L", 1), ("R", -1)):
    sh, el, wr = P["UpperArm_" + s], P["LowerArm_" + s], P["Hand_" + s]
    hp, kn, an = P["UpperLeg_" + s], P["LowerLeg_" + s], P["Foot_" + s]
    # arms: undersuit, a gauntlet with a glowing seam, and three flared plates on the shoulder
    add(f"Upper arm {s}", capsule(sh + [0, 0.02, 0], el, 0.066), "Undersuit", "UpperArm_" + s, True)
    add(f"Bicep plate {s}", ellipsoid((sh + el) / 2 + [sg * 0.02, 0, 0.02], (0.06, 0.12, 0.062)), "Armour", "UpperArm_" + s)
    for k, (dy, dx, w, mat) in enumerate([(0.07, 0.03, 1.0, "Armour plate"), (0.03, 0.055, 0.92, "Armour"), (-0.01, 0.075, 0.8, "Armour plate")]):
        add(f"Pauldron {k} {s}", ellipsoid(sh + [sg * dx, dy, 0], (0.12 * w, 0.075 * w, 0.125 * w), euler(z=-sg * (0.45 + k * 0.18)), lat=(-0.25, np.pi / 2)), mat, "UpperArm_" + s)
    add(f"Pauldron inlay {s}", box(sh + [sg * 0.1, 0.035, 0.0], (0.012, 0.012, 0.2), euler(z=-sg * 0.6)), "Teal inlay", "UpperArm_" + s)
    add(f"Pauldron spike {s}", ellipsoid(sh + [sg * 0.13, 0.11, -0.02], (0.02, 0.06, 0.03), euler(z=-sg * 0.7)), "Armour plate", "UpperArm_" + s)
    add(f"Forearm {s}", capsule(el, wr + [0, 0.03, 0], 0.056), "Undersuit", "LowerArm_" + s, True)
    add(f"Gauntlet {s}", capsule(el + [0, -0.04, 0], wr + [0, 0.045, 0], 0.066, 1.0, 1.1), "Armour plate", "LowerArm_" + s)
    add(f"Gauntlet inlay {s}", box((el + wr) / 2 + [sg * 0.004, -0.01, 0.068], (0.012, 0.17, 0.008)), "Teal inlay", "LowerArm_" + s)
    add(f"Elbow guard {s}", ellipsoid(el + [0, 0.0, -0.05], (0.05, 0.065, 0.04)), "Armour", "LowerArm_" + s)
    add(f"Hand {s}", ellipsoid(wr + [0, -0.07, 0.012], (0.042, 0.072, 0.032)), "Armour", "Hand_" + s)
    add(f"Knuckles {s}", box(wr + [0, -0.105, 0.03], (0.07, 0.03, 0.03)), "Armour plate", "Hand_" + s)
    add(f"Thumb {s}", capsule(wr + [-sg * 0.005, -0.03, 0.035], wr + [-sg * 0.02, -0.09, 0.055], 0.015), "Armour", "Hand_" + s)
    # legs: undersuit, sculpted thigh plates, knee cops, greaves with inlays, armoured boots
    add(f"Thigh {s}", capsule(hp + [0, 0.02, 0], kn, 0.088), "Undersuit", "UpperLeg_" + s, True)
    add(f"Thigh plate {s}", ellipsoid((hp + kn) / 2 + [sg * 0.01, 0.02, 0.035], (0.078, 0.18, 0.06)), "Armour plate", "UpperLeg_" + s)
    add(f"Thigh inlay {s}", box((hp + kn) / 2 + [sg * 0.03, 0.0, 0.095], (0.01, 0.2, 0.008), euler(z=sg * 0.1)), "Violet inlay", "UpperLeg_" + s)
    add(f"Shin {s}", capsule(kn, an + [0, 0.07, 0], 0.07), "Undersuit", "LowerLeg_" + s, True)
    add(f"Greave {s}", ellipsoid((kn + an) / 2 + [0, 0.02, 0.03], (0.066, 0.2, 0.06)), "Armour", "LowerLeg_" + s)
    add(f"Greave inlay {s}", box((kn + an) / 2 + [0, 0.03, 0.09], (0.012, 0.22, 0.008)), "Teal inlay", "LowerLeg_" + s)
    add(f"Knee cop {s}", ellipsoid(kn + [0, 0.01, 0.06], (0.064, 0.075, 0.045)), "Armour plate", "LowerLeg_" + s)
    add(f"Knee spike {s}", ellipsoid(kn + [0, 0.07, 0.07], (0.02, 0.05, 0.02), euler(x=0.4)), "Armour plate", "LowerLeg_" + s)
    add(f"Boot {s}", ellipsoid(an + [0, -0.03, 0.05], (0.064, 0.075, 0.14)), "Armour", "Foot_" + s)
    add(f"Boot cuff {s}", capsule(an, an + [0, 0.12, 0], 0.078), "Armour plate", "Foot_" + s)
    add(f"Sole {s}", box(an + [0, -0.095, 0.05], (0.12, 0.03, 0.28)), "Dark", "Foot_" + s)

# torso: undersuit, a sculpted breastplate, ribbed abdomen, a glowing V and a gem at the heart
add("Torso", capsule(P["Spine"] + [0, 0.02, 0], [0, 1.36, 0], 0.17, 1.12, 0.8), "Undersuit", "Spine", True)
add("Abdomen", capsule([0, 0.9, 0], [0, 1.06, 0], 0.145, 1.05, 0.82), "Undersuit", "Spine", True)
add("Pelvis", capsule([-0.085, 0.88, 0], [0.085, 0.88, 0], 0.12), "Undersuit", "Hips", True)
add("Breastplate", ellipsoid([0, 1.28, 0.06], (0.2, 0.15, 0.12), lat=(-0.6, np.pi / 2)), "Armour plate", "Spine")
for sg, s in ((1, "L"), (-1, "R")):
    add(f"Pectoral {s}", ellipsoid([sg * 0.085, 1.27, 0.12], (0.085, 0.07, 0.05), euler(z=sg * 0.2)), "Armour", "Spine")
    add(f"Chest V {s}", box([sg * 0.06, 1.2, 0.17], (0.014, 0.17, 0.01), euler(z=sg * 0.55, x=-0.15)), "Teal inlay", "Spine")
    add(f"Collar plate {s}", ellipsoid([sg * 0.1, 1.42, 0.02], (0.1, 0.045, 0.1), euler(z=sg * 0.3)), "Armour", "Spine")
    add(f"Side plate {s}", ellipsoid([sg * 0.15, 1.12, 0.0], (0.05, 0.12, 0.09)), "Armour", "Spine")
add("Heart gem", ellipsoid([0, 1.16, 0.165], (0.026, 0.034, 0.016)), "Teal inlay", "Spine")
for k in range(3):
    add(f"Abdominal plate {k}", ellipsoid([0, 1.06 - k * 0.055, 0.115 - k * 0.005], (0.12 - k * 0.01, 0.03, 0.04)), "Armour", "Spine")
add("Back plate", ellipsoid([0, 1.25, -0.08], (0.19, 0.17, 0.09)), "Armour", "Spine")
add("Spine ridge", box([0, 1.2, -0.17], (0.02, 0.3, 0.02)), "Violet inlay", "Spine")
add("Belt", torus([0, 0.97, 0.005], 0.165, 0.022, sz=0.8), "Armour plate", "Hips")
add("Belt clasp", ellipsoid([0, 0.97, 0.14], (0.04, 0.03, 0.015)), "Teal inlay", "Hips")
for sg, s in ((1, "L"), (-1, "R")):
    add(f"Hip fauld {s}", box([sg * 0.13, 0.88, 0.04], (0.1, 0.13, 0.02), euler(y=-sg * 0.5, z=sg * 0.12)), "Armour", "Hips")
add("Front fauld", box([0, 0.86, 0.13], (0.12, 0.12, 0.02), euler(x=0.1)), "Armour plate", "Hips")
# the cape: three sheer panels hanging from the shoulders behind
for k, (x, w, rz) in enumerate([(-0.15, 0.22, 0.1), (0.0, 0.26, 0.0), (0.15, 0.22, -0.1)]):
    add(f"Cape {k}", box([x, 0.92, -0.2 - abs(x) * 0.15], (w, 0.95, 0.008), euler(x=0.12, z=rz)), "Cape", "Spine")
add("Cape clasp L", ellipsoid([0.16, 1.4, -0.06], (0.03, 0.03, 0.02)), "Teal inlay", "Spine")
add("Cape clasp R", ellipsoid([-0.16, 1.4, -0.06], (0.03, 0.03, 0.02)), "Teal inlay", "Spine")
# neck and a high collar
add("Neck", capsule([0, 1.44, 0], [0, 1.56, 0], 0.058), "Skin", "Neck")
add("Gorget", torus([0, 1.47, 0.0], 0.1, 0.028, sz=0.9), "Armour plate", "Neck")
# the head: a smooth, tall blue cranium, swept-back pointed ears, heavy brow, a short dark beard
add("Head", ellipsoid([0, 1.68, 0.01], (0.088, 0.125, 0.104)), "Skin", "Head")
add("Cranium", ellipsoid([0, 1.75, -0.025], (0.082, 0.085, 0.105)), "Skin", "Head")
add("Jaw", ellipsoid([0, 1.6, 0.04], (0.064, 0.052, 0.07)), "Skin", "Head")
add("Crest", ellipsoid([0, 1.79, 0.0], (0.012, 0.04, 0.09)), "Skin shade", "Head")
add("Nose ridge", ellipsoid([0, 1.665, 0.098], (0.012, 0.03, 0.014)), "Skin shade", "Head")
for sg, s in ((1, "L"), (-1, "R")):
    add(f"Ear {s}", ellipsoid([sg * 0.09, 1.7, -0.02], (0.012, 0.03, 0.065), euler(x=-0.5, y=sg * 0.35)), "Skin", "Head")
    add(f"Ear tip {s}", ellipsoid([sg * 0.1, 1.735, -0.075], (0.008, 0.015, 0.035), euler(x=-0.9, y=sg * 0.35)), "Skin shade", "Head")
    add(f"Cheekbone {s}", ellipsoid([sg * 0.058, 1.655, 0.068], (0.034, 0.02, 0.04)), "Skin shade", "Head")
    add(f"Brow {s}", ellipsoid([sg * 0.038, 1.728, 0.085], (0.042, 0.015, 0.03), euler(z=-sg * 0.22)), "Skin shade", "Head")
    add(f"Eye {s}", ellipsoid([sg * 0.04, 1.703, 0.086], (0.026, 0.014, 0.016), euler(z=-sg * 0.25)), "Eye", "Eye_" + s)
    add(f"Eye glint {s}", ellipsoid([sg * 0.046, 1.708, 0.1], (0.004, 0.003, 0.002)), "Glint", "Eye_" + s)
    add(f"Moustache {s}", ellipsoid([sg * 0.018, 1.625, 0.103], (0.022, 0.007, 0.008), euler(z=sg * 0.3)), "Beard", "Head")
add("Mouth", box([0, 1.615, 0.103], (0.032, 0.003, 0.005)), "Dark", "Head")
add("Beard", ellipsoid([0, 1.575, 0.075], (0.05, 0.05, 0.04)), "Beard", "Head")
add("Beard jaw", ellipsoid([0, 1.59, 0.04], (0.068, 0.04, 0.062), lat=(-np.pi / 2, 0.1)), "Beard", "Head")

# ---------------- skin weights ----------------
def nrm(v): return v / np.linalg.norm(v)
BOUNDS = [("Hips", "Spine", P["Spine"], np.array([0, 1.0, 0]), 0.32), ("Spine", "Neck", P["Neck"], np.array([0, 1.0, 0]), 0.16)]
for s in "LR":
    BOUNDS += [("Spine", "UpperArm_" + s, P["UpperArm_" + s], nrm(P["LowerArm_" + s] - P["UpperArm_" + s]), 0.16),
               ("UpperArm_" + s, "LowerArm_" + s, P["LowerArm_" + s], nrm(P["Hand_" + s] - P["LowerArm_" + s]), 0.12),
               ("Hips", "UpperLeg_" + s, P["UpperLeg_" + s], nrm(P["LowerLeg_" + s] - P["UpperLeg_" + s]), 0.14),
               ("UpperLeg_" + s, "LowerLeg_" + s, P["LowerLeg_" + s], nrm(P["Foot_" + s] - P["LowerLeg_" + s]), 0.12),
               ("LowerLeg_" + s, "Foot_" + s, P["Foot_" + s] + [0, 0.07, 0], np.array([0, -1.0, 0]), 0.12)]
D, CAP = 0.05, 0.85
BI = {b: i for i, b in enumerate(BONES)}

def weights(V, bone, soft):
    n = len(V); J = np.zeros((n, 4), np.uint8); W = np.zeros((n, 4), np.float32)
    J[:, 0] = BI[bone]; W[:, 0] = 1
    if soft:
        bw = np.zeros(n); bo = np.full(n, BI[bone])
        for pb, cb, pt, dr, rad in BOUNDS:
            if bone not in (pb, cb): continue
            rel = V - pt; t = rel @ dr; perp = np.linalg.norm(rel - np.outer(t, dr), axis=1)
            w = np.clip(0.5 - t / (2 * D), 0, CAP) if bone == cb else np.clip(0.5 + t / (2 * D), 0, CAP)
            w = np.where(perp < rad, w, 0); o = BI[pb] if bone == cb else BI[cb]
            take = w > bw; bw = np.where(take, w, bw); bo = np.where(take, o, bo)
        J[:, 1] = bo; W[:, 0] = 1 - bw; W[:, 1] = bw
    return J, W

def normals(V, T):
    N = np.zeros_like(V); f = np.cross(V[T[:, 1]] - V[T[:, 0]], V[T[:, 2]] - V[T[:, 0]])
    for k in range(3): np.add.at(N, T[:, k], f)
    l = np.linalg.norm(N, axis=1, keepdims=True); l[l == 0] = 1
    return N / l

# ---------------- write GLB ----------------
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
    for name, (V, UV, T), mat, bone, soft in parts:
        V = V.astype(np.float32); N = normals(V.astype(float), T).astype(np.float32)
        J, W = weights(V.astype(float), bone, soft)
        prim = {"attributes": {"POSITION": acc(V, 5126, "VEC3", 34962, True), "NORMAL": acc(N, 5126, "VEC3", 34962),
                               "TEXCOORD_0": acc(UV.astype(np.float32), 5126, "VEC2", 34962),
                               "JOINTS_0": acc(J, 5121, "VEC4", 34962), "WEIGHTS_0": acc(W, 5126, "VEC4", 34962)},
                "indices": acc(T.astype(np.uint16).reshape(-1), 5123, "SCALAR", 34963), "material": MI[mat]}
        meshes.append({"name": name, "primitives": [prim]})
        nodes.append({"name": name, "mesh": len(meshes) - 1, "skin": 0}); nodes[0]["children"].append(len(nodes) - 1)
    first = len(nodes)
    for b in BONES:
        p = PARENT[b]; t = P[b] - (P[p] if p else 0)
        nodes.append({"name": b, "translation": [round(float(x), 6) for x in t]})
    for b in BONES:
        if PARENT[b]: nodes[first + BI[PARENT[b]]].setdefault("children", []).append(first + BI[b])
    nodes[0]["children"].append(first + BI["Hips"])
    ibm = np.zeros((len(BONES), 16), np.float32)
    for k, b in enumerate(BONES):
        m = np.eye(4, dtype=np.float32); m[0:3, 3] = -P[b]; ibm[k] = m.T.reshape(-1)
    ibm_acc = acc(ibm, 5126, "MAT4")
    images = [{"bufferView": view(png), "mimeType": "image/png"} for png in TEX]
    gl = {"asset": {"version": "2.0", "generator": "NOSTRAVECTOR Taredesiban builder (rigged, %d bones)" % len(BONES)},
          "scene": 0, "scenes": [{"nodes": [0]}], "nodes": nodes, "meshes": meshes,
          "materials": [dict(name=n, **m) for n, m in MATS],
          "samplers": [{"magFilter": 9729, "minFilter": 9987, "wrapS": 10497, "wrapT": 10497}],
          "images": images, "textures": [{"sampler": 0, "source": i} for i in range(len(images))],
          "skins": [{"name": "Armature", "joints": [first + k for k in range(len(BONES))], "skeleton": first + BI["Hips"], "inverseBindMatrices": ibm_acc}],
          "accessors": accs, "bufferViews": views, "buffers": [{"byteLength": 0}]}
    while len(blob) % 4: blob.append(0)
    gl["buffers"][0]["byteLength"] = len(blob)
    js = json.dumps(gl, separators=(",", ":")).encode()
    while len(js) % 4: js += b" "
    out_b = struct.pack("<4sII", b"glTF", 2, 28 + len(js) + len(blob)) + struct.pack("<I4s", len(js), b"JSON") + js + struct.pack("<I4s", len(blob), b"BIN\x00") + bytes(blob)
    open(out, "wb").write(out_b)
    print(f"{len(parts)} parts, {sum(len(p[1][0]) for p in parts)} vertices, {len(out_b)//1024} KB")

if __name__ == "__main__":
    main(sys.argv[1])
