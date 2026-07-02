# PharBP 查詢 — mini report

**Date:** 2026-07-01 · **Code:** `code/0701_pharbp_query/` · **狀態:** Track A 完成;Track B 全量跑完後更新

教授任務:在 [PharBP](https://pharbp.ugent.be/)(UGent Boeckaerts group,與 PhageRBPdetection
同一實驗室)確認我們的 bacteria receptor 在不在裡面、有沒有已記錄的 pairs,並用其 API 執行。

## 核心發現(重新定義了任務)
**PharBP 是「噬菌體 RBP」資料庫,不是 receptor 資料庫。** 每筆 = 一個 RBP(tail fiber /
tailspike)→ 對應的 **phage** 與 **host 細菌**;**沒有細菌 receptor 欄位**(LPS / 具名 OMP /
pili / flagella 都沒有),唯一的「pairs」是 RBP↔host,且**多為電腦預測**,非實驗驗證的結合對。

因此:
- 我們的 441 個細菌 receptor **無法在此查詢**;把 receptor(OMP)序列 BLAST 進 RBP 庫生物學上也不對。
- 可行且有價值的是兩條(已與教授意圖確認 = 兩者都做):

## Track A — 拉出 PharBP 裡的 Pseudomonas RBP ✅
用 `GET /export/results/?host_genus=Pseudomonas&unique=1&download=csv`。

- **198** 個去冗餘 RBP 記錄、**60** 個 phage、**21** 個 host strain。
- 其中 **22** 筆 host 屬 *P. putida* group / 非 aeruginosa(最接近我們的 *Pseudomonas_E* 分離株)——
  PharBP 的 Pseudomonas 大多是 *P. aeruginosa*,少數 *P. syringae* / *protegens* / *putida*。
- 這是此 DB 能提供、最接近「recorded pairs」的東西(phage–host + 結構 + evidence)。
- 產物:`code/output/0701_pharbp_query/pseudomonas_rbps.csv` + `_summary.md`。

## Track B — 把我們的 RBP 比對 PharBP ⏳(全量跑完更新)
把 `0701_phagerbp_metagenome` 的 **1,293 個** metagenome RBP 逐條 BLASTP 進 PharBP,
每個 hit 直接帶 phage + host + identity/evalue/coverage。

**初步(前 30 條驗證):** 只有 **8/30** 有 hit,且都是**低相似度(30–46%)、對到非 Pseudomonas 的
phage**(Salmonella / Cyanophage / Bacillus prophage)。初步訊號:我們的土壤 metagenome RBP
**相當新穎**,與資料庫(多為 aeruginosa/臨床)不相似。
→ 完整 1,293 條的命中率、host/phage 分布、是否有對到 Pseudomonas,待全量跑完填入。

## 對專案的意義
- PharBP 對我們最實際的用途:**Track A 的 198 個 Pseudomonas RBP 可當 binding screen 的 phage 側輸入**。
- **receptor↔RBP 配對 PharBP 給不了**;要做那個得靠我們自己的 in-silico fold screen
  (`data/processed_genome/binding_screen/`)。

## API 備註(已實測,免認證)
- CSV export 見上。
- BLASTP 需 CSRF:GET `/blastp/` 取 `csrftoken` cookie → POST `/api/blastp/upload/`
  (form 欄位 `sequence=`,**一次一條**,multi-FASTA 會被串接)+ `X-CSRFToken` header + `Referer`
  → 同步回 `query_id` → GET `/api/blastp/results/<id>/`。

---
*Log — 2026-07-01:研究 PharBP + API;DB 無 receptor 欄位,任務改為 Track A(198 Pseudomonas RBP)
+ Track B(BLAST 我們 1,293 RBP,進行中)。API/CSRF 已實測。*
