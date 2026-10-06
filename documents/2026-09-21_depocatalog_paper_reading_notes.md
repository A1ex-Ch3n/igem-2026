# 2026-09-21 — DepoCatalog 論文導讀（重點：Depolymerase activity assay）

教授 2026-09-21 早上丟的論文。原話：「very similar to what we are trying to do, Im
annoyed we missed it… but we can still sell our project from the evolutionary side」，
並指定 **"Depolymerase activity assay" 就是下一個大實驗**（spot test）。

**書目**

| 欄位 | 值 |
|---|---|
| 標題 | DepoCatalog: mapping diversity of 129 recombinantly produced *Klebsiella* phage depolymerases |
| 作者 | Otwinowska A, Olejniczak S, Latka A, … Green S（Wrocław 大學為主，含 LSHTM、BfR） |
| 期刊 | *Nature Communications*，2026-05-22，Open Access |
| URL | https://www.nature.com/articles/s41467-026-73570-7 |
| 資料庫 | DepoCat — https://depocat.uwr.edu.pl |
| 原始圖檔 | Zenodo https://doi.org/10.5281/zenodo.19927711（**每個蛋白的 SDS-PAGE + halo 照片都在裡面**） |

---

## 1. 這篇在做什麼

129 個 *Klebsiella* phage depolymerase，其中 **90 個在這篇裡重組表現並實測**。
90 的組成要講清楚（教授一定會追這個數字）：129 = 自家收藏 72 + 文獻 57；
文獻的 57 個裡，18 個與自家蛋白無同源、被重做一次，另外 39 個是同源物、直接沿用已發表數據。
所以 **90 = 自家 72 + 重做的文獻 18**。
拿去 spot 在 171 株、涵蓋 146 種 KL-type 的 *Klebsiella* lawn 上，看 halo。
結果 map 出 75 種 KL-type 的專一性，其中 48 種是首次被指認、約 50 個酵素是首次被賦予活性。
再用 AlphaFold3 建 homotrimer 模型 + PyMOL 切 domain，提出 **5 大類 14 亞類**的結構分類，
最後做成公開資料庫 DepoCat。

酵素來源橫跨 podo-(46)、sipho-(10)、myo-(13)、jumbo myo-(40) 與 prophage(20)。

## 2. 為什麼教授說「很像我們在做的事」

重疊處：找 RBP/depolymerase → 重組表現 → 測對多糖的降解專一性 → 結構建模切 domain → 講演化。
連 pipeline 圖的五步都跟我們的路線幾乎同構。

**但他們沒做、我們有做的（＝可以賣的點）：**

1. **祖先序列重建（ASR）**。他們全部是現存序列的比較。我們的 `CDS12_ANC_Node1 /
   Node40 / Node281`（`documents/2026-09-10_twist_construct_order_second_set/`）是
   **時間軸上往回走**的變異體。論文 Discussion 自己挑明這是未解問題：
   > "major uncertainty is whether evolution enables rapid adaptation to other capsule
   > types by separate enzymatic or C-terminus domain exchange."

   他們只能從現生序列反推，我們可以直接把祖先做出來測。這正中缺口。
2. **宿主是環境 *Pseudomonas*，不是臨床 *Klebsiella***。他們 163 個 KL-locus 都是臨床分離株；
   我們是加州植物園土壤分離株，演化敘事（共演化、地理來源）本來就不一樣。
3. **受體是 LPS 糖，不是 capsule**（見 repo README / `2026-07-13_why_protein_protein_binding_fails.qmd`）。
   這同時是機會也是麻煩，見第 5 節。

他們最強的結論剛好是我們可以拿來當假說去驗的：
**central β-helix domain 高度保守、專一性的改變幾乎都落在 C-terminal domain**，
C-term 是「最快分化的 domain」。判準很具體：**C-term TM-score > 0.9 就是同一專一性；
0.8–0.9 之間不能排除部分重疊**。我們的 ASR 變異體正好可以測這條規則在時間軸上成不成立。

---

## 3. Depolymerase activity assay ── 教授要我們做的那段（逐字要點）

原文 Methods 標題就叫 "Depolymerase activity assay"。拆解如下。

### 3.1 菌苔

