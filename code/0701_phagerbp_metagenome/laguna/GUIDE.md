# PhageRBPdetect v4 on Laguna — 完整操作指南

Detect RBPs in the two soil metagenomes (MG08, MG09) with PhageRBPdetect v4 on an L40S GPU.

Paths used:
- Work dir (你建立的):   `/project/jespinoza_1541/$USER/phagerbp/`
- Metagenomes (共用):    `/project/jespinoza_1541/soil_mgs/`  ← 先 `ls` 確認檔名
- Model:                 downloaded from Zenodo 14810759 by `setup_env.sh`

---

## Step 1 — 開哪個 session + 資源設定

用 **Code Server (VS Code)** 最順手：可以直接改 `run_interactive.sh` 的路徑，又有內建
terminal 跑指令。（JupyterLab 也可以；Laguna Desktop 太重、不需要。）

在 OnDemand 開 Code Server 的表單填：

| 欄位 | 值 |
|---|---|
| Account / Allocation | `jespinoza@kgi.edu_1541` |
| Partition | `gpu` |
| GPUs | `1`  (type `l40s` → `gres=gpu:l40s:1`) |
| CPUs / cores | `8` |
| Memory | `40 GB` |
| Wall time | `2:00:00`  （整個工作 <1 小時，多給緩衝） |

送出後就會在一個 **GPU 節點** 上開好 session。

> ⚠️ 有些 compute 節點沒有對外網路。Step 3 的下載/安裝若失敗（wget / pip 連不上），
> 就改在 **login node**（SSH 進 Laguna）跑 `setup_env.sh`，之後回到 GPU session 執行。

---

## Step 2 — 把我們的兩個腳本放上 Laguna

需要 `run_rbp_inference.py` 和 `summarize_rbps.py`（在本機 repo 的
`code/0701_phagerbp_metagenome/`）。二選一：

**A. OnDemand 檔案上傳（最簡單）** — 用 OnDemand 的 *Files* app，進到
`/project/jespinoza_1541/<你>/phagerbp/scripts/`（先建資料夾），Upload 這兩個 `.py`
以及 `laguna/` 底下的三個腳本。

**B. 從 Mac scp：**
```bash
cd "/Users/alexy/Desktop/iGEM 26/code/0701_phagerbp_metagenome"
DEST="$USER@<你的-laguna-login-host>:/project/jespinoza_1541/$USER/phagerbp/scripts/"
ssh $USER@<你的-laguna-login-host> "mkdir -p /project/jespinoza_1541/$USER/phagerbp/scripts"
scp run_rbp_inference.py summarize_rbps.py laguna/*.sh laguna/*.sbatch "$DEST"
```

---

## Step 3 — 一次性環境安裝（需要網路的節點）

在 session terminal（或 login node）：
```bash
cd /project/jespinoza_1541/$USER/phagerbp/scripts
bash setup_env.sh
```
它會：clone 工具 repo、從 Zenodo 下載 v4 模型（~126 MB）、建立 conda env `phagerbp`
（CUDA PyTorch + transformers + biopython）。最後會印出 torch 版本確認。

---

## Step 4 — 執行（在 GPU session）

先確認 metagenome 檔名：
```bash
ls -la /project/jespinoza_1541/soil_mgs/
```
若不是 `MG08.faa` / `MG09.faa`，就打開 `scripts/run_interactive.sh` 改 `MG08=` / `MG09=` 兩行。

然後跑：
```bash
cd /project/jespinoza_1541/$USER/phagerbp/scripts
bash run_interactive.sh
```
流程：印出 GPU 名稱 → 3 條範例序列 sanity（應全部 `preds=1`）→ 跑 MG08（706,108）→
MG09（650,535）→ 產生 RBP 清單。預計 <1 小時。中斷了直接重跑同指令會**接續**（已算過的會跳過）。

> 若表單沒有 GPU 選項，改用一般 session 開 terminal，再自己搶 GPU：
> ```bash
> salloc --account=jespinoza@kgi.edu_1541 --partition=gpu --gres=gpu:l40s:1 \
>        --cpus-per-task=8 --mem=40G --time=2:00:00
> ```
> 進到 GPU 節點後再 `bash run_interactive.sh`。

---

## Step 5 — 取回結果並 commit

輸出在 `/project/jespinoza_1541/$USER/phagerbp/output/`：
- `predictions_MG08.csv`, `predictions_MG09.csv` — 全部蛋白的分數表
- `MG08_RBPs.{tsv,faa}`, `MG09_RBPs.{tsv,faa}` — 各 metagenome 預測為 RBP 的
- `all_metagenome_RBPs.{tsv,faa}` — 合併後的 **RBP 總清單**（主要交付物）

傳回本機 repo 的 `code/output/0701_phagerbp_metagenome/`（scp 或 OnDemand 下載），再 commit。
告訴我每個 metagenome 的 RBP 數量和執行時間，我就把 `README.md` 補完。

---

## 驗證重點
- sanity 3 條全 `preds=1`（本機已驗過，Laguna 上再確認一次）。
- `wc -l predictions_MG08.csv` 應為 706,108 + 1（表頭）；MG09 為 650,535 + 1。
- top-score 命中挑幾條看長度是否合理；可選：mmseqs/BLAST 對我們的 `RBP_DB`，預期有一部分
  已知 + 一部分新的（這正是這個工具相對 homology 法的價值）。
