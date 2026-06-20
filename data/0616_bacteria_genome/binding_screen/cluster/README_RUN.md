# Tier-1 binding screen — run on Laguna

Everything below runs on USC CARC **Laguna**. You upload via **OnDemand → Files** (drag-drop;
SSH/scp is blocked until your key is registered). Target dir:
`/project/jespinoza_1541/<your_user>/binding_screen/`

## What to upload
Upload `binding_screen_upload.zip` (made for you) and unzip it on the cluster, OR upload these:
```
colabfold_input/      all_pairs.csv, 10-10-2.csv, 9-2-1.csv, 9-6-2.csv, smoke.csv
cluster/              setup_colabfold.sh, run_smoke.sh, split_input.py, tier1_array.sbatch
collect_results.py    (stdlib only — runs on the cluster)
manifest/pairs_36x60.csv   (reference)
```
`make_heatmap.py` stays on your laptop (needs matplotlib; run it there after downloading the matrix).

## Steps

**1. Unzip + check (OnDemand Jupyter terminal)**
```bash
cd /project/jespinoza_1541/$USER
unzip -o binding_screen_upload.zip       # creates binding_screen/
cd binding_screen
wc -l colabfold_input/all_pairs.csv      # expect 7885 (7884 + header)
```

**2. Install ColabFold — ONCE (needs internet on the node)**
```bash
bash cluster/setup_colabfold.sh
```
If `wget` hangs/fails → compute nodes have no internet; stop and tell Claude (we switch MSA strategy).

**3. Smoke test — 6 pairs on 1 GPU (do this BEFORE the full run)**
Open an OnDemand GPU session (or `salloc ... --partition=gpu --gres=gpu:l40s:1`), then:
```bash
bash cluster/run_smoke.sh
python3 collect_results.py results/smoke smoke_matrix.csv
```
Download `smoke_matrix.csv` → on laptop: `python3 make_heatmap.py smoke_matrix.csv`.
**Note the wall-time per pair** from `run_smoke.sh` — that sets the budget for the full 7,884.

**4. Full Tier-1 (only after smoke looks right)**
```bash
python3 cluster/split_input.py 40        # prints the array range, e.g. 0-197%8
# edit cluster/tier1_array.sbatch  ->  #SBATCH --array=0-197%8   (use the printed number)
sbatch cluster/tier1_array.sbatch
squeue --me                              # monitor
```

**5. Collect → real heatmap**
```bash
python3 collect_results.py results binding_matrix.csv
```
Download `binding_matrix.csv` → on laptop:
```bash
python3 make_heatmap.py binding_matrix.csv     # M3: real per-strain ipTM heatmaps
```

## Caveats / decision points
- **Budget**: shared 10k-hour allocation (11 users). 7,884 folds is significant — the smoke test
  (step 3) tells you the per-pair cost; `%8` in the array caps concurrency. Consider running **one
  strain first** (`colabfold_input/10-10-2.csv`) if budget is tight.
- **MSA mode**: default `colabfold_batch` queries the remote MMseqs2 API per job (needs node
  internet). For 7,884 jobs that's heavy — after the smoke we may switch to precomputed per-sequence
  MSAs or `--msa-mode single_sequence`. Decide with Claude based on smoke timing.
- **Account/QOS**: if jobs reject with an account/QOS error, run `sacctmgr show assoc user=$USER format=account,qos`
  and add the right `#SBATCH --qos=...` line.
