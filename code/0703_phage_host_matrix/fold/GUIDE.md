# RBP × receptor fold on Laguna — 完整操作指南

> **⚡ 改用 Boltz-2**:AF2-multimer 實測 ~3.5 min/折 + single_seq 精度差(pLDDT≈28)。
> 改走 **Boltz-2(MSA-free,~30s/折、堪用)** → 見 [`boltz/GUIDE.md`](boltz/GUIDE.md)。
> 下面的 ColabFold 版保留作備援。

---


Fold **114 candidate RBP families × 63 overlapped receptors = 7,182 ColabFold multimer**
預測 → 每對 ipTM → 最終 RBP × receptor 矩陣 + 熱圖。程式碼透過 git branch
`rbp-receptor-fold` 上 Laguna,結果在 Laguna 上 **commit + push** 回來。

路徑:
- Clone:`/project/jespinoza_1541/$USER/igem-2026/`
- 工作區:`/project/jespinoza_1541/$USER/rbp_receptor_fold/`(組裝腳本+輸入)
- ColabFold:`/project/jespinoza_1541/$USER/localcolabfold`(一次性安裝,共用)

---

## Step 1 — 開哪個 session + 資源設定

用 **Code Server (VS Code)**。OnDemand 表單填:

| 欄位 | 值 |
|---|---|
| Account / Allocation | `jespinoza@kgi.edu_1541` |
| Partition | `gpu` |
| GPUs | `1`(type `l40s`) |
| CPUs / cores | `8` |
| Memory | `40 GB` |
| Wall time | `4:00:00`(ColabFold 安裝 ~30min + smoke + 送出 array) |

> ⚠️ **Step A/B/D(clone、colabfold 安裝)需要對外網路**。若 GPU compute 節點沒 egress,
> 就在 **login node**(SSH 或 OnDemand shell)跑 A/B/D,再回 GPU session 跑 smoke。
> array job 是 `sbatch` 丟出去在別的節點跑,不佔這個 session。

## Step A — GitHub Token(一次性,要能 push)
github.com → Settings → Developer settings → **Personal access tokens → Fine-grained tokens**:
- Repository access:`A1ex-Ch3n/igem-2026`
- Permissions → **Contents: Read and write**(等下 clone 和 push 結果都用)
- 複製 token。

## Step B — 取得程式碼(sparse,只抓 fold 資料夾)

**情況 1 — 還沒 clone 過 `igem-2026`:**
```bash
cd /project/jespinoza_1541/$USER
git clone --filter=blob:none --no-checkout --branch rbp-receptor-fold \
  https://github.com/A1ex-Ch3n/igem-2026.git igem-2026
cd igem-2026
```

**情況 2 — 之前的 task 已經 clone 過 `igem-2026`(沿用它,要先 fetch 這個新 branch):**
```bash
cd /project/jespinoza_1541/$USER/igem-2026
git fetch origin rbp-receptor-fold        # ← 沒這行 checkout 會說 "pathspec did not match"
```

**兩種情況都接著跑:**
```bash
git sparse-checkout set code/0703_phage_host_matrix/fold code/output/0703_phage_host_matrix/fold
git checkout rbp-receptor-fold
```
帳密:Username `A1ex-Ch3n`,Password 貼 token。確認:
```bash
ls code/0703_phage_host_matrix/fold code/output/0703_phage_host_matrix/fold
```

## Step C — 組裝工作區(腳本 + 輸入放一起,重生 all_pairs.csv)
```bash
WORK=/project/jespinoza_1541/$USER/rbp_receptor_fold
mkdir -p "$WORK"
cd /project/jespinoza_1541/$USER/igem-2026
cp code/0703_phage_host_matrix/fold/{make_pairs.py,split_input.py,rbp_receptor.sbatch,run_smoke.sh,setup_colabfold.sh,collect_results.py,fold_heatmap.py} "$WORK/"
cp code/output/0703_phage_host_matrix/fold/{probes.fasta,receptors_panel.fasta,probe_map.tsv,receptor_map.tsv} "$WORK/"
cd "$WORK"
python3 make_pairs.py     # 重生 all_pairs.csv(7,182 對)+ smoke.csv(gitignore 沒帶)
```

