"""Build a Catharsis Spawn (an armoured reptilian predator: plated in gunmetal and crimson, clawed, a spined tail
with a blade at the tip, eyes burning red) as a rigged GLB, on the same 18-bone armature as the alien settler.
Character faces +Z, units are metres; the game scales it (2.05 m, the Commander 2.6 m).

usage: python3 build_catharsis_spawn.py out.glb
"""
import io, json, struct, sys
import numpy as np
from PIL import Image

rng = np.random.default_rng(17)

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
SCALE = 1.0  # the game scales it to its own height
P = {k: np.array(v, float) * SCALE for k, v in PIV.items()}

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


def cone(A, B, r, n=10):
    """a cone from base centre A to tip B"""
    A, B = np.array(A, float), np.array(B, float)
    V, UV, T = lathe([(0, 0), (r, 0), (0, np.linalg.norm(B - A))], n)
    return V @ rot_to(B - A).T + A, UV, T

# ---------------- materials ----------------
def scale_png(seed, base, dark):
    g = np.random.default_rng(seed); S = 256
    yy, xx = np.mgrid[0:S, 0:S].astype(float)
    cell = ((np.sin(xx * 0.38) + np.sin(yy * 0.38 + (xx // 8) % 2 * 1.5)) * 0.5)  # overlapping scales
    img = np.zeros((S, S, 3)) + base
    img += (cell[..., None] * 0.5 + 0.5) * (np.array(dark) - np.array(base)) * -0.8
    img += g.normal(0, 3, img.shape)
    buf = io.BytesIO(); Image.fromarray(np.clip(img, 0, 255).astype(np.uint8)).save(buf, "PNG"); return buf.getvalue()

TEX = [scale_png(5, (22, 21, 26), (6, 6, 8))]
MATS = [
    ("Scales", dict(pbrMetallicRoughness=dict(baseColorTexture=dict(index=0), metallicFactor=0.25, roughnessFactor=0.45))),
    ("Gunmetal", dict(pbrMetallicRoughness=dict(baseColorFactor=[0.16, 0.165, 0.18, 1], metallicFactor=0.85, roughnessFactor=0.38))),
    ("Crimson", dict(pbrMetallicRoughness=dict(baseColorFactor=[0.42, 0.035, 0.06, 1], metallicFactor=0.7, roughnessFactor=0.42))),
    ("Claw", dict(pbrMetallicRoughness=dict(baseColorFactor=[0.03, 0.028, 0.03, 1], metallicFactor=0.4, roughnessFactor=0.2))),
    ("Teeth", dict(pbrMetallicRoughness=dict(baseColorFactor=[0.62, 0.58, 0.5, 1], metallicFactor=0.0, roughnessFactor=0.5))),
    ("Maw", dict(pbrMetallicRoughness=dict(baseColorFactor=[0.12, 0.01, 0.02, 1], metallicFactor=0.0, roughnessFactor=0.6))),
    ("Red glow", dict(emissiveFactor=[1.0, 0.06, 0.04], pbrMetallicRoughness=dict(baseColorFactor=[0.9, 0.08, 0.05, 1]))),
]
MI = {n: i for i, (n, _) in enumerate(MATS)}

parts = []
def add(name, mesh, mat, bone, soft=False): parts.append((name, mesh, mat, bone, soft))

# ---------------- limbs: lean and long, plated at the shoulder, forearm, thigh and shin ----------------
for s, sg in (("L", 1), ("R", -1)):
    sh, el, wr = P["UpperArm_" + s], P["LowerArm_" + s], P["Hand_" + s]
    hp, kn, an = P["UpperLeg_" + s], P["LowerLeg_" + s], P["Foot_" + s]
    add(f"Upper arm {s}", capsule(sh, el, 0.052), "Scales", "UpperArm_" + s, True)
    add(f"Pauldron {s}", ellipsoid(sh + [sg * 0.045, 0.045, 0], (0.12, 0.08, 0.12), euler(z=-sg * 0.45), lat=(-0.25, np.pi / 2)), "Crimson", "UpperArm_" + s)
    add(f"Pauldron rim {s}", ellipsoid(sh + [sg * 0.045, 0.03, 0], (0.13, 0.04, 0.13), euler(z=-sg * 0.45), lat=(-0.25, 0.3)), "Gunmetal", "UpperArm_" + s)
    for k in range(3):
        a = sh + [sg * (0.06 + k * 0.03), 0.1 - k * 0.02, -0.04 + k * 0.04]
        add(f"Pauldron spike {s}{k}", cone(a, a + [sg * 0.07, 0.1, -0.02], 0.022), "Crimson", "UpperArm_" + s)
    add(f"Forearm {s}", capsule(el, wr + [0, 0.03, 0], 0.046), "Scales", "LowerArm_" + s, True)
    add(f"Vambrace {s}", capsule(el + (wr - el) * 0.12, el + (wr - el) * 0.82, 0.062, 1.1, 1.05), "Gunmetal", "LowerArm_" + s)
    add(f"Vambrace plate {s}", box((el + wr) / 2 + [sg * 0.035, 0, 0.03], (0.04, np.linalg.norm(wr - el) * 0.55, 0.07), rot_to(wr - el)), "Crimson", "LowerArm_" + s)
    for k in range(2):
        a = el + (wr - el) * (0.3 + k * 0.3) + [sg * 0.06, 0, -0.02]
        add(f"Forearm spike {s}{k}", cone(a, a + [sg * 0.08, 0.03, -0.03], 0.018), "Crimson", "LowerArm_" + s)
    add(f"Hand {s}", ellipsoid(wr + [0, -0.06, 0.015], (0.045, 0.06, 0.035)), "Scales", "Hand_" + s)
    for k in range(4):  # four long claws, curling forward
        b = wr + [sg * (-0.03 + k * 0.02), -0.09, 0.03]
        add(f"Claw {s}{k}", cone(b, b + [sg * (-0.015 + k * 0.01), -0.14, 0.08], 0.012), "Claw", "Hand_" + s)
    add(f"Thigh {s}", capsule(hp, kn, 0.078), "Scales", "UpperLeg_" + s, True)
    add(f"Thigh plate {s}", ellipsoid((hp + kn) / 2 + [sg * 0.035, 0.03, 0.045], (0.052, 0.11, 0.035)), "Crimson", "UpperLeg_" + s)
    add(f"Shin {s}", capsule(kn, an + [0, 0.05, 0], 0.06), "Scales", "LowerLeg_" + s, True)
    add(f"Shin guard {s}", ellipsoid((kn + an) / 2 + [0, 0.02, 0.045], (0.062, 0.16, 0.045)), "Gunmetal", "LowerLeg_" + s)
    add(f"Knee plate {s}", ellipsoid(kn + [0, 0.02, 0.065], (0.068, 0.07, 0.04)), "Crimson", "LowerLeg_" + s)
    add(f"Knee spike {s}", cone(kn + [0, 0.03, 0.09], kn + [0, 0.1, 0.16], 0.024), "Crimson", "LowerLeg_" + s)
    add(f"Foot {s}", ellipsoid(an + [0, -0.05, 0.07], (0.065, 0.05, 0.13)), "Scales", "Foot_" + s)
    add(f"Foot plate {s}", ellipsoid(an + [0, -0.025, 0.05], (0.06, 0.04, 0.09), lat=(0, np.pi / 2)), "Gunmetal", "Foot_" + s)
    for k in range(3):  # three toe claws and a dewclaw
        b = an + [(k - 1) * 0.035, -0.08, 0.17]
        add(f"Toe claw {s}{k}", cone(b, b + [(k - 1) * 0.015, -0.03, 0.1], 0.018), "Claw", "Foot_" + s)
    add(f"Dewclaw {s}", cone(an + [0, -0.05, -0.04], an + [0, -0.1, -0.12], 0.016), "Claw", "Foot_" + s)

# ---------------- body: broad plated chest over a narrow waist ----------------
add("Torso", capsule(P["Spine"] + [0, 0.06, 0], [0, 1.34, 0], 0.15, 1.25, 0.78), "Scales", "Spine", True)
add("Waist", capsule([0, 0.93, 0], [0, 1.06, 0], 0.1, 1.1, 0.85), "Scales", "Spine", True)
add("Pelvis", capsule([-0.08, 0.9, 0], [0.08, 0.9, 0], 0.1), "Scales", "Hips", True)
add("Chest plate", ellipsoid([0, 1.3, 0.07], (0.22, 0.14, 0.1), lat=(-0.5, np.pi / 2)), "Gunmetal", "Spine")
for sg in (1, -1):
    add(f"Chest panel {'L' if sg > 0 else 'R'}", box([sg * 0.085, 1.31, 0.16], (0.1, 0.09, 0.025), euler(y=sg * 0.35, x=-0.15)), "Crimson", "Spine")
add("Heart light", box([0, 1.235, 0.175], (0.045, 0.035, 0.02)), "Red glow", "Spine")
for k in range(3):  # armoured belly segments
    add(f"Belly plate {k}", ellipsoid([0, 1.14 - k * 0.065, 0.1 - k * 0.006], (0.12 - k * 0.01, 0.032, 0.045)), "Gunmetal", "Spine")
add("Belt", torus([0, 0.97, 0.0], 0.13, 0.022, sz=0.8), "Gunmetal", "Hips")
add("Belt light", box([0, 0.97, 0.115], (0.03, 0.02, 0.01)), "Red glow", "Hips")
add("Fauld", box([0, 0.9, 0.1], (0.15, 0.12, 0.025), euler(x=-0.12)), "Crimson", "Hips")
for sg in (1, -1):
    add(f"Hip plate {'L' if sg > 0 else 'R'}", box([sg * 0.15, 0.88, 0.02], (0.045, 0.15, 0.13), euler(z=sg * 0.15)), "Crimson", "Hips")
add("Back plate", ellipsoid([0, 1.3, -0.07], (0.2, 0.15, 0.08), lat=(-0.5, np.pi / 2)), "Gunmetal", "Spine")
for k in range(5):  # spines down the back
    a = np.array([0, 1.42 - k * 0.09, -0.12 + k * 0.006])
    add(f"Back spine {k}", cone(a, a + [0, 0.05, -0.1], 0.022 - k * 0.002), "Gunmetal", "Spine")
add("Gorget", torus([0, 1.45, 0.0], 0.1, 0.03), "Gunmetal", "Neck")
add("Neck", capsule([0, 1.43, 0.0], [0, 1.58, 0.03], 0.062), "Scales", "Neck")

# ---------------- head: an armoured reptile skull, eyes burning, a maw full of teeth ----------------
H = np.array([0, 1.67, 0.04])
add("Skull", ellipsoid(H, (0.1, 0.1, 0.12)), "Scales", "Head")
add("Snout", ellipsoid(H + [0, -0.045, 0.12], (0.075, 0.06, 0.1)), "Scales", "Head")
add("Helm", ellipsoid(H + [0, 0.03, -0.01], (0.115, 0.095, 0.135), lat=(-0.25, np.pi / 2)), "Gunmetal", "Head")
add("Helm brow", box(H + [0, 0.035, 0.115], (0.17, 0.03, 0.045), euler(x=0.3)), "Crimson", "Head")
add("Faceplate", ellipsoid(H + [0, -0.005, 0.16], (0.064, 0.042, 0.06), lat=(-0.1, np.pi / 2)), "Gunmetal", "Head")
for sg, s in ((1, "L"), (-1, "R")):
    add(f"Eye {s}", ellipsoid(H + [sg * 0.052, 0.003, 0.142], (0.03, 0.02, 0.016), euler(z=sg * 0.3)), "Red glow", "Eye_" + s)
    add(f"Cheek guard {s}", box(H + [sg * 0.092, -0.035, 0.05], (0.025, 0.07, 0.12), euler(y=sg * 0.25)), "Crimson", "Head")
    add(f"Horn {s}", cone(H + [sg * 0.085, 0.06, -0.03], H + [sg * 0.17, 0.17, -0.13], 0.025), "Gunmetal", "Head")
    add(f"Horn {s}2", cone(H + [sg * 0.05, 0.085, -0.07], H + [sg * 0.095, 0.19, -0.17], 0.018), "Gunmetal", "Head")
for k in range(4):  # the crest
    a = H + [0, 0.095 - k * 0.01, 0.05 - k * 0.05]
    add(f"Crest {k}", cone(a, a + [0, 0.09 - k * 0.012, -0.04], 0.02), "Gunmetal", "Head")
add("Lower jaw", ellipsoid(H + [0, -0.11, 0.115], (0.068, 0.028, 0.095)), "Scales", "Head")
add("Maw", ellipsoid(H + [0, -0.08, 0.17], (0.058, 0.03, 0.06)), "Maw", "Head")
for k in range(9):  # teeth, top and bottom
    x = (k - 4) * 0.0125; zt = 0.215 - abs(k - 4) * 0.009
    add(f"Tooth top {k}", cone(H + [x, -0.058, zt], H + [x, -0.09, zt + 0.004], 0.0065, 6), "Teeth", "Head")
    add(f"Tooth bottom {k}", cone(H + [x, -0.104, zt - 0.006], H + [x, -0.074, zt - 0.002], 0.0055, 6), "Teeth", "Head")

# ---------------- the tail: from the hips, down and round to one side, spined, a blade at the tip ----------------
pts = []
for k in range(14):
    t = k / 13
    pts.append(np.array([-0.32 * t ** 1.4, 0.9 - 0.7 * t + 0.22 * t ** 2.2, -0.12 - 0.72 * t]))
for k in range(13):
    a, b = pts[k], pts[k + 1]; r = 0.075 - k * 0.0049
    add(f"Tail {k}", capsule(a, b, r), "Scales", "Hips")
    if k % 2 == 0: add(f"Tail plate {k}", ellipsoid((a + b) / 2 + [0, r * 0.6, 0], (r * 1.1, r * 0.55, np.linalg.norm(b - a) * 0.6)), "Crimson" if k % 4 == 0 else "Gunmetal", "Hips")
    add(f"Tail spine {k}", cone((a + b) / 2 + [0, r * 0.8, 0], (a + b) / 2 + [0, r * 0.8 + 0.055, 0] + (a - b) * 0.25, r * 0.4), "Gunmetal", "Hips")
tip, prev = pts[-1], pts[-2]; d = (tip - prev) / np.linalg.norm(tip - prev)
add("Tail blade", cone(tip, tip + d * 0.24 + [0, 0.08, 0], 0.04), "Crimson", "Hips")
add("Tail blade edge", cone(tip + [0, 0.015, 0], tip + d * 0.2 + [0, 0.11, 0], 0.02), "Gunmetal", "Hips")

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

    meshes = []; nodes = [{"name": "CATHARSIS SPAWN", "children": []}]
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
    gl = {"asset": {"version": "2.0", "generator": "NOSTRAVECTOR Catharsis Spawn builder (rigged, %d bones)" % len(BONES)},
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
