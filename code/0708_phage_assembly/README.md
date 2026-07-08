# 0708 — Phage genome assembly

Assemble + annotate the first returned phage genome, **9-2-1 Φ8** (vendor `3NKSC3`), from raw
Illumina reads. Redoes host removal from scratch against our own 9-2-1 host reference (does not
trust the vendor's host-removed files).

Reads + provenance: [`../../data/phage_genome/`](../../data/phage_genome/).
Runs on Laguna — see [`laguna/README_RUN.md`](laguna/README_RUN.md).

## Pipeline (all on Laguna, one SLURM job)
`fastp` trim → `bowtie2` host removal (vs 9-2-1 ref, keep unmapped) → `bbnorm` normalize to ~100×
(data is ~10,000×+ overcovered) → `spades.py --isolate` → validate all contigs (length, coverage,
circularity, read-back) → `pharokka` annotation + `checkv` completeness.

## Files
| File | What |
|---|---|
| `laguna/setup_env.sh` | one-time: build 2 conda envs + download pharokka/CheckV DBs |
| `laguna/run_assembly.sbatch` | the pipeline as a CPU SLURM job |
| `laguna/README_RUN.md` | upload (OnDemand) + run + pull-back steps, caveats |

## Key caveats
- **Overcoverage** — normalization to ~100× is mandatory, not optional.
- **Single-phage origin unconfirmed** (re-isolation rounds 2 & 3 never done) → inspect *all* contigs;
  metaSPAdes fallback if the assembly looks mixed.

Results land in `../../data/phage_genome/9-2-1/assembly/` (large intermediates stay on Laguna).

---
*Log: 2026-07-08 — created. Pipeline scripts written; not yet run on Laguna.*
