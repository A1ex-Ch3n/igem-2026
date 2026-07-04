# 0703 — Phage–host receptor interaction matrix

Building toward the PI's "interaction matrix": which known Pseudomonas phages could infect
our isolates, judged by whether their host bacteria share receptors with us (clue-level,
homology-based — see the thinking log for the full reasoning).

Full context + decisions: [`documents/2026-07-02_phage_host_receptor_matrix_thinking-log.md`](../../documents/2026-07-02_phage_host_receptor_matrix_thinking-log.md).

**Counts — 54 host strains vs 43 genomes** (different units, both correct): **54** = distinct
PharBP host *name* strings; **43** = distinct NCBI *genomes* they resolve to (53 resolved − 10
that share a genome, e.g. 8 aeruginosa names → PAO1). Use 54 for "PharBP hosts", 43 for
"genomes we compared". `receptor_host_presence.tsv` counts at the 54 host-strain level.

## Scripts
- `build_receptor_by_strain.py` — clusters our 441 receptors (mmseqs 90% id / 80% cov)
  across the 5 sequenced isolates → receptor × strain presence table + repertoire summary.
- `step1_pharbp_hosts.py` — retrieve + clean PharBP's Pseudomonas host list; resolve each
  to an NCBI assembly (strain-preferred) via the `datasets` CLI. **No genome download.**

## Outputs (`code/output/0703_phage_host_matrix/`)
- `receptor_by_strain.tsv` — 144 receptor groups × 5 strains (presence 0/1).
- `receptor_by_strain.md` — per-strain receptor counts by class; core vs strain-specific.
- `pharbp_pseudomonas_hosts.tsv` — 54 hosts → 43 distinct NCBI genomes (Step 1).
- `pharbp_pseudomonas_hosts.md` — resolved/unresolved summary; near-relative hosts ranked.
- `unresolved_hosts.txt` — hosts with no findable genome (1).

## Progress
- ✅ receptor × strain reference table (our isolates)
- ✅ Step 1: PharBP hosts → NCBI genomes (54 hosts, 43 genomes; filter by HOST not phage,
  reproduces PharBP's 6,376 records)
- ✅ Step 2 (`step2_host_receptors.py`): downloaded the 43 genomes, mined 3,850 host
  receptors, mmseqs'd our 144 receptor reps vs each → **host × our-receptor overlap matrix**.
  Validates 0623: P. putida max 99.4% id (57–68 receptors shared ≥90%, KT2440 = 71 phages);
  aeruginosa far (81.7%, 0 shared ≥90%).
- ✅ Step 3 viz (`step3_shared_receptor_heatmap.py`): **host × our-strain heatmap**, colour =
  # receptors shared ≥90%. Only the P. putida group lights up; phage-rich hosts (PAO1 = 767
  phages) share 0 — KT2440 (71 phages, ~48 shared) is the sweet spot. Row labels carry phage counts.
- ✅ Step 4–5 (`step4_pull_rbp_sequences.py`, `step5_rbp_table_and_view.py`): pulled the
  candidate RBPs from PharBP — every RBP whose host shares ≥1 of our receptors at ≥90%
  (8 hosts). **347 RBPs → 201 unique sequences** (KT2440 204, NBRC 98…). Clean table +
  a rough RBP × strain heatmap (host-level colour).
- ✅ Step 6 (`fold/step6_build_fold_inputs.py`): built the RBP × receptor fold inputs —
  201 unique RBPs → **114 families** (mmseqs 90%), overlapped receptors → **63-panel**
  (dropped efflux/LptD) → **7,182 ColabFold pairs**. Laguna run scripts + `fold/GUIDE.md` ready.
- ⏭ On Laguna: smoke-test (measure per-fold cost) → array fold (`%8` budget guard) → collect
  ipTM → `rbp_receptor_iptm_heatmap.png` (the final RBP × receptor matrix).

## Step 4–5 outputs
- `candidate_rbps_table.tsv` — 347 candidate RBPs: phage, host, TF/TSP, length, seq-rep flag,
  per-strain shared-receptor counts.
- `candidate_rbps.faa` / `candidate_rbps_meta.tsv` — sequences (for folding) + metadata.
- RBP × our-strain heatmaps: `rbp_by_strain_heatmap.png` (summary, host-grouped) +
  `rbp_by_strain_detailed.png` (one row per RBP), colour = receptors that isolate shares with
  the RBP's host. (Host-level colour — a candidate-RBP sanity view; RBP × specific receptor
  needs folding.)

## Step 3 outputs
- `shared_receptors_heatmap.png` — host (43 genomes) × our 5 isolates, colour = shared receptors ≥90%.
- `shared_receptors_by_strain.tsv` — the underlying matrix.
- Note: shared-receptors is a HOST-level quantity, so this is the honest axis now; an RBP-level
  heatmap (colour = per-RBP fold score) waits for the fold step.

## Step 2 outputs
- `host_overlap_matrix.tsv` — 144 our-receptors × 43 host genomes, cell = best % identity.
- `host_overlap_summary.{tsv,md}` — hosts ranked by receptors shared with us + PharBP RBP/phages.
- `host_receptor_overlap.tsv` (long) · `host_receptor_counts.tsv` (per-host repertoire).
