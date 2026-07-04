#!/bin/bash
# RBP x receptor ESMFold array. Submit from the workspace:
#   python3 split_esm.py 60           # prints the array range
#   sbatch --array=0-119%8 esmfold.sbatch
#SBATCH --job-name=rbp_recep_esm
#SBATCH --account=jespinoza@kgi.edu_1541
#SBATCH --partition=gpu
#SBATCH --gres=gpu:l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=40G
#SBATCH --time=8:00:00
#SBATCH --array=0-0%8          # <-- override on the sbatch line from split_esm.py
#SBATCH --output=logs/esm_%A_%a.out
set -euo pipefail

BASE="${SLURM_SUBMIT_DIR:-$PWD}"
module load cuda/12.6.3 cudnn gcc 2>/dev/null || true
command -v conda >/dev/null 2>&1 || module load anaconda3 2>/dev/null || true
source "$(conda info --base)/etc/profile.d/conda.sh"; conda activate boltz
cd "$BASE"; mkdir -p logs results

CH=$(printf "chunks/chunk_%03d.tsv" "$SLURM_ARRAY_TASK_ID")
OUT=$(printf "results/chunk_%03d.csv" "$SLURM_ARRAY_TASK_ID")
echo ">> task $SLURM_ARRAY_TASK_ID : $CH -> $OUT"
python3 esmfold_run.py "$CH" "$OUT" --num-recycles 1   # fast PoC bulk run; re-fold top hits with more recycles
echo ">> task $SLURM_ARRAY_TASK_ID done"
