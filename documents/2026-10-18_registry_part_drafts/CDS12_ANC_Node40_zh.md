# CDS12_ANC_Node40 — 重建的祖先 GH5，node 40（part page 草稿・中文版）

英文正本：[`CDS12_ANC_Node40.md`](CDS12_ANC_Node40.md)。**送件貼英文版。**

| 欄位 | 內容 |
|---|---|
| Part type / role | CDS（`SO:0000316`），**basic part** |
| Title | `Phi8-GH5-ancN40` — reconstructed ancestral GH5 glycoside hydrolase (node 40) |
| Sequence | 1089 bp = `ATG` + CDS + stop → 362 aa。取自 `registry_parts.ffn` |
| Source | **電腦設計序列 — 自然界不存在。** 以噬菌體 9-2-1 Φ8 的 CDS_0012 為核心建立的 GH5 系統發育樹，在 node 40 做 ancestral-state reconstruction，由 Espinoza 教授完成。重建方法：以 CDS_0012 查詢 NCBI nr 取前 1000 個 hits，在 SeaView 內以 MUSCLE 比對並人工修剪至現存序列覆蓋的區段；以 PhyML 建樹（WAG，不變位點比例固定 0.1，100 次 bootstrap）；再於 IQ-TREE 以同一 WAG 矩陣、midpoint-rooted 推論祖先序列。 |
| Designed for | *Escherichia coli*（表現宿主） |
| 序列中**不**包含 | pET-28a 的 `MGSSHHHHHHSSGLVPRGSHM` N 端 His6 leader |
| 團隊簡稱 | `e40` |

**Functional description（設計意圖）：** 噬菌體 GH5 glycoside hydrolase 的重建祖先，比 node 1
更遠離現代酵素，用來測試祖先型酵素是否有**更廣的受質範圍**。

---

## design

**假說**與另外兩個祖先相同：祖先型酵素反覆被發現比現代特化的後代更雜泛，因此我們 GH5 的
祖先型可能切得動野生型切不動的表面多醣 — 包括在**抗噬菌體**宿主上。三個節點只有當成一組
才有意義，見 collection 頁。

**這條序列的位置**（361 aa 成熟 insert 上的 identity）：

| | CDS12_WT | Node1 | Node40 | Node281 |
|---|---|---|---|---|
| **Node40** | **52.6** | 61.8 | — | **87.3** |
| Node1 | 77.8 | — | 61.8 | 57.1 |
| Node281 | 51.0 | 57.1 | 87.3 | — |

這個節點**離現代酵素很遠（52.6%），卻與 Node281 非常接近（87.3%）**。所以 Node40 與 Node281
表現為一*對*：兩者都出現、而 Node1 沒有的差異，才是這個設計最強預測的樣態；只有 Node40 單獨
出現的差異則需要額外解釋。

> **樹上位置（2026-10-18 已確認）。** 教授重建了 CDS_0012 到樹根這條路徑上的每一個祖先節點。
> 編號是任意識別碼、不是深度，但順序是 1, 2, 38, 39, 40, 42, 267, 277, 281，由最晚近排到最古老。
> 因此 node 40 是這條路徑上的中間節點。重建順序與序列 identity 一致，所以這三個祖先 part 是真正的深度序列，
> 不是三個任意點。

**結構。** ESMFold v1，單序列、無 MSA、無 template：**mean pLDDT 85.5**，87.3% 的殘基高於 70。
疊到 CDS12_WT 的 ESMFold 模型上，主鏈 **RMSD 0.50 Å** — 即使序列只有約 52% 相同，仍是同一個
GH5 TIM barrel。相對 Node1 偏低的 pLDDT 集中在表面 loop，也正是重建差異最大的地方。

方法驗證與其他祖先相同：用同一單序列方法摺的野生型 CDS12_WT，疊到 Espinoza 教授同區段的
AlphaFold3 模型得到 **0.28 Å／2139 atoms**。

**催化機制完整。** acid/base glutamate 位於保守的 **NEP** motif — insert 位置 166 的
`IGADLHNEPHG` — 下游有保守的 `SPHDY`。注意相對於 Node1 與野生型，motif 正前方有一個
Tyr→His 取代（`…DLY NEP…` → `…DLH NEP…`），且與 Node281 共有；它緊鄰催化殘基，若兩個遠親
祖先行為相似，這是第一個值得檢查的位置。

**與其他 part 的關係。** **CDS12_WT**（template 確認的 GH5）的變體，是**游離、獨立的酵素**。
與 tail spike **CDS_0011**（depolymerase 只有摺疊證據）及功能未知的 **CDS_0010** 無關。

## experiment

以 NdeI/XhoI 選殖進 **pET-28a(+)**，Twist Bioscience 合成；訂單表 2026-09-10 歸檔。
*E. coli* BL21(DE3)、kanamycin、16–20 °C IPTG 誘導。

⚠️ **`Codon Optimized: No`**，偏哺乳類 codon bias — band 不見時的第一嫌疑；可改用 Rosetta 或
BL21-CodonPlus。

**2026-09-15 SDS-PAGE**：這個 construct 在 gel 1 的 lane **幾乎沒有上樣**，所以那次實驗對它
沒有任何資訊。之後也沒有再跑出可用的 lane。在專案的表現計畫裡它排 **batch 2**，在 CDS12_WT
與 `e1` 之後。

## characterisation

**沒有。** 沒有可解讀的膠 lane、沒有純化、沒有活性資料。

- **與 CDS12_WT 及另外兩個祖先在 SDS-PAGE 上無法區分** — 四者相差最多 0.43 kDa（1.0%）。
  要鑑定需定序或 intact-mass MS。
- 預定讀值：純化後在敏感與 Φ8 抗性菌苔上點樣，與野生型酵素並列，含 imidazole vehicle 與
  PBS 對照。

## application

與 Node281 共同構成祖先面板的**遠端臂**：這一對探得離現代酵素的專一性最遠，因此三者中最有
可能作用在野生型處理不了的多醣上。

## discussion

**限制。** 重建序列是對已不存在之蛋白的假說。尚無表現、無活性、連可解讀的膠 lane 都還沒有。
未最佳化的 codon usage 是實際風險。結構證據是單序列模型：顯示摺疊在重建後存活，不代表酵素能
運作。

**在這組裡的角色。** Node40 與 Node281 彼此 87.3% 相同、與野生型約 52%。把它們視為一對是對
這個面板誠實的讀法，也讓實驗更可解讀：兩個幾乎相同的遠親祖先，提供了 Node1 所沒有的
內部重複。

## attribution

- **Espinoza 教授** — GH5 系統發育樹、ancestral-state reconstruction、節點選擇。
  **本 part 的序列是他的設計，不是學生的。**
- **學生團隊** — 變體的結構比較、選殖、表現試驗、膠密度分析。
- 所有具名作者（含教授）必須先在 registry.igem.org 上 opt in。

---
*草稿 — 2026-10-18。數字：`code/output/1018_construct_structures/`。證據等級：
[`../2026-10-18_parts_structure_comparison.md`](../2026-10-18_parts_structure_comparison.md)。
上面兩個待補項目已於 2026-10-18 依教授交付的資料解決，見
[`../2026-10-18_pi_questionnaire_answers.md`](../2026-10-18_pi_questionnaire_answers.md) A1。*
