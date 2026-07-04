# RBP × receptor fold on Laguna — **ESMFold** (simple, brute-force)

換到 **ESMFold**(HuggingFace `transformers` 版):純 PyTorch、無 MSA、**無 cuequivariance / cuBLAS
kernel** → 躲開 Boltz 那串 CUDA 地雷。每對 RBP+receptor 用 **glycine linker 串成複合物**折,從
**跨鏈 PAE** 算一個 pseudo-ipTM 當粗結合分數。114 RBP × 63 receptor = 7,182 對。

> **性質**:ESMFold 本是單鏈模型,這裡是「拼複合物」的 hack,分數是**粗排序、非定論**;高分區塊之後再用
> 複合物原生模型細折。這正是你要的「先跑完整矩陣、幾小時出圖,之後再細跑數字」。

> **重用 boltz env**:它已經有跑得動的 cu124 torch + GPU,直接在裡面裝 `transformers` 即可,不用再碰
> torch 安裝。這條路的坎坷全記在 `documents/2026-07-04_folding_tool_odyssey.md`。

---

## Step 1 — session
Code Server (GPU):Account `jespinoza@kgi.edu_1541`、Partition `gpu`、GPU `1×l40s`、CPU `8`、
Mem `40G`、Wall `4:00:00`。(裝 transformers / 抓權重需 egress → 沒 egress 就在 login node 做那兩步。)

## Step 2 — 拉更新
```bash
cd /project/jespinoza_1541/$USER/igem-2026
git pull origin rbp-receptor-fold
```

## Step 3 — 組裝工作區
```bash
WORK=/project/jespinoza_1541/$USER/rbp_esm_fold
mkdir -p "$WORK"
cd /project/jespinoza_1541/$USER/igem-2026
cp code/0703_phage_host_matrix/fold/esmfold/* "$WORK/"
cp code/0703_phage_host_matrix/fold/fold_heatmap.py "$WORK/"
cp code/output/0703_phage_host_matrix/fold/{probes.fasta,receptors_panel.fasta,probe_map.tsv,receptor_map.tsv} "$WORK/"
cd "$WORK"
python3 make_esm_pairs.py            # -> esm_pairs.tsv (7,182) + esm_pairs_smoke.tsv (6)
```

## Step 4 — 裝 ESMFold(一次性,在 boltz env 裡)
```bash
conda activate boltz                 # 重用那顆能跑的 cu124 torch
bash setup_esmfold.sh                # pip install transformers + accelerate
```

## Step 5 — smoke(先驗證 + 量時間!)
GPU 節點、**已 `conda activate boltz`**:
```bash
bash run_smoke_esm.sh                # 折 6 對 + 首次下載 ~2.5GB 權重
```
會印出 `results/smoke.csv`(每列 rbp_id,rec_id,iptm,ptm,pae,plddt,len,status)。記 `time`。
**扣掉一次性抓權重**後 ÷6 = 每折;×7,182 = 全跑 GPU-hr。若報錯把訊息貼給 Claude。

## Step 6 — 切塊 + 送 array
```bash
python3 split_esm.py 60               # 7,182 -> 120 塊;印出 --array=0-119%8
sbatch --array=0-119%8 esmfold.sbatch
squeue -u $USER
```
`esmfold_run.py` 每對即時寫檔且**可續跑**(重跑會跳過已完成的對);array 掛了重送即可。
> 太長(>2000 aa)的對會標 `SKIP_TOOLONG`(~179 對,2.5%),OOM 的標 `OOM` —— 都有記錄,不是靜默丟掉。

## Step 7 — 收集 + 熱圖
```bash
python3 collect_esm.py results binding_matrix.csv
python3 fold_heatmap.py binding_matrix.csv    # -> rbp_receptor_iptm_heatmap.png
```

## Step 8 — 在 Laguna commit + push
```bash
cd /project/jespinoza_1541/$USER/igem-2026
cp "$WORK"/{binding_matrix.csv,rbp_receptor_iptm_heatmap.png} code/output/0703_phage_host_matrix/fold/
git config user.name "CChen29"; git config user.email "CChen29@cmc.edu"
git pull --rebase origin rbp-receptor-fold
git add code/output/0703_phage_host_matrix/fold/binding_matrix.csv \
        code/output/0703_phage_host_matrix/fold/rbp_receptor_iptm_heatmap.png
git commit -m "results(0703): RBP × receptor ESMFold pseudo-ipTM matrix + heatmap
Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
git push origin rbp-receptor-fold
```

## 分數與限制
- **`iptm`** = 跨鏈 PAE 導出的 interface-pTM 代理(0–1,越高=界面相對位置越有把握)。**不是** AF 的 ipTM,
  ESMFold 也不是為複合物訓練的 → 當**粗排序**,高分才進濕實驗/細折。
- 另存 `interchain_pae_min/mean`(越低越好)、`ptm`(整體)、`plddt_mean`(骨架品質)供交叉看。
- Monomer×monomer 近似仍在(RBP 多為同源三聚體);linker-拼接是額外近似。
- 大型結構輸出不落地(只存分數 CSV + 熱圖)。