- 菌養到 **OD600 = 1.0**。
- **取 1 mL 菌液直接倒到 TSA 平板上**鋪開，**風乾**。
  注意：這不是 soft-agar overlay，是「倒菌液 → 乾掉」的乾菌苔。比 overlay 省事，
  但乾燥程度會直接影響 halo 清晰度，是最需要先練手的一步。
  ⚠️ **論文沒寫**：1 mL 倒下去之後多餘菌液要不要倒掉、風乾要多久、在哪裡乾。
  這是第一次做最可能失敗的一步，而原文確實沒交代，只能自己先試幾片定條件。

### 3.2 點樣

| 點的東西 | 體積 | 內容 |
|---|---|---|
| 樣品 | 10 µL | 重組酵素，在 PBS 中做 **two-fold serial dilution** |
| 陰性對照 | 10 µL | 純 PBS |
| 陽性對照 | 10 µL | 對應的 **phage filtrate，10⁷–10⁸ PFU/mL** |

PBS 配方（論文明列）：137 mM NaCl、2.7 mM KCl、10 mM Na₂HPO₄、1.8 mM KH₂PO₄、pH 7.4。

陽性對照用噬菌體本體，理由是：噬菌體自己帶著這顆 depolymerase，
牠打出來的 halo 就是「這株菌的多糖確實會被這顆酵素降解」的 ground truth。

### 3.3 培養與判讀

- **37 °C 隔夜 → 再室溫放 24 h**。第二段室溫放置不能省，halo 常常是這時候才顯影。
- 判讀：
  - 酵素點 → **halo zone（霧狀/半透明暈）**，菌沒被殺死，只是莢膜被剝掉。
  - 噬菌體點 → **clear plaque 外圍帶 halo**。
- **只判 presence / absence**。論文自己註明：
  > "our assays qualitatively assessed depolymerase activity (presence vs. absence),
  > rather than enabling strict quantitative comparisons."

  〔本筆記推論，非論文原文〕two-fold dilution 因此不是為了算活性單位，
  比較像是找出還看得到 halo 的最高稀釋倍數，順便避開高濃度蛋白本身造成的點樣假影。

### 3.4 重複數

- 自家酵素與噬菌體：**至少生物學三重複**。
- 文獻來源的 18 個酵素：全 panel 至少測兩次，陽性結果再補三重複。

### 3.5 ★ 對我們 0915 gel 僵局最關鍵的一句

> "clear halo formation was consistently observed even when purified proteins were
> present at very low levels and **not prominently visible on SDS–PAGE**, reflecting the
> high catalytic efficiency of these enzymes."

意思是：**spot assay 的靈敏度遠高於 Coomassie gel**。我們 0915 兩張 gel 判不出來
（沒誘導對照、半數 lane 沒上樣），不代表蛋白沒表現。
不必等 gel 漂亮才動手，可以邊純化邊開始點板。

---

## 4. 他們的表現／純化條件（可直接對照我們的 pET-28a 流程）

> ### ★ 誘導條件：**16–20 °C、16 h**。絕不是 37 °C。
>
> Methods 原文：*"Recombinant protein expression was induced at* **16–20 °C for 16 h**
> *by adding isopropyl-β-D-thiogalactopyranoside (IPTG) to a final concentration of
> 0.2–1 mM."* 誘導起點 OD₆₀₀ 0.5–1.0，培養量 500 mL LB。
>
> Supplementary Data 5 的逐蛋白分布（n = 90）把這個範圍拆得更細：
> **16 °C 佔 44、18 °C 佔 41、20 °C 佔 5**，搭配的 IPTG 是 0.5 mM 44、1 mM 41、0.2 mM 5。
> **90 個蛋白沒有任何一個在 37 °C 誘導。**
>
> 16 h 這個時間只出現在正文，Supplementary Data 5 沒有時間欄位，所以 16 h 是通用值、
> 不是逐蛋白的值。
>
> 我們六個 pET-28a 建構要抄的是 16 °C / 0.5 mM 那一組（pET30a、kanamycin、N-term His，
> 架構最接近）：**16 °C、0.5 mM IPTG、16 h、BL21 (DE3) STAR、OD₆₀₀ 0.5–1.0 誘導**。
>
> 理由：β-helix depolymerase 形成 trimer 很慢，37 °C 快速誘導容易全部進 inclusion body。
> 這是 0915 gel 看不到誘導帶時第一個該動的變數。


