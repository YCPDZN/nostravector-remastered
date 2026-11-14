"""Build Timpur IV, First Consul of the Republic of Timpur, as a rigged GLB.

He is a Taredesiban (the body, armour and 18-bone rig come from build_taredesiban.py), crowned:
a gold circlet of nine points with a crimson stone at the brow and teal stones at the others,
the Consul's gold chain across his breastplate, gold cape clasps, a heavy teal mantle in place of
the sheer cape, and a beard gone grey at the edges.

usage: python3 build_timpur_iv.py out.glb   (keep build_taredesiban.py beside it)
"""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_taredesiban as T

T.MATS += [
    ("Gold", dict(pbrMetallicRoughness=dict(baseColorFactor=[1.0, 0.72, 0.28, 1], metallicFactor=1.0, roughnessFactor=0.2))),
    ("Gold dark", dict(pbrMetallicRoughness=dict(baseColorFactor=[0.62, 0.4, 0.12, 1], metallicFactor=1.0, roughnessFactor=0.32))),
    ("Crown stone", dict(emissiveFactor=[0.7, 0.04, 0.08], pbrMetallicRoughness=dict(baseColorFactor=[0.55, 0.02, 0.05, 1], metallicFactor=0.2, roughnessFactor=0.08))),
    ("Mantle", dict(doubleSided=True, emissiveFactor=[0.0, 0.03, 0.03], pbrMetallicRoughness=dict(baseColorFactor=[0.02, 0.16, 0.17, 1], metallicFactor=0.1, roughnessFactor=0.55))),
]
T.MI.clear(); T.MI.update({n: i for i, (n, _) in enumerate(T.MATS)})
for n, m in T.MATS:  # an older Consul: the beard is going grey
    if n == "Beard": m["pbrMetallicRoughness"]["baseColorFactor"] = [0.2, 0.21, 0.24, 1]

# the sheer cape becomes a heavy mantle; the clasps are gold
T.parts[:] = [(nm, mesh, "Mantle" if nm.startswith("Cape ") and "clasp" not in nm else "Gold" if "Cape clasp" in nm else mat, bone, soft) for nm, mesh, mat, bone, soft in T.parts]
add, P, euler = T.add, T.P, T.euler

# the crown: a band around the cranium, a thin upper rim, nine points (the brow point tallest), stones at their feet
CZ, CY, RX, RZ = -0.022, 1.772, 0.083, 0.104
add("Crown band", T.torus([0, CY, CZ], RX, 0.013, sz=RZ / RX, n=40, m=10), "Gold", "Head")
add("Crown rim", T.torus([0, CY + 0.022, CZ], RX * 0.97, 0.006, sz=RZ / RX, n=40, m=8), "Gold dark", "Head")
for k in range(9):
    a = k / 9 * 2 * np.pi                      # k = 0 at the brow (+Z)
    x, z = np.sin(a) * RX * 1.02, CZ + np.cos(a) * RZ * 1.02
    h = 0.062 if k == 0 else 0.046 if k % 2 == 0 else 0.034
    tilt = euler(x=np.cos(a) * 0.22, z=-np.sin(a) * 0.22)  # each point leans a little outward
    add(f"Crown point {k}", T.ellipsoid([x, CY + 0.012 + h * 0.5, z], (0.011, h * 0.55, 0.008), tilt, n=12, rings=8), "Gold", "Head")
    add(f"Crown point tip {k}", T.ellipsoid([x * 1.02, CY + 0.012 + h * 1.02, CZ + (z - CZ) * 1.02], (0.007, 0.007, 0.007), n=10, rings=6), "Gold", "Head")
    add(f"Crown stone {k}", T.ellipsoid([x * 1.08, CY + 0.004, CZ + (z - CZ) * 1.08], (0.012 if k == 0 else 0.007, 0.012 if k == 0 else 0.007, 0.006), euler(y=a), n=12, rings=8),
        "Crown stone" if k == 0 else "Teal inlay", "Head")

# the Consul's chain: gold links in a V from the collar to a medallion at the heart, and gold rims on the pauldrons
for sg in (1, -1):
    A, B = np.array([sg * 0.15, 1.39, 0.1]), np.array([0.0, 1.215, 0.178])
    for i in range(7):
        t = (i + 0.5) / 7; p = A + (B - A) * t + [0, -0.012 * np.sin(t * np.pi), 0.01 * np.sin(t * np.pi)]
        add(f"Chain link {i} {'L' if sg > 0 else 'R'}", T.ellipsoid(p, (0.012, 0.008, 0.006), euler(z=sg * 0.8), n=10, rings=6), "Gold", "Spine")
add("Consul medallion", T.cylinder([0, 1.195, 0.182], 0.03, 0.008, T.rot_to(np.array([0, 0, 1.0])), n=24), "Gold", "Spine")
add("Medallion stone", T.ellipsoid([0, 1.195, 0.188], (0.012, 0.012, 0.006), n=12, rings=8), "Crown stone", "Spine")
for s, sg in (("L", 1), ("R", -1)):
    sh = P["UpperArm_" + s]
    add(f"Pauldron rim {s}", T.ellipsoid(sh + [sg * 0.03, 0.072, 0], (0.122, 0.012, 0.127), euler(z=-sg * 0.45), n=24, rings=6), "Gold dark", "UpperArm_" + s)

if __name__ == "__main__":
    T.main(sys.argv[1])
