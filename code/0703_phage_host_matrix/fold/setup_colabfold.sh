#!/bin/bash
# ONE-TIME LocalColabFold install on Laguna. Run on a node WITH internet egress
# (login node or an OnDemand terminal) — it downloads ~5 GB of weights (~15-30 min).
# Installs to /project/jespinoza_1541/$USER/localcolabfold (shared; skip if already there).
set -euo pipefail

BASE="/project/jespinoza_1541/${USER}"
if [ -x "$BASE/localcolabfold/colabfold-conda/bin/colabfold_batch" ]; then
  echo ">> LocalColabFold already installed at $BASE/localcolabfold — skipping."
  exit 0
fi
cd "$BASE"
module purge
module load cuda/12.6.3 cudnn gcc 2>/dev/null || echo "WARN: module load partial; continuing"

echo ">> downloading installer..."
wget -q https://raw.githubusercontent.com/YoshitakaMo/localcolabfold/main/install_colabbatch_linux.sh
echo ">> installing LocalColabFold (~5 GB, 15-30 min)..."
bash install_colabbatch_linux.sh    # creates ./localcolabfold

CF="$BASE/localcolabfold/colabfold-conda/bin"
"$CF/colabfold_batch" --help >/dev/null 2>&1 && echo ">> SELF-TEST OK: $CF/colabfold_batch" \
    || echo ">> SELF-TEST FAILED — paste output to Claude"
