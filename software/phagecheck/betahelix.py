#!/usr/bin/env python3
"""Database-free β-helix / β-solenoid classification of a predicted structure.

Tail-spike depolymerases are built on a right-handed β-helix, and that fold has a
signature no database is needed to see: the **sequence-offset distribution of
backbone hydrogen bonds** (donor N(i) … acceptor O(j), < 3.5 Å, |i-j| > 2).

* α-helix → offset 4 dominates.
* β-helix / β-solenoid → a sustained peak at the **coil period** (~16–26 residues),
  because adjacent coils hydrogen-bond in register.
* β-sandwich or globular → short, non-periodic offsets.

Reported alongside: mean pLDDT (from the B-factor column), Ramachandran β and
helix fractions, the span of the periodic core, and PCA elongation.

Ported from `code/0712_phage_rbp_detect/fold_structure/beta_helix_analysis.py`,
which made the β-helix call for the 9-2-1 Φ8 tail spike without a structure DB.
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np
from Bio.PDB import PDBParser

HBOND_CUTOFF = 3.5        # Å, N···O
MIN_RESIDUES = 30
PERIOD_RANGE = (16, 26)   # plausible β-solenoid coil periods


@dataclass
class FoldCall:
    structure: str
    n_residues: int
    mean_plddt: float
    beta_fraction: float
    helix_fraction: float
    alpha4_count: int
    period: int
    period_peak: int
    core_start: int
    core_end: int
    core_residues: int
    elongation: float
    verdict: str


def _backbone(chain):
    N, CA, C, O, plddt = [], [], [], [], []
    for res in chain:
        if all(atom in res for atom in ("N", "CA", "C", "O")):
            N.append(res["N"].coord)
            CA.append(res["CA"].coord)
            C.append(res["C"].coord)
            O.append(res["O"].coord)
            plddt.append(res["CA"].bfactor)
    return (np.array(N), np.array(CA), np.array(C), np.array(O), np.array(plddt))


def _dihedral(p0, p1, p2, p3) -> float:
    b0, b1, b2 = p0 - p1, p2 - p1, p3 - p2
    b1n = b1 / np.linalg.norm(b1)
    v = b0 - np.dot(b0, b1n) * b1n
    w = b2 - np.dot(b2, b1n) * b1n
    return np.degrees(np.arctan2(np.dot(np.cross(b1n, v), w), np.dot(v, w)))


def ramachandran_fractions(N, CA, C) -> tuple[float, float]:
    """Fraction of residues in the β and the α region of the Ramachandran plot."""
    beta = helix = total = 0
    for i in range(1, len(CA) - 1):
        phi = _dihedral(C[i - 1], N[i], CA[i], C[i])
        psi = _dihedral(N[i], CA[i], C[i], N[i + 1])
        total += 1
        if -180 <= phi <= -40 and 60 <= psi <= 180:
            beta += 1
        elif -160 <= phi <= -30 and -90 <= psi <= -10:
            helix += 1
    return beta / total, helix / total


def hbond_offset_histogram(N, O, max_offset: int = 40) -> np.ndarray:
    offsets = []
    for i in range(len(N)):
        dist = np.linalg.norm(O - N[i], axis=1)
        offsets += [abs(i - j) for j in np.where(dist < HBOND_CUTOFF)[0] if abs(i - j) > 2]
    if not offsets:
        return np.zeros(max_offset + 1, int)
    return np.bincount(np.array(offsets, int), minlength=max_offset + 1)[:max_offset + 1]


def periodic_core(N, O, period: int, tol: int = 2) -> tuple[int, int, int]:
    """Residue span whose H-bonds sit at the coil period — the solenoid core."""
    core = np.zeros(len(N), bool)
    for i in range(len(N)):
        dist = np.linalg.norm(O - N[i], axis=1)
        for j in np.where(dist < HBOND_CUTOFF)[0]:
            if abs(abs(i - j) - period) <= tol:
                core[i] = core[j] = True
    idx = np.where(core)[0]
    return (int(idx.min()), int(idx.max()), int(core.sum())) if len(idx) else (0, 0, 0)


def elongation(CA) -> float:
    """sqrt of the ratio of the first two PCA eigenvalues — 1 is a ball, >2 a rod."""
    ev = np.linalg.eigvalsh(np.cov((CA - CA.mean(0)).T))[::-1]
    return float((ev[0] / max(ev[1], 1e-6)) ** 0.5)


def classify(pdb: str | Path, *, chain_id: str | None = None) -> FoldCall | None:
    """Fold-call one chain of one PDB. Returns None if the chain is too short."""
    model = next(iter(PDBParser(QUIET=True).get_structure("s", str(pdb))))
    chain = model[chain_id] if chain_id else next(iter(model))
    N, CA, C, O, plddt = _backbone(chain)
    if len(CA) < MIN_RESIDUES:
        return None

    beta_frac, helix_frac = ramachandran_fractions(N, CA, C)
    hist = hbond_offset_histogram(N, O)
    far = hist.copy()
    far[:6] = 0                      # ignore the local α/turn offsets
    period = int(np.argmax(far))
    peak = int(far[period])
    core = periodic_core(N, O, period) if peak >= 6 else (0, 0, 0)
    elong = elongation(CA)

    is_bhelix = (PERIOD_RANGE[0] <= period <= PERIOD_RANGE[1] and peak >= 8
                 and core[2] >= 40 and beta_frac >= 0.3 and helix_frac <= 0.35
                 and elong >= 2.0)
    if is_bhelix:
        verdict = "beta-helix"
    elif helix_frac >= 0.6:
        verdict = "alpha-fiber"
    elif hist[4] > 2.5 * peak and helix_frac >= 0.3:
        verdict = "alpha-rich"
    else:
        verdict = "beta-other"

    return FoldCall(
        structure=Path(pdb).stem, n_residues=len(CA),
        mean_plddt=round(float(np.mean(plddt)), 1),
        beta_fraction=round(beta_frac, 2), helix_fraction=round(helix_frac, 2),
        alpha4_count=int(hist[4]), period=period, period_peak=peak,
        core_start=core[0], core_end=core[1], core_residues=core[2],
        elongation=round(elong, 1), verdict=verdict,
    )


def classify_all(pdbs: Iterable[str | Path]) -> list[FoldCall]:
    return [call for call in (classify(p) for p in pdbs) if call is not None]


def main(argv: Sequence[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("pdb", nargs="+", help="PDB file(s) to classify")
    ap.add_argument("--out", help="also write the table as TSV to this path")
    args = ap.parse_args(argv)

    calls = classify_all(args.pdb)
    header = (f"{'structure':28s} {'n':>4} {'pLDDT':>6} {'%b':>5} {'%h':>5} "
              f"{'a4':>4} {'per':>4} {'pk':>4} {'core':>11} {'elg':>5}  verdict")
    print(header)
    for c in calls:
        print(f"{c.structure[:28]:28s} {c.n_residues:>4} {c.mean_plddt:>6} "
              f"{c.beta_fraction:>5} {c.helix_fraction:>5} {c.alpha4_count:>4} "
              f"{c.period:>4} {c.period_peak:>4} "
              f"{f'{c.core_start}-{c.core_end}':>11} {c.elongation:>5}  {c.verdict}")
    if args.out and calls:
        fields = list(asdict(calls[0]))
        with open(args.out, "w", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=fields, delimiter="\t")
            writer.writeheader()
            writer.writerows(asdict(c) for c in calls)
        print(f"\nWrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
