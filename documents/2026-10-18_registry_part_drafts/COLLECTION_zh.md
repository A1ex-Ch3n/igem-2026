# Collection 頁 — 噬菌體 Φ8 表面多醣工具組（草稿・中文版）

六個 part 當成一套。英文版（要貼到 Registry 的是英文）：[`COLLECTION.md`](COLLECTION.md)。

---

## 標題

**Phage 9-2-1 Φ8 surface-polysaccharide toolkit: three virion proteins and an ancestral series
of their glycoside hydrolase**

## 摘要

六個 basic part，全部來自同一株土壤噬菌體 **9-2-1 Φ8** —— 由我們團隊從 *Pseudomonas* 宿主分離並定序。
三個是噬菌體自己的 virion 蛋白，直接取自基因體；另外三個是其中一個蛋白的重建祖先。
六個放在一起只問一個問題：**祖先酵素能不能作用在現代後代碰不到的細菌表面醣上？**

| Part | Registry ID | 是什麼 | 證據等級 |
|---|---|---|---|
| CDS12_WT | `BBa_267WQM51` | GH5 glycoside hydrolase，獨立的游離酵素 | template 確認 |
| CDS11_WT | `BBa_26DKNAEC` | tail-spike β-helix depolymerase 本體 | 只有摺疊層級 |
| CDS10_WT | `BBa_269KJB8G` | virion fiber | 功能未知 |
| CDS12_ANC_Node1 | `BBa_26TWEX42` | CDS12 的重建祖先，最近 | 計算設計 |
| CDS12_ANC_Node40 | `BBa_26EK89VW` | 重建祖先，較深 | 計算設計 |
| CDS12_ANC_Node281 | `BBa_26LHLSLW` | 重建祖先，三者中最深 | 計算設計 |

## 為什麼這六個是一組

**問題。** 宿主一旦改變噬菌體所結合的表面醣，phage therapy 就失效。噬菌體的 depolymerase 是專一的，
各自對應一種宿主多醣。這個專一性同時是它有用的地方，也是它的失效模式。

**假說。** 酵素家族的重建祖先，一再被發現比現代後代更**雜食（promiscuous）**。
如果這對噬菌體 depolymerase 也成立，祖先型就可能切得動現代酵素切不動的多醣 —— 包含已經逃脫噬菌體的宿主。

**設計。** CDS12_WT 是現代酵素；三個祖先節點是從它往其 GH5 phylogeny 根部這條路徑上的重建。
CDS11_WT 和 CDS10_WT 是同一個 virion 上另外兩個接觸表面的蛋白，納入是因為這個問題針對的是
噬菌體整套表面辨識裝置，不是單一酵素。

**這個 panel 不是等距的**，而且是刻意的。以 361 aa 成熟片段計算，Node1 與 CDS12_WT 有 **77.8%** 相同；
Node40、Node281 對野生型只有 **52.6%** 和 **51.0%**，但彼此有 **87.3%**。
所以這一組是 *野生型 + 一個近親 + 一對較遠的姊妹*。Node1 是保守的測試：
如果連它都表現不同，那個效果就不太可能只是序列距離造成的假象。

## 已經確立的

- **三個祖先都摺疊成跟野生型一樣的 GH5 TIM barrel。** ESMFold v1、單序列：主鏈 RMSD
  Node1 / Node40 / Node281 分別為 0.28 / 0.50 / 0.52 Å，遠在 2 Å 等價標準之內。
  重建改的是表面，不是摺疊。
- **這個建模方法本身在這裡被驗證過。** 用同樣方法摺野生型，再疊到 Espinoza 教授同一區域的
  AlphaFold3 模型上，得到 **0.28 Å / 2139 atoms**，所以祖先模型不是單序列的假象。
- **三者的催化機構都完整** —— GH5 的 acid/base glutamate 位在保守的 NEP motif 上，
  下游有保守的 SPHEY 區塊。
- **CDS10_WT 與 CDS11_WT 共用 N 端 Calx-β anchor**（107 aa 上 42% 相同，兩個 anchor 疊合
  0.50 Å / 446 atoms）：建立在共同 virion 附著模組上的旁系 fiber。

## 還沒確立的

直說，因為重用的人最需要知道的就是這些：

- **六個 part 都還沒有確認的表現。** 三次 SDS-PAGE 只給出 CDS12_WT 一條落在預測質量上的誘導依賴 band，
  以及 `e1` 一條未指認的 band；能分辨兩者的未轉型 BL21(DE3) 對照 lane 還沒跑。
- **CDS_0012 家族的四個蛋白無法用 SDS-PAGE 區分** —— 彼此相差最多 0.43 kDa（1.0%）。
  要鑑定必須靠定序或 intact-mass MS。
- **只有一筆活性結果，而且還沒歸因。** 2026-10-16 的 spot test 中，`e1` 製備液把滴內菌落壓到
  同盤滅菌 PBS 對照的 12%（中位數），Φ8 是 0%，`e40`、`e281` crude lysate 是 53–67%。
  但 `e1` 是逐株跟著 phage 走的，連同一株失效都一致，所以
  **「從 Φ8 原液帶過來可感染的 phage」仍然是最主要的替代解釋**。
  要排除，就要直接對製備液做 plaque assay，目前還沒做。
- **還沒有做過「祖先 vs 現代」的比較。** CDS12_WT 不在那次 spot test 裡。
- **插入序列沒有 codon 最佳化**，而且帶哺乳類風格的 codon bias，這是 band 消失時第一個要懷疑的原因。
  下一個明顯的宿主是 Rosetta 或 BL21-CodonPlus。

## 怎麼重用這組 part

這組設計成可以整組拿，也可以拆成兩半。

- **做 phage therapy 的隊伍**：CDS12_WT 加三個祖先，就是一套現成的「現代 vs 祖先」panel，
  可以接任何 depolymerase 活性試驗。摺疊和催化殘基都查過了，缺的是表現和活性，
  所以這是起點而不是結論。
- **做祖先序列重建（ASR）的隊伍**：三個節點是一個完整記錄的範例 ——
  NCBI nr 前 1000 個 hit、SeaView 裡的 MUSCLE、人工整理、PhyML（WAG、p-inv 0.1、100 bootstraps）、
  IQ-TREE 推祖先態、midpoint-rooted —— 外加對所得序列的結構驗證。
- **做噬菌體生物學的隊伍**：CDS10_WT 和 CDS11_WT 是一株新穎 62 kb 噬菌體上的兩個表面蛋白，
  一個有摺疊層級的 depolymerase 指派，一個完全未指派。

六個都是選殖進 **pET-28a(+)**（NdeI/XhoI）、供 *E. coli* BL21(DE3) 表現的構築。
**載體的 N 端 His6 leader 不屬於任何一個 part 的序列**，也沒有任何一個 part 帶 C 端標籤。

## 貢獻歸屬

GH5 phylogeny、祖先態重建、節點的選擇都是 **Espinoza 教授的工作**，不是學生的；
三條祖先序列是他的設計。學生負責噬菌體分離與定序、變體的結構比較、選殖與表現試驗、
膠體定量，以及 spot test。
所有具名作者（包含教授）都必須先在 registry.igem.org 上 opt in 才能被列名。

---
*草稿 — 2026-10-18。數字：`code/output/1018_construct_structures/` 與
`code/output/1016_spot_test_result/`。證據等級：
[`../2026-10-18_parts_structure_comparison.md`](../2026-10-18_parts_structure_comparison.md)。*
