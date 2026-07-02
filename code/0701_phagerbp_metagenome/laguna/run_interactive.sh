#!/bin/bash
# Run the RBP detection on a GPU node, interactively.
#
# STEP 0 — grab a GPU (from a login node / OnDemand shell), then run this script:
#   salloc --account=jespinoza@kgi.edu_1541 --partition=gpu --gres=gpu:l40s:1 \
#          --cpus-per-task=8 --mem=40G --time=2:00:00
#   (or open an OnDemand "Jupyter (GPU)" session and use its terminal)
#
# Then:  bash run_interactive.sh
set -euo pipefail

BASE="/project/jespinoza_1541/${USER}/phagerbp"
MODEL="$BASE/model/RBPdetect_v4_ESMfine"
SCRIPTS="$BASE/scripts"                 # where you put run_rbp_inference.py + summarize_rbps.py
OUT="$BASE/output"; mkdir -p "$OUT"

# Metagenomes live in the shared soil_mgs dir. Confirm exact filenames with:
#   ls -la /project/jespinoza_1541/soil_mgs/
MGDIR="/project/jespinoza_1541/soil_mgs"
MG08="$MGDIR/MG08.faa"
MG09="$MGDIR/MG09.faa"
for f in "$MG08" "$MG09"; do
  if [ ! -f "$f" ]; then
    echo "ERROR: not found: $f"
    echo "Contents of $MGDIR (fix MG08/MG09 above to match):"; ls -la "$MGDIR"
    exit 1
  fi
done

module purge
module load cuda/12.6.3 cudnn gcc 2>/dev/null || true
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate phagerbp

# model dir is fully local -> stay offline even if the compute node has egress
export HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1 TOKENIZERS_PARALLELISM=false

echo "=== GPU check ==="
python -c "import torch;print('cuda',torch.cuda.is_available(),torch.cuda.get_device_name(0) if torch.cuda.is_available() else '')"

echo "=== sanity: 3 bundled RBPs should all be preds=1 ==="
python "$SCRIPTS/run_rbp_inference.py" \
  --fasta "$BASE/PhageRBPdetection/data/sequences.fasta" \
  --model-dir "$MODEL" --out "$OUT/sanity.csv" --batch-size 8
cat "$OUT/sanity.csv"

echo "=== MG08 (706,108 proteins) ==="
time python "$SCRIPTS/run_rbp_inference.py" \
  --fasta "$MG08" --model-dir "$MODEL" \
  --out "$OUT/predictions_MG08.csv" --batch-size 256

echo "=== MG09 (650,535 proteins) ==="
time python "$SCRIPTS/run_rbp_inference.py" \
  --fasta "$MG09" --model-dir "$MODEL" \
  --out "$OUT/predictions_MG09.csv" --batch-size 256

echo "=== build RBP lists ==="
python "$SCRIPTS/summarize_rbps.py" --out-dir "$OUT" \
  --sample MG08 "$OUT/predictions_MG08.csv" "$MG08" \
  --sample MG09 "$OUT/predictions_MG09.csv" "$MG09"

echo "=== done. deliverables in $OUT ==="
ls -la "$OUT"
