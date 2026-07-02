# Pseudomonas 受體 → Moriniere 2026 受體分類

把三株環境 *Pseudomonas*(`9-2-1`、`9-6-2`、`10-10-2`)基因組註解出的表面/外膜蛋白,用**同源比對**分到 Moriniere et al. 2026(EcoliPhage / GenoPHI)的受體類別,讓它和噬菌體端的 [`../0619_literature_rbp_database/`](../0619_literature_rbp_database/) 共用同一套受體詞彙。
由 [`../../0620_receptor_classification.ipynb`](../../0620_receptor_classification.ipynb) 建置。(English: [`README.md`](README.md))

## 方法(一句話)
**受體 vs 受體**的同源比對 —— 把我們 curate 過的 Pseudomonas OMP,用 MMseqs2 去比對**定義那 13 類的 E. coli K-12 受體蛋白**,過門檻就標成那一類,過不了就 `Unclassified`。
> ⚠️ **不是** BLAST 我們的受體 vs RBP 資料庫:受體是「鎖」、RBP(噬菌體尾絲)是「鑰匙」,兩者不同源,那樣比會全部 Unclassified。

## 檔案

| 檔案 | 內容 |
|---|---|
| `receptor_classification.tsv` | **主結果**,每條受體一列(237):菌株、locus、註解、curated 分類、`curation`(kept / rescued-by-homology)、`assigned_class`、`fold_family`、最佳 E. coli 命中、%identity、coverage、e-value、bitscore、信心、依據 |
| `class_summary.tsv` | 每個 class × 每株的數量 |
| `excluded_log.tsv` | 被當非受體排除的 305 條,附理由 —— 且**確認其中 0 條能過同源門檻**(沒有把真受體偷偷丟掉) |
| `pseudomonas_receptors_curated.fasta` | 用註解 curate 出的「純受體」清單(233 條) |
| `ecoli_receptor_refs.fasta` | 13 條 E. coli K-12 參考受體(= 比對 target) |
| `ecoli_receptor_refs_meta.tsv` | 13 條參考的 gene / UniProt accession / 長度 |
| `blast_raw_hits.m8` | 全 542 條的 MMseqs2 原始比對結果(可重新調門檻用) |

## 怎麼讀 `receptor_classification.tsv`

先看階層:
```
542 全部表面蛋白
├── 237 純受體(= 這張表)
│     ├── 81  已分類(對到某個 Moriniere class)
│     └── 156 Unclassified(是受體,但跨屬對不到那 13 類)
└── 305 非受體(在 excluded_log.tsv,不在這張表)
```

每一列 = 一條純受體。重點欄位:

| 欄位 | 怎麼讀 |
|---|---|
| `assigned_class` | 對到的 Moriniere 類別(`fhuA`/`ompA`/`tolC`/`tsx`…);`Unclassified` = 是受體但對不到那 13 類 |
| `fold_family` | **主要看這欄** —— 誠實的家族層級(TBDR / OmpA-family / TolC-family / porin…)。跨屬無法可靠區分 fhuA vs btuB,**信家族、不要信成員名** |
| `confidence` | `family-level` = 過門檻、家族可信;`none` = Unclassified |
| `curation` | `kept` = 註解判為受體;`rescued-by-homology` = 註解本來排除、但同源把它救回(共 4 條) |
| `curated_category` | 註解 curate 的初判分類(可逐條稽核) |
| `best_ref_gene` / `pct_identity` / `query_cov` / `evalue` / `bitscore` | 對最佳 E. coli 參考的比對證據;想重新調門檻就看這幾欄 |
| `basis_note` | 一句話依據(含 rescued 說明、或 Unclassified 為何沒過) |

判讀提醒:
- **`Unclassified` ≠ 不是受體** —— 它仍在純受體裡,只是跨屬對不到那 13 類(典型:OprD-family porin)。「不是受體」的在 `excluded_log.tsv`。
- **class 是同源/家族註解,不是結合預測**(同 fold ≠ 同一隻噬菌體會結合)。
- 只想看「有分到類的」→ 篩 `assigned_class != Unclassified`(81 條);想看某一類 → 篩該 `fold_family`。

## 那 13 類怎麼來的
**清單來自原文**(p.5–6, 15:E. coli K-12 的 ~60–180 個 OMP 裡,只有 13 個曾被噬菌體當受體):
`Tsx, FadL, OmpA, OmpF, OmpW, OmpC, FhuA, BtuB, LptD, NupG, LamB, TolC, YncD`。
**序列來自 UniProt**(原文沒附受體序列,只給基因身分),按「基因名 + E. coli K-12 (taxid 83333) + Swiss-Prot」抓該基因的標準蛋白(accession 與長度在抓取時驗證)。13 類全收(不只資料庫有 phage RBP 的 8 類),這樣 TolC/OmpA 等也有得比。

