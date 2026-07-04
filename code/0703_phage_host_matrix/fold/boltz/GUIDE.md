# RBP × receptor fold on Laguna — **Boltz-2** (MSA-free) 指南

換用 **Boltz-2**(AF3-like,MSA-free 也堪用、~30s/折 vs AF2 的 ~3.5min)。同樣 114 RBP × 63
receptor = 7,182 對,只是換成 Boltz 的 YAML 輸入。走 branch `rbp-receptor-fold` → Laguna →
在 Laguna commit/push 回來。

> 這組腳本我照官方文件寫、**沒在本機測過**,所以 **Step 5 smoke 一定先跑**驗證;有錯就把訊息貼給 Claude。

## Step 1 — session
Code Server (GPU):Account `jespinoza@kgi.edu_1541`、Partition `gpu`、GPU `1×l40s`、CPU `8`、
Mem `40G`、Wall `4:00:00`。(clone / 裝 boltz / 抓權重需 egress → 沒 egress 就在 login node 做。)

## Step 2 — 拉更新(在既有 clone 裡)
```bash
cd /project/jespinoza_1541/$USER/igem-2026
git pull origin rbp-receptor-fold          # 取得新的 fold/boltz/ 腳本
```

## Step 3 — 組裝工作區
```bash
WORK=/project/jespinoza_1541/$USER/rbp_boltz_fold
mkdir -p "$WORK"
cd /project/jespinoza_1541/$USER/igem-2026
cp code/0703_phage_host_matrix/fold/boltz/* "$WORK/"
cp code/0703_phage_host_matrix/fold/fold_heatmap.py "$WORK/"
cp code/output/0703_phage_host_matrix/fold/{probes.fasta,receptors_panel.fasta,probe_map.tsv,receptor_map.tsv} "$WORK/"
cd "$WORK"
python3 make_boltz_inputs.py               # 7,182 個 YAML -> boltz_input/ + smoke_input/(6)
```

## Step 4 — 裝 Boltz-2(一次性,需 egress 的節點)
```bash
bash setup_boltz.sh                         # conda env `boltz` + pip install boltz[cuda]
```

## Step 5 — smoke(先驗證 + 量時間!)
GPU 節點:
```bash
bash run_smoke_boltz.sh
```
應看到 6 個 `confidence_*_model_0.json`,記 `time`。**若報錯**(CLI/YAML 格式),把訊息貼給 Claude。
> Boltz 首跑會下載模型權重(~幾 GB)到 `~/.boltz`,需 egress;之後就快。

## Step 6 — 切塊 + 送 array
```bash
python3 split_boltz.py 40                    # 印出 --array=0-179%8
sbatch --array=0-179%8 boltz.sbatch
squeue -u $USER
```

## Step 7 — 收集 + 熱圖
```bash
python3 collect_boltz.py results binding_matrix.csv
python3 fold_heatmap.py binding_matrix.csv   # -> rbp_receptor_iptm_heatmap.png
```

## Step 8 — 在 Laguna commit + push
```bash
cd /project/jespinoza_1541/$USER/igem-2026
cp "$WORK"/{binding_matrix.csv,rbp_receptor_iptm_heatmap.png} code/output/0703_phage_host_matrix/fold/
git config user.name "CChen29"; git config user.email "CChen29@cmc.edu"
git pull --rebase origin rbp-receptor-fold
git add code/output/0703_phage_host_matrix/fold/binding_matrix.csv \
        code/output/0703_phage_host_matrix/fold/rbp_receptor_iptm_heatmap.png
git commit -m "results(0703): RBP × receptor Boltz-2 ipTM matrix + heatmap
Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
git push origin rbp-receptor-fold
```

## 限制
- MSA-free(`msa: empty`)精度較低但堪用;高 ipTM 當濕實驗優先候選,不是定論。
- Boltz `iptm` = 整體;`protein_iptm` = 只算蛋白-蛋白界面(collect 兩個都存)。
- 若 smoke 每折仍偏慢,可把 `--recycling_steps` 降到 1、或 `--diffusion_samples 1`(已是)。
