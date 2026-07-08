# Fold the 9-2-1 Φ8 RBPs on Laguna ｜ 在 Laguna 上摺疊噬菌體 RBP

Structure-predict the real 9-2-1 Φ8 receptor-binding proteins to (1) confirm the β-helix depolymerase
fold + localize the variable RBD, and (2) re-run the RBP × receptor binding screen with the REAL RBPs.
Uses the ColabFold setup you already have on Laguna (`localcolabfold`, the `rbp_receptor.sbatch` /
`tier1_array.sbatch` array pattern). **Run structure prediction here — do NOT send these novel phage
sequences to public folding APIs.**

## Files
| File | What | Folds |
|---|---|---|
| `structure_monomers.csv` | 4 RBPs as monomers (TS1/0015, TS2/0016, TP/0017, TF/0018) | 4 |
| `structure_tailspike_trimers.csv` | the 2 tailspikes as homotrimers (functional spike) | 2 |
| `binding_screen_pairs.csv` | RBP RBDs × 15 shortlisted 9-2-1 receptors (`id,sequence`, `RBP:receptor`) | 60 |
| `rbd_fragments.faa`, `receptor_shortlist_9-2-1.faa` | source sequences | — |

## Priority order
1. **Structures first (6 folds, cheap, most decisive).** Concatenate `structure_monomers.csv` +
   `structure_tailspike_trimers.csv` and fold with ColabFold. Look for a **right-handed β-helix /
   β-solenoid with a long surface groove** on the tailspikes (0015/0016) → depolymerase → the receptor
   is **LPS O-antigen**, and the groove/active site marks the variable RBD precisely.
2. **Binding screen (60 pairs)** — same array pattern as `data/processed_genome/binding_screen/cluster/`.
   Score by ipTM; this tests the *protein*-receptor (secondary) hypothesis.

## Run (mirror the existing ColabFold array)
```bash
# on Laguna, in a workspace dir (path WITHOUT '@' — see project_laguna_conventions):
CF=/project/jespinoza_1541/$USER/localcolabfold/colabfold-conda
export PATH="$CF/bin:$PATH"; export LD_LIBRARY_PATH="$CF/lib:${LD_LIBRARY_PATH:-}"
mkdir -p logs results
# structures:
cat structure_monomers.csv > structures.csv && tail -n +2 structure_tailspike_trimers.csv >> structures.csv
colabfold_batch --num-models 1 --num-recycle 3 structures.csv results/structures
# binding screen (chunk + array like rbp_receptor.sbatch, or one shot if budget allows):
colabfold_batch --num-models 1 --num-recycle 3 --msa-mode single_sequence binding_screen_pairs.csv results/screen
```
(For the 60-pair screen, reuse `split_input.py` + the `%8` array from the existing cluster scripts to
stay within the shared allocation budget.)

## Interpreting
- **Tailspike is a β-helix with a groove** → depolymerase → **primary receptor = LPS O-antigen**. The
  ipTM protein screen is then only the *secondary* test; pivot receptor validation to the O-antigen
  (host locus OHPLIO_01274–01298, rhamnose pathway) + a wet-lab LPS/O-antigen-mutant assay.
- **High ipTM RBP × a specific OMP/TBDR** → that protein is a candidate (esp. for the tail fiber 0018).
- Full reasoning: [`../RBP_variable_region_analysis.md`](../RBP_variable_region_analysis.md).

---
*Log: 2026-07-08 — created overnight alongside the RBP analysis. Fold inputs use the real sequenced RBPs
(the earlier binding screen used placeholder/junk RBPs).*
