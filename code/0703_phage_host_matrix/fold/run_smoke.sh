#!/bin/bash
# Smoke test: fold the 6 smoke pairs end-to-end on one GPU and time it.
# Run on a GPU node (OnDemand GPU session terminal, or salloc):
#   salloc --account=jespinoza@kgi.edu_1541 --partition=gpu --gres=gpu:l40s:1 \
#          --cpus-per-task=8 --mem=32G --time=2:00:00
#   bash run_smoke.sh
set -euo pipefail
BASE="/project/jespinoza_1541/${USER}/rbp_receptor_fold"
CF="/project/jespinoza_1541/${USER}/localcolabfold/colabfold-conda"
export PATH="$CF/bin:$PATH"
export LD_LIBRARY_PATH="$CF/lib:${LD_LIBRARY_PATH:-}"
cd "$BASE"; mkdir -p results logs

echo ">> folding smoke.csv (6 pairs, 1 model, 3 recycles) — timing per-pair budget..."
time colabfold_batch --num-models 1 --num-recycle 3 smoke.csv results/smoke
echo ">> rank_001 score files:"; ls results/smoke/*_scores_rank_001_*.json
echo ">> divide the wall-time above by 6 = per-fold cost; × 7182 = full-run GPU-hours."
echo ">> if MSA (remote MMseqs2) is slow/blocked, add --msa-mode single_sequence in rbp_receptor.sbatch."
