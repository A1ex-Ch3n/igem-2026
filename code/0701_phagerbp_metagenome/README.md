# 0701 — PhageRBPdetect v4 on the soil metagenomes

De novo RBP (receptor binding protein) detection over the MG08/MG09 metagenome proteomes,
using [dimiboeckaerts/PhageRBPdetection](https://github.com/dimiboeckaerts/PhageRBPdetection).
Complementary to the homology-based `code/0623_metagenome_rbp/` pipeline: this one classifies
each protein directly, so it can flag RBPs with no match in the literature RBP DB.

## Method
- **Model:** PhageRBPdetect **v4** — fine-tuned ESM-2 t12 (~35M params), from Zenodo record
  **14810759**. Binary classifier over protein sequences.
- **Score / call:** `score = softmax(logits)[:,1]`; `preds = argmax` (i.e. RBP iff score ≥ 0.5).
  We keep the tool's default 0.5 boundary and report full scores so a stricter cutoff can be
  applied later.
- **Inputs:** the delivered Prodigal proteomes `MG08.faa` (706,108) and `MG09.faa` (650,535) —
  no gene-calling needed.

## How to run
On Laguna (L40S GPU). Full copy-paste steps in [`laguna/GUIDE.md`](laguna/GUIDE.md): sparse-clone
this branch → `bash laguna/setup_env.sh` → `bash laguna/run_interactive.sh`. Scripts:
- `run_rbp_inference.py` — batched, resumable inference wrapper (auto-selects CUDA).
- `summarize_rbps.py` — filters `preds==1` and builds the per-sample + combined RBP lists.

## Results
Run on one NVIDIA L40S, ~800 seq/s, **~8 min per metagenome (~16 min total)**.

| Metagenome | proteins | predicted RBPs | rate |
|---|---|---|---|
| MG08 | 706,108 | 632 | 0.09% |
| MG09 | 650,535 | 661 | 0.10% |
| combined | 1,356,643 | 1,293 | — |

Score distribution (both): strongly bimodal, most hits at 0.9–1.0 (MG08 456, MG09 454), the
rest spread across 0.5–0.9.

## Outputs (`output/`, gitignored on Laguna; copy into `code/output/0701_phagerbp_metagenome/`)
- `predictions_MG08.csv`, `predictions_MG09.csv` — every protein: `protein_name, preds, score`.
- `MG08_RBPs.{tsv,faa}`, `MG09_RBPs.{tsv,faa}` — predicted RBPs per metagenome (score-sorted).
- `all_metagenome_RBPs.{tsv,faa}` — the combined RBP list (headline deliverable; FASTA IDs
  prefixed `MG08|` / `MG09|`).

## Caveats
- Metagenome proteomes include **partial genes** (`partial=10/11` fragments); short fragments
  may score less reliably — reported, not filtered.
- No nucleotide contigs shipped for the metagenomes, so partial ORFs can't be extended — we
  classify exactly the delivered proteins.

---
*Log — 2026-07-01: built + validated locally (M2/MPS too slow, ~22 h), moved to Laguna L40S;
ran both metagenomes (1,293 RBPs total) in ~16 min. Branch `phagerbp-metagenome`.*
