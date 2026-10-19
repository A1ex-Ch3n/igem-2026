# CDS12_ANC_Node1 — 重建的祖先 GH5，node 1（part page 草稿・中文版）

英文正本：[`CDS12_ANC_Node1.md`](CDS12_ANC_Node1.md)。**送件貼英文版。**

| 欄位 | 內容 |
|---|---|
| Part type / role | CDS（`SO:0000316`），**basic part** |
| Title | `Phi8-GH5-ancN1` — reconstructed ancestral GH5 glycoside hydrolase (node 1) |
| Sequence | 1089 bp = `ATG` + CDS + stop → 362 aa。取自 `registry_parts.ffn` |
| Source | **電腦設計序列 — 自然界不存在。** 以噬菌體 9-2-1 Φ8 的 CDS_0012 為核心建立的 GH5 系統發育樹，在 node 1 做 ancestral-state reconstruction，由 Espinoza 教授完成。重建方法：以 CDS_0012 查詢 NCBI nr 取前 1000 個 hits，在 SeaView 內以 MUSCLE 比對並人工修剪至現存序列覆蓋的區段；以 PhyML 建樹（WAG，不變位點比例固定 0.1，100 次 bootstrap）；再於 IQ-TREE 以同一 WAG 矩陣、midpoint-rooted 推論祖先序列。 |
| Designed for | *Escherichia coli*（表現宿主） |
| 序列中**不**包含 | pET-28a 的 `MGSSHHHHHHSSGLVPRGSHM` N 端 His6 leader |
| 團隊簡稱 | `e1` |

**Functional description（設計意圖）：** 噬菌體 GH5 glycoside hydrolase 的重建祖先，用來測試
祖先型酵素是否比現代、已特化的版本有**更廣的受質範圍**。

---

## design

**假說。** 現代噬菌體 depolymerase 是專一型的：每一個都針對自己宿主的表面醣調校過，這也正是
宿主一旦改變那個醣、噬菌體療法就失效的原因。酵素家族的重建祖先反覆被發現比現代後代更
**雜泛（promiscuous）**。因此我們 GH5 的祖先型，可能切得動野生型酵素切不動的多醣 — 包括在
**抗噬菌體**的突變株上。這三個祖先（`_Node1`、`_Node40`、`_Node281`）就是這個測試，而且只有
當成一組才有意義，見 collection 頁。

**這條序列相對其他的位置**（361 aa 成熟 insert 上的 identity，`sequence_identity.csv`）：

| | CDS12_WT | Node1 | Node40 | Node281 |
|---|---|---|---|---|
| **Node1** | **77.8** | — | 61.8 | 57.1 |
| Node40 | 52.6 | 61.8 | — | 87.3 |
| Node281 | 51.0 | 57.1 | 87.3 | — |

Node1 是**三者中最接近現代酵素的**（77.8%）。Node40 與 Node281 離它遠得多（約 52%），但彼此
高達 87.3%。所以這個面板是*野生型 + 一個近親 + 一對遠親*，不是三個等距的點。

> **樹上位置（2026-10-18 已確認）。** 教授重建了 CDS_0012 到樹根這條路徑上的每一個祖先節點。
> 編號是任意識別碼、不是深度，但順序是 1, 2, 38, 39, 40, 42, 267, 277, 281，由最晚近排到最古老。
> 因此 node 1 是這條路徑上最晚近的重建祖先。重建順序與序列 identity 一致，所以這三個祖先 part 是真正的深度序列，
> 不是三個任意點。

**結構。** ESMFold v1，單序列、無 MSA、無 template：**mean pLDDT 90.0**，95.8% 的殘基高於 70 —
三個祖先模型中最有信心的一個。疊到 CDS12_WT 的 ESMFold 模型上，主鏈 **RMSD 0.28 Å**，遠在 2 Å
等價判準之內。重建改的是表面，不是摺疊。

方法本身在這裡也被驗證過：用同樣的單序列方法摺野生型，再疊到 Espinoza 教授同一區段的
AlphaFold3 模型，得到 **0.28 Å／2139 atoms**，所以這些祖先模型不是單序列方法的假象。

**催化機制完整。** GH5 的 acid/base glutamate 位於保守的 **NEP** motif — insert 位置 166 的
`IGADLYNEPHQ` — 下游有保守的 `SPHEY` 區塊。同樣的摺疊、同樣的催化殘基、不同的表面：這是
「活性酵素但專一性改變」的結構前提。

**與其他 part 的關係。** 這是 **CDS12_WT**（template 確認的 GH5）的變體 — 一個**游離、獨立的
酵素**。它與 tail spike **CDS_0011** 無關（後者的 depolymerase 身分只有摺疊證據），也與功能
未知的 **CDS_0010** 無關。

## experiment

以 NdeI/XhoI 選殖進 **pET-28a(+)**，Twist Bioscience 合成；訂單表於 2026-09-10 歸檔。
*E. coli* BL21(DE3)、kanamycin、16–20 °C IPTG 誘導。

