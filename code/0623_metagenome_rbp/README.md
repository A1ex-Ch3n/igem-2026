# 0623 — Metagenome / receptor / phage-host pipeline

Finding usable phages for our 3 isolates (sites **9-6-2 / 9-2-1 / 10-10-2**).
No known phage infects them, so we work protein-wise: extract receptor proteins,
find named bacteria that share them and *do* have phages (surrogate hosts), then
(next) mine those phages' RBPs in environmental metagenomes.

Decision flow: `../../documents/2026-06-24_phage_decision_tree.html`
Running conclusions: `../../documents/2026-06-24_strain_phage_conclusions.md`

## Inputs
- 3 ONT bacterial genomes (Bakta), `data/bacteria_genome/` — all *Pseudomonas* sp. (P. putida group, ≈ sp. CM27).
- 2 metagenome proteomes MG08 / MG09, `data/metagenomes/` — the RBP-homolog search space (step 5, not yet run).

## Steps & files
| # | Script / notebook | What it does | Output |
|---|---|---|---|
| — | `data_overview.ipynb` / `.md` | Trace every figure of the delivered genomes + metagenomes | — |
| 1 | `finding_RBPs_literature.ipynb` | Host identity: ANI → CM27 / P. putida group (not aeruginosa/putida); 16S | `out_finding_rbps/` (incl. `ani/ani_matrix.csv`) |
| 2 | `receptor_fasta.py` | Pull receptor-only proteins from each genome (porin, TBDR, OmpA/W, TolC, LptD, FadL, Tsx, usher, flagellin, pilin) | `out_receptor_fasta/` — 264 receptors + `reconciliation_vs_0620.md` |
| 3 | `receptor_ncbi_search.py` | Search receptors vs 395 NCBI Pseudomonas reference proteomes → carriers with known phages (surrogate hosts) | `out_receptor_ncbi/` — `surrogate_hosts.md` (P. putida standout) |
| 4 | *(todo)* | Collect surrogate-host phage RBPs | `list_NCBIprotein` |
| 5 | *(todo)* | Search MG08/MG09 for those RBPs | `list_mg` |

## Running
- Notebooks: anaconda-py3.13 kernel (has `pyfastani`, `biopython`).
- `receptor_fasta.py`: any Python 3 (stdlib only).
- `receptor_ncbi_search.py`: needs Biopython + `mmseqs` + NCBI `datasets`.
  Run with the framework python that has Biopython:
  ```
  PATH="/opt/homebrew/bin:/opt/anaconda3/bin:$PATH" \
  /Library/Frameworks/Python.framework/Versions/3.14/bin/python3 receptor_ncbi_search.py
  ```
  Stages skip if their output exists. The 2 GB Pseudomonas reference DB is
  regenerable under `$CLAUDE_JOB_DIR/tmp/psref` (not committed).

---
*Log: 2026-06-24 — created.*
