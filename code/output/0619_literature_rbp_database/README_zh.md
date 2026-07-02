# 噬菌體 RBP 統合參考資料庫

把三篇文獻的受體結合蛋白(receptor-binding protein, RBP)整合成單一 FASTA + metadata 表。
由 [`../../0619_literature_database/build_rbp_database.ipynb`](../../0619_literature_database/build_rbp_database.ipynb) 建置。
(English version: [`README.md`](README.md))

## 檔案

| 檔案 | 列數 | 內容 |
|---|---|---|
| `rbp_database.fasta` | **1673** | 去重後的 unique RBP 蛋白序列(每個 100% identity 群集一條);header = `rbp_id` |
| `rbp_metadata.tsv` | 2447 | 每條來源 RBP 一列(**含完全重複**),完整 schema + 群集交叉引用 |
| `rbp_clusters.tsv` | 2447 | `rbp_id → cluster_rep_100 / cluster_rep_95`(MMseqs2 群集歸屬) |
| `pseudomonas_rbp_candidates.fasta` | 115 | *Pseudomonas* 切片,供 binding screen 使用(`../../0616_binding-screen-fold-plan.md`) |
| `rbp_by_receptor_class.tsv` | 1215 | **每個受體類別 → 對應 RBP 清單(含序列)** —— 所有有受體標註的 RBP,依 `receptor` 分組(OMP 類在前)、驗證等級高的在前。欄位:receptor, receptor_class, rbp_id, phage, host, source, confidence, rbp_type, seq_length, sequence。篩 `confidence ∈ {experimentally_validated, af3_validated}` 取高信心(173 列),或 `receptor_class==OMP` 取 E. coli 蛋白受體(362 列) |

> **2447 vs 1673**:metadata 共 2447 列 = 1673 條 unique 代表序列 + 774 列完全重複
> (不同來源/phage 的同一條序列)。重複列透過 `cluster_rep_100` 指向同一條 unique 序列,
> 資訊不會遺失。FASTA 只放 1673 條代表。

## 三個來源

| `source` | 文獻 | RBP 數(總列 / unique) | 標註依據 |
|---|---|---|---|
| `boeckaerts2021` | Boeckaerts et al. 2021, *Sci Rep* — 由 RBP 預測宿主 | 1232 / 933 | 依宿主(9 種) |
| `krusche_chm` | Krusche et al., *Cell Host & Microbe*(PhARIS) | 575 / 266 | 依 cluster;全部結合 WTA;`rbp_type` = main(不可逆)/ reversible(可逆) |
| `moriniere2026` | Moriniere et al. 2026, bioRxiv(GenoPHI) | 640 / 474 | 依 receptor + class;附 `confidence` 來源等級 |

Unique 資料庫宿主分布:*E. coli* 792、*S. aureus* 320、*K. pneumoniae* 175、
*P. aeruginosa* 115、*S. enterica* 114、*A. baumannii* 64、*C. difficile* 21、
*E. cloacae* 17、*Shigella* spp. 約 17。

## Schema(`rbp_metadata.tsv`)

`rbp_id, source, phage_name, host_species, rbp_type, cluster, receptor,
receptor_class, accession, seq_length, is_pseudomonas, confidence,
protein_sequence, cluster_rep_100, cluster_rep_95`

`confidence` 取值:`literature_annotated`(Boeckaerts/Krusche — 照文獻原樣);
`experimentally_validated` / `af3_validated` / `kmer_candidate`(Moriniere,見下方注意事項)。

## 群集歸屬(`cluster_rep_100`、`cluster_rep_95`)

**MMseqs2** 會把夠相似的序列歸成一群(cluster),每群推派一條當「代表
(representative)」。「群集歸屬」就是記錄**每條序列屬於哪一群、代表是誰**。
存了兩種嚴格度:

| 欄位 | 門檻 | 用途 |
|---|---|---|
| `cluster_rep_100` | 100% 相同 | **去重** — 完全一樣的序列歸一群,只留代表進 FASTA |
| `cluster_rep_95` | 95% 相似 | **找跨來源冗餘** — 高度相似(但不完全相同)的歸一群 |

