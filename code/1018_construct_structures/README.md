# 1018 — 3D models and comparison of the six expressed constructs

Structure + sequence comparison of the six pET-28a(+) parts we express, prepared for
the iGEM **Parts** submission: `CDS10_WT`, `CDS11_WT`, `CDS12_WT` (2026-07-27 Twist
order) and `CDS12_ANC_Node1 / _Node40 / _Node281` (second order, filed 2026-09-10).

```bash
conda activate igem2026
python code/1018_construct_structures/fold_ancestors.py      # ESMFold, base env (transformers)
python code/1018_construct_structures/render_constructs.py   # PyMOL panels + figures
python code/1018_construct_structures/compare_constructs.py  # tables
```

> `fold_ancestors.py` needs `transformers`, which lives in the **base** conda env, not
> `igem2026`; `render_constructs.py` needs **PyMOL**, which lives in `igem2026`, not base.
> Run each with the interpreter that has its dependency.

## Structure sources — not equivalent evidence

| Protein | Source | Why |
|---|---|---|
| CDS_0010, CDS_0011 (trimer), CDS_0012 | **AlphaFold3 Server**, Prof. Espinoza, 2026-07-14/15 | real MSA + PDB templates; `data/phage_genome/9-2-1/folds_espinoza/` (gitignored bulk data) |
| CDS12_ANC_Node1/40/281 | **ESMFold v1**, run locally here | the ancestors are reconstructed sequences with no AF3 job; a single-sequence language-model fold, so panels are coloured by pLDDT, not by domain |

The AF3 jobs are the **full-length** proteins. The plasmids carry truncations
(CDS10 res 105–917, CDS11 res 305–941, CDS12 res 117–477, parent numbering —
see [`project CDS numbering convention`](../0716_espinoza_fiber_construct/README.md)),
so each wild-type panel greys out the part of the fold that is **not** in the construct.

## Outputs → [`../output/1018_construct_structures/`](../output/1018_construct_structures/)

| File | What |
|---|---|
| `esmfold/<name>.pdb` | ESMFold models, pLDDT in the B-factor column |
| `panels/*.png` | individual PyMOL renders |
| `fig_constructs_overview.{png,svg}` | 6-panel figure, one per construct |
| `fig_cds12_family.{png,svg}` | WT vs the three ancestors + superposition |
| `construct_comparison.csv` | one row per construct: length, MW, pI, AF3/ESMFold confidence, RMSD |
| `sequence_identity.csv` | pairwise % identity of the mature inserts |
| `plddt_profiles.csv` | per-residue pLDDT of the ESMFold models |

The written comparison lives in
[`documents/2026-10-18_parts_structure_comparison.md`](../../documents/2026-10-18_parts_structure_comparison.md).