⚠️ **`Codon Optimized: No`**，而且 insert 用的是偏哺乳類的 codon bias（`CCC`/`GGG`/`GCC` 偏多）
而不是 *E. coli*。band 不見時這是第一個要懷疑的；下一步宿主可換 Rosetta 或 BL21-CodonPlus。

**2026-09-29 SDS-PAGE**（`code/0929_gel_annotation.ipynb`）：在 **45–50 kDa 出現一條強而乾淨的
band，四個 lane（誘導與未誘導）都有**，比預測的 41.9 kDa 高 7–19%。**未歸屬。** 它不能單純
當成產物，因為同一次實驗裡質量相同的 CDS12_WT 是落在預測值上的。宿主蛋白同樣符合這筆資料，
而能一槌定音的未轉形 BL21(DE3) 對照 lane 仍然欠缺。

## characterisation

**第一筆活性資料，2026-10-16 — 正向但初步。**

**Spot test，2026-10-16**（`code/1016_spot_test_result.ipynb`；圖與 caption 在
`code/output/1016_spot_test_result/`）。7 株 *Pseudomonas* 以 double-layer 方式鋪菌苔
（200 µL 菌液 + 3 mL soft agar）。每盤點 5 滴、各 7 µL：Φ8 phage 原液（陽性對照）、
滅菌 1× PBS（陰性對照），以及 `e1`、`e40`、`e281` 製備液，都用同一管滅菌 PBS 稀釋 1:10。
10/12 點盤，10/16 判讀。

沒有任何一滴出現透明的裂解區，Φ8 也沒有。看得到的讀值是**滴內長出的菌落數**：滅菌 PBS 滴
穩定長出獨立菌落（中位數 14），這是一滴液體落在這種菌苔上的基準。以此為基準，各處理的中位數為
**Φ8 0、`e1` 1、`e40` 10、`e281` 9**。

`e1` 滴幾乎完全壓住了菌落生長，程度和 phage 相當，7 株中有 6 株如此。`e1` 滴有 90% 是同一管
滅菌 PBS，所以差別來自 `e1` 製備液本身。

**這能說什麼、不能說什麼**
- 這是第一個證據，顯示 `e1` 製備液帶有對 *Pseudomonas* 的活性，也是三個祖先變體中最強的訊號。
- 這**不能**指認活性來自這個蛋白。表現仍未確認（見 *experiment*），而且製備液所在的
  elution buffer（imidazole）沒有單獨點過 — 那個 vehicle 對照是下一個實驗。
- 這次**沒有**點野生型 CDS12_WT，所以設計要問的「祖先 vs 現代」比較還沒做。
- 單一濃度、每株一盤，菌落由影像自動分割計數；沒有重複、沒有統計。
- 沒有透明區就沒有 halo，所以這還不是傳統意義上的 depolymerase 活性。
- **與 CDS12_WT 及另外兩個祖先在 SDS-PAGE 上無法區分** — 四者相差最多 0.43 kDa（1.0%）。
  要鑑定需定序或 intact-mass MS。
- 下一步：imidazole vehicle 單獨一滴、`e1` 稀釋系列，以及把 CDS12_WT 和 Φ8 抗性突變株
  排在同一盤上重跑。

## application

噬菌體衍生抗菌工具組中的**廣效臂**：可能清除現代酵素清不掉的表面多醣，用於已經靠改變醣而
逃脫噬菌體的宿主。任何想要「祖先型 vs 現代型 depolymerase 對照」的團隊都能重用。

## discussion

**限制。**
- 重建序列是**對一個已不存在的蛋白所做的假說**，不是任何真實祖先噬菌體的證據。
- 表現未確認、沒有活性資料，唯一觀察到的 band 未歸屬。
- 未最佳化、偏哺乳類的 codon usage 是實際的表現風險。
- 結構證據是單序列模型：它說的是摺疊在重建後存活下來，不是酵素能運作。

**在這組裡的角色。** 與野生型 77.8% 相同，這個節點是保守的測試：如果連*這個*祖先都表現得與
CDS12_WT 不同，那效應就不太可能只是序列距離造成的假象。Node40 與 Node281 則探得遠得多。

## attribution

- **Espinoza 教授** — GH5 系統發育樹、ancestral-state reconstruction、節點的選擇。
  **本 part 的序列是他的設計，不是學生的**，Contribution Roles 必須這樣寫。
- **學生團隊** — 變體的結構比較、選殖、表現試驗、膠密度分析。
- 所有具名作者（含教授）必須先在 registry.igem.org 上 opt in。

---
*草稿 — 2026-10-18。數字：`code/output/1018_construct_structures/`。證據等級：
[`../2026-10-18_parts_structure_comparison.md`](../2026-10-18_parts_structure_comparison.md)。
上面兩個待補項目已於 2026-10-18 依教授交付的資料解決，見
[`../2026-10-18_pi_questionnaire_answers.md`](../2026-10-18_pi_questionnaire_answers.md) A1。*

*紀錄 — 2026-10-18：characterisation 依 2026-10-16 的 spot test 更新
（[`../../code/1016_spot_test_result.ipynb`](../../code/1016_spot_test_result.ipynb)）。
**這筆修改還沒同步到 registry.igem.org** — 線上的 part page 是依更早的版本轉錄的。*
