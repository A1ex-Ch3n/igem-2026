# Phage assembly — run on Laguna ｜ 噬菌體組裝 — 在 Laguna 上執行

Assemble + annotate **9-2-1 Φ8** (vendor `3NKSC3`) from **raw** reads (we redo host removal
ourselves — we do NOT trust the vendor's host-removed files). Runs on USC CARC **Laguna**.
從 **raw** reads 開始組裝＋註解 **9-2-1 Φ8**（廠商編號 `3NKSC3`）；宿主移除我們自己重做，**不用**廠商的
`hostremoved` 版本。整個流程跑在 USC CARC **Laguna**。

Upload via **OnDemand → Files** (drag-drop; SSH/scp is blocked until your key is registered).
上傳走 **OnDemand → Files**（拖拉即可；在你的金鑰註冊前，SSH/scp 是被擋的）。

Target dir ｜ 目標目錄：`/project/jespinoza_1541/$USER/phage_assembly/`
（Your `$USER` is `CChen29@cmc.edu` — the `@` is normal, this allocation spans several schools.
你的 `$USER` 是 `CChen29@cmc.edu`,含 `@` 是正常的,這個 allocation 跨好幾間學校。）

---

## 0. Where you are now ｜ 你現在的狀態

You've already uploaded the `.gz` reads, but they landed **directly in your personal dir**
`/project/jespinoza_1541/$USER/`, not inside a `phage_assembly/` subfolder. That's fine — we just
tidy them into place (a `mv` on the same filesystem is instant; no need to re-upload the 1.24 GB).
你已經把 `.gz` reads 傳上去了,但它們**直接落在你的個人目錄** `/project/jespinoza_1541/$USER/`,
不在 `phage_assembly/` 子資料夾裡。沒關係——歸位一下就好(同一個檔案系統上 `mv` 是瞬間的,不用重傳 1.24 GB)。

First, open an OnDemand terminal (*Clusters → Shell*, or a Jupyter session's Terminal) and look:
先開一個 OnDemand 終端機(*Clusters → Shell*,或 Jupyter session 的 Terminal)看一下:
```bash
echo "$USER"                         # should print CChen29@cmc.edu
cd /project/jespinoza_1541/$USER
ls -la                               # see exactly which files you uploaded ｜ 看你到底傳了哪些檔
```

---

## 1. Build the layout + tidy the uploaded files ｜ 建結構＋歸位已上傳的檔案

```bash
cd /project/jespinoza_1541/$USER
mkdir -p phage_assembly/{reads,ref,laguna}

# move the RAW reads into reads/  ｜ 把 RAW reads 移進 reads/
mv 3NKSC3_1_9_2_1_ph8_R1.fastq.gz 3NKSC3_1_9_2_1_ph8_R2.fastq.gz phage_assembly/reads/
```

> Only the two **raw** files are needed. If you also uploaded the `hostremoved` ones, leave them out
> (we redo host removal from raw) — you can delete them to save space.
> 只需要 **raw** 兩個檔。如果你也傳了 `hostremoved`,不用它們(我們從 raw 自己重做去宿主),可以刪掉省空間。

Then make sure the other two pieces are in place ｜ 再確認另外兩樣也就位:

| Needs to be at ｜ 要放到 | What ｜ 是什麼 | From laptop ｜ 筆電來源 |
|---|---|---|
| `phage_assembly/ref/`    | 9-2-1 host genome ｜ 宿主基因體 | `data/bacteria_genome/9-2-1/XH254M_1_sample_1_1_reference.fasta` |
| `phage_assembly/laguna/` | the 3 scripts ｜ 3 個腳本 | this `code/0708_phage_assembly/laguna/` folder |

If either is still sitting in your personal dir → `mv` it in; if not uploaded yet → upload via
**OnDemand → Files** into that subfolder. **Keep original filenames** — the sbatch refers to them literally.
若這兩樣還躺在你個人目錄 → `mv` 進去;若還沒傳 → 用 **OnDemand → Files** 拖到對應子資料夾。
**檔名保持原樣**,sbatch 是直接寫死檔名去找的。

Final layout ｜ 最後結構:
```
phage_assembly/
├── laguna/        setup_env.sh, run_assembly.sbatch, README_RUN.md
├── reads/         3NKSC3_1_9_2_1_ph8_R1.fastq.gz , _R2.fastq.gz      (RAW ｜ 原始 reads, ~1.24 GB)
└── ref/           XH254M_1_sample_1_1_reference.fasta
```
Verify ｜ 驗證:
```bash
ls phage_assembly/reads/ phage_assembly/ref/ phage_assembly/laguna/
```

---

## 2. Setup — ONCE, and let it FINISH (needs internet on the node) ｜ 一次性設定,且要等它跑完(節點要有網路)

This is the prerequisite — the assembly job will refuse to start until the `phage_asm` env exists.
這是前置步驟——組裝工作會拒絕啟動,直到 `phage_asm` 環境建好為止。

Open an OnDemand terminal (Clusters → Shell, has internet), then ｜ 開一個 OnDemand 終端機(Clusters → Shell,有網路),然後:
```bash
cd /project/jespinoza_1541/$USER/phage_assembly
bash laguna/setup_env.sh
```
It builds two conda envs (`phage_asm`, `pharokka`) and downloads the pharokka + CheckV databases —
**this takes several minutes to ~15 min, not seconds. Wait for it.**
它會建兩個 conda 環境(`phage_asm`、`pharokka`)並下載 pharokka + CheckV 資料庫——
**要花數分鐘到約 15 分鐘,不是秒級,請等它跑完。**

Success ends with ｜ 成功會以這幾行結尾:
```
>> setup complete.
   envs : phage_asm (assembly), pharokka (annotation)
   next : sbatch laguna/run_assembly.sbatch ...
```
If a download hangs → that node has no internet; get an internet-capable node and re-run.
如果某個下載卡住 → 這個節點沒網路;換一個有網路的節點重跑。

---

## 3. Assemble + annotate ｜ 組裝＋註解

Only after setup finished ｜ setup 跑完之後才做:
```bash
cd /project/jespinoza_1541/$USER/phage_assembly
sbatch laguna/run_assembly.sbatch
squeue --me                       # monitor ｜ 監控
tail -f phage_asm_*.out           # log is in the submit dir, named by job id ｜ log 在提交目錄,以 job 號命名
```
Stages skip if their output exists, so a re-`sbatch` resumes after any failure. Annotation
(pharokka/checkv) is best-effort — if its env/DBs aren't ready the job still finishes with the
assembly. 每個階段產物若已存在就跳過,失敗後再 `sbatch` 一次會從斷點續跑。註解那步是 best-effort,
就算環境/DB 沒好,組裝結果照樣會產出、工作不會整個失敗。

---

## 4. Pull results back to the laptop ｜ 把結果拉回筆電

Download these into `data/phage_genome/9-2-1/assembly/` ｜ 下載這些到 `data/phage_genome/9-2-1/assembly/`:
```
work/contigs_min1kb.fasta        # final contigs (>= 1 kb) ｜ 最終 contigs
work/contig_summary.txt          # per-contig length + coverage ｜ 每條 contig 的長度＋覆蓋度
work/fastp.html                  # read QC ｜ reads 品質報告
work/bowtie2_host.log            # our host % (cross-check vs vendor 1.9%) ｜ 我們算的宿主比例(對照廠商 1.9%)
work/readback.log                # read-back mapping rate ｜ reads 回貼比例
work/pharokka/                   # annotation (gff, genbank, CDS, tRNA, plots) ｜ 註解結果
work/checkv/quality_summary.tsv  # completeness ｜ 完整度
```

---

## Caveats / decision points ｜ 注意事項與判斷點

- **Workspace path must NOT contain `@` ｜ 工作區路徑不能含 `@`** — a conda env whose install prefix
  has `@` breaks its bundled perl (`bowtie2`, pharokka's tRNAscan) with `interpolation of @...` /
  `Compilation failed`. Your `$USER` is `CChen29@cmc.edu`, so **don't** keep the workspace under
  `/project/jespinoza_1541/$USER/` — put it under a no-`@` dir like
  `/project/jespinoza_1541/cchen_phage/phage_assembly/`. The scripts abort early if they detect `@`.
  conda 環境安裝路徑含 `@` 會弄壞內建的 perl(bowtie2、pharokka 的 tRNAscan)。你的 `$USER` 是
  `CChen29@cmc.edu`,所以工作區**別**放在 `/project/jespinoza_1541/$USER/` 底下,改放不含 `@` 的目錄如
  `/project/jespinoza_1541/cchen_phage/phage_assembly/`。腳本偵測到 `@` 會提早中止。

- **CPU partition ｜ CPU 分區** — set to `--partition=compute` (128 cores / 376 G / 7-day, the cluster
  default; `gpu` is reserved for folding). If jobs reject on account/QOS, run
  `sacctmgr show assoc user=$USER format=account,qos` and add a `#SBATCH --qos=...` line.
  已設為 `--partition=compute`(128 核 / 376 G / 7 天,叢集預設;`gpu` 留給 folding)。若因 account/QOS 被拒,
  跑上面那行查出正確 QOS 再補一行 `#SBATCH --qos=...`。

- **Overcoverage ｜ 覆蓋度爆高** — data is ~10,000×+; step 3 normalizes to ~100× before SPAdes.
  Do not skip it. 資料約 1 萬倍以上;步驟裡先用 bbnorm 正規化到約 100× 再組裝,這步不能跳。

- **Single vs multi phage ｜ 單一 vs 多噬菌體** — this pick was NOT re-isolated to single-phage purity.
  Step 5 prints the count of phage-sized (≥10 kb) contigs. **>1 → possible multi-phage**; if so, re-run
  assembly with `metaspades.py` (swap the `spades.py --isolate` line in the sbatch) and treat each contig
  separately. 這個 plaque 沒有再分離到單一噬菌體純度。腳本會印出 ≥10 kb 的 contig 數,**>1 就可能是多噬菌體**;
  若是,把 sbatch 裡 `spades.py --isolate` 換成 `metaspades.py` 重跑,並把每條 contig 分開看。

- **CheckV completeness ｜ CheckV 完整度** — low completeness on the largest contig can mean a fragmented
  assembly or a genuinely partial genome; cross-read with the coverage in `contig_summary.txt`.
  最大那條 contig 若完整度低,可能是組裝破碎、也可能真的是不完整基因體;搭配 `contig_summary.txt` 的覆蓋度一起判讀。

- **CheckV DB download is flaky ｜ CheckV 資料庫下載不穩** — the NERSC host sometimes drops the SSL
  connection (`UNEXPECTED_EOF`). Usually transient — just re-run `bash laguna/setup_env.sh` (the
  pharokka DB skips if already there, only CheckV retries). Assembly + pharokka do NOT need it, so
  don't let this block you. If it keeps failing, from the pharokka env: `cd db && checkv download_database .`
  NERSC 那台 server 偶爾會斷 SSL 連線(`UNEXPECTED_EOF`),通常是暫時的——直接再跑一次 `bash laguna/setup_env.sh`
  (pharokka DB 已有就跳過,只重試 CheckV)。組裝＋pharokka **不需要**它,別被這步卡住。若一直失敗,在 pharokka 環境下
  `cd db && checkv download_database .` 重試。

---
*Log ｜ 紀錄: 2026-07-08 — created alongside the pipeline scripts ｜ 與流程腳本一同建立。2026-07-08 — rewritten bilingual (EN/中文), added a from-scratch "get into Laguna" step ｜ 改寫成中英雙語,補上從零進 Laguna 的步驟。2026-07-08 — reworked steps 0–1 to match the real upload: reads landed in the personal dir (`$USER`=`CChen29@cmc.edu`), so tidy-in-place with `mv` instead of re-uploading ｜ 依實際上傳情況改寫步驟 0–1:reads 落在個人目錄,改用 `mv` 歸位而非重傳。2026-07-08 — rewrote the pipeline scripts against the proven Laguna conventions (0703 esmfold/boltz): `SLURM_SUBMIT_DIR` base, log in submit dir, `partition=compute`, env-exists precheck, best-effort annotation ｜ 依 0703 成功慣例重寫流程腳本(SLURM_SUBMIT_DIR、log 放提交目錄、compute 分區、環境前置檢查、註解 best-effort)。*
