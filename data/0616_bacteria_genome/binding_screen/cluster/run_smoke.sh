#!/bin/bash
# Smoke test: fold the 6 smoke pairs end-to-end on ONE GPU, then you collect + heatmap.
# Run on a GPU node: either an OnDemand "Jupyter (GPU)" session terminal, or:
#   salloc --account=jespinoza@kgi.edu_1541 --partition=gpu --gres=gpu:l40s:1 --cpus-per-task=8 --mem=32G --time=2:00:00
set -euo pipefail

BASE="/project/jespinoza_1541/${USER}/binding_screen"
CF="/project/jespinoza_1541/${USER}/localcolabfold/colabfold-conda"
export PATH="$CF/bin:$PATH"
export LD_LIBRARY_PATH="$CF/lib:${LD_LIBRARY_PATH:-}"   # conda libstdc++ (GLIBCXX); do NOT module-load system cuda
cd "$BASE"

mkdir -p results logs
echo ">> folding smoke.csv (6 pairs, 1 model, 3 recycles)..."
time colabfold_batch --num-models 1 --num-recycle 3 \
     colabfold_input/smoke.csv results/smoke

echo ">> rank_001 score files produced:"
ls results/smoke/*_scores_rank_001_*.json
echo ">> now run:  python3 collect_results.py results/smoke smoke_matrix.csv"
