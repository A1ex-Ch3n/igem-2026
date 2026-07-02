# Metagenome RBP detection — PhageRBPdetect v4 (overview)

**Date:** 2026-07-01 · **Run by:** Laguna L40S GPU (~16 min total) · **Code:** `code/0701_phagerbp_metagenome/`

教授交代「玩看看 PhageRBPdetection」的第一個任務:用該工具從我們的**兩個土壤 metagenome**
（MG08、MG09）產出一份 **RBP(receptor binding protein)清單**。這是**de novo 模型預測**,
與 `code/0623_metagenome_rbp/` 的 homology-BLAST 法互補——它能標出**文獻庫裡沒有對應**的 RBP。

## 關鍵結論

| Metagenome | 蛋白總數 | 預測 RBP | 比例 |
|---|---|---|---|
| MG08 | 706,108 | **632** | 0.09% |
| MG09 | 650,535 | **661** | 0.10% |
| **合計** | 1,356,643 | **1,293** | — |

- **方法:** PhageRBPdetect **v4** = fine-tuned ESM-2 t12(Zenodo 14810759)。二元分類器,
  `score = softmax(logits)[:,1]`,**score ≥ 0.5 判為 RBP**(工具預設)。
- **分數分布:** 明顯雙峰,大多數落在 **0.9–1.0**(高信心;MG08 456、MG09 454),其餘散在 0.5–0.9。
- **~0.1% 命中率合理**:RBP 本就稀少,metagenome 主要是細菌蛋白而非噬菌體蛋白。
- **長度:** 中位數 129 aa(偏短,反映 metagenome 常見的**片段基因**),最長 1255 aa(可能是完整 tailspike 類)。

## 產物檔案(`code/output/0701_phagerbp_metagenome/`)

| 檔案 | 內容 |
|---|---|
| `all_metagenome_RBPs.tsv` | **主清單**:1,293 條 RBP(欄位 `sample, protein_name, score, length`,依分數排序) |
| `all_metagenome_RBPs.faa` | 主清單的蛋白序列(header 前綴 `MG08\|` / `MG09\|`) |
| `MG08_RBPs.{tsv,faa}` | MG08 的 632 條 RBP(清單 + 序列) |
| `MG09_RBPs.{tsv,faa}` | MG09 的 661 條 RBP(清單 + 序列) |
| `predictions_MG08.csv.gz` | MG08 **全部** 706,108 蛋白的分數表(`protein_name, preds, score`) |
| `predictions_MG09.csv.gz` | MG09 全部 650,535 蛋白的分數表 |

> 想用更嚴格的門檻,直接對 `predictions_*.csv.gz` 的 `score` 欄再篩即可(例如只留 ≥ 0.9)。

## 注意事項

- Metagenome 蛋白多為 Prodigal 呼叫的**片段基因**(`partial=10/11`);短片段的分數可靠度較低,
  清單中保留未過濾。
- 沒有交付對應的核酸 contig,無法把片段 ORF 補成全長——分析對象即為交付的蛋白本身。

## 如何重現 / 延伸

- 完整操作見 `code/0701_phagerbp_metagenome/laguna/GUIDE.md`(Laguna 上 clone → setup → run)。
- 可接續:(1) 把 1,293 條對現有 `RBP_DB` 做 mmseqs/BLAST,分「已知 vs 全新」;
  (2) 高分 RBP 餵入 binding screen,對 Pseudomonas host 的 OMP 折疊算 ipTM。

---
*Log — 2026-07-01:PhageRBPdetect v4 首跑完成,MG08/MG09 共 1,293 RBP。本機 M2/MPS 太慢(~22 h),
改用 Laguna L40S ~16 min 完成。產物與腳本在 branch `phagerbp-metagenome`。*
