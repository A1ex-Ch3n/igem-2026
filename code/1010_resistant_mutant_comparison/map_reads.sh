#!/usr/bin/env bash
# Map every read set onto ONE reference -- the 9-2-1 wild-type assembly -- so all
# pileups share a coordinate frame. 9-2-1 and 9-6-2 are the same clone (100% ANI),
# so 962_mut reads map onto it just as well as onto the 9-6-2 assembly.
#
# Usage:  conda activate igem2026 && bash code/1010_resistant_mutant_comparison/map_reads.sh
# Skips any BAM that already exists. Output -> code/output/1010_resistant_mutant_comparison/bam/
set -euo pipefail
cd "$(dirname "$0")/../.."

REF=data/bacteria_genome/9-2-1/XH254M_1_sample_1_1_reference.fasta
OUT=code/output/1010_resistant_mutant_comparison/bam
T=${THREADS:-8}
mkdir -p "$OUT"

# name  preset  reads...
SETS=(
  "921_mut|map-ont|data/bacteria_genome/9-2-1/resistant_r1_SBYK6W/SBYK6W_1_sample_1_921_mut.fastq.gz"
  "962_mut|map-ont|data/bacteria_genome/9-6-2/resistant_r1_SBYK6W/SBYK6W_2_sample_2_962_mut.fastq.gz"
  "921_wt|map-ont|data/bacteria_genome/9-2-1/reads/SRR39379361_9-2-1_parent.fastq.gz"
  # Illumina reads from the Φ8 sequencing run (3NKSC3): the lysate carried 9-2-1 host DNA,
  # which gives an ONT-independent look at the parent allele at each site.
  "921_wt_illumina|sr|data/phage_genome/9-2-1/3NKSC3_1_9_2_1_ph8_R1.fastq.gz data/phage_genome/9-2-1/3NKSC3_1_9_2_1_ph8_R2.fastq.gz"
)

for s in "${SETS[@]}"; do
  IFS='|' read -r name preset reads <<< "$s"
  bam="$OUT/$name.bam"
  if [[ -s "$bam.bai" ]]; then echo "skip $name (exists)"; continue; fi
  # shellcheck disable=SC2086
  for r in $reads; do [[ -s "$r" ]] || { echo "missing $r -- skipping $name"; continue 2; }; done
  echo "map $name ($preset)"
  # shellcheck disable=SC2086
  minimap2 -t "$T" -ax "$preset" "$REF" $reads 2> "$OUT/$name.minimap2.log" \
    | samtools sort -@ 4 -m 1G -o "$bam" -
  samtools index "$bam"
  samtools flagstat "$bam" > "$OUT/$name.flagstat.txt"
done
