# PharBP 查詢 — mini report

**Date:** 2026-07-01 · **Code:** `code/0701_pharbp_query/` · **狀態:** Track A + Track B 皆完成

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

## Track B — 把我們的 RBP 比對 PharBP ✅
把 `0701_phagerbp_metagenome` 的 **1,293 個** metagenome RBP 逐條 BLASTP 進 PharBP(28.9 min),
每個 hit 直接帶 phage + host + identity/evalue/coverage。

- **429 / 1,293(33.2%)** 有 ≥1 hit;**864 條完全沒有 hit**。
- best-hit 相似度**普遍很低**:≥90% 只有 **1** 條、≥70% 共 6 條;大多落在 30–50%。
- 對到**已記錄 Pseudomonas host** 的:**0 筆**。
- 對到 **Pseudomonas *phage*(依 phage 名)**:**15 條**我們的 RBP —— Pseudomonas phage
  **Y5**(13)、**Phabio**(1,55.4% 最高)、**Y12**(1),但全為**遠緣**(28–55% identity)。
- 其餘 hit 多為 prophage / *Bacillus* / *Bacteroides* / *Brevibacillus* 等環境或腸道宿主。

**結論:我們的土壤 metagenome RBP 絕大多數是新穎序列**(2/3 在 PharBP 找不到同源,有 hit 者也多為遠緣)。
只有少數(~15 條)與已知 Pseudomonas phage(Y5/Phabio/Y12)遠緣相關,可列為優先關注候選。
→ 完整結果:`code/output/0701_pharbp_query/rbp_vs_pharbp_hits.tsv`。

## 我們的三個 strain 直接查 PharBP host

問題:測序回來的三個 site isolate(9-6-2 / 9-2-1 / 10-10-2)能在 PharBP 上找到嗎?
先釐清:依 ANI(`0623` 定論),**這三株其實幾乎相同(~99.4–100% ANI),是同一個 strain**,
物種 = *Pseudomonas_E* sp013179515(GTDB 未命名種;最接近的已命名基因體 = *Pseudomonas* sp. CM27)。

用 PharBP host autocomplete(`/export/autocomplete/?field=host&term=…`)逐一查:

| 我們的 strain | 物種(GTDB) | PharBP host 查詢 | 結果 |
|---|---|---|---|
| **9-6-2** | *Pseudomonas_E* sp013179515 | `9-6-2` / `sp013179515` / `CM27` | **查無** |
| **9-2-1** | *Pseudomonas_E* sp013179515(與 9-6-2 同株) | 同上 | **查無** |
| **10-10-2** | *Pseudomonas_E* sp013179515(與 9-6-2 同株) | 同上 | **查無** |
| (8-10-2) | *Pseudomonas_E* capeferrum | `capeferrum` | **查無** |

**結論:三株(以及它們的種名、最接近的 CM27)在 PharBP 完全查無** —— 合理,因為它們是我們自己的
新環境分離株,而 PharBP 的 host 是以已發表的具名菌株命名。唯一在 PharBP 有記錄的**近緣**是
***Pseudomonas putida***(host 變體 KT2440 / NBRC 14164 / S12,共 **8** 個 unique RBP 記錄),
正是 `0623` 找到的 surrogate host —— 它的 phage 是最實際的測試來源。

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
