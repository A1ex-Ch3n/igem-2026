# 0703 — Phage–host receptor interaction matrix

Building toward the PI's "interaction matrix": which known Pseudomonas phages could infect
our isolates, judged by whether their host bacteria share receptors with us (clue-level,
homology-based — see the thinking log for the full reasoning).

Full context + decisions: [`documents/2026-07-02_phage_host_receptor_matrix_thinking-log.md`](../../documents/2026-07-02_phage_host_receptor_matrix_thinking-log.md).

## Scripts
- `build_receptor_by_strain.py` — clusters our 441 receptors (mmseqs 90% id / 80% cov)
  across the 5 sequenced isolates → receptor × strain presence table + repertoire summary.

## Outputs (`code/output/0703_phage_host_matrix/`)
- `receptor_by_strain.tsv` — 144 receptor groups × 5 strains (presence 0/1).
- `receptor_by_strain.md` — per-strain receptor counts by class; core vs strain-specific.

## Planned next
Retrieve + clean PharBP's full Pseudomonas host list → download host genomes → annotate
receptors (local or Laguna, code here) → BLAST vs our receptors → host × our-receptor
overlap table → join PharBP RBPs for top hosts.
