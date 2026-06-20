#!/bin/bash
# One-time ColabFold install on Laguna (run once, on a node with internet egress).
# Installs LocalColabFold under /project/jespinoza_1541/$USER/localcolabfold.
set -euo pipefail

BASE="/project/jespinoza_1541/${USER}"
cd "$BASE"

module purge
module load cuda/12.6.3 cudnn gcc 2>/dev/null || echo "WARN: module load partial; continuing"

# requires internet egress; if this fails, compute nodes are offline -> tell Claude.
echo ">> downloading installer..."
wget -q https://raw.githubusercontent.com/YoshitakaMo/localcolabfold/main/install_colabbatch_linux.sh

echo ">> installing LocalColabFold (downloads ~5GB weights, ~15-30 min)..."
bash install_colabbatch_linux.sh    # creates ./localcolabfold

CF="$BASE/localcolabfold/colabfold-conda/bin"
echo ">> done. colabfold_batch at: $CF/colabfold_batch"
echo ">> add to PATH:  export PATH=\"$CF:\$PATH\""
"$CF/colabfold_batch" --help >/dev/null 2>&1 && echo ">> SELF-TEST OK" || echo ">> SELF-TEST FAILED — paste output to Claude"
