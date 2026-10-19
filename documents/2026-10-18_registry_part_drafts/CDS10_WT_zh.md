# CDS10_WT — 功能未知的 virion fiber（part page 草稿・中文版）

英文正本：[`CDS10_WT.md`](CDS10_WT.md)。**送件貼英文版。**

| 欄位 | 內容 |
|---|---|
| Part type / role | CDS（`SO:0000316`），**basic part** |
| Title | `Phi8-Fiber10` — virion fiber of unknown function（CDS_0010 res 105–917） |
| Sequence | 2445 bp = `ATG` + CDS + stop → 814 aa。取自 `registry_parts.ffn` |
| Source | Bacteriophage 9-2-1 Φ8，本團隊自土壤分離的新穎 ~62 kb podovirus；CDS_0010 採用教授 `UUAIURNK_` Pharokka 註解的編號。Construct = 917 aa 蛋白的 res 105–917 |
| Designed for | *Escherichia coli*（表現宿主）；source organism = phage 9-2-1 Φ8 |
| 序列中**不**包含 | pET-28a 的 `MGSSHHHHHHSSGLVPRGSHM` N 端 His6 leader |

**Functional description（設計意圖）：** 一條與 tail spike 旁系同源的 virion fiber，表現它的
目的就是**弄清楚它在做什麼** — 功能確實未知，這個 part 也就以這個狀態送件。

---

## design

CDS_0010 位於噬菌體 9-2-1 Φ8 的 tail 模組，與 tail spike CDS_0011 共用 N 端的
**Calx-β anchor**：序列 42% identity／107 aa，兩個 anchor 疊合 **RMSD 0.50 Å／446 atoms**
（CE 法 0.96 Å／88 殘基）。兩者是**建立在同一個 virion 附著模組上的旁系 fiber** — 這是我們對
這個蛋白所能說的、支持度最高的一件事。

其餘一切都還是開放的：

- 剩下約 800 個殘基**完全沒有結構 template**。整條鏈唯一的命中是 res 361–456 一個微弱的 IspD。
- AF3 模型作為**形狀**是有信心的 — pTM 0.80，cloned 區域內 mean pLDDT 90.8，其中 98.3% 的殘基
  高於 70 — 但對摺疊有信心並不等於知道功能。

> **這個 part 刻意*不*被稱為 glycosidase。** 早期註解曾這樣建議；我們的 template 分析從來不支持，
> 教授也已於 2026-07-29 撤回該說法。誠實的敘述是 **unknown function**。我們選擇把它選殖、表現，正是因為如此：
> 一個沒有結構 template 的 tail-module 蛋白，功能只能靠實驗決定。
>
> 三個野生型 part 要分清楚：**CDS_0010 = 功能未知**；**CDS_0011** = 附著於 virion 的 tail spike，
> 其 depolymerase 身分**只有摺疊層級證據**（β-helix、無 template、無具名同源蛋白）；
> **CDS_0012** = template 確認的 **GH5 glycoside hydrolase**，是獨立的游離蛋白。三個蛋白、
> 三種宣稱、三種證據等級。

**Construct 邊界。** res 105–917 切在 Calx-β anchor（res 1–110）內側一點點，完整保留那段大面積
未解析的區域。Anchor 是 fiber 附著到 virion 的部位，所以移除它的大部分會得到可溶蛋白，而不是
一個組裝元件。

**模型：** AlphaFold3 Server 單體，由 **Espinoza 教授**製作。

## experiment

以 NdeI/XhoI 選殖進 **pET-28a(+)**，Twist Bioscience 合成，2026-07-27 訂單。*E. coli* BL21(DE3)、
kanamycin、16–20 °C IPTG 誘導。

**狀態：尚未認真嘗試。** 在專案的表現計畫裡，這個 construct 排在 **batch 3**，在 CDS12_WT 與三個
祖先變體之後；而且 91.6 kDa 是六個當中最難表現的。目前所有膠都沒有它可解讀的 lane。

## characterisation

**沒有。** 沒有表現、沒有純化、沒有活性資料。以「序列＋結構」的貢獻送件，並明確標示功能未定。

## application

兩種用途，兩種都對現況誠實：

1. **功能鑑定的標的。** 質體已在手上；任何擁有 *Pseudomonas* 宿主與表面多醣試驗的團隊都可以
   接手測試。
2. **Calx-β anchor 模組的來源。** 共用的 anchor（res 1–110，與 tail spike 有 42% identity）是
   chimeric fiber 工程的候選附著零件 — 這個噬菌體的兩條不同 fiber 都在用的模組。

## discussion

**限制。** 功能未知；約 800 aa 沒有 template；模型只對形狀有信心。表現未經測試，而且 91.6 kDa
是硬骨頭。

**為什麼要送一個功能未知的 part？** 因為序列與那個結構關係本身就是真實的結果，而且 Registry
明確肯定負面與不確定的紀錄。一條 fiber 與已鑑定的 tail spike 共用 anchor、其餘 800 個殘基在 PDB
裡找不到任何對應 — 這正是未來某個團隊可能認得出來的那種條目；而另一條路，也就是在毫無證據下
把它標成 glycosidase，正是先前註解出錯的方式。

**未來方向。** 低溫表現；若可溶，與 CDS_0012 並排對宿主純化 LPS 測試；同時隨著結構資料庫擴充，
持續搜尋遠源同源蛋白。

## attribution

- **Espinoza 教授** — AlphaFold3 摺疊與 Pharokka 註解（`UUAIURNK_`）；以及 2026-07-29 撤回
  glycosidase 的判斷，本頁遵循該判斷。
- **學生團隊** — 噬菌體分離、定序與組裝；template 與 anchor 同源性分析；選殖。
- 用 Registry 的 **Contribution Roles** 逐位作者記錄；所有作者必須先 opt in。

---
*草稿 — 2026-10-18。數字：`code/output/1018_construct_structures/`。證據等級：
[`../2026-10-18_parts_structure_comparison.md`](../2026-10-18_parts_structure_comparison.md)。*
