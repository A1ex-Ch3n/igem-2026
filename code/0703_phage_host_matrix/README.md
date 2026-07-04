# 0703 — Phage–host receptor interaction matrix

Building toward the PI's "interaction matrix": which known Pseudomonas phages could infect
our isolates, judged by whether their host bacteria share receptors with us (clue-level,
homology-based — see the thinking log for the full reasoning).

Full context + decisions: [`documents/2026-07-02_phage_host_receptor_matrix_thinking-log.md`](../../documents/2026-07-02_phage_host_receptor_matrix_thinking-log.md).

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
- ⏭ Next: join PharBP RBP sequences for the top hosts (P. putida group) → the RBP × receptor
  layer; optional fold/ipTM on the shortlist.

## Step 2 outputs
- `host_overlap_matrix.tsv` — 144 our-receptors × 43 host genomes, cell = best % identity.
- `host_overlap_summary.{tsv,md}` — hosts ranked by receptors shared with us + PharBP RBP/phages.
- `host_receptor_overlap.tsv` (long) · `host_receptor_counts.tsv` (per-host repertoire).
