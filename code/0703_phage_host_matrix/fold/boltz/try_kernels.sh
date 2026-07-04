#!/bin/bash
# Try to RE-ENABLE the fast cuequivariance kernels (the --no_kernels pure-torch path is ~13x
# slower: 403s/fold vs ~30-60s with kernels). The kernels failed only because libcue_ops.so
# needs cuBLAS symbol cublasGemmGroupedBatchedEx (cuBLAS 12.5+), and cu124 torch ships cuBLAS
# 12.4. Fix: bump ONLY the cuBLAS pip lib to 12.6 — torch stays cu124 so its driver check
# (on libcudart 12.4) still passes; cuBLAS 12.6 has the symbol and runs on the 12.4 driver via
# CUDA minor-version compatibility. Run on a GPU node:
#   bash try_kernels.sh
# If the libcue_ops symbol error returns, revert: pip install nvidia-cublas-cu12==12.4.5.8
set -euo pipefail
BASE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
module load cuda/12.6.3 cudnn gcc 2>/dev/null || true
command -v conda >/dev/null 2>&1 || module load anaconda3 2>/dev/null || true
source "$(conda info --base)/etc/profile.d/conda.sh"; conda activate boltz
cd "$BASE"

echo ">> bumping cuBLAS to 12.6 (keeps torch cu124; only swaps the cuBLAS runtime lib)"
pip install "nvidia-cublas-cu12>=12.6,<12.7"
python -c "import torch; print('torch', torch.__version__, '| cuda', torch.version.cuda, '| avail', torch.cuda.is_available())"

echo ">> smoke WITH kernels (NO --no_kernels). Timing 6 folds..."
time boltz predict smoke_input --out_dir results/smoke_kernels \
     --accelerator gpu --devices 1 --diffusion_samples 1 --recycling_steps 3 \
     --output_format pdb --cache "$HOME/.boltz"
echo ">> if this finished without a libcue_ops error, per-fold = wall/6. Compare to 403s."
