#!/bin/bash
#SBATCH --job-name=tier1_cf
#SBATCH --account=jespinoza@kgi.edu_1541
#SBATCH --partition=gpu
#SBATCH --gres=gpu:l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=40G
#SBATCH --time=8:00:00
#SBATCH --array=0-0%8          # <-- set 0-<N> from split_input.py output (e.g. 0-197%8)
#SBATCH --output=logs/tier1_%A_%a.out
# Tier-1 ColabFold screen, one array task per input chunk.
# %8 = at most 8 chunks running at once (budget guard on the shared 10k-hour allocation).
set -euo pipefail

BASE="/project/jespinoza_1541/${USER}/binding_screen"
CF="/project/jespinoza_1541/${USER}/localcolabfold/colabfold-conda"
export PATH="$CF/bin:$PATH"
export LD_LIBRARY_PATH="$CF/lib:${LD_LIBRARY_PATH:-}"   # conda libstdc++ (GLIBCXX); do NOT module-load system cuda
cd "$BASE"
mkdir -p logs results

CHUNK=$(printf "colabfold_input/chunks/chunk_%03d.csv" "$SLURM_ARRAY_TASK_ID")
OUT=$(printf "results/chunk_%03d" "$SLURM_ARRAY_TASK_ID")
echo ">> task $SLURM_ARRAY_TASK_ID : $CHUNK -> $OUT"

colabfold_batch --num-models 1 --num-recycle 3 "$CHUNK" "$OUT"
echo ">> task $SLURM_ARRAY_TASK_ID done"
