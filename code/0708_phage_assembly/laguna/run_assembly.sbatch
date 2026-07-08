#!/bin/bash
#SBATCH --job-name=phage_asm
#SBATCH --account=jespinoza@kgi.edu_1541
#SBATCH --partition=compute          # CPU partition (128 cores / 376 G / 7-day, the default). `gpu` is for folding.
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --time=12:00:00
#SBATCH --output=phage_asm_%j.out    # in the submit dir (phage_assembly/) — no pre-made logs/ needed
#
# Phage assembly + annotation for 9-2-1 Φ8 (vendor 3NKSC3). Redo host removal from RAW.
# PREREQUISITE: run `bash laguna/setup_env.sh` ONCE first (builds the conda envs + DBs).
# Submit from the phage_assembly/ dir:  sbatch laguna/run_assembly.sbatch
# Each stage skips if its output exists, so a re-sbatch resumes after any failure.
#
# Expected layout under the submit dir:
#   reads/3NKSC3_1_9_2_1_ph8_R1.fastq.gz , _R2.fastq.gz      (RAW reads)
#   ref/XH254M_1_sample_1_1_reference.fasta                   (9-2-1 host genome)
#   laguna/  db/  (from setup_env.sh)
set -euo pipefail

BASE="${SLURM_SUBMIT_DIR:-$PWD}"     # the dir you ran `sbatch` from (holds reads/, ref/, db/)
cd "$BASE"
mkdir -p work

R1="reads/3NKSC3_1_9_2_1_ph8_R1.fastq.gz"
R2="reads/3NKSC3_1_9_2_1_ph8_R2.fastq.gz"
REF="ref/XH254M_1_sample_1_1_reference.fasta"
DB="db"
T=${SLURM_CPUS_PER_TASK:-8}

for f in "$R1" "$R2" "$REF"; do
  [ -f "$f" ] || { echo "ERROR: missing input: $f  (upload it under $BASE — see laguna/README_RUN.md)"; exit 1; }
done

# --- conda (assembly is CPU-only; no cuda needed) ---
# Envs live by prefix under the project dir — the system conda base (/apps/conda) is read-only.
ENVROOT="$BASE/envs"
export CONDA_PKGS_DIRS="$BASE/.conda_pkgs"
# env prefix must not contain '@' — it breaks conda's bundled perl (bowtie2/tRNAscan). See README_RUN.md.
case "$BASE" in *@*) echo "ERROR: workspace path contains '@' ($BASE) — breaks conda perl (bowtie2). Move phage_assembly/ to a path without '@'; see laguna/README_RUN.md."; exit 1;; esac
command -v conda >/dev/null 2>&1 || module load anaconda3 2>/dev/null || true
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "$ENVROOT/phage_asm" 2>/dev/null || {
  echo "ERROR: conda env not found at $ENVROOT/phage_asm. Run this ONCE on an internet node first:"
  echo "         cd $BASE && bash laguna/setup_env.sh"
  exit 1; }

echo "===== [1/6] fastp — adapter/quality trim ====="
if [ ! -f work/trim_R1.fastq.gz ]; then
  fastp -i "$R1" -I "$R2" -o work/trim_R1.fastq.gz -O work/trim_R2.fastq.gz \
    --thread "$T" --detect_adapter_for_pe --html work/fastp.html --json work/fastp.json
else echo "  skip — work/trim_R1.fastq.gz exists"; fi

echo "===== [2/6] bowtie2 — remove host (9-2-1) reads ====="
if [ ! -f work/host_idx.1.bt2 ]; then bowtie2-build --threads "$T" "$REF" work/host_idx; fi
if [ ! -f work/nohost_R1.fastq.gz ]; then
  # --un-conc-gz writes the pairs that do NOT align concordantly to the host = phage-enriched reads.
  # 2>log captures the alignment rate (host fraction) for the cross-check vs vendor's 1.9%.
  bowtie2 -x work/host_idx -1 work/trim_R1.fastq.gz -2 work/trim_R2.fastq.gz \
    -p "$T" --no-unal --un-conc-gz "work/nohost_R%.fastq.gz" -S /dev/null 2> work/bowtie2_host.log
  echo "  --- host-removal summary (compare 'aligned concordantly' to vendor 1.9%) ---"; cat work/bowtie2_host.log
fi

