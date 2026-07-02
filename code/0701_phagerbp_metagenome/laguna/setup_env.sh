#!/bin/bash
# ONE-TIME setup, run from inside the cloned repo. Needs a node WITH internet.
# Everything (tool, model, conda env) is set up relative to this script — no hardcoded paths.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"   # .../code/0701_phagerbp_metagenome/laguna
PKG="$(dirname "$HERE")"                               # .../code/0701_phagerbp_metagenome
cd "$PKG"

module purge
module load cuda/12.6.3 cudnn gcc 2>/dev/null || echo "WARN: module load partial; continuing"

# 1) tool repo (for the bundled 3-seq sanity FASTA; the model is NOT in git)
[ -d tool ] || git clone --depth 1 https://github.com/dimiboeckaerts/PhageRBPdetection.git tool

# 2) v4 fine-tuned ESM-2 t12 model from Zenodo 14810759 (~126 MB)
if [ ! -d model/RBPdetect_v4_ESMfine ]; then
  mkdir -p model && cd model
  echo ">> downloading v4 model..."
  wget -q -O v4.zip "https://zenodo.org/records/14810759/files/RBPdetect_v4_ESMfine.zip?download=1"
  unzip -q v4.zip && rm -f v4.zip
  cd "$PKG"
fi
echo ">> model files:"; ls model/RBPdetect_v4_ESMfine

# 3) conda env: CUDA PyTorch + transformers + biopython
if ! command -v conda >/dev/null 2>&1; then
  module load anaconda3 2>/dev/null || module load miniconda3 2>/dev/null || module load anaconda 2>/dev/null || true
fi
if ! command -v conda >/dev/null 2>&1; then
  echo "ERROR: 'conda' not found. Run 'module avail', load your anaconda/miniconda module, re-run."
  echo "       Or paste 'module avail' output to Claude."
  exit 1
fi
conda env list | grep -q "^phagerbp " || conda create -n phagerbp python=3.11 -y
# shellcheck disable=SC1091
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate phagerbp
pip install --upgrade pip
pip install torch --index-url https://download.pytorch.org/whl/cu124
pip install transformers biopython pandas tqdm

python -c "import torch,transformers,Bio;print('torch',torch.__version__,'cuda_build',torch.version.cuda,'tf',transformers.__version__)"
echo ">> setup complete. PKG=$PKG"
