# PhageRBPdetect v4 on Laguna — 完整操作指南

用 PhageRBPdetect v4(fine-tuned ESM-2 t12)在兩個土壤 metagenome(MG08、MG09)上偵測 RBP。
做法:把這個 repo 的 `phagerbp-metagenome` branch clone 到 Laguna,**直接在 clone 裡跑**。
模型、輸出、工具都放在 clone 內(相對路徑,不用改任何硬編路徑,也不用複製檔案)。

路徑:
- Clone 位置:`/project/jespinoza_1541/$USER/igem-2026/`
- 套件資料夾(工作目錄):`.../igem-2026/code/0701_phagerbp_metagenome/`
- Metagenomes(共用,只讀):`/project/jespinoza_1541/soil_mgs/`  ← 先 `ls` 確認檔名

---

## Step 0 — 清掉之前失敗的殘留(若跑過前面的貼上嘗試)

**先開一個新的 Terminal 分頁**(舊的可能被 `set -euo pipefail` 污染)。然後:
```bash
rm -rf /project/jespinoza_1541/$USER/phagerbp          # 之前貼上失敗建的半成品
rm -rf /project/jespinoza_1541/$USER/igem-2026         # 之前若 clone 過也清掉,重來
conda env remove -n phagerbp -y 2>/dev/null || true    # 若之前半途建過 env
```
> ⚠️ 只刪你自己的資料夾。metagenome 在 `/project/jespinoza_1541/soil_mgs/`(不同資料夾),不受影響。

---

## Step 1 — 開哪個 session + 資源設定

用 **Code Server (VS Code)** 最順手。OnDemand 表單填:

| 欄位 | 值 |
|---|---|
| Account / Allocation | `jespinoza@kgi.edu_1541` |
| Partition | `gpu` |
| GPUs | `1`(type `l40s`) |
| CPUs / cores | `8` |
| Memory | `40 GB` |
| Wall time | `2:00:00` |

> 若 GPU compute 節點沒有對外網路,Step C 的下載會失敗——那就在 **login node** 跑 Step A–C,再回 GPU session 跑 Step D。

---

## Step A — 弄一個 GitHub Token(一次性)

repo 是 private,clone 需要認證。github.com → Settings → Developer settings →
**Personal access tokens → Fine-grained tokens → Generate**:
- Repository access:只選 `A1ex-Ch3n/igem-2026`
- Permissions → **Contents: Read and write**(clone 只需 read,但 Step F 要 push 結果需要 write,一次設好)
- 複製產生的 token(clone / push 時當密碼用)

## Step B — clone(只抓這個套件資料夾,不下載 974 MB 的 data)

```bash
cd /project/jespinoza_1541/$USER
git clone --filter=blob:none --no-checkout --branch phagerbp-metagenome \
  https://github.com/A1ex-Ch3n/igem-2026.git igem-2026
cd igem-2026
git sparse-checkout set code/0701_phagerbp_metagenome
git checkout phagerbp-metagenome
cd code/0701_phagerbp_metagenome          # <-- 之後都在這裡跑
```
會問帳密:**Username** = `A1ex-Ch3n`,**Password** = 貼上剛剛的 token。確認完整:
```bash
wc -l *.py     # run_rbp_inference.py ~150、summarize_rbps.py ~110 行
```

## Step C — 安裝(需要網路的節點)

在套件資料夾裡:
```bash
bash laguna/setup_env.sh
```
會 clone 工具到 `./tool`、下載 v4 模型到 `./model`、建 conda env `phagerbp`。
成功會印 `torch ... setup complete`。
> 若停在 `conda not found`:先 `module avail` 找 anaconda/miniconda module,`module load <名字>` 後再跑一次;或把 `module avail` 輸出貼給 Claude。

## Step D — 執行(在 GPU 節點,套件資料夾裡)

```bash
ls -la /project/jespinoza_1541/soil_mgs/     # 確認檔名是不是 MG08.faa / MG09.faa
bash laguna/run_interactive.sh
```
流程:印 GPU 名稱 → 3 條 sanity(應全 `preds=1`)→ MG08(706,108)→ MG09(650,535)→ 產生清單。
中斷後直接重跑同指令會**接續**(已算過的跳過)。

> 若檔名不是 `MG08.faa`/`MG09.faa`,腳本會停下並列出 `soil_mgs/` 內容;
> 改 `laguna/run_interactive.sh` 裡的 `MG08=` / `MG09=` 兩行即可。

---

## Step E — 交付物

在套件資料夾的 `output/`:
- `predictions_MG08.csv`, `predictions_MG09.csv` — 全部蛋白的分數表
- `MG08_RBPs.{tsv,faa}`, `MG09_RBPs.{tsv,faa}` — 各 metagenome 的預測 RBP
- `all_metagenome_RBPs.{tsv,faa}` — 合併後的 **RBP 總清單**(主要交付物)

（`output/`、`model/`、`tool/` 都在 `.gitignore` 裡,不會污染 git 狀態。）

## Step F — push 結果回 repo(直接在 Laguna)

前提:Step A 的 token 要有 **Contents: Read and write**(read-only 推不上去,會 403)。
在套件資料夾裡整段貼上:
```bash
cd /project/jespinoza_1541/$USER/igem-2026/code/0701_phagerbp_metagenome

# 1. 兩個 ~33 MB 的 predictions CSV 先壓縮(大多是 preds=0,壓得很小)
gzip -kf output/predictions_MG08.csv output/predictions_MG09.csv

# 2. 設 git 身分(若還沒設過)
git config user.name  "CChen29"
git config user.email "CChen29@cmc.edu"

# 3. 先把遠端的更新拉下來(避免 non-fast-forward)
git pull --rebase origin phagerbp-metagenome

# 4. output/ 有被 .gitignore,用 -f 強制加入交付物(清單 + 壓縮後的分數表)
git add -f output/all_metagenome_RBPs.tsv output/all_metagenome_RBPs.faa \
           output/MG08_RBPs.tsv output/MG08_RBPs.faa \
           output/MG09_RBPs.tsv output/MG09_RBPs.faa \
           output/predictions_MG08.csv.gz output/predictions_MG09.csv.gz

git commit -m "results(0701): PhageRBPdetect v4 RBP lists for MG08/MG09 (1,293 RBPs)
Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>"

# 5. 推上去(帳密:Username=A1ex-Ch3n,Password=有寫入權限的 token)
git push origin phagerbp-metagenome
```
- 只加**壓縮後**的 `.csv.gz`,不加原始 35 MB CSV,免得 repo 歷史暴肥。不想要完整分數表就把第 4 步兩行 `predictions_*.csv.gz` 拿掉。
- 若 `git push` 出現 **403** → token 沒有寫入權限,重產一顆 Read and write 的再試。

### 驗證重點
- sanity 3 條全 `preds=1`(本機已驗過,Laguna 上再確認)。
- `wc -l output/predictions_MG08.csv` 應為 706,108 + 1(表頭);MG09 為 650,535 + 1。
- top-score 命中挑幾條看長度是否合理;可選:mmseqs/BLAST 對 `RBP_DB`,預期有已知 + 新的。

### 更新腳本
之後 Claude 在 `phagerbp-metagenome` branch 改完 push,你在套件資料夾 `git pull` 就會拿到,直接重跑即可。
