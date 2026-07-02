#!/bin/bash
# ONE-TIME setup for PhageRBPdetect v4 on Laguna.
# Run on a node WITH internet egress (login node or an OnDemand terminal) — it
# git-clones the tool, downloads the v4 model from Zenodo, and builds a conda env.
# Compute (GPU) nodes may be offline, so do all downloading here.
set -euo pipefail

BASE="/project/jespinoza_1541/${USER}/phagerbp"
mkdir -p "$BASE"
cd "$BASE"

module purge
module load cuda/12.6.3 cudnn gcc 2>/dev/null || echo "WARN: module load partial; continuing"

# 1) tool repo (for the bundled 3-seq sanity FASTA + reference; model is NOT in git)
if [ ! -d PhageRBPdetection ]; then
  git clone --depth 1 https://github.com/dimiboeckaerts/PhageRBPdetection.git
fi

# 2) v4 fine-tuned ESM-2 t12 model from Zenodo record 14810759 (~126 MB zip)
if [ ! -d model/RBPdetect_v4_ESMfine ]; then
  mkdir -p model && cd model
  echo ">> downloading v4 model..."
  wget -q -O RBPdetect_v4_ESMfine.zip \
    "https://zenodo.org/records/14810759/files/RBPdetect_v4_ESMfine.zip?download=1"
  unzip -q RBPdetect_v4_ESMfine.zip && rm -f RBPdetect_v4_ESMfine.zip
  cd "$BASE"
fi
echo ">> model files:"; ls model/RBPdetect_v4_ESMfine

# 3) conda env with CUDA PyTorch + transformers + biopython
if ! command -v conda >/dev/null 2>&1; then
  module load anaconda3 2>/dev/null || module load miniconda3 2>/dev/null || module load anaconda 2>/dev/null || true
fi
if ! command -v conda >/dev/null 2>&1; then
  echo "ERROR: 'conda' not found. Run 'module avail' to find your anaconda/miniconda module,"
  echo "       load it (module load <name>), then re-run this script. Or paste 'module avail' output to Claude."
  exit 1
fi
if ! conda env list | grep -q "^phagerbp "; then
  conda create -n phagerbp python=3.11 -y
fi
# shellcheck disable=SC1091
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate phagerbp
pip install --upgrade pip
# CUDA 12.x PyTorch wheel (bundles its own CUDA runtime; needs only the NVIDIA driver)
pip install torch --index-url https://download.pytorch.org/whl/cu124
pip install transformers biopython pandas tqdm

echo ">> verifying torch/CUDA (note: login nodes usually have NO GPU — CUDA=True is confirmed later on the GPU node):"
python -c "import torch,transformers,Bio;print('torch',torch.__version__,'cuda_build',torch.version.cuda,'tf',transformers.__version__)"
echo ">> setup complete. BASE=$BASE"
