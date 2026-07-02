#!/bin/bash
# OPTIONAL batch alternative to run_interactive.sh (fire-and-forget).
# Submit from inside the clone:  sbatch laguna/rbp_inference.sbatch
#SBATCH --job-name=rbp_v4
#SBATCH --account=jespinoza@kgi.edu_1541
#SBATCH --partition=gpu
#SBATCH --gres=gpu:l40s:1
#SBATCH --cpus-per-task=8
#SBATCH --mem=40G
#SBATCH --time=2:00:00
#SBATCH --output=rbp_v4_%j.out
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$HERE/run_interactive.sh"
