# CDS12_WT — GH5 glycoside hydrolase（part page 草稿・中文版）

英文正本：[`CDS12_WT.md`](CDS12_WT.md)。**送件貼英文版。**

| 欄位 | 內容 |
|---|---|
| Part type / role | CDS（`SO:0000316`），**basic part** |
| Title | `Phi8-GH5` — phage GH5 glycoside hydrolase（CDS_0012 res 117–477） |
| Sequence | 1089 bp = `ATG` + CDS + stop → 362 aa。取自 `registry_parts.ffn` |
| Source | Bacteriophage 9-2-1 Φ8，本團隊自土壤分離的新穎 ~62 kb podovirus；CDS_0012 採用教授 `UUAIURNK_` Pharokka 註解的編號。Construct = 477 aa 蛋白的 res 117–477 |
| Designed for | *Escherichia coli*（表現宿主）；source organism = phage 9-2-1 Φ8 |
| 序列中**不**包含 | pET-28a 的 `MGSSHHHHHHSSGLVPRGSHM` N 端 His6 leader |

**Functional description（設計意圖）：** 一個噬菌體 glycoside hydrolase family 5（GH5）酵素，
以游離蛋白形式表現，用來降解宿主的表面多醣。

---

## design

CDS_0012 是 **glycoside hydrolase family 5** 酵素：CAZy clan GH-A，**(β/α)₈ TIM barrel**，
retaining 機制，催化用的兩個 glutamate 位於 barrel 的 C 端面。GH5 涵蓋了經典的細菌
endoglucanase；在噬菌體基因組裡，GH5 類酵素扮演 **depolymerase** — 剝除擋在噬菌體與細胞表面
之間的莢膜、EPS 或 O-antigen。因為它是可溶酵素而非 virion 組成，所以不需要噬菌體本體就能作用。

**這是全專案最強的結構宣稱。** res 118–475 上的四個 AlphaFold3 template 全部是 GH5
endoglucanase — **1ECE**（帶 cellotetraose）、**1VRX**、**4TUF**、**2ZUM** — pLDDT 95–98。
AF3 單體 pTM 0.77；cloned 區域內 mean pLDDT **96.4**，其中 98.9% 的殘基高於 70。

> **CDS_0012 是*獨立的蛋白*，不是 tail spike 的 domain。** 當問題被問成「tail spike 裡面的酵素
> domain」時，被確認的 glycoside hydrolase 其實是這個獨立蛋白。Tail spike 是 **CDS_0011**，
> 另一個 part：附著於 virion，而且它的 depolymerase 身分**只有摺疊層級的證據**（β-helix、
> 無 template、無具名同源蛋白）。兩個不同蛋白、兩個不同的酵素宣稱、兩個差很多的證據等級。
> CDS_0010 又是第三種情況 — **功能未知**。

**Construct 邊界。** res 117–477 基本上就是整個 TIM barrel，只留掉一小段 N 端延伸。Barrel 就是
催化單元，所以這個 part 就是那個酵素。

**催化機制。** GH5 的 acid/base glutamate 位於保守的 **NEP** motif — 本序列 insert 位置 165 的
`IGADLYNEPHL` — 下游還有保守的 `SPH(D/E)Y` 區塊，兩者都在。*待辦：第二個催化 glutamate
（nucleophile）應該用疊合 1ECE 來指認，而不是靠 motif 比對。*

**變體。** 這個酵素的三個重建祖先（`CDS12_ANC_Node1 / _Node40 / _Node281`）各自是獨立的 part，
並屬於同一個 collection。三個都摺疊成同一個 TIM barrel：疊到本蛋白的模型上，主鏈 RMSD 分別是
**0.28 / 0.50 / 0.52 Å**，遠在 2 Å 等價判準之內 — 即使 Node40 與 Node281 跟它只有約 52% 的序列
相同度。

**模型驗證。** 用 **ESMFold**（單序列、無 MSA、無 template）摺這條序列，再疊到同一區段的 AF3
模型上，得到 **0.28 Å／2139 atoms** — 兩個獨立方法給出一致結果，這也正是我們敢用 ESMFold 模型
來處理祖先變體的依據。AF3 摺疊是 **Espinoza 教授**的工作。

## experiment

以 NdeI/XhoI 選殖進 **pET-28a(+)**，Twist Bioscience 合成，2026-07-27 訂單。*E. coli* BL21(DE3)、
kanamycin、16–20 °C IPTG 誘導 16 小時。

