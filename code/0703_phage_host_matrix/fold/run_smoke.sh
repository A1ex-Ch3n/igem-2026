#!/bin/bash
# Smoke test: fold the 6 smoke pairs end-to-end on one GPU and time it.
# Run on a GPU node (OnDemand GPU session terminal, or salloc):
#   salloc --account=jespinoza@kgi.edu_1541 --partition=gpu --gres=gpu:l40s:1 \
#          --cpus-per-task=8 --mem=32G --time=2:00:00
#   bash run_smoke.sh
set -euo pipefail
BASE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"   # this script's workspace
CF="/project/jespinoza_1541/${USER}/localcolabfold/colabfold-conda"
export PATH="$CF/bin:$PATH"
export LD_LIBRARY_PATH="$CF/lib:${LD_LIBRARY_PATH:-}"
cd "$BASE"; mkdir -p results logs

# single_sequence = no MSA -> pure GPU, offline, no remote-MMseqs2 queue (the default MSA
# server is rate-limited to ~a few thousand/day and idles the GPU while it waits). Required
# for a 7k-fold screen. Drop this flag only to re-fold a few TOP hits with full MSA later.
echo ">> folding smoke.csv (6 pairs, 1 model, 3 recycles, single_sequence) — timing..."
time colabfold_batch --num-models 1 --num-recycle 3 --msa-mode single_sequence smoke.csv results/smoke
echo ">> rank_001 score files:"; ls results/smoke/*_scores_rank_001_*.json
echo ">> wall-time ÷ 6 = per-fold cost; × 7182 = full-run GPU-hours."
