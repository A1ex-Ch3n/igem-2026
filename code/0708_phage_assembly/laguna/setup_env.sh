#!/bin/bash
# ONE-TIME setup for the phage assembly + annotation pipeline. Run on a node WITH internet
# (login node or an OnDemand terminal) — it builds conda envs and downloads databases.
# Safe to re-run: existing envs are kept, DBs skip if already present.
#
# The system conda base (/apps/conda) is READ-ONLY, and mamba won't fall back to $HOME, so we
# build envs by PREFIX under the project dir (writable, big quota) and point the pkg cache there too.
#
# Two envs (kept apart so the fussy pharokka solve can't break the assembler):
#   envs/phage_asm = fastp bbmap bowtie2 samtools spades seqtk   (assembly + QC — small, no big DB)
#   envs/pharokka  = pharokka checkv                             (annotation + completeness + DBs)
#
#   bash laguna/setup_env.sh
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"   # .../phage_assembly/laguna
PKG="$(dirname "$HERE")"                               # .../phage_assembly
DB="$PKG/db"
ENVROOT="$PKG/envs"                                    # writable env location (system /apps/conda is read-only)
export CONDA_PKGS_DIRS="$PKG/.conda_pkgs"              # writable pkg cache (system one is read-only too)
# A conda env whose install prefix contains '@' breaks its bundled perl (bowtie2, tRNAscan): perl
# interpolates the '@...' in Config_heavy.pl. $USER here is CChen29@cmc.edu, so DON'T put the
# workspace under it — move phage_assembly/ to a path with no '@'. (Data paths with '@' are fine.)
case "$PKG" in *@*) echo "ERROR: workspace path contains '@' ($PKG). This breaks conda's perl (bowtie2/tRNAscan)."; \
  echo "       Move phage_assembly/ to a path WITHOUT '@', e.g. /project/jespinoza_1541/cchen_phage/phage_assembly"; \
  echo "       (NOT under \$USER = $USER). See laguna/README_RUN.md."; exit 1;; esac
mkdir -p "$DB" "$ENVROOT" "$CONDA_PKGS_DIRS"
cd "$PKG"

# --- conda (same pattern as setup_boltz.sh) ---
if ! command -v conda >/dev/null 2>&1; then
  module load anaconda3 2>/dev/null || module load miniconda3 2>/dev/null || module load anaconda 2>/dev/null || true
fi
command -v conda >/dev/null 2>&1 || { echo "ERROR: conda not found — run 'module avail', load your anaconda module, re-run."; exit 1; }
source "$(conda info --base)/etc/profile.d/conda.sh"
SOLVER=conda; command -v mamba >/dev/null 2>&1 && SOLVER=mamba
echo ">> solver: $SOLVER ; envs -> $ENVROOT ; pkgs -> $CONDA_PKGS_DIRS"

# --- env 1: assembly + QC (small, fast) ---
if [ -d "$ENVROOT/phage_asm" ]; then
  echo ">> env phage_asm exists — skip"
else
  echo ">> creating phage_asm ..."
  $SOLVER create -p "$ENVROOT/phage_asm" -y -c conda-forge -c bioconda fastp bbmap bowtie2 samtools spades seqtk
fi

# --- env 2: annotation + completeness ---
if [ -d "$ENVROOT/pharokka" ]; then
  echo ">> env pharokka exists — skip"
else
  echo ">> creating pharokka ..."
  $SOLVER create -p "$ENVROOT/pharokka" -y -c conda-forge -c bioconda pharokka checkv
fi

# --- databases (need internet on this node) ---
# DB downloads are for annotation/completeness only (best-effort). A failure here WARNS and
# continues — assembly still works, and run_assembly.sbatch skips whichever DB is missing.
conda activate "$ENVROOT/pharokka"
if [ -z "$(ls -A "$DB/pharokka" 2>/dev/null)" ]; then
  echo ">> downloading pharokka DB (~1.5 GB) ..."
  install_databases.py -o "$DB/pharokka" \
    || echo ">> WARN: pharokka DB download failed — pharokka annotation will be skipped at run time. Re-run setup on a better-connected node to enable it."
else echo ">> pharokka DB present — skip"; fi
if ls -d "$DB"/checkv-db-* >/dev/null 2>&1; then
  echo ">> CheckV DB present — skip"
else
  echo ">> downloading CheckV DB (~few GB) ..."
  checkv download_database "$DB" \
    || echo ">> WARN: CheckV DB download failed (SSL/network) — completeness (checkv) will be skipped. Retry later, or fetch it manually (see README_RUN.md)."
fi
conda deactivate

# --- verify the assembler tools are all on PATH (this is what the sbatch needs) ---
echo ">> verifying phage_asm tools:"
conda activate "$ENVROOT/phage_asm"
miss=0
for t in fastp bowtie2 bowtie2-build spades.py samtools bbnorm.sh seqtk; do
  if p=$(command -v "$t"); then printf "   %-14s %s\n" "$t" "$p"; else printf "   %-14s MISSING\n" "$t"; miss=1; fi
done
conda deactivate
[ "$miss" = 0 ] || { echo "ERROR: some phage_asm tools missing — re-run setup or paste output to Claude."; exit 1; }

echo ">> setup complete."
echo "   envs : $ENVROOT/phage_asm (assembly) , $ENVROOT/pharokka (annotation)"
echo "   DBs  : $DB/pharokka  +  $(ls -d "$DB"/checkv-db-* 2>/dev/null | head -1)"
echo "   next : sbatch laguna/run_assembly.sbatch   (from the phage_assembly/ dir)"
