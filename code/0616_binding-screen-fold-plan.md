---
title: Phage RBP × Receptor Binding Screen — plan
purpose: Predict which surface protein is the phage receptor on 3 Pseudomonas strains by folding phage RBP × receptor and ranking by ipTM/iPAE
last_updated: 2026-06-16
compute: USC CARC "Laguna" (Slurm, L40S GPUs); access via OnDemand (Jupyter/Code Server)
---

# Phage RBP × Receptor Binding Screen

## Goal
For each *Pseudomonas* strain (`10-10-2`, `9-2-1`, `9-6-2`), find **which bacterial surface protein is the phage receptor** by folding phage **RBP × receptor** complexes and ranking by **ipTM / interface PAE** (a protein–protein binding proxy — Boltz-2's affinity head is small-molecule-only and does not apply here).

Two tiers:
- **Tier-1 (screen)** — ColabFold AF2-Multimer, **monomer RBP × monomer receptor**, fast settings, over the full matrix.
- **Tier-2 (confirm)** — top hits re-folded as **trimeric RBP × receptor**, high quality.

Matrix ≈ **36 phage RBPs × ~60 receptors × 3 strains ≈ 6,500 folds**.

## Inputs (corrected 2026-06-16)
- **Phage probes**: 36 dereplicated real *Pseudomonas*-phage RBPs (tail fiber/spike/baseplate spike) from 42 host-filtered RefSeq phages — `binding_screen/pseudomonas_phage_RBP_probes_strict.fasta` → sanitized to `binding_screen/phage_probes/probes.fasta`.
  - NOTE: the colleague's `*_phage_matches*.tsv` is a genome-vs-viral-DB homology dump (Bacillus/Salmonella phages + eukaryotic giant viruses) — **not** an RBP source; do not use it.
- **Receptors**: surface phage-receptor panel per strain (~60) — TonB-dependent/siderophore receptors, porins, type IV pili/fimbriae, flagellin, autotransporters — `binding_screen/receptors_panel/<strain>_receptors.fasta`. Drops Bam/Lpt/Lol assembly, efflux adaptors, TonB/ExbBD energizers, inner-membrane transporters.
- **Manifest**: `binding_screen/manifest/pairs_36x60.csv` (strain, phage_id, receptor_id).

## Milestones
| | Product | Where | GPU? |
|--|---------|-------|------|
| M1 | finalized inputs (probes, receptor panel, manifest) | local | no |
| M2 | Tier-1 `binding_matrix.csv` (ipTM/iPAE per pair) | Laguna | yes |
| **M3** | **per-strain ipTM heatmap (3 PNGs)** | local | no |
| M4 | ranked top-hits table per strain | local | no |
| M5 | Tier-2 trimeric RBP × receptor structures | Laguna | yes |
| M6 | results report (top receptors + method + caveats) | local | no |
| M7 | Tier-2 PyMOL/ChimeraX interface renders | local | no |

## Pipeline
0. **Laguna recon** — done 2026-06-16: GPU partition `gpu` (L40S ×2/node), `conda/25.11.0`, `cuda/12.6.3`+cudnn, no colabfold module (install needed), storage `/project/jespinoza_1541`, slurm account `jespinoza@kgi.edu_1541`. Access via OnDemand (SSH key login to laguna1 unresolved; OnDemand Jupyter/Code Server works without keys).
1. **Finalize inputs (local)** — receptor panel filter, sanitize/recluster probes, manifest, ColabFold input CSVs.
2. **Fold runner + Slurm array** — `colabfold_batch`, Tier-1 fast (`--num-models 1 --num-recycle 3 --rank iptm`, no templates). Precompute single-chain MSAs once per unique sequence (~216), then assemble per complex.
3. **Smoke test** — 2–3 pairs + a positive control; confirm ipTM JSON.
4. **Full Tier-1** — Slurm array; log failures.
5. **Collect & heatmap (local)** — parse JSON → `binding_matrix.csv` → per-strain ipTM heatmap → top hits.
6. **Tier-2 + render** — re-fold top hits as trimer; PyMOL interface renders.
7. **Report** — `code/2026-06-16_binding-screen-results.md`.

## Limitations (record for the team)
- **LPS-blind**: many *Pseudomonas* phages use LPS (O-antigen, a polysaccharide) as receptor — not foldable here. All-low-ipTM ≠ no receptor.
- **Probe skew**: probes skew to *P. aeruginosa* phages; hosts are environmental *Pseudomonas_E*. Hits = "receptor classes *Pseudomonas* phages use", a **proxy until the team's own phages are sequenced**.
- Computational screen is hypothesis-generating; definitive receptor ID is genetic (phage-resistant mutant → resequence).

---

## Log
- 2026-06-16 — Plan created. Inputs corrected (dropped contaminated phage_matches list; built 36 Pseudomonas-phage RBP probes via `datasets --host Pseudomonas`). Laguna recon done. Stage 1 (local inputs + heatmap scaffold) started.
