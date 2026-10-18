#!/usr/bin/env python3
"""Sequence + structure comparison of the six expressed constructs.

Covers the three first-set constructs (CDS10_WT, CDS11_WT, CDS12_WT) and the three
CDS_0012 ancestral reconstructions (ANC_Node1 / Node40 / Node281).

Sequence side  : length, MW, pI, extinction, pairwise identity matrix of the mature
                 inserts (pET-28a leader stripped).
Structure side : AlphaFold3 confidences for the full-length CDS_0010/0011/0012 folds
                 (Prof. Espinoza's 2026-07-14/15 server jobs) restricted to the part of
                 the chain that the construct actually expresses, plus ESMFold pLDDT and
                 backbone RMSD for the four CDS_0012-family models folded here.

Outputs -> code/output/1018_construct_structures/
    sequence_identity.csv      pairwise % identity of mature inserts
    construct_comparison.csv   one row per construct, all metrics
    plddt_profiles.csv         per-residue pLDDT of the four ESMFold models
"""
from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

import numpy as np
import pandas as pd
from Bio import SeqIO
from Bio.Align import PairwiseAligner, substitution_matrices
from Bio.PDB import PDBParser, Superimposer
from Bio.PDB.MMCIFParser import MMCIFParser

ROOT = Path(__file__).resolve().parents[2]
FAA = ROOT / "data/expressed_proteins"
FOLDS = ROOT / "data/phage_genome/9-2-1/folds_espinoza"
OUT = ROOT / "code/output/1018_construct_structures"
ESM = OUT / "esmfold"

LEADER = "MGSSHHHHHHSSGLVPRGSHM"

# construct -> (parent protein, 1-based residue range of the parent that was ordered)
# ranges verified in documents/2026-07-27_twist_construct_order/
PARENT = {
    "CDS10_WT": ("CDS_0010", (105, 917)),
    "CDS11_WT": ("CDS_0011", (305, 941)),
    "CDS12_WT": ("CDS_0012", (117, 477)),
}
AF3 = {
    "CDS_0010": FOLDS / "fold_cds_0010",
    "CDS_0011": FOLDS / "fold_cds_011_trimer",
    "CDS_0012": FOLDS / "fold_cds_0012",
}
CDS12_FAMILY = ["CDS12_WT", "CDS12_ANC_Node1", "CDS12_ANC_Node40", "CDS12_ANC_Node281"]


def load_constructs() -> dict[str, dict]:
    out = {}
    for faa in sorted(FAA.glob("*.faa")):
        rec = next(SeqIO.parse(faa, "fasta"))
        fields = [f.strip() for f in rec.description.split("|")]
        meta = {"name": fields[0], "twist_file": fields[1], "vector": fields[2]}
        for f in fields[3:]:
            if "kDa" in f:
                meta["mw_kda"] = float(f.split()[0])
            elif f.startswith("pI"):
                meta["pi"] = float(f.split()[1])
        seq = str(rec.seq)
        meta["full_len"] = len(seq)
        meta["mature"] = seq[len(LEADER):] if seq.startswith(LEADER) else seq
        meta["insert_len"] = len(meta["mature"])
        out[meta["name"]] = meta
    return out


def identity_matrix(seqs: dict[str, str]) -> pd.DataFrame:
    aligner = PairwiseAligner(
        substitution_matrix=substitution_matrices.load("BLOSUM62"),
        open_gap_score=-11, extend_gap_score=-1, mode="global",
    )
    names = list(seqs)
    m = pd.DataFrame(np.nan, index=names, columns=names, dtype=float)
    for a, b in combinations(names, 2):
        aln = aligner.align(seqs[a], seqs[b])[0]
        top, bot = aln[0], aln[1]
        ident = sum(x == y and x != "-" for x, y in zip(top, bot))
        pct = 100 * ident / min(len(seqs[a]), len(seqs[b]))
        m.loc[a, b] = m.loc[b, a] = round(pct, 1)
    for n in names:
        m.loc[n, n] = 100.0
    return m


