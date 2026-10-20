# CDS12_ANC_Node281 — 重建的祖先 GH5，node 281（part page 草稿・中文版）

英文正本：[`CDS12_ANC_Node281.md`](CDS12_ANC_Node281.md)。**送件貼英文版。**

| 欄位 | 內容 |
|---|---|
| Part type / role | CDS（`SO:0000316`），**basic part** |
| Title | `Phi8-GH5-ancN281` — reconstructed ancestral GH5 glycoside hydrolase (node 281) |
| Sequence | 1089 bp = `ATG` + CDS + stop → 362 aa。取自 `registry_parts.ffn` |
| Source | **電腦設計序列 — 自然界不存在。** 以噬菌體 9-2-1 Φ8 的 CDS_0012 為核心建立的 GH5 系統發育樹，在 node 281 做 ancestral-state reconstruction，由 Espinoza 教授完成。重建方法：以 CDS_0012 查詢 NCBI nr 取前 1000 個 hits，在 SeaView 內以 MUSCLE 比對並人工修剪至現存序列覆蓋的區段；以 PhyML 建樹（WAG，不變位點比例固定 0.1，100 次 bootstrap）；再於 IQ-TREE 以同一 WAG 矩陣、midpoint-rooted 推論祖先序列。 |
| Designed for | *Escherichia coli*（表現宿主） |
| 序列中**不**包含 | pET-28a 的 `MGSSHHHHHHSSGLVPRGSHM` N 端 His6 leader |
| 團隊簡稱 | `e281` |

**Functional description（設計意圖）：** 噬菌體 GH5 glycoside hydrolase 的重建祖先，是我們三
個之中離現代酵素最遠的一個，用來測試祖先型酵素是否有**更廣的受質範圍**。

> **Registry「Functional Description」欄位 —— 末句，2026-10-19 更新。**
> `registry.igem.org/parts/bba-26lhlslw` 線上版本結尾是 *"One purification of this construct was
> attempted and failed; see the documentation entries."*，現在不完整了 —— blot 說明了失敗原因。
> 改成：
>
> > One purification of this construct was attempted and failed, but an anti-His dot blot on
> > 2026-10-19 found the flow-through positive at 2.9x the negative control, indicating the
> > protein was expressed and did not bind the resin. See the documentation entries.
>
> 另外兩個 Documentation **標題**也要改：
> - Experiment：*"Cloning, and a failed Ni-NTA purification (2026-10-10)"* →
>   **"Cloning, a failed Ni-NTA purification, and the dot blot that explains it"**
> - Characterisation：*"First activity data, plus one documented failed purification"* →
>   **"First activity data, and anti-His evidence that the protein was expressed"**

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

> **樹上位置（2026-10-18 已確認）。** 教授重建了 CDS_0012 到樹根這條路徑上的每一個祖先節點。
> 編號是任意識別碼、不是深度，但順序是 1, 2, 38, 39, 40, 42, 267, 277, 281，由最晚近排到最古老。
> 因此 node 281 是我們三個之中最深、最接近樹根的一個。重建順序與序列 identity 一致，所以這三個祖先 part 是真正的深度序列，
> 不是三個任意點。

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

只看 10-10 那張膠，無法區分「沒有表現」「產物不可溶」「管柱失效」。

**Anti-His dot blot，2026-10-19**（`lab_notebook/digitalized/2026-10-19_dot-blot-his-tag.md`；
量化在 `code/1019_dotblot/`）。11 個樣品直接點在膜上，用單一步 anti-His HRP conjugate 偵測。
陽性對照達到陰性對照的約 18 倍，顯色化學確實有效。dot blot 報告的是 **His tag，不是大小也不是
活性**，而且這張的偵測下限偏高——膜上所有 1:10 稀釋都掉到背景——所以「沒有訊號」只是很弱的
反證。

**這個 part 的 flow-through（`e281 FT1`）驗出 His 陽性，是陰性對照的 2.9 倍**，為膜上第二強的
訊號。這解掉了上面的三選一：**蛋白有表現，只是沒有結合樹脂。** 失敗的是捕捉而不是表現，所以
下一步要動的是結合條件——load 裡帶進去的 imidazole、結合時間、樹脂選擇——而不是再做一次一模
一樣的純化。未轉形 BL21(DE3) 對照 lane 仍然欠著。