| 步驟 | 論文條件 | 我們現況 |
|---|---|---|
| 宿主 | *E. coli* BL21 Star (DE3) / BL21 (DE3) | 同 |
| 培養量 | 500 mL LB + 抗生素 | 待定 |
| 誘導點 | OD600 **0.5–1.0** | — |
| IPTG | **0.2–1 mM** | — |
| 誘導條件 | ★ **16–20 °C、16 h**（低溫過夜） | 0915 沒有明確誘導證據 |
| 破菌 | freeze/thaw ×3 + sonication | — |
| 澄清 | 16,000 ×g、30 min、4 °C，再過 0.22 µm | — |
| lysis buffer | 500 mM NaCl、20 mM NaH₂PO₄、pH 7.4 | — |
| 純化 | HisTrap HP 1 mL / IMAC，洗 **32 CV**，500 mM imidazole 沖提 | 下一步就是 Ni-NTA |
| 替代方案 | **Cobalt-NTA magnetic beads（Dynabeads His-Tag）** | 小量篩選可考慮 |
| 定量 | NanoPhotometer + ProtParam 莫耳消光係數 | — |
| 形式 | **全部用 full-length 蛋白**，不做截短 | 我們 CDS_0011 是 res 305–941 截短 ⚠️ |

兩個對我們的直接啟示：

- **低溫長時間誘導（16–20 °C, 16 h）**。β-helix trimer 折疊慢，37 °C 快速誘導容易進 inclusion body。
  這是 0915 沒有明顯誘導帶時第一個該改的變數（第二個是 codon bias，見第二批建構的 README 警告）。
- **Cobalt magnetic beads** 適合一次平行處理六個建構的小量純化，不必每個都上 FPLC。

---

## 5. 搬到我們系統上的四個障礙（要先想清楚，不然點了也看不到東西）

1. ***Klebsiella* 有厚莢膜，我們的 *Pseudomonas* 不一定有。**
   halo 之所以肉眼可見，是因為 CPS 又厚又黏，剝掉以後菌苔的折射率明顯改變。
   環境 *Pseudomonas* 的 LPS O-antigen 薄很多，**halo 可能根本看不出來**。
   對策（擇一或並用）：
   - 先用噬菌體原液在我們的宿主 lawn 上點，**確認 plaque 周圍到底有沒有 halo**。
     這是零成本的可行性測試，而且我們以前的 plaque 照片可能已經有答案了 → 值得先翻
     `photos/` 與 `lab_notebook/digitalized/`。**如果噬菌體本身就打不出 halo，
     純酵素幾乎不可能打得出來**，那就得換讀值方式。
   - 換成黏液型（mucoid、alginate 過量）的宿主，或加長室溫顯影時間。
   - 改用生化讀值：DNS reducing-sugar assay、TLC、多糖 PAGE/agarose。
     這些能給定量結果，反而補上論文自承的弱點（他們只有 qualitative）。
2. **我們的受體是 LPS 糖，酵素分類上可能不是 capsule depolymerase 而是 GH。**
   CDS_0012 是 GH5（glycoside hydrolase family 5），CDS_0011 才是 fiber/RBP。
   底物到底是 LPS O-antigen、Psl/Pel 類 EPS、還是纖維素類多糖，會決定要不要改用純化底物做反應。
3. **CDS_0011 是截短建構（res 305–941）。** 這點論文給的訊號是兩面的，要照實講：
   - Methods 明寫 **"All proteins were produced and tested as full-length versions."**
     ——他們沒有任何一個蛋白是截短表現的。
   - 但在結構比較那節，他們把 N-terminus 切掉才做 alignment，理由是
     N-terminus 是 virion-anchoring 部位、**對酵素活性沒有影響**（引 Latka et al.）。

   也就是說「切掉 N-term 不影響活性」是他們引用的既有結論，不是他們自己表現實驗的結果。
   截短仍然是點不出 halo 時的合理懷疑對象之一，但不是第一順位。
4. **沒有宿主 panel。** 論文的力氣有一半花在 171 株的 KL panel 上。
   我們手上是三株（9-6-2 / 9-2-1 / 10-10-2）。cross-reactivity 這條線我們暫時做不了，
   所以敘事重心必須放在 **ASR 時間軸**，不是宿主廣度。

---

## 6. 補充材料（已下載，重點已抽出）

檔案位置（Open Access，CC BY 4.0，可直接抓）：

| 內容 | 連結 |
|---|---|
| Supplementary Information（64 頁 PDF，含 Supp Fig 1–12） | `…/MediaObjects/41467_2026_73570_MOESM1_ESM.pdf` |
| Supplementary Data 5（逐蛋白表現條件，XLSX） | `…/MediaObjects/41467_2026_73570_MOESM7_ESM.xlsx` |

