#!/bin/bash
# OPTIONAL batch alternative to run_interactive.sh (fire-and-forget).
# Submit from a login node:  sbatch rbp_inference.sbatch
#SBATCH --job-name=rbp_v4
#SBATCH --account=jespinoza@kgi.edu_1541
#SBATCH --partition=gpu
#SBATCH --gres=gpu:l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=40G
#SBATCH --time=2:00:00
#SBATCH --output=logs/rbp_v4_%j.out
set -euo pipefail

BASE="/project/jespinoza_1541/${USER}/phagerbp"
mkdir -p "$BASE/logs"
cd "$BASE"
bash scripts/run_interactive.sh   # same steps; runs non-interactively under Slurm