## characterisation

**第一筆活性資料，2026-10-16 — 對這個變體而言基本上是負面的。**

**Spot test，2026-10-16**（`code/1016_spot_test_result.ipynb`；圖與 caption 在
`code/output/1016_spot_test_result/`）。7 株 *Pseudomonas* 以 double-layer 方式鋪菌苔
（200 µL 菌液 + 3 mL soft agar）。每盤點 5 滴、各 7 µL：Φ8 phage 原液（陽性對照）、
滅菌 1× PBS（陰性對照），以及 `e1`、`e40`、`e281` 製備液，都用同一管滅菌 PBS 稀釋 1:10。
10/12 點盤，10/16 判讀。

沒有任何一滴出現透明的裂解區，Φ8 也沒有。看得到的讀值是**滴內長出的菌落數**：滅菌 PBS 滴
穩定長出獨立菌落（中位數 14），這是一滴液體落在這種菌苔上的基準。以此為基準，各處理的中位數為
**Φ8 0、`e1` 1、`e40` 10、`e281` 9**。

`e281` crude lysate 只讓菌落數略為減少，中位數從 14 降到 9。

每一盤都點了自己的滅菌 PBS 對照，而各盤的基準本來就不同（7–17 顆），所以可比的數字是
**每一滴佔同一盤 PBS 滴的百分比**。換算後的中位數是
**Φ8 0%、`e1` 12%、`e281` 53%、`e40` 67%**（`spot_percent_of_pbs.tsv`）。 這個變體落在 **53%**，很接近無效果線。

**這能說什麼、不能說什麼**
- `e281` 製備液是 **crude lysate**，不是純化蛋白，酵素沒有被濃縮。這裡效果弱
  **不代表**這個變體沒有活性；這個實驗分不出「沒有活性」和「被稀釋掉的活性」。
- 表現現在有正面證據了：`e281` 的 flow-through 在 2026-10-19 的 blot 上 His 陽性。但這**救不了**
  這個結果，因為這裡點的是 **1:10 crude lysate**，而那張 blot 上所有 1:10 稀釋都掉到偵測下限
  以下。滴裡到底有多少酵素仍然未知。
- 相對地，唯一經過純化步驟的 `e1` 製備液在同一個實驗裡幾乎完全壓住菌落（中位數 1）。這個差別
  對應的是製備方式，不一定是序列。
- 這次**沒有**點野生型 CDS12_WT，所以設計要問的「祖先 vs 現代」比較還沒做。
- 單一濃度、每株一盤，菌落由影像自動分割計數；沒有重複、沒有統計。
- 沒有透明區就沒有 halo，所以這還不是傳統意義上的 depolymerase 活性。
- **與 CDS12_WT 及另外兩個祖先在 SDS-PAGE 上無法區分** — 四者相差最多 0.43 kDa（1.0%）。
  要鑑定需定序或 intact-mass MS。
- 給同時在看 `e1` 結果的人：那個活性**也還沒有歸因到蛋白**。`e1` 是逐株跟著 Φ8 走的，
  所以「從 Φ8 原液帶過來可感染的 phage」仍然是最主要的替代解釋，要用對製備液做 plaque assay
  才能排除。
- 下一步：純化這個變體、與其他樣品等量後，連同 elution buffer 單獨對照與 CDS12_WT 一起重點。

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
上面兩個待補項目已於 2026-10-18 依教授交付的資料解決，見
[`../2026-10-18_pi_questionnaire_answers.md`](../2026-10-18_pi_questionnaire_answers.md) A1。*

*紀錄 — 2026-10-18：characterisation 依 2026-10-16 的 spot test 更新
（[`../../code/1016_spot_test_result.ipynb`](../../code/1016_spot_test_result.ipynb)）。
**這筆修改還沒同步到 registry.igem.org** — 線上的 part page 是依更早的版本轉錄的。*
