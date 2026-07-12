# 9-2-1 Φ8 RBP × receptor binding screen — ColabFold AF2-multimer + **real MSA**

Fold the 8 union RBPs × 15 receptor shortlist (120 pairs) as AF2-multimer complexes
**with real MSA** (default remote mmseqs2, NOT `--msa-mode single_sequence`), rank by ipTM.
**Run the controls first and gate on them** — the earlier MSA-free run's controls did not
separate, so ipTM was non-informative. This run is only trustworthy if the positives separate here.

## ⚠️ Infra fork — remote MSA needs internet; Laguna batch nodes have NONE
The default MSA hits the remote MMseqs2 server → needs outbound internet. Laguna's **sbatch
compute/GPU nodes have no egress** (that's why the old screen used `single_sequence`). So:

- **Run `colabfold_batch` in an OnDemand *interactive GPU session* that has internet.** Test first:
  ```bash
  curl -sI https://api.colabfold.com | head -1     # ANY HTTP code (200/404/...) = egress OK; timeout/refused/DNS-fail = no egress
  ```
- If that GPU session has **no** egress → we need the two-stage split (fetch MSAs on an internet
  terminal, fold offline on the GPU node). Ping me and I'll build it (needs your colabfold version).

Only **23 unique sequences** need MSA (8 RBP + 15 receptor), so remote is fine at this scale
(the old rate-limit was thousands of seqs). Note: `colabfold_batch` re-fetches MSA per job, so
129 folds ≈ many redundant queries — tolerable here; if the server throttles, ask for the
precompute-MSA-once version.

## Setup (reuse the shared localcolabfold; NO single_sequence this time)
```bash
CF=/project/jespinoza_1541/$USER/localcolabfold/colabfold-conda
export PATH="$CF/bin:$PATH"; export LD_LIBRARY_PATH="$CF/lib:${LD_LIBRARY_PATH:-}"
```
Build the inputs (local, done in repo): `binding_pairs.csv` (120), `control_pairs.csv` (9) +
`control_key.csv`. Regenerate with `python make_binding_pairs.py` / `make_control_pairs.py`.

## Step 1 — CONTROLS FIRST (9 folds, the go/no-go gate)
```bash
mkdir -p results
colabfold_batch --num-models 3 --num-recycle 3 control_pairs.csv results/controls
python collect_binding.py control results/controls control_key.csv \
  ../../output/0712_phage_rbp_detect/binding/control_scores.csv
```
Read the printed VERDICT:
- **SEPARATE** (min positive ipTM > max negative ipTM) → screen is trustworthy; use min(positive) as the threshold.
- **OVERLAP** → ipTM is non-informative even with MSA (expected risk: cross-kingdom phage×OMP pairs
  have no *paired* MSA). Then STOP — report the matrix as non-informative and pivot to the LPS
  O-antigen hypothesis + structure evidence, don't ship a random-ranked heatmap.

## Step 2 — the 120-pair screen (only if controls separate)
```bash
colabfold_batch --num-models 1 --num-recycle 3 binding_pairs.csv results/screen
python collect_binding.py screen results/screen \
  ../../output/0712_phage_rbp_detect/binding/binding_matrix.csv
```
~129 folds; complex length 532–1783 (mean ~1033). In one OnDemand GPU session, sequential ≈ 8–12 h;
split `binding_pairs.csv` across 2–3 sessions to parallelize. Commit only the CSVs (+ optional
heatmap) from Laguna; structures stay on the cluster.

## Step 3 — refold the single top hit on AlphaFold3 web (independent high-quality check)
Take the top-ipTM RBP×receptor from `binding_matrix.csv`, paste both chains into the
**AlphaFold Server** (alphafoldserver.com; free non-commercial, does its own MSA, ~20–30 jobs/day).
Note: this uploads that one novel phage RBP to Google — acceptable for a single top hit, your call.
Compare AF3's ipTM/interface to ColabFold's.

## Caveats (do not over-read the number)
- ipTM = interface-confidence proxy, **not** a binding affinity / Kd.
- Cross-kingdom RBP×OMP pairs lack a *paired* MSA → MSA improves each monomer but the interface
  signal stays weak; the controls are the arbiter.
- This phage's **primary receptor is likely LPS O-antigen (sugar)** — protein-protein folding can't
  test that. This screen only probes the *secondary* protein-receptor (OMP/TBDR) hypothesis.

---
## Positive controls — provenance (all characterized RBP × OMP protein pairs)
- **pb5 × FhuA** — phage T5 RBP × E. coli ferrichrome transporter; cryo-EM **PDB 8A8C** (pb5 binds as a monomer).
- **gpJrbd × LamB** — phage λ tail protein gpJ (RBD) × E. coli maltoporin.
- **gp54 × LptD** — **Pseudomonas aeruginosa phage DEV**; its gp54/55/56 receptor-binding fiber uses the
  essential OMP LptD (the one genuinely *Pseudomonas* protein–protein positive; most Pseudomonas phage
  receptors are LPS/pili, e.g. PaP1/JG004 → LPS, and are NOT usable in a protein–protein fold).

---
*Log: 2026-07-12 — binding screen prepped (8 union RBP × 15 receptor = 120 pairs) with real-MSA
ColabFold + a 9-fold control gate. Positives reused from 0703 and confirmed by literature (T5 pb5×FhuA
PDB 8A8C; λ gpJ×LamB; Pseudomonas phage DEV gp54×LptD). Laguna run + AF3-web top-hit refold UNDONE.*