## 判定邏輯
1. **Curate**:用關鍵字把 542 條分成「保留(OMP 受體 fold)/ 標記 out-of-scheme(pili、autotransporter、flagellin、secretin)/ 排除(Bam-Lol 組裝、TonB-ExbBD 能量器、內膜運輸、efflux 內膜泵與週質接頭、胞內訊息…)」。`curated_category` 欄可逐條稽核。
2. **MMseqs2 easy-search**(`-s 7.5`)—— **全 542 條** → 13 參考(不只 curated,讓同源可以蓋過錯誤註解)。
3. **門檻閘**:`e-value ≤ 1e-5` **且** `query coverage ≥ 0.50`。跨屬時 e-value+coverage 才可靠,**原始 %identity 不可靠**(真同源常只有 20–35%),所以 identity 只用來分信心,不當硬門檻。
4. 過閘 → 標成最佳命中的類別;沒過 → `Unclassified`(仍記錄最接近的參考,方便看為何沒過)。
5. **同源蓋過註解**:被註解排除、但能過門檻的蛋白會被「救回」進表(`curation = rescued-by-homology`)。這裡救回 **4 列 / 2 條** —— 一條「Secretin/TonB short N-terminal」(→ `fhuA`, e=2e-17,其實是 TonB-dependent 受體)和外膜脂蛋白 YfiB(→ `ompA`, e=8e-12)。最後再回頭檢查排除集:**305 條中 0 條能過門檻。**

## 結果

| 分類 | 數量(3 株合計) |
|---|---|
| **已分類** | **81** |
| └ TonB-dependent 受體(fhuA 41 / btuB 12 / yncD 7) | 60 |
| └ ompA | 12 |
| └ tolC | 6 |
| └ tsx | 3 |
| **Unclassified**(仍當受體候選保留) | **156** |
| (curate 排除的非受體,另計) | 305 |

> **菌株提醒:** `9-2-1` 與 `9-6-2` 的產物清單幾乎相同,所以 3 株合計大致是把同一批蛋白**重複計兩次**(兩份 + `10-10-2` 變異)。合計請當「量級」看,不是多樣性;逐株數字在 `class_summary.tsv`。

**幾個關鍵的科學結論:**
- **最高 identity 只有 ~40%** —— 沒有任何一條達到「close ortholog(>40% id)」,信心全部停在 `family-level`。這本身就說明:**Pseudomonas 沒有 E. coli 受體的近緣同源物,只能對到家族層級。**
- **81 條 porin 全部 Unclassified** —— Pseudomonas 的孔道以 **OprD family** 為主,在此門檻下用 MMseqs2 偵測不到 E. coli OmpF/OmpC/LamB 的同源訊號。(更敏感的 profile 方法如 HMMER/HHpred 在 20–30% identity 仍可能抓到遠源訊號;「porin 全 Unclassified」是相對於這個搜尋工具,不是「絕對無關係」的論斷。)
- **最會分的是 TonB-dependent 受體**(60 條對到 FhuA/BtuB/YncD 家族),符合 Pseudomonas 大量靠鐵載體搶鐵的生物學。
- `fold_family` 欄記的是**誠實的家族層級**;`fhuA`/`btuB`/`yncD` 之間、porin 各成員之間,跨屬無法可靠區分,請看到家族就好。

## 重要限制(務必和教授說明)
1. 這 13 類是 **E. coli K-12 的功能清單**(基因剔除實測),不是通用受體分類;直接套到 Pseudomonas 本就有對應落差。
2. **class = 同源/家族註解,不是結合預測。** 同 fold 不代表同一隻噬菌體會結合(例:OprF 屬 OmpA 家族,但胞外 loop 與 E. coli OmpA 完全不同)。
3. **涵蓋不全**:Pseudomonas 噬菌體常用的 type IV pili、LPS O-antigen、鞭毛不在這 13 類裡(多醣或非此清單),會落在 out-of-scheme / Unclassified。
4. 門檻(cov 0.5 / e 1e-5)可調 —— 所有原始數值都在 `blast_raw_hits.m8` 與主表,改門檻不必重跑比對。

## 重現方式
需要 `mmseqs`、`pandas`、`requests`、網路(抓 UniProt)。執行 [`../../0620_receptor_classification.ipynb`](../../0620_receptor_classification.ipynb)(或同名 `.py`),輸出全寫進本資料夾。

---
*Log: 2026-06-20 — 初版。542 表面蛋白全部對 13 條 E. coli 參考比對 → 受體表 237(curate 保留 233 + 同源救回 4)/ 非受體 305(0 條過門檻)。81 已分類 / 156 Unclassified。門檻 cov≥0.5 & e≤1e-5。*