## Step D — 安裝 LocalColabFold(一次性,需網路的節點)
```bash
bash /project/jespinoza_1541/$USER/rbp_receptor_fold/setup_colabfold.sh
```
下載 ~5GB、約 15–30 分鐘;裝到 `/project/jespinoza_1541/$USER/localcolabfold`。已裝就自動跳過。

## Step E — smoke(先量每對成本!)
在 GPU 節點:
```bash
cd /project/jespinoza_1541/$USER/rbp_receptor_fold
bash run_smoke.sh
```
記 `time` 的 wall-time ÷ 6 = 每對成本;× 7,182 = 全跑 GPU-hr,對照共用 10k-hour 額度。
> **MSA(重要)**:`run_smoke.sh` 和 `rbp_receptor.sbatch` 已預設 **`--msa-mode single_sequence`**
> ——純 GPU、離線、不碰遠端 MMseqs2 伺服器(那台 rate-limited、一天只幾千個、還會讓 GPU 空等)。
> 7,182 folds 只能這樣跑。**代價**:沒有 MSA、精度較低,所以把 ipTM 當**粗排序**;跑完後可對
> **top hits** 拿掉這個 flag(`MSA_FLAGS=""`)用完整 MSA 重折幾個、拿較可信的分數。

## Step F — 切塊 + 送出 array
```bash
cd /project/jespinoza_1541/$USER/rbp_receptor_fold
python3 split_input.py 40           # 7,182 對 → 180 塊;印出 --array=0-179%8
sbatch --array=0-179%8 rbp_receptor.sbatch
squeue -u $USER                     # 看進度
```
`%8` = 最多同時 8 個 task(共用額度保護)。array 在別的節點跑,可關掉 session,之後再回來收。

## Step G — 收集 + 熱圖(array 跑完後)
```bash
cd /project/jespinoza_1541/$USER/rbp_receptor_fold
python3 collect_results.py results binding_matrix.csv
python3 fold_heatmap.py binding_matrix.csv        # → rbp_receptor_iptm_heatmap.png
```

## Step H — 在 Laguna 上 commit + push 回來
把結果放進 clone 的 output 資料夾再 push(token 要有 write):
```bash
cd /project/jespinoza_1541/$USER/igem-2026
cp /project/jespinoza_1541/$USER/rbp_receptor_fold/{binding_matrix.csv,rbp_receptor_iptm_heatmap.png} \
   code/output/0703_phage_host_matrix/fold/
git config user.name "CChen29"; git config user.email "CChen29@cmc.edu"
git pull --rebase origin rbp-receptor-fold
git add code/output/0703_phage_host_matrix/fold/binding_matrix.csv \
        code/output/0703_phage_host_matrix/fold/rbp_receptor_iptm_heatmap.png
git commit -m "results(0703): RBP × receptor ColabFold ipTM matrix + heatmap
Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"
git push origin rbp-receptor-fold
```
(若 push 出現 403 → token 沒有寫入權限,重產一顆 Read and write 的。)

---

## 之後
跑完通知 Claude(貼 smoke 的每對時間、或 push 完的 commit),我會把 `binding_matrix.csv` 拉下來、
把 branch 併回 main,並解讀熱圖(哪些 RBP–receptor 高 ipTM = 濕實驗優先)。

## 限制
- **Monomer×monomer 近似**:RBP 多為同源三聚體,ipTM 是近似訊號,高分當候選、非定論。
- ipTM 無公定門檻;先看分布(binding_screen smoke ipTM ~0.25–0.41)。
- ColabFold 結構輸出(results/)很大,留 Laguna,不進 git(只回傳 matrix + 熱圖)。
