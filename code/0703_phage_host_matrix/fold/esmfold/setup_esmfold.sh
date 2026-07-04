#!/bin/bash
# Install ESMFold (HuggingFace transformers) into the ALREADY-WORKING `boltz` conda env — it
# has a functioning cu124 torch + GPU, so we reuse it instead of re-fighting the torch install.
# HF ESMFold is pure PyTorch (vendored openfold utils, no CUDA kernels) -> none of the Boltz
# cuequivariance/cuBLAS pain. Run INSIDE the active env:
#   conda activate boltz
#   bash setup_esmfold.sh
set -euo pipefail

python -c "import torch; print('torch', torch.__version__, '| cuda', torch.version.cuda, '| avail', torch.cuda.is_available())"
echo ">> installing transformers + accelerate ..."
pip install --upgrade "transformers>=4.40" accelerate
python -c "from transformers import EsmForProteinFolding, AutoTokenizer; print('ESMFold import OK')"
echo ">> done. Model weights (~2.5GB) auto-download to ~/.cache/huggingface on first fold."
