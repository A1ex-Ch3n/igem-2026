#!/bin/bash
# RBP × receptor Boltz-2 array (MSA-free). Submit from the workspace:
#   python3 split_boltz.py 40           # prints the array range
#   sbatch --array=0-179%8 boltz.sbatch
#SBATCH --job-name=rbp_recep_boltz
#SBATCH --account=jespinoza@kgi.edu_1541
#SBATCH --partition=gpu
#SBATCH --gres=gpu:l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=40G
#SBATCH --time=8:00:00
#SBATCH --array=0-0%8          # <-- override on the sbatch line from split_boltz.py
#SBATCH --output=logs/boltz_%A_%a.out
set -euo pipefail

BASE="${SLURM_SUBMIT_DIR:-$PWD}"
module load cuda/12.6.3 cudnn gcc 2>/dev/null || true
command -v conda >/dev/null 2>&1 || module load anaconda3 2>/dev/null || true
source "$(conda info --base)/etc/profile.d/conda.sh"; conda activate boltz
cd "$BASE"; mkdir -p logs results

CH=$(printf "chunks/chunk_%03d" "$SLURM_ARRAY_TASK_ID")
OUT=$(printf "results/chunk_%03d" "$SLURM_ARRAY_TASK_ID")
echo ">> task $SLURM_ARRAY_TASK_ID : $CH -> $OUT"
boltz predict "$CH" --out_dir "$OUT" \
     --accelerator gpu --devices 1 --diffusion_samples 1 --recycling_steps 3 \
     --output_format pdb --cache "$HOME/.boltz"
echo ">> task $SLURM_ARRAY_TASK_ID done"
