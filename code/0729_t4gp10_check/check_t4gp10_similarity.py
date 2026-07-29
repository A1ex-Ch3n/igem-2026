#!/usr/bin/env python3
"""
C5 -- does CDS_0010 carry a T4gp10-like fragment?

Latka et al. 2019 define group D by its first RBP having an N-terminal anchor
that includes a fragment similar to *subdomains D2 and D3* of phage T4 gp10
(their examples map to roughly gp10 res 61-256), detected by HHpred.

HHpred is not available locally and sequence search already came back empty
(phmmer, T4 gp10 and gp9 vs all 80 phage proteins, nothing at E<=10). So this
tests the same claim structurally, which is more sensitive for remote homology.

Reference: 5iv5 chain AC = T4 gp10, fully modelled 1-602, cryo-EM.
Query: Prof. Espinoza's AF3 models.

RMSD alone means nothing without knowing how many residues were aligned and
without controls, so every comparison reports both and the panel includes:
  * positive control -- CDS_0010 anchor vs a real Calx-beta structure (3US9)
  * negative control -- CDS_0012 (GH5 TIM barrel) vs gp10 D2/D3
"""
from pathlib import Path

from pymol import cmd

TMP = Path("/Users/alexy/.claude/jobs/e461b39f/tmp")
FOLDS = Path("/Users/alexy/Desktop/iGEM 26/data/phage_genome/9-2-1/folds_espinoza")

cmd.set("fetch_path", str(TMP))
cmd.set("assembly", "")

# --- reference structures -------------------------------------------------
# 5iv5 chain AC models gp10 completely (602/602, D2/D3 196/196);
# 5hx2 chain G resolves only 83 of the 196 D2/D3 residues and must not be used.
cmd.fetch("5iv5", "gp10_full", type="cif", async_=0)
cmd.create("gp10_d2d3", "gp10_full and chain AC and polymer and resi 61-256")
cmd.create("gp10_all", "gp10_full and chain AC and polymer")
cmd.delete("gp10_full")

cmd.fetch("3us9", "calx_ref", type="pdb1", async_=0)
cmd.create("calx", "calx_ref and polymer and chain A")
cmd.delete("calx_ref")

# --- our models -----------------------------------------------------------
cmd.load(FOLDS / "fold_cds_0010/fold_cds_0010_model_0.cif", "c10_raw")
cmd.create("cds0010", "c10_raw and polymer and chain A")
cmd.create("cds0010_anchor", "c10_raw and polymer and chain A and resi 1-120")
cmd.delete("c10_raw")

cmd.load(FOLDS / "fold_cds_011_trimer/fold_cds_011_trimer_model_0.cif", "c11_raw")
cmd.create("cds0011_anchor", "c11_raw and polymer and chain A and resi 1-120")
cmd.delete("c11_raw")

cmd.load(FOLDS / "fold_cds_0012/fold_cds_0012_model_0.cif", "c12_raw")
cmd.create("cds0012", "c12_raw and polymer and chain A")
cmd.delete("c12_raw")

for o in ("gp10_d2d3", "gp10_all", "calx", "cds0010", "cds0010_anchor",
          "cds0011_anchor", "cds0012"):
    n = cmd.count_atoms(f"{o} and name CA")
    print(f"  {o:16s} {n:4d} residues")

print()


def span(aln_name: str, obj: str) -> str:
    """Which residues of `obj` took part in the alignment."""
    idx = {i for (o, i) in
           [p for pair in cmd.get_raw_alignment(aln_name) for p in pair]
           if o == obj}
    if not idx:
        return "-"
    resis = set()
    for i in idx:
        cmd.iterate(f"{obj} and index {i}", "resis.add(int(resi))",
                    space={"resis": resis})
    return f"{min(resis)}-{max(resis)}" if resis else "-"


def test(label: str, target: str, mobile: str) -> None:
    cmd.delete("aln")
    try:
        r = cmd.cealign(target, mobile, object="aln")
    except Exception as e:                                    # noqa: BLE001
        print(f"  {label:52s} FAILED  {e}")
        return
    print(f"  {label:52s} RMSD {r['RMSD']:5.2f} A over {r['alignment_length']:3d} res"
          f"   [{mobile} {span('aln', mobile)}]")


print("=== TEST — is there a T4gp10 D2/D3-like piece in our proteins? ===")
test("gp10 D2/D3  vs  CDS_0010 (full, 917 aa)", "gp10_d2d3", "cds0010")
test("gp10 D2/D3  vs  CDS_0010 anchor (1-120)", "gp10_d2d3", "cds0010_anchor")
test("gp10 D2/D3  vs  CDS_0011 anchor (1-120)", "gp10_d2d3", "cds0011_anchor")
test("gp10 FULL   vs  CDS_0010 (full)", "gp10_all", "cds0010")

print()
print("=== CONTROLS ===")
test("POSITIVE: Calx-beta 3US9  vs  CDS_0010 anchor", "calx", "cds0010_anchor")
test("POSITIVE: Calx-beta 3US9  vs  CDS_0011 anchor", "calx", "cds0011_anchor")
test("NEGATIVE: gp10 D2/D3  vs  CDS_0012 (GH5)", "gp10_d2d3", "cds0012")
test("NEGATIVE: Calx-beta 3US9  vs  CDS_0012 (GH5)", "calx", "cds0012")
