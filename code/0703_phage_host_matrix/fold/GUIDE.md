# RBP × receptor fold on Laguna — run guide

Fold **114 candidate RBP families × 63 of our overlapped receptors = 7,182 ColabFold
multimer predictions** → ipTM per pair → the final RBP × receptor matrix + heatmap.
Reuses the `binding_screen` ColabFold pattern. ~same scale as the 7,884 they ran.

Inputs (built locally by `step6_build_fold_inputs.py`, in `code/output/0703_phage_host_matrix/fold/`):
`probes.fasta` (114), `receptors_panel.fasta` (63), `all_pairs.csv` (7,182), `smoke.csv` (6),
`probe_map.tsv`, `receptor_map.tsv`.

## Step 0 — prerequisite
LocalColabFold at `/project/jespinoza_1541/$USER/localcolabfold` (already installed for
binding_screen — reuse it). If missing: run `binding_screen/cluster/setup_colabfold.sh`.

## Step 1 — stage to Laguna
Copy the fold folder into `/project/jespinoza_1541/$USER/rbp_receptor_fold/`:
```bash
mkdir -p /project/jespinoza_1541/$USER/rbp_receptor_fold
# from the repo clone on Laguna, or scp from your Mac:
cp code/0703_phage_host_matrix/fold/* \
   code/output/0703_phage_host_matrix/fold/{probes.fasta,receptors_panel.fasta,all_pairs.csv,smoke.csv,probe_map.tsv,receptor_map.tsv} \
   /project/jespinoza_1541/$USER/rbp_receptor_fold/
```
(If `all_pairs.csv` wasn't committed, regenerate it: `python3 step6_build_fold_inputs.py` locally.)

## Step 2 — smoke (measure per-fold cost FIRST)
Grab a GPU (`salloc … --gres=gpu:l40s:1` or OnDemand GPU terminal), then:
```bash
cd /project/jespinoza_1541/$USER/rbp_receptor_fold
bash run_smoke.sh
```
Note the wall-time; ÷6 = per-fold; ×7,182 = full-run GPU-hours. Budget against the shared
10k-hour allocation. If the remote MMseqs2 MSA is slow or blocked (no compute-node egress),
add `--msa-mode single_sequence` to `MSA_FLAGS` in `rbp_receptor.sbatch`.

## Step 3 — split + submit the array
```bash
python3 split_input.py 40           # 7,182 pairs -> 180 chunks; prints: --array=0-179%8
sbatch --array=0-179%8 rbp_receptor.sbatch
```
`%8` caps concurrent tasks (budget guard). Resumable per chunk (re-submit missing chunks).

## Step 4 — collect + heatmap
```bash
python3 collect_results.py results binding_matrix.csv
python3 fold_heatmap.py binding_matrix.csv        # -> rbp_receptor_iptm_heatmap.png
```

## Step 5 — bring results back
Copy `binding_matrix.csv` + `rbp_receptor_iptm_heatmap.png` into
`code/output/0703_phage_host_matrix/fold/` and commit. (Large ColabFold structure outputs
stay on Laguna — regenerable.)

## Caveats
- **Monomer×monomer approximation** — RBPs are usually homotrimers; ipTM here is an
  approximate signal, so treat high ipTM as a wet-lab priority, not proof.
- No fixed ipTM hit threshold; inspect the distribution (binding_screen smoke ipTM ~0.25–0.41).
