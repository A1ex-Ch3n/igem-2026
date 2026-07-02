#!/bin/bash
# Run RBP detection on a GPU node, from inside the cloned repo.
# First get a GPU (OnDemand GPU session, or salloc), then: bash laguna/run_interactive.sh
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"   # .../code/0701_phagerbp_metagenome/laguna
PKG="$(dirname "$HERE")"                               # .../code/0701_phagerbp_metagenome
MODEL="$PKG/model/RBPdetect_v4_ESMfine"
OUT="$PKG/output"; mkdir -p "$OUT"

# Metagenomes live in the shared soil_mgs dir. Confirm names: ls -la /project/jespinoza_1541/soil_mgs/
MGDIR="/project/jespinoza_1541/soil_mgs"
MG08="$MGDIR/MG08.faa"     # <-- 若檔名不同就改這兩行
MG09="$MGDIR/MG09.faa"
for f in "$MG08" "$MG09"; do
  if [ ! -f "$f" ]; then
    echo "ERROR: not found: $f"; echo "Contents of $MGDIR:"; ls -la "$MGDIR"; exit 1
  fi
done

module purge
module load cuda/12.6.3 cudnn gcc 2>/dev/null || true
command -v conda >/dev/null 2>&1 || module load anaconda3 2>/dev/null || true
# shellcheck disable=SC1091
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate phagerbp
export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TOKENIZERS_PARALLELISM=false

echo "=== GPU check ==="
python -c "import torch;print('cuda',torch.cuda.is_available(),torch.cuda.get_device_name(0) if torch.cuda.is_available() else '')"

echo "=== sanity: 3 bundled RBPs should all be preds=1 ==="
python "$PKG/run_rbp_inference.py" --fasta "$PKG/tool/data/sequences.fasta" \
  --model-dir "$MODEL" --out "$OUT/sanity.csv" --batch-size 8
cat "$OUT/sanity.csv"

echo "=== MG08 ==="
time python "$PKG/run_rbp_inference.py" --fasta "$MG08" --model-dir "$MODEL" \
  --out "$OUT/predictions_MG08.csv" --batch-size 256
echo "=== MG09 ==="
time python "$PKG/run_rbp_inference.py" --fasta "$MG09" --model-dir "$MODEL" \
  --out "$OUT/predictions_MG09.csv" --batch-size 256

echo "=== build RBP lists ==="
python "$PKG/summarize_rbps.py" --out-dir "$OUT" \
  --sample MG08 "$OUT/predictions_MG08.csv" "$MG08" \
  --sample MG09 "$OUT/predictions_MG09.csv" "$MG09"
echo "=== done. deliverables in $OUT ==="; ls -la "$OUT"