判讀方式:**若某列的 `rbp_id` 等於它的 `cluster_rep_100`,它就是該群代表**
(這些就是進 `rbp_database.fasta` 的 1673 條);否則它是被代表「吸收」掉的重複。

- *例(100%):* 群 `krusche_0074` 有 **28 條完全相同的序列**(不同 *S. aureus* phage
  帶一模一樣的 RBP)—— 28 列都保留在 metadata,FASTA 只放代表 `krusche_0074`。這就是
  2447 → 1673 的去重。
- *例(95%):* 群 `boeckaerts_0009`(1026 aa 的 *E. coli* RBP)同時含 **Boeckaerts 與
  Moriniere 兩個來源**的列 —— 兩篇論文各自獨立收錄了幾乎相同的同一條 RBP。它們的
  `cluster_rep_100` 不同(序列是 95% 而非 100% 相同),所以 FASTA 中仍各自保留,但
  `cluster_rep_95` 把它們標記為同一個 RBP。這就是下方所述的跨來源冗餘。

也就是說,這個欄位讓你能追溯「哪些序列是哪一條代表的重複/近重複」,且去重時不遺失任何來源資訊。

## RBP 如何萃取

- **Boeckaerts、Krusche** — 直接解析已沉積的 RBP 集合(GitHub)。Krusche 的
  `RBPs_main/` + `RBPs_rev/` FASTA 已含每個 phage 的分群 RBP,**不需重跑 pipeline**。
- **Moriniere** — 其補充資料是 **feature-centric**:Dataset S6 列出每個帶 receptor 預測
  k-mer 的蛋白(每 phage 約 20 個,**並非全是 RBP**)。我把每個 `(phage × receptor)` 的
  RBP 取為「帶最多該受體預測 k-mer 的蛋白」,並先把每個蛋白指派到其 **argmax receptor**
  (避免一個蛋白被攤到多個受體 — 已驗證:EV240 的 *gp38* 只落在 OmpA,與論文一致)。
  受體指派再用文獻表標註 provenance。

## 注意事項

- **Moriniere 的 RBP 屬啟發式推定。** `experimentally_validated`(66,Tables S8/S9)與
  `af3_validated`(107,Table S5)為論文人工確認;`kmer_candidate`(467)為推定,應視為候選。
  AlphaFold3 驗證**僅限 OMP**,因此 LPS core sugar(Kdo/Hep/Glu)與 NGR 受體永遠不會是
  `af3_validated` — 與 binding-screen 計畫中提到的「蛋白 vs 多醣」盲點相同。
- **對照論文 ground truth 的覆蓋率**(因 Dataset S6 是唯一序列來源,只有當 RBP 在其中帶
  預測 k-mer 才會被收錄):AF3 配對 **149/163**、實驗驗證配對 **66/83** 被收錄;其餘在
  Dataset S6 無可取序列而未收錄。
- **Boeckaerts** 為*收集*集合(去重前);1232 列 → 933 unique。論文最終模型用的是再經
  長度過濾後的 887 條。
- 跨來源 95% identity 冗餘:Boeckaerts↔Moriniere(*E. coli*)16 群、Boeckaerts↔Krusche
  (*S. aureus*)6 群 — metadata 保留全部,FASTA 中合併。
- `is_pseudomonas` 標記所有 *Pseudomonas* 宿主(115 條 unique,**全部為 P. aeruginosa**,
  即感染 *Pseudomonas* 的 phage 的 RBP);可當作 binding screen 候選 probe。這些是
  *P. aeruginosa* 的 phage,作為團隊環境 *Pseudomonas* 株的 proxy。

## 重現方式

原始 deposit 快取在 `../../0619_literature_database/raw/`(已 gitignore)。重抓指令在
notebook 第一個 cell;接著執行 notebook(cwd = notebook 所在資料夾)。需要 `mmseqs`、
`pandas`、`openpyxl`。

---
*Log: 2026-06-19 — 初版建置。3 個來源 → 2447 列 RBP → 1673 條 unique 序列。*
