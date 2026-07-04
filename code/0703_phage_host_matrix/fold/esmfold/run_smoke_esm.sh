#!/bin/bash
# ESMFold smoke: fold the 6 smoke pairs and time it. Run INSIDE the active boltz env on a GPU node
# (do NOT re-activate conda here — that broke earlier; activate first, then run):
#   conda activate boltz
#   bash run_smoke_esm.sh
set -euo pipefail
BASE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"; cd "$BASE"
mkdir -p results

echo ">> ESMFold smoke on 6 pairs (first run also downloads ~2.5GB weights) — timing..."
time python3 esmfold_run.py esm_pairs_smoke.tsv results/smoke.csv
echo ">> results:"; cat results/smoke.csv
echo ">> per-fold ~= wall/6 (minus the one-time weight download); x7182 = full-run GPU-hours."
