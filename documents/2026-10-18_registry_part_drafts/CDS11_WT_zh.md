# CDS11_WT — tail spike 的 β-helix depolymerase body（part page 草稿・中文版）

英文正本：[`CDS11_WT.md`](CDS11_WT.md)。**送件貼英文版。**

| 欄位 | 內容 |
|---|---|
| Part type / role | CDS（`SO:0000316`），**basic part** |
| Title | `Phi8-TSP-body` — tail-spike β-helix depolymerase body（CDS_0011 res 305–941） |
| Sequence | 1917 bp = `ATG` + CDS + stop → 638 aa。取自 `registry_parts.ffn` |
| Source | Bacteriophage 9-2-1 Φ8，本團隊自土壤分離的新穎 ~62 kb podovirus；CDS_0011 採用教授 `UUAIURNK_` Pharokka 註解的編號。Construct = 全長 941 aa 蛋白的 res 305–941 |
| Designed for | *Escherichia coli*（表現宿主）；source organism = phage 9-2-1 Φ8 |
| 序列中**不**包含 | pET-28a 的 `MGSSHHHHHHSSGLVPRGSHM` leader，以及我們設計的 `GGSGGGGS`-His6-`ENLYFQ`-`GGGGSGGGGS` 純化 linker — 兩者都在下方說明 |

**Functional description（設計意圖）：** 噬菌體 tail spike 的三聚體 β-helix body，單獨表現，
作為針對宿主 LPS O-antigen 的候選 polysaccharide depolymerase。

---

## design

CDS_0011 是噬菌體 9-2-1 Φ8 的 **tail spike** — virion 的結構蛋白，也是接觸宿主表面的那個蛋白。
全長 941 aa 的摺疊分三段：

| 殘基 | 模組 | 信心度 |
|---|---|---|
| 1–110 | Calx-β β-sandwich — virion 附著用的 anchor | 四個 AF3 template（3US9、3EAD、2FWU、2KLT）全部對應到這裡 |
| 111–300 | shaft | **AF3 擺不定**：五個模型之間相距 41–52 Å |
| 301–941 | 右手 **β-helix / β-solenoid body** + 受體結合區 | 剛性，pLDDT 88–94，模型間疊合 0.44–0.99 Å |
| 921–941 | foldon — 承擔三聚體接觸，必須留在 construct 裡 | — |

**Construct 是 res 305–941**：保留穩固的 body 與 foldon，切掉擺不定的 shaft 與 anchor。這個邊界
來自疊合教授的五個 AF3 模型 — body 會自行三聚化、自成一體，而 ~301 之前的一切都是鬆散的附屬。