def af3_metrics(folder: Path, res_range: tuple[int, int]) -> dict:
    name = folder.name
    summary = json.loads((folder / f"{name}_summary_confidences_0.json").read_text())
    full = json.loads((folder / f"{name}_full_data_0.json").read_text())
    plddt = np.asarray(full["atom_plddts"], dtype=float)
    ids = np.asarray(full["token_res_ids"] if "token_res_ids" in full else [], dtype=int)
    out = {
        "af3_ptm": summary.get("ptm"),
        "af3_iptm": summary.get("iptm"),
        "af3_ranking": summary.get("ranking_score"),
        "af3_fraction_disordered": summary.get("fraction_disordered"),
    }
    # per-residue pLDDT over the ordered construct, taken from the CA atoms of chain A
    st = MMCIFParser(QUIET=True).get_structure(name, folder / f"{name}_model_0.cif")
    chain = next(iter(next(iter(st))))
    ca = {r.id[1]: r["CA"].get_bfactor() for r in chain if "CA" in r}
    lo, hi = res_range
    inside = [v for k, v in ca.items() if lo <= k <= hi]
    out["af3_mean_plddt_construct"] = round(float(np.mean(inside)), 1) if inside else None
    out["af3_mean_plddt_full"] = round(float(np.mean(list(ca.values()))), 1)
    out["af3_frac_plddt70_construct"] = (
        round(float(np.mean([v >= 70 for v in inside])), 3) if inside else None
    )
    del plddt, ids
    return out


def esmfold_metrics() -> tuple[dict[str, dict], pd.DataFrame, dict[str, float]]:
    """mean pLDDT per model, per-residue profiles, and RMSD to the CDS12_WT model."""
    parser = PDBParser(QUIET=True)
    models, profiles = {}, []
    structures = {}
    for name in CDS12_FAMILY:
        pdb = ESM / f"{name}.pdb"
        if not pdb.exists():
            continue
        st = parser.get_structure(name, pdb)
        structures[name] = st
        ca = [(r.id[1], r["CA"]) for r in next(iter(next(iter(st)))) if "CA" in r]
        vals = [a.get_bfactor() for _, a in ca]
        models[name] = {
            "esmfold_mean_plddt": round(float(np.mean(vals)), 1),
            "esmfold_frac_plddt70": round(float(np.mean([v >= 70 for v in vals])), 3),
        }
        profiles.append(pd.DataFrame({"construct": name,
                                      "residue": [i for i, _ in ca],
                                      "plddt": vals}))
    rmsd = {}
    if "CDS12_WT" in structures:
        ref_ca = [r["CA"] for r in next(iter(next(iter(structures["CDS12_WT"]))))
                  if "CA" in r]
        for name, st in structures.items():
            if name == "CDS12_WT":
                continue
            ca = [r["CA"] for r in next(iter(next(iter(st)))) if "CA" in r]
            n = min(len(ca), len(ref_ca))  # all four inserts are 361 aa, gap-free
            sup = Superimposer()
            sup.set_atoms(ref_ca[:n], ca[:n])
            rmsd[name] = round(float(sup.rms), 2)
    prof = pd.concat(profiles) if profiles else pd.DataFrame()
    return models, prof, rmsd


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    c = load_constructs()

    ident = identity_matrix({k: v["mature"] for k, v in c.items()})
    ident.to_csv(OUT / "sequence_identity.csv")

    esm_models, prof, rmsd = esmfold_metrics()
    if not prof.empty:
        prof.to_csv(OUT / "plddt_profiles.csv", index=False)

    rows = []
    for name, meta in c.items():
        row = {k: meta[k] for k in
               ("name", "twist_file", "insert_len", "full_len", "mw_kda", "pi")}
        if name in PARENT:
            parent, rng = PARENT[name]
            row["parent"] = parent
            row["parent_residues"] = f"{rng[0]}-{rng[1]}"
            row.update(af3_metrics(AF3[parent], rng))
        else:
            row["parent"] = "CDS_0012 (ancestral reconstruction)"
            row["parent_residues"] = "117-477 equivalent"
        row.update(esm_models.get(name, {}))
        row["esmfold_rmsd_to_CDS12_WT"] = rmsd.get(name)
        row["identity_to_CDS12_WT"] = ident.loc[name, "CDS12_WT"]
        rows.append(row)

    df = pd.DataFrame(rows).sort_values("name")
    df.to_csv(OUT / "construct_comparison.csv", index=False)
    print(df.to_string(index=False))
    print("\nidentity matrix (% over mature insert):")
    print(ident.to_string())


if __name__ == "__main__":
    main()
