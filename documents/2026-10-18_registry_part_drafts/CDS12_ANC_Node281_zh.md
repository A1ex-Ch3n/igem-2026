# CDS12_ANC_Node281 — 重建的祖先 GH5，node 281（part page 草稿・中文版）

英文正本：[`CDS12_ANC_Node281.md`](CDS12_ANC_Node281.md)。**送件貼英文版。**

| 欄位 | 內容 |
|---|---|
| Part type / role | CDS（`SO:0000316`），**basic part** |
| Title | `Phi8-GH5-ancN281` — reconstructed ancestral GH5 glycoside hydrolase (node 281) |
| Sequence | 1089 bp = `ATG` + CDS + stop → 362 aa。取自 `registry_parts.ffn` |
| Source | **電腦設計序列 — 自然界不存在。** 以噬菌體 9-2-1 Φ8 的 CDS_0012 為核心建立的 GH5 系統發育樹，在 node 281 做 ancestral-state reconstruction，由 Espinoza 教授完成。⬜ **UNDONE：送件前要補上重建所用的程式、比對與樹。** |
| Designed for | *Escherichia coli*（表現宿主） |
| 序列中**不**包含 | pET-28a 的 `MGSSHHHHHHSSGLVPRGSHM` N 端 His6 leader |
| 團隊簡稱 | `e281` |

**Functional description（設計意圖）：** 噬菌體 GH5 glycoside hydrolase 的重建祖先，是我們三
個之中離現代酵素最遠的一個，用來測試祖先型酵素是否有**更廣的受質範圍**。

---

## design

**假說**三個祖先共用：祖先型酵素傾向比現代特化後代更雜泛，因此祖先型 GH5 可能切得動野生型
切不動的表面多醣 — 包括在**抗噬菌體**宿主上。三個節點是當成一組設計的，見 collection 頁。

**這條序列的位置**（361 aa 成熟 insert 上的 identity）：

| | CDS12_WT | Node1 | Node40 | Node281 |
|---|---|---|---|---|
| **Node281** | **51.0** | 57.1 | **87.3** | — |
| Node1 | 77.8 | — | 61.8 | 57.1 |
| Node40 | 52.6 | 61.8 | — | 87.3 |

**三者中離現代酵素最遠（51.0%）**，而與 Node40 有 87.3%。兩者表現為一對，讓面板在最遠端
有了內部重複。

> ⬜ **UNDONE — 在教授說明 node 281 在樹上的位置之前，不要用樹深度描述它**（「淺」「晚近」
> 「最接近現生分支」）。只有上面的 identity 是我們能講的。

**結構。** ESMFold v1，單序列、無 MSA、無 template：**mean pLDDT 85.8**，88.1% 的殘基高於 70。
疊到 CDS12_WT 的 ESMFold 模型上，主鏈 **RMSD 0.52 Å**。序列變了一半，GH5 TIM barrel 卻紋風
不動；差異落在表面 loop，也正是模型信心最低的地方。

方法驗證同前：用同一單序列方法摺的野生型 CDS12_WT，疊到教授同區段的 AlphaFold3 模型得到
**0.28 Å／2139 atoms**。

**催化機制完整。** acid/base glutamate 位於保守的 **NEP** motif — insert 位置 166 的
`IGADLHNEPHG` — 下游有保守的 `SPHDY`。它與 Node40 共有 motif 正前方的 Tyr→His 取代，這點與
Node1 和野生型都不同；若這兩個遠親祖先行為相似，這是第一個該測的位置。

**與其他 part 的關係。** **CDS12_WT**（template 確認的 GH5）的變體，是**游離、獨立的酵素**。
與 tail spike **CDS_0011**（depolymerase 只有摺疊證據）及功能未知的 **CDS_0010** 無關。

## experiment

以 NdeI/XhoI 選殖進 **pET-28a(+)**，Twist Bioscience 合成；訂單表 2026-09-10 歸檔。
*E. coli* BL21(DE3)、kanamycin、16–20 °C IPTG 誘導。

⚠️ **`Codon Optimized: No`**，偏哺乳類 codon bias — band 不見時的第一嫌疑；可改用 Rosetta 或
BL21-CodonPlus。

這是唯一一個我們嘗試純化的 construct，而且**純化失敗了**（2026-10-10，
`code/1010_gel_annotation.ipynb`）：

- Ni-NTA 的 **elution E1、E2 是空白膠** — peak prominence 0.011，對比實測噪訊底 0.020；
  lane 總量落在「從未上樣」的區間內。
- **Flow-through 與 load 無法區分**：兩者都有同一條 40–44 kDa band。沒有東西結合樹脂，
  所以那條接近預測 42.3 kDa 的 band 行為像宿主蛋白，不像 His6 標籤的 construct。
- 2026-09-29 的粗萃膠早已顯示這個 construct 在 42.3 kDa 沒有 band。

這個結果無法區分「沒有表現」「產物不可溶」「管柱失效」。文件化的下一步**不是**再純化一次，
而是跑粗萃 ±IPTG 並附上未轉形 BL21(DE3) 的 lane，或做 anti-His western。

## characterisation

**沒有，但有一個記錄在案的負面結果**（上述失敗的純化）。之所以寫進來，是因為 Registry 明講
負面與不確定的結果仍有價值。

- **與 CDS12_WT 及其他祖先在 SDS-PAGE 上無法區分** — 四者相差最多 0.43 kDa（1.0%）。
  要鑑定需定序或 intact-mass MS。
- 預定讀值：先確立表現，再於敏感與 Φ8 抗性菌苔上點樣，與野生型酵素並列，含 imidazole
  vehicle 與 PBS 對照。

## application

與 Node40 共同構成祖先面板的**遠端臂** — 離現代酵素專一性最遠的一對，也是三者中最可能在
野生型失效處起作用的。

## discussion

**限制。** 重建序列是對已不存在之蛋白的假說。表現未確認，且一次純化嘗試徹底失敗。未最佳化的
codon usage 是實際風險。結構證據是單序列模型。

**那次失敗的純化說明了什麼、沒說明什麼。** 它**沒有**證明蛋白不存在 — 還沒有任何對照 lane
排除「這個 construct 根本沒在表現」，也沒有跑不可溶沉澱的 lane。任何重用這個 part 的人，
應該先在粗萃液中證明蛋白存在，再投入管柱，並且把沉澱留成獨立的一個 lane。

**在這組裡的角色。** 作為分歧最大的一個（與野生型 51.0%），這個節點是雜泛性假說最強的測試，
也是最可能錯誤摺疊或表現不良的一個。它的近雙胞 Node40 正好是這兩項風險的對照。

## attribution

- **Espinoza 教授** — GH5 系統發育樹、ancestral-state reconstruction、節點選擇。
  **本 part 的序列是他的設計，不是學生的。**
- **學生團隊** — 變體的結構比較、選殖、表現試驗、Ni-NTA 嘗試、膠密度分析。
- 所有具名作者（含教授）必須先在 registry.igem.org 上 opt in。

---
*草稿 — 2026-10-18。數字：`code/output/1018_construct_structures/`。證據等級：
[`../2026-10-18_parts_structure_comparison.md`](../2026-10-18_parts_structure_comparison.md)。
上面兩個 UNDONE 必須先與教授確認，這個 part 才能離開 Draft。*