**它是哪一種酵素，以及這個宣稱有多強。** 右手 β-helix 是噬菌體 **depolymerase** 的經典摺疊 —
這種酵素會「切開」宿主表面多醣，而不只是結合。我們稱 CDS_0011 為 depolymerase **僅憑摺疊證據**：
AF3 對 res 111–941 **沒有任何** template，β-helix 是從主鏈氫鍵的序列 offset 週期判定出來的
（方法已包裝成我們的 [`phagecheck`](https://gitlab.igem.org) 工具），不是來自具名的同源蛋白。

> **這和 CDS_0012 是不同的宣稱，證據強度也不同。** CDS_0012 是 template 確認的 GH5 glycoside
> hydrolase，而且是**另一個獨立的蛋白**，不是這個 tail spike 的 domain。任何地方都不要寫成
> 「tail spike 含有 GH5」——我們沒有這個證據。CDS_0011 = 附著於 virion、body 是 β-helix
> depolymerase 的 spike；CDS_0012 = 獨立的 GH5 酵素。

**與 CDS_0010 的關係。** 兩條 fiber 共用同一個 N 端 Calx-β virion 附著模組：序列 42% identity／
107 aa，兩個 anchor 疊合 **RMSD 0.50 Å／446 atoms**。它們是建立在同一個附著零件上的旁系 fiber。

**Tag 與 linker。** 我們建構的質體加上 pET-28a 的 N 端 His6 leader，再加一段設計的
`GGSGGGGS`-His6-`ENLYFQ`（TEV）linker，供 Ni-NTA 純化與切除 tag 使用。Insert 以自己的 stop codon
結束，所以載體的 C 端 His6 永遠不會被轉譯 — **儘管檔名叫 CTERM_HIS6TAG，這個蛋白沒有 C 端 tag。**
leader 與 linker 都不是生物序列的一部分，所以都不放進送件的 part。

**模型：** AlphaFold3 Server 三聚體，pTM 0.66 / ipTM 0.64，cloned 區域內 mean pLDDT 90.3。
ipTM 偏低不代表界面不好 — 是被 N 端鬆散附屬拖低的，鏈間 PAE 最小值約 2 Å。AF3 摺疊是
**Espinoza 教授**的工作（見下方 *attribution*）。

## experiment

以 NdeI/XhoI 選殖進 **pET-28a(+)**，Twist Bioscience 合成，2026-07-27 訂單。表現宿主
*E. coli* BL21(DE3)，kanamycin 篩選，16–20 °C IPTG 誘導。

**狀態：這個 part 尚未證實能表現。** 三次 SDS-PAGE（2026-09-15、09-29、10-10）在預期的 72.0 kDa
都沒有看到 band；09-29 這個 construct 沒有跑未稀釋的 lane，所以「沒有 band」目前還不能解讀。
未轉形 BL21(DE3) 的對照 lane 仍然欠缺，因此這些膠上的任何 band 都無法歸屬。

## characterisation

**沒有。** 未確認表現（見 *experiment*）、沒有純化蛋白，因此沒有活性試驗。

這個 part 需要的讀值是**在宿主菌苔上做 spot assay**：純化蛋白產生 halo 而 buffer 對照沒有，
就是 depolymerase 活性的直接證據。對照組事先定好：imidazole vehicle、PBS、phage-positive，
以及同批的敏感親代菌株。2026-10-16 做了第一次 spot test，但只涵蓋三個祖先 GH5 變體 —
**這個 part 不在裡面**。

在那個試驗完成之前，本 part 的 depolymerase 身分是**結構上的假說，不是量到的活性**。

## application

定位為針對土壤 *Pseudomonas* 的噬菌體衍生抗菌工具組中的**標靶與表面剝除模組**。游離的
depolymerase 不需要具感染力的 virion 就能剝除多醣屏障 — 這正是我們把 body 從噬菌體獨立出來
表現的原因。

專案脈絡：三個 ANI 相異的宿主菌株，在同一個 `ihfB` 側翼的位置上攜帶**三組非同源的 O-antigen
cassette**，45 個 ortholog cluster 中只共用 4 個。由於受體就是那個醣，宿主範圍預期會跟著 cassette
走 — **尚未驗證，這裡寫成預測而不是結果。**

## discussion

**限制。**
- depolymerase 的歸屬是**摺疊層級**，沒有具名同源蛋白、res 111–941 沒有 template。在有活性
  試驗之前，應視為假說。
- res 305 的切點刻意移除了 virion anchor：這個 part 無法組裝進 virion，也不是為此設計。
- 72 kDa 的三聚體 β-solenoid 是很難表現的目標；若不可溶，下一步是復性或更低的誘導溫度。

**對其他團隊的價值。** 可重用的是**決定 construct 邊界的方法**：疊合多個預測模型，保留跨模型
剛性的部分，在模型彼此不一致的地方切。在這裡，它把一個曖昧的 941 aa 蛋白變成自成一體的
637 aa 三聚體。

## attribution

- **Espinoza 教授** — CDS_0010/0011/0012 的 AlphaFold3 摺疊，以及本編號所依據的 Pharokka 註解
  （`UUAIURNK_`）；提出 construct 邊界的需求。
- **學生團隊** — 噬菌體分離、定序與組裝；決定 res 305–941 的 domain mapping 分析；選殖、表現
  試驗與膠分析。
- 用 Registry 的 **Contribution Roles** 逐位作者記錄。所有具名作者（包含教授）必須先在
  registry.igem.org 上 opt in。

---
*草稿 — 2026-10-18。數字：`code/output/1018_construct_structures/`。證據等級：
[`../2026-10-18_parts_structure_comparison.md`](../2026-10-18_parts_structure_comparison.md)。*
