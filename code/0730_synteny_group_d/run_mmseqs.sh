#!/usr/bin/env bash
# 0730 synteny + similarity — mmseqs orthology.
#
# mmseqs breaks on this repo's path space ("iGEM 26"), so run everything in a
# no-space WORK dir (memory: local_env_gotchas). Stage 1 (extract_proteomes.py)
# already writes the .faa there; point WORK at the same place.
#
#   WORK=/tmp/syn/work ./run_mmseqs.sh
set -euo pipefail
WORK="${WORK:?set WORK to a no-space dir holding the .faa from extract_proteomes.py}"
cd "$WORK"
FMT="query,target,pident,alnlen,qlen,tlen,evalue,bits"

# reference reciprocal best hits (the conserved-core ribbons in the figure)
for pair in "T7 phiKMV" "T7 KP32" "phiKMV KP32"; do
  set -- $pair
  mmseqs easy-rbh "$1.faa" "$2.faa" "rbh_${1}_${2}.m8" "rt_${1}_${2}" \
    --format-output "$FMT" -e 1e-3
done

# our phage vs each reference: RBH (strict) + sensitive search (remote homology)
for ref in T7 phiKMV KP32; do
  mmseqs easy-rbh    our_phage.faa "$ref.faa" "rbh_${ref}.m8"  "rt_${ref}"  --format-output "$FMT" -e 1e-3
  mmseqs easy-search our_phage.faa "$ref.faa" "srch_${ref}.m8" "ss_${ref}"  --format-output "$FMT" -s 7.5 -e 1e-3
done

# positive controls (pipeline sanity): φKMV↔T7 should recover ~6 orthologs
echo "phiKMV vs T7 orthologs: $(wc -l < rbh_T7_phiKMV.m8)"
echo "9-2-1 Φ8 vs T7 orthologs: $(wc -l < rbh_T7.m8)"