（前綴皆為 `https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41467-026-73570-7`）

**Supplementary Fig. 12 在 PDF 第 63 頁**，就是 halo 的判讀參考圖，圖說原文：

> "Representative images illustrating phage activity with halo formation, as well as
> recombinant enzyme halo visualization. Phage titration with single plaques with halo
> zones (A–C); Spot test - phage with halo zone and halo zone of recombinant
> depolymerase (D)."

**Supplementary Data 5** 是 90 個蛋白逐一列的表現條件（vector / His-tag 位置 / 引子 /
菌株 / 溫度 / IPTG / 抗生素）。全表統計如下：

| 欄位 | 分布（n = 90） |
|---|---|
| Vector | pET30a 44、pET101 27、pET-19b 14、pEXP5-CT/TOPO 4、pEXP5-NT/TOPO 1 |
| His-tag | N-term 60、C-term 30 |
| 菌株 | BL21 (DE3) STAR 81、BL21 (DE3) 9 |
| 誘導溫度 | **16 °C 44、18 °C 41、20 °C 5** |
| IPTG | **0.5 mM 44、1 mM 41、0.2 mM 5** |
| 抗生素 | ampicillin 46、kanamycin 44 |

溫度與 IPTG 是綁在一起的：**16 °C + 0.5 mM** 這 44 個就是 pET30a 那一組
（kanamycin、N-term His）——**架構跟我們的 pET-28a 最接近**。
所以我們第一次重做誘導的預設值就抄這組：**16 °C、0.5 mM IPTG、16 h、BL21 (DE3) STAR**。
沒有任何一個蛋白是在 37 °C 誘導的。

---

## 7. 下一步（UNDONE）

- [ ] **UNDONE** — 確認 9-2-1 Φ8 的 plaque 周圍有沒有 halo。這決定整個 spot assay
      走不走得通，成本為零，應該最先做。
      查過了：`photos/` 只有 `0529/` 與 `0605/` 兩批（早期，非 plaque assay），
      數位化筆記全文也搜不到 halo / 暈 / plaque morphology 的描述。
      所以要嘛翻 EOP 系列的原始掃描頁（p.71–p.72 附近），要嘛直接重點一次板來看。
- [ ] **UNDONE** — 依 Supplementary Data 5 的 pET30a 組條件重做誘導：
      **16 °C、0.5 mM IPTG、16 h**，並補上 **empty-vector 對照與 pre-induction 樣品**
      （0915 兩張 gel 缺的就是這兩個）。
- [ ] **UNDONE** — Ni-NTA 或 cobalt magnetic beads 小量純化六個建構。
- [ ] **UNDONE** — 建立 spot assay SOP：TSA 平板、OD600 1.0 菌苔、1 mL 倒板風乾、
      10 µL two-fold dilution、PBS 陰性對照、10⁷–10⁸ PFU/mL 噬菌體陽性對照、
      37 °C o/n → RT 24 h、三重複。
- [ ] **UNDONE** — 下載 Zenodo 19927711 的 source data（每個蛋白的 SDS-PAGE 與 halo 原圖），
      當判讀參考。第 6 節只取了 Supplementary Fig. 12 的圖說，Zenodo 本體尚未下載。
- [ ] **UNDONE** — 讀 Supplementary Data 1（171 株 KL panel）與 Data 3（逐酵素的
      cleaved bond / catalytic site）。若要跟 CDS_0012 的 GH5 活性位比對，Data 3 是入口。

---

*Log — 2026-09-21：建立。內容取自 nature.com 全文（正文 + Methods，2026-05-22 版，
Nat Commun 17, 6724）。另下載 Supplementary Information PDF 與 Supplementary Data 5，
統計結果見第 6 節；Supplementary Data 1–4、6 與 Zenodo source data 尚未取得，已標 UNDONE。
第 3 節的 assay 參數為論文逐字轉述，其中標註〔本筆記推論〕者除外；
第 2 節的「可賣點」與第 5 節的障礙分析為本筆記的推論，非論文內容。*

*Log — 2026-09-21：依 Alex 要求，把正文的誘導條件 **16–20 °C、16 h** 提為 §4 開頭的
標示區塊，並與 Supplementary Data 5 的逐蛋白溫度分布並列。同一段標示也加進
[`protocol/md/workflows/depolymerase_activity_assay.md`](../protocol/md/workflows/depolymerase_activity_assay.md)
的 Prerequisite callout。*
