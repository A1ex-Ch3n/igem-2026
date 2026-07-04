#!/bin/bash
# RBP × receptor ColabFold array. Submit from the fold workspace:
#   python3 split_input.py 40         # -> prints the array range
#   sbatch --array=0-<N>%8 rbp_receptor.sbatch
#SBATCH --job-name=rbp_recep_cf
#SBATCH --account=jespinoza@kgi.edu_1541
#SBATCH --partition=gpu
#SBATCH --gres=gpu:l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=40G
#SBATCH --time=8:00:00
#SBATCH --array=0-0%8          # <-- override on the sbatch line from split_input.py output
#SBATCH --output=logs/cf_%A_%a.out
# %8 = at most 8 array tasks at once (budget guard on the shared 10k-hour allocation).
set -euo pipefail

# workspace = the dir you ran `sbatch` from (holds chunks/, results/)
BASE="${SLURM_SUBMIT_DIR:-$PWD}"
CF="/project/jespinoza_1541/${USER}/localcolabfold/colabfold-conda"
export PATH="$CF/bin:$PATH"
export LD_LIBRARY_PATH="$CF/lib:${LD_LIBRARY_PATH:-}"   # conda libstdc++ (GLIBCXX); do NOT module-load system cuda
cd "$BASE"
mkdir -p logs results

# single_sequence = no MSA -> pure GPU on the l40s, offline, no remote-MMseqs2 queue.
# The default MSA server is rate-limited (~few thousand/day, "submit from a single IP") and
# idles the GPU while waiting, so it's impractical for 7,182 folds. Use single_sequence for
# the screen; re-fold the top-ipTM hits with full MSA (MSA_FLAGS="") afterwards for confidence.
MSA_FLAGS="--msa-mode single_sequence"

CHUNK=$(printf "chunks/chunk_%03d.csv" "$SLURM_ARRAY_TASK_ID")
OUT=$(printf "results/chunk_%03d" "$SLURM_ARRAY_TASK_ID")
echo ">> task $SLURM_ARRAY_TASK_ID : $CHUNK -> $OUT"
colabfold_batch --num-models 1 --num-recycle 3 $MSA_FLAGS "$CHUNK" "$OUT"
echo ">> task $SLURM_ARRAY_TASK_ID done"
