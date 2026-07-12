"""
Fold-classify the 9-2-1 Φ8 union RBP structure predictions (real-MSA ColabFold)
WITHOUT a structure DB, to test the β-helix depolymerase hypothesis.

Signature used (DB-free, decisive for solenoids): the sequence-offset distribution
of backbone H-bonds (donor N(i) ... acceptor O(j), <3.5 Å, |i-j|>2).
  - α-helix   -> offset 4
  - β-helix / β-solenoid -> a sustained peak at the COIL PERIOD (~16-24 residues),
    because adjacent coils H-bond in register (parallel β-sheet between rungs)
  - β-sandwich / globular -> short, non-periodic offsets
Plus per-residue pLDDT (B-factor), Ramachandran %β/%helix, and PCA elongation.

Input : code/output/0712_phage_rbp_detect/structure/pdb/*_unrelaxed_rank_001_*.pdb
Output : prints a table; call with an --out path to also write a TSV.
"""

import glob
import os
import sys
import numpy as np
from Bio.PDB import PDBParser

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
PDBDIR = os.path.join(REPO, "code/output/0712_phage_rbp_detect/structure/pdb")
p = PDBParser(QUIET=True)


def backbone(chain):
    N, CA, C, O, pl = [], [], [], [], []
    for r in chain:
        if all(a in r for a in ("N", "CA", "C", "O")):
            N.append(r["N"].coord); CA.append(r["CA"].coord)
            C.append(r["C"].coord); O.append(r["O"].coord); pl.append(r["CA"].bfactor)
    return map(np.array, (N, CA, C, O, pl))


def dih(p0, p1, p2, p3):
    b0, b1, b2 = p0 - p1, p2 - p1, p3 - p2
    b1n = b1 / np.linalg.norm(b1)
    v = b0 - np.dot(b0, b1n) * b1n; w = b2 - np.dot(b2, b1n) * b1n
    return np.degrees(np.arctan2(np.dot(np.cross(b1n, v), w), np.dot(v, w)))


def rama(N, CA, C):
    n = len(CA); b = h = t = 0
    for i in range(1, n - 1):
        phi = dih(C[i - 1], N[i], CA[i], C[i]); psi = dih(N[i], CA[i], C[i], N[i + 1])
        t += 1
        if -180 <= phi <= -40 and 60 <= psi <= 180: b += 1
        elif -160 <= phi <= -30 and -90 <= psi <= -10: h += 1
    return b / t, h / t


def hb_offsets(N, O):
    offs = []
    for i in range(len(N)):
        d = np.linalg.norm(O - N[i], axis=1)
        offs += [abs(i - j) for j in np.where(d < 3.5)[0] if abs(i - j) > 2]
    return np.bincount(np.array(offs, int), minlength=41)[:41] if offs else np.zeros(41, int)


def core_span(N, O, period, tol=2):
    n = len(N); core = np.zeros(n, bool)
    for i in range(n):
        d = np.linalg.norm(O - N[i], axis=1)
        for j in np.where(d < 3.5)[0]:
            if abs(abs(i - j) - period) <= tol: core[i] = core[j] = True
    idx = np.where(core)[0]
    return (int(idx.min()), int(idx.max()), int(core.sum())) if len(idx) else (0, 0, 0)


def elong(CA):
    ev = np.linalg.eigvalsh(np.cov((CA - CA.mean(0)).T))[::-1]
    return float((ev[0] / max(ev[1], 1e-6)) ** 0.5)


def analyze(pdb):
    N, CA, C, O, pl = backbone(list(p.get_structure("x", pdb)[0])[0])
    if len(CA) < 30: return None
    bfrac, hfrac = rama(N, CA, C)
    hist = hb_offsets(N, O); far = hist.copy(); far[:6] = 0
    period = int(np.argmax(far)); peak = int(far[period])
    cs, ce, cn = core_span(N, O, period) if peak >= 6 else (0, 0, 0)
    # β-helix call: dominant far-HB period in the coil range, real core span, β-rich, elongated, low helix
    is_bhelix = (16 <= period <= 26 and peak >= 8 and cn >= 40
                 and bfrac >= 0.3 and hfrac <= 0.35 and elong(CA) >= 2.0)
    return dict(n=len(CA), plddt=round(float(np.mean(pl)), 1), beta=round(bfrac, 2),
                helix=round(hfrac, 2), a4=int(hist[4]), period=period, peak=peak,
                core=f"{cs}-{ce}", core_n=cn, elong=round(elong(CA), 1),
                verdict="beta-helix" if is_bhelix else
                        ("alpha-fiber" if hfrac >= 0.6 else
                         "alpha-rich" if hist[4] > 2.5 * peak and hfrac >= 0.3 else "beta-other"))


NAMES = ["CDS_0002__monomer", "CDS_0014__monomer", "CDS_0015__monomer", "CDS_0016__monomer",
         "CDS_0017__monomer", "CDS_0018__monomer", "CDS_0019__monomer", "CDS_0020__monomer",
         "CDS_0015__trimer", "CDS_0016__trimer", "CDS_0018__trimer"]
COLS = ["structure", "n", "plddt", "beta", "helix", "a4", "period", "peak", "core", "core_n", "elong", "verdict"]


def main():
    rows = []
    hdr = f"{'structure':20s} {'n':>4} {'pLDDT':>5} {'%b':>4} {'%h':>4} {'a4':>3} {'per':>3} {'pk':>3} {'core':>9} {'cn':>3} {'elg':>4}  verdict"
    print(hdr)
    for nm in NAMES:
        g = glob.glob(f"{PDBDIR}/*{nm}_unrelaxed_rank_001*.pdb")
        if not g: continue
        r = analyze(g[0])
        if not r: continue
        rows.append([nm] + [r[k] for k in COLS[1:]])
        print(f"{nm:20s} {r['n']:>4} {r['plddt']:>5} {r['beta']:>4} {r['helix']:>4} {r['a4']:>3} "
              f"{r['period']:>3} {r['peak']:>3} {r['core']:>9} {r['core_n']:>3} {r['elong']:>4}  {r['verdict']}")
    if "--out" in sys.argv:
        out = sys.argv[sys.argv.index("--out") + 1]
        with open(out, "w") as fh:
            fh.write("\t".join(COLS) + "\n")
            for row in rows: fh.write("\t".join(str(x) for x in row) + "\n")
        print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
