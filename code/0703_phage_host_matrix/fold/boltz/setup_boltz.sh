#!/bin/bash
# ONE-TIME Boltz-2 install on Laguna. Run on a node WITH internet egress (login node or an
# OnDemand terminal) — pip + first-run model weights download need egress.
set -euo pipefail

module purge
module load cuda/12.6.3 cudnn gcc 2>/dev/null || echo "WARN: module load partial; continuing"
if ! command -v conda >/dev/null 2>&1; then
  module load anaconda3 2>/dev/null || module load miniconda3 2>/dev/null || true
fi
command -v conda >/dev/null 2>&1 || { echo "ERROR: conda not found — run 'module avail', load anaconda, re-run."; exit 1; }

source "$(conda info --base)/etc/profile.d/conda.sh"
conda env list | grep -q "^boltz " || conda create -n boltz python=3.11 -y
conda activate boltz
pip install --upgrade pip
pip install "boltz[cuda]" -U
# Laguna GPU driver is CUDA 12.4 (found version 12040); boltz[cuda] pulls a too-new torch
# -> "NVIDIA driver too old". Force the cu124 build (--force-reinstall because pip skips a
# same-version wheel even when the CUDA build differs; --no-deps to leave torch's deps alone).
pip install torch --index-url https://download.pytorch.org/whl/cu124 --force-reinstall --no-deps
python -c "import torch; print('torch', torch.__version__, '| cuda', torch.version.cuda)"

echo ">> verifying:"; boltz predict --help >/dev/null 2>&1 && echo ">> boltz OK ($(boltz --version 2>/dev/null || echo installed))" \
    || echo ">> boltz --help FAILED — paste output to Claude"
echo ">> weights auto-download to ~/.boltz on first predict (a few GB, needs egress)."
