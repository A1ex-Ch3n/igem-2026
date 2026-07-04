#!/bin/bash
# Smoke: run Boltz-2 on the 6 smoke pairs and time it. On a GPU node:
#   salloc --account=jespinoza@kgi.edu_1541 --partition=gpu --gres=gpu:l40s:1 --cpus-per-task=8 --mem=40G --time=2:00:00
#   bash run_smoke_boltz.sh
set -euo pipefail
BASE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
module load cuda/12.6.3 cudnn gcc 2>/dev/null || true
command -v conda >/dev/null 2>&1 || module load anaconda3 2>/dev/null || true
source "$(conda info --base)/etc/profile.d/conda.sh"; conda activate boltz
cd "$BASE"

echo ">> Boltz-2 on 6 smoke pairs (MSA-free, 1 diffusion sample, 3 recycles) — timing..."
time boltz predict smoke_input --out_dir results/smoke \
     --accelerator gpu --devices 1 --diffusion_samples 1 --recycling_steps 3 \
     --output_format pdb --cache "$HOME/.boltz"
echo ">> confidence files:"; find results/smoke -name 'confidence_*_model_0.json'
echo ">> wall-time ÷ 6 = per-fold; × 7182 = full-run GPU-hours."