2026-09-29 的 SDS-PAGE（`code/0929_gel_annotation.ipynb`）：在 40–43 kDa 出現一條
**IPTG 依賴的 band**，落在預測的 41.8 kDa 上；未誘導 lane 雖然總蛋白更多卻沒有這條。這是全專案
第一個誘導依賴訊號，因此這個 construct 排在純化隊列第一位。

**Anti-His dot blot，2026-10-19**（`lab_notebook/digitalized/2026-10-19_dot-blot-his-tag.md`；
量化在 `code/1019_dotblot/`）。這個 construct 以「誘導／未誘導」成對點在膜上，**兩者分不出
來**——4.4 對 3.9，即 1.1 倍，落在雜訊裡——所以這張 blot 對本 construct **沒有給出誘導依賴的
His 訊號**；而同一張膜上陽性對照達到陰性的約 18 倍，另外兩個 construct 也是陽性。這不推翻
09-29 那條 band，但也不支持它，兩個結果應該並讀。該 blot 偵測下限偏高（膜上所有 1:10 稀釋都掉
到背景），而且 dot blot 驗的是 His tag 不是蛋白本身。

尚未完成：未轉形 BL21(DE3) 對照 lane、能分離大小的 anti-His western、本 construct 的 Ni-NTA
純化。

## characterisation

**初步且不完整。**

- 一條落在預測質量上的誘導依賴 band（見上）。**尚未確認**就是這個蛋白：沒有 western、沒有質譜，
  而且能排除宿主蛋白的對照 lane 還沒跑。
- 沒有純化蛋白，因此**沒有活性資料**。這個 construct 也**沒有**被納入 2026-10-16 的 spot
  test，所以設計上要求的「祖先 vs 現代」比較至今仍然缺少現代那一側。
- 給重用者的提醒：本蛋白與三個祖先變體彼此質量差距最多 0.43 kDa（1.0%），
  **SDS-PAGE 無法區分**。要確認身分必須靠定序或 intact-mass MS。
- **沒有納入 2026-10-16 的 spot test。** 那次是在 7 株 *Pseudomonas* 菌苔上，把三個祖先變體
  與 Φ8 phage、滅菌 PBS 對照並排比較（`code/1016_spot_test_result.ipynb`）；`e1` 製備液把滴內
  菌落壓制的程度幾乎和 phage 一樣。**這個野生型酵素正是缺席的對照組** — 沒有它在同一盤上，
  就不能下任何「祖先 vs 現代」的結論。把 CDS12_WT 放進這個 assay，是這個 part 下一步最有價值的實驗。
- 預定讀值：宿主菌苔上的 spot assay，與 imidazole vehicle 對照比較 halo。

## application

針對土壤 *Pseudomonas* 的噬菌體衍生抗菌工具組中的**溶解／表面剝除模組**。作為游離酵素，不需要
具感染力的 virion 即可施用 — 這正是我們針對抗性宿主採取的路線，也是測試祖先變體是否比現代酵素
有更廣受質範圍的原因。

## discussion

**限制。**
- GH5 的歸屬是結構性的（template + 摺疊），不是酵素學的：尚未測試任何受質，且假定的天然受質是
  宿主表面多醣而不是纖維素。
- 表現證據只有一條大小正確的 band，還稱不上身分鑑定。
- Nucleophile 尚未以結構指認（見 *design*）。

**比較。** 相對於 tail spike CDS_0011，本蛋白是證據較強的酵素，但標靶能力較弱：spike 承擔宿主
辨識功能與三聚體 β-helix，而本蛋白是緊緻、可溶、單體的 barrel — 更容易表現、純化與施用。

**未來方向。** 純化 → 用 western 或 MS 確認身分 → 對宿主純化 LPS 以及抗性突變株做活性試驗，
並與三個祖先並排比較。

## attribution

- **Espinoza 教授** — AlphaFold3 摺疊、Pharokka 註解（`UUAIURNK_`），以及三個變體 part 背後的
  GH5 系統發育樹與 ancestral-state reconstruction。
- **學生團隊** — 噬菌體分離、定序與組裝；template 與 domain 分析；選殖、表現試驗、膠密度分析。
- 用 Registry 的 **Contribution Roles** 逐位作者記錄；所有作者必須先 opt in。

---
*草稿 — 2026-10-18。數字：`code/output/1018_construct_structures/`。證據等級：
[`../2026-10-18_parts_structure_comparison.md`](../2026-10-18_parts_structure_comparison.md)。*

*紀錄 — 2026-10-18：characterisation 依 2026-10-16 的 spot test 更新
（[`../../code/1016_spot_test_result.ipynb`](../../code/1016_spot_test_result.ipynb)）。
**這筆修改還沒同步到 registry.igem.org** — 線上的 part page 是依更早的版本轉錄的。*
