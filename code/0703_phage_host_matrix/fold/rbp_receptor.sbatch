#!/bin/bash
# RBP × receptor ColabFold array. Submit from the fold workspace:
#   python3 split_input.py 40         # -> prints the array range
#   sbatch --array=0-<N>%8 rbp_receptor.sbatch
#SBATCH --job-name=rbp_recep_cf
#SBATCH --account=jespinoza@kgi.edu_1541
#SBATCH --partition=gpu
#SBATCH --gres=gpu:l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=40G
#SBATCH --time=8:00:00
#SBATCH --array=0-0%8          # <-- override on the sbatch line from split_input.py output
#SBATCH --output=logs/cf_%A_%a.out
# %8 = at most 8 array tasks at once (budget guard on the shared 10k-hour allocation).
set -euo pipefail

BASE="/project/jespinoza_1541/${USER}/rbp_receptor_fold"
CF="/project/jespinoza_1541/${USER}/localcolabfold/colabfold-conda"   # reuse binding_screen's install
export PATH="$CF/bin:$PATH"
export LD_LIBRARY_PATH="$CF/lib:${LD_LIBRARY_PATH:-}"   # conda libstdc++ (GLIBCXX); do NOT module-load system cuda
cd "$BASE"
mkdir -p logs results

# MSA: default uses the remote MMseqs2 API (needs compute-node egress; slower). If the smoke
# test shows that's blocked or too slow for 7k folds, add:  --msa-mode single_sequence
MSA_FLAGS=""

CHUNK=$(printf "chunks/chunk_%03d.csv" "$SLURM_ARRAY_TASK_ID")
OUT=$(printf "results/chunk_%03d" "$SLURM_ARRAY_TASK_ID")
echo ">> task $SLURM_ARRAY_TASK_ID : $CHUNK -> $OUT"
colabfold_batch --num-models 1 --num-recycle 3 $MSA_FLAGS "$CHUNK" "$OUT"
echo ">> task $SLURM_ARRAY_TASK_ID done"
