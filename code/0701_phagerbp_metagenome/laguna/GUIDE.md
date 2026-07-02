# PhageRBPdetect v4 on Laguna — 完整操作指南

用 PhageRBPdetect v4(fine-tuned ESM-2 t12)在兩個土壤 metagenome(MG08、MG09)上偵測 RBP。
腳本透過 git branch `phagerbp-metagenome` 傳到 Laguna(避免終端機貼上被截斷)。

路徑:
- 工作資料夾:`/project/jespinoza_1541/$USER/phagerbp/`
- Metagenomes(共用,只讀):`/project/jespinoza_1541/soil_mgs/`  ← 先 `ls` 確認檔名
- 模型:由 `setup_env.sh` 從 Zenodo 14810759 下載

---

## Step 0 — 清掉之前失敗的半成品(若有跑過前面的貼上嘗試)

**先開一個新的 Terminal 分頁**(舊的可能被 `set -euo pipefail` 污染)。然後:
```bash
# 看目前有什麼(soil_mgs 的 metagenome 不在這裡面,不會被動到)
ls -la /project/jespinoza_1541/$USER/phagerbp 2>/dev/null
conda env list 2>/dev/null | grep phagerbp
# 刪掉半成品工作資料夾
rm -rf /project/jespinoza_1541/$USER/phagerbp
# 若之前有半途建好的 conda env 也移除(沒有就自動略過)
conda env remove -n phagerbp -y 2>/dev/null || true
```
> ⚠️ 只刪 `.../$USER/phagerbp`。metagenome 在 `/project/jespinoza_1541/soil_mgs/`(不同資料夾),不受影響。

---

## Step 1 — 開哪個 session + 資源設定

用 **Code Server (VS Code)** 最順手(有編輯器 + 內建 terminal)。OnDemand 表單填:

| 欄位 | 值 |
|---|---|
| Account / Allocation | `jespinoza@kgi.edu_1541` |
| Partition | `gpu` |
| GPUs | `1`(type `l40s`) |
| CPUs / cores | `8` |
| Memory | `40 GB` |
| Wall time | `2:00:00` |

> 若 GPU compute 節點沒有對外網路,Step D 的下載會失敗——那就在 **login node** 跑 Step A–D,再回 GPU session 跑 Step E。

---

## Step A — 弄一個 GitHub Token(一次性)

repo 是 private,clone 需要認證。到 github.com → Settings → Developer settings →
**Personal access tokens → Fine-grained tokens → Generate**:
- Repository access:只選 `A1ex-Ch3n/igem-2026`
- Permissions → **Contents: Read-only**
- 複製產生的 token(等下當密碼用)

## Step B — clone(只抓腳本資料夾,不下載 data)

```bash
cd /project/jespinoza_1541/$USER
git clone --filter=blob:none --no-checkout --branch phagerbp-metagenome \
  https://github.com/A1ex-Ch3n/igem-2026.git igem-2026
cd igem-2026
git sparse-checkout set code/0701_phagerbp_metagenome
git checkout phagerbp-metagenome
```
會問帳密:**Username** = `A1ex-Ch3n`,**Password** = 貼上剛剛的 token。確認完整:
```bash
wc -l code/0701_phagerbp_metagenome/*.py     # 應約 150 / 110 行
```

## Step C — 把腳本放到工作資料夾

```bash
mkdir -p /project/jespinoza_1541/$USER/phagerbp/scripts
cp code/0701_phagerbp_metagenome/*.py \
   code/0701_phagerbp_metagenome/laguna/* \
   /project/jespinoza_1541/$USER/phagerbp/scripts/
```

## Step D — 安裝(需要網路的節點)

```bash
bash /project/jespinoza_1541/$USER/phagerbp/scripts/setup_env.sh
```
會 clone 工具、下載 v4 模型(~126 MB)、建 conda env `phagerbp`(CUDA torch + transformers + biopython)。
成功會印 `torch ... setup complete`。
> 若停在 `conda not found`:先 `module avail` 找 anaconda/miniconda module,`module load <名字>` 後再跑一次;或把 `module avail` 輸出貼給 Claude。

## Step E — 執行(在 GPU 節點)

```bash
ls -la /project/jespinoza_1541/soil_mgs/          # 確認檔名是不是 MG08.faa / MG09.faa
bash /project/jespinoza_1541/$USER/phagerbp/scripts/run_interactive.sh
```
流程:印 GPU 名稱 → 3 條 sanity(應全 `preds=1`)→ MG08(706,108)→ MG09(650,535)→ 產生清單。
中斷後直接重跑同指令會**接續**(已算過的跳過)。

> 若檔名不是 `MG08.faa`/`MG09.faa`,腳本會停下並列出 `soil_mgs/` 內容;
> 改 `scripts/run_interactive.sh` 裡的 `MG08=` / `MG09=` 兩行即可。

---

## Step F — 取回結果並 commit

交付物在 `/project/jespinoza_1541/$USER/phagerbp/output/`:
- `predictions_MG08.csv`, `predictions_MG09.csv` — 全部蛋白的分數表
- `MG08_RBPs.{tsv,faa}`, `MG09_RBPs.{tsv,faa}` — 各 metagenome 的預測 RBP
- `all_metagenome_RBPs.{tsv,faa}` — 合併後的 **RBP 總清單**(主要交付物)

用 OnDemand Files 下載,或 scp 回本機 repo 的 `code/output/0701_phagerbp_metagenome/`,再 commit。

## 驗證重點
- sanity 3 條全 `preds=1`(本機已驗過,Laguna 上再確認)。
- `wc -l predictions_MG08.csv` 應為 706,108 + 1(表頭);MG09 為 650,535 + 1。
- top-score 命中挑幾條看長度是否合理;可選:mmseqs/BLAST 對 `RBP_DB`,預期有已知 + 新的。

## 更新腳本
之後 Claude 在 `phagerbp-metagenome` branch 改完 push,你在 `igem-2026/` 裡 `git pull`,
再重跑 Step C 的 `cp` 即可。