echo "===== [3/6] downsample reads (seqtk) ====="
# bowtie2's multi-thread --un-conc-gz writes a MULTI-MEMBER gzip. bbnorm mis-reads it (only ~5700
# of the 8.4M reads) then crashes in downsample. seqtk reads the whole concatenated stream reliably.
# A random subsample to a fixed pair count is plenty of depth for a single phage and light for SPAdes.
# Same -s seed on R1/R2 keeps mates paired.
SUB=600000
if [ ! -f work/norm_R1.fastq.gz ]; then
  n=$(( $(zcat work/nohost_R1.fastq.gz | wc -l) / 4 ))
  echo "  nohost pairs: $n ; subsampling to $SUB (seqtk takes all if fewer)"
  seqtk sample -s100 work/nohost_R1.fastq.gz "$SUB" | gzip > work/norm_R1.fastq.gz
  seqtk sample -s100 work/nohost_R2.fastq.gz "$SUB" | gzip > work/norm_R2.fastq.gz
else echo "  skip — work/norm_R1.fastq.gz exists"; fi

echo "===== [4/6] SPAdes — assemble ====="
if [ ! -f work/assembly/contigs.fasta ]; then
  # --isolate suits high-coverage single-isolate data (we've normalized). If the graph looks mixed
  # (multiple phage-sized contigs / uneven cov), re-run with metaspades.py — see README_RUN.md.
  spades.py --isolate -1 work/norm_R1.fastq.gz -2 work/norm_R2.fastq.gz -o work/assembly -t "$T" -m 48
else echo "  skip — work/assembly/contigs.fasta exists"; fi

echo "===== [5/6] validate contigs ====="
seqtk seq -L 1000 work/assembly/contigs.fasta > work/contigs_min1kb.fasta || true
echo "  --- contigs >= 1 kb (node  length  coverage) ---"
grep '^>' work/contigs_min1kb.fasta | awk -F'_' '{printf "  %-14s len=%-8s cov=%s\n",$1$2,$4,$6}' > work/contig_summary.txt || true
cat work/contig_summary.txt
NPH=$(awk -F'_' '/^>/ && $4>=10000 {n++} END{print n+0}' work/contigs_min1kb.fasta)
echo "  contigs >= 10 kb (phage-sized): $NPH   <-- >1 means possible multi-phage pick"
if [ ! -f work/readback.log ]; then
  bowtie2-build --threads "$T" work/contigs_min1kb.fasta work/asm_idx >/dev/null
  bowtie2 -x work/asm_idx -1 work/nohost_R1.fastq.gz -2 work/nohost_R2.fastq.gz -p "$T" -S /dev/null 2> work/readback.log
fi
echo "  --- read-back mapping rate (want high) ---"; cat work/readback.log

echo "===== [6/6] annotate (pharokka) + completeness (checkv) — best-effort ====="
# Assembly (steps 1-5) is already done + saved. Annotation is optional: if its env/DBs aren't ready,
# we SKIP it (not fail the job) so the genome still lands. Enable later by (re-)running setup_env.sh.
conda deactivate
if conda activate "$ENVROOT/pharokka" 2>/dev/null; then
  if [ -n "$(ls -A "$DB/pharokka" 2>/dev/null)" ] && [ ! -f work/pharokka/pharokka.gff ]; then
    pharokka.py -i work/contigs_min1kb.fasta -o work/pharokka -d "$DB/pharokka" -t "$T" -f || echo "  WARN: pharokka failed — see output above"
  else echo "  skip pharokka (DB missing or already done)"; fi
  CHECKV_DB=$(ls -d "$DB"/checkv-db-* 2>/dev/null | head -1)
  if [ -n "$CHECKV_DB" ] && [ ! -f work/checkv/quality_summary.tsv ]; then
    checkv end_to_end work/contigs_min1kb.fasta work/checkv -d "$CHECKV_DB" -t "$T" || echo "  WARN: checkv failed"
  else echo "  skip checkv (DB missing or already done)"; fi
else
  echo "  pharokka env not found — SKIPPING annotation. Assembly is complete; run setup_env.sh to enable annotation."
fi

echo
echo "===== DONE ====="
echo "Pull back to laptop (data/phage_genome/9-2-1/assembly/):"
echo "  work/contigs_min1kb.fasta  work/contig_summary.txt  work/fastp.html"
echo "  work/bowtie2_host.log  work/readback.log  work/pharokka/  work/checkv/quality_summary.tsv"
