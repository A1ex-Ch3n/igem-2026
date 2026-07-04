#!/bin/bash
# Clean ONE-TIME Boltz-2 install on Laguna. Run on a node WITH internet egress (login node
# or an OnDemand terminal). Recreates the `boltz` conda env from scratch (safe to re-run) and
# installs a torch build that matches the node's CUDA-12.4 driver.
#
#   bash setup_boltz.sh
set -euo pipefail

module purge
module load cuda/12.6.3 cudnn gcc 2>/dev/null || echo "WARN: module load partial; continuing"
if ! command -v conda >/dev/null 2>&1; then
  module load anaconda3 2>/dev/null || module load miniconda3 2>/dev/null || true
fi
command -v conda >/dev/null 2>&1 || { echo "ERROR: conda not found — 'module avail', load anaconda, re-run."; exit 1; }
source "$(conda info --base)/etc/profile.d/conda.sh"

# fresh env (the previous one may be half-broken from a bad torch reinstall)
echo ">> recreating conda env 'boltz'..."
conda deactivate 2>/dev/null || true
conda env remove -n boltz -y 2>/dev/null || true
conda create -n boltz python=3.11 -y
conda activate boltz
pip install --upgrade pip

# 1) Boltz-2 (pulls its torch + all deps; that torch is built for too-new CUDA though)
echo ">> installing boltz..."
pip install "boltz[cuda]"

# 2) swap torch to the cu124 build of the SAME version boltz pinned — this reinstalls torch
#    AND its bundled NVIDIA CUDA runtime libs (libcudart etc.) at cu124 versions, matching the
#    node's 12.4 driver. (Do NOT use --no-deps: that leaves torch without its CUDA libs.)
TVER=$(python -c "import torch; print(torch.__version__.split('+')[0])")
echo ">> boltz pinned torch $TVER; installing its cu124 build..."
pip install "torch==${TVER}" --index-url https://download.pytorch.org/whl/cu124 --force-reinstall \
  || { echo ">> exact version not on cu124 index; falling back to latest cu124 torch"; \
       pip install torch --index-url https://download.pytorch.org/whl/cu124 --force-reinstall; }

# 3) verify (torch.version.cuda must say 12.4; cuda.is_available() is False on a non-GPU node —
#    that's fine, it's confirmed for real by the GPU smoke)
python -c "import torch; print('torch', torch.__version__, '| cuda', torch.version.cuda, '| gpu_here', torch.cuda.is_available())"
boltz predict --help >/dev/null 2>&1 && echo ">> boltz OK" || echo ">> boltz --help FAILED — paste to Claude"
echo ">> done. weights auto-download to ~/.boltz on first predict."
