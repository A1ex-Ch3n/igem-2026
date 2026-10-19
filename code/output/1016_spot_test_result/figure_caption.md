# Figure — first spot test of the expressed CDS_0012-family proteins

Files: `fig_spot_test.png` (300 dpi), `fig_spot_test.pdf`. Made by `code/1016_spot_test_result.ipynb`, section 6.

**Figure X. Proof-of-concept spot test of three expressed CDS_0012-family proteins on seven *Pseudomonas* lawns.**
Each strain was grown as a double-layer lawn (200 µL culture in 3 mL soft agar). Each plate received five 7 µL drops:
phage Φ8 stock (positive control), sterile 1× PBS (negative control), purified e1, and crude lysates of e40 and e281.
All protein samples were diluted 1:10 in sterile PBS. Drops were spotted on 12 Oct 2026 and photographed on 16 Oct.
R1 = Φ8-resistant isolate picked from the parent strain.
**(A)** Each drop, cropped from the plate photograph without colour correction. Rows are strains; columns are treatments.
**(B)** Colonies counted inside each drop by automated image segmentation (touching colonies count as one, so these
are lower bounds). One point per strain; bars show medians.
The lawns grew well, but no obvious clear zone is visible in the photographs. The clearest trend is in colony growth
inside the drop. Sterile PBS drops consistently developed discrete colonies (median 14 per drop), so this is the
baseline for a liquid drop landing on these lawns. Both the Φ8 drops (median 0) and the purified e1 drops (median 1)
almost completely suppressed this growth on six of the seven strains. The e1 drops were 90 % PBS, so the difference
from the PBS control comes from the e1 preparation itself, and its effect was comparable to that of the phage.
The crude e40 and e281 lysates reduced colony numbers only slightly (medians 10 and 9). In these lysates the target
protein is not enriched, so this result does not show that e40 and e281 lack activity. Together, these results give
a first indication that the purified e1 fraction contains a biologically active product.

## 中文說明（wiki 用）

**第一次 spot test（proof of concept）。** 7 株 *Pseudomonas* lawn，每盤點 5 滴（各 7 µL）：
- Φ8（陽性對照）
- 滅菌 PBS（陰性對照）
- 純化 e1
- e40、e281 crude lysate

蛋白樣品都用滅菌 PBS 1:10 稀釋。

**結果**
- lawn 長得不錯，但照片上看不到明顯的透明區。
- 看得到的趨勢是**滴裡長出來的菌落數**：滅菌 PBS 滴穩定長出菌落（中位數 14），這是一滴液體落在 lawn 上的基準。
- Φ8 滴（中位數 0）和**純化 e1 滴（中位數 1）在 7 株中的 6 株上幾乎完全抑制了這些菌落**。e1 滴有 90% 是 PBS，所以差別來自 e1 本身，效果接近 phage。
- e40、e281 crude lysate 只稍微減少菌落（中位數 10、9）。它們沒有純化，目標蛋白濃度低，不代表沒有活性。

**初步結論**：純化的 e1 帶有生物活性。

## Remaining caveats (for the methods / discussion)

- The 10 % e1 fraction also contains its purification buffer (e.g. imidazole). A buffer-only drop (elution buffer
  1:10) has not been tested yet.
- Protein amounts were not equalised between samples.
- A spot test shows activity of a preparation; it does not by itself prove expression of the intended construct.
  For that, show it alongside the gel / anti-His western.
- Φ8 gave no visible clearing on its parental hosts either, so this plate does not address R1 resistance.
- On 9-1-1, colonies grew in the Φ8 and e1 drops as well (sector map confirmed).

---

# Second figure — grouped by Φ8 host range

Files: `fig_spot_test_hostrange.png` (300 dpi), `fig_spot_test_hostrange.pdf`.
Made by `code/1016_spot_test_result.ipynb`, section 7.

**Figure Y. The same spot test, arranged by whether Φ8 can infect the strain.**
Each cell is one 7 µL drop; the number is the colony count inside it and the shading follows
that number. Rows are grouped by the host range of phage Φ8, scored independently in a
plaque assay of 18 strains against two Φ8 lysates
(`lab_notebook/digitalized/2026-07-04_host-range-results-matrix.md`): 9-2-1 and 9-6-2 are the
strains Φ8 was isolated on, and 8-10-2, 9-1-1 and 10-10-2 gave no plaques with either lysate.
✱ marks the two Φ8-resistant isolates picked from the sensitive parents.
Sterile PBS gave a high colony count in every row, host and non-host alike (group medians 12.5
and 15), so the baseline does not depend on host range. **The `e1` preparation suppressed
colony growth in every row** (group medians 1 and 4), including on strains that phage Φ8 cannot
infect and on the two resistant isolates.
**Host range does not separate this data set, and this figure should not be read as if it did.**
Φ8 itself suppressed colonies on two of the three non-hosts (8-10-2 and 10-10-2), so suppression
in this assay does not require infection — and therefore the fact that `e1` works on non-hosts
does **not** rule out phage carried over in the preparation. The crude `e40`
and `e281` lysates show no such grouping (medians 9.5–10 and 7–10, against a PBS baseline of
12.5–15).
Two cells should not be over-read: the 3 counted in the 9-6-2 Φ8 drop are reflections at the
drop edge, not colonies, and 9-1-1 is the one strain where the Φ8 drop did not suppress growth
(11 colonies), consistent with it being a non-host.
n = 1 plate per strain, one concentration, colonies counted by automated image segmentation.

## 中文說明

**同一批 spot test，改用 Φ8 宿主範圍分組。** 一格 = 一滴，數字 = 滴內菌落數，顏色深淺跟著數字。

分組依據是獨立做過的 plaque assay（18 株 × 2 個 Φ8 lysate，
`lab_notebook/digitalized/2026-07-04_host-range-results-matrix.md`）：
- **Φ8 宿主**：9-2-1、9-6-2（Φ8 就是從這兩株分離的）＋它們的抗性衍生株（✱）
- **非宿主**：8-10-2、9-1-1、10-10-2，對兩個 lysate 都沒有 plaque

重點：
- 滅菌 PBS 在兩組都給出高菌落數（組中位數 12.5 與 15），所以基準線跟宿主範圍無關。
- **`e1` 在每一列都壓住了菌落**（組中位數 1 與 4），包括 Φ8 感染不了的非宿主，以及兩株抗性株。
- **但宿主範圍切不開這批資料，不要照這個方向解讀。** Φ8 自己在三株非宿主中的兩株
  （8-10-2、10-10-2）也壓住了菌落，所以這個 assay 裡的抑制**不需要感染**；因此
  「e1 在非宿主也有效 ⇒ 排除 phage carryover」這個推論**不成立**。
- `e40`、`e281` crude lysate 看不出這種分組。

兩格不要過度解讀：9-6-2 的 Φ8 那格算到的 3 是滴緣反光，不是菌落；9-1-1 是唯一 Φ8 沒有壓住的
一株（11 顆），這跟它是非宿主一致。

每株 1 盤、單一濃度，菌落以影像自動分割計數。

---

# Third figure — each drop against its own plate's PBS control

Files: `fig_spot_test_normalised.png` (300 dpi), `fig_spot_test_normalised.pdf`,
numbers in `spot_percent_of_pbs.tsv`. Made by `code/1016_spot_test_result.ipynb`, section 8.

**Figure Z. Colony suppression in the spot test, normalised to the sterile-PBS control on the
same plate.** Every plate carried its own 7 µL sterile-PBS drop, and the colony count in that
drop varied between plates (7–17). Each point here is one strain, expressed as the colonies in
that treatment's drop as a percentage of the PBS drop on the same plate; 100 % is no effect.
Filled points are the four strains phage Φ8 can infect, two of which are Φ8-resistant isolates;
open points are the three strains that gave no plaques with either Φ8 lysate
(`lab_notebook/digitalized/2026-07-04_host-range-results-matrix.md`).
Phage Φ8 (median 0 %) and the `e1` preparation (median 12 %) both suppressed colony growth
almost completely, while the crude `e40` and `e281` lysates stayed near the no-effect line
(medians 67 % and 53 %). **`e1` tracks the phage strain by strain**: on six of the seven strains
both fall below 40 %, and the single strain where the phage failed — 9-1-1, at 157 % — is also
the one strain where `e1` failed, at 114 %.
That agreement is the strongest signal in this experiment, and it is also the strongest
remaining confound: an activity carried over from the phage stock would behave the same way.
Suppression here does not require infection — Φ8 also cleared colonies on two of the three
strains it cannot plaque — so the host-range split, shown for completeness, does not separate
the data.
n = 1 plate per strain, one concentration, colonies counted by automated image segmentation;
9-1-1 is a single plate and is labelled rather than treated as an established exception.

## 中文說明

**把每一滴換算成「佔同一盤 PBS 對照的百分比」。** 每盤都點了自己的滅菌 PBS 對照，而各盤的
PBS 菌落數本來就不同（7–17），所以絕對數字不能跨株比較。100% = 跟 PBS 一樣、沒有效果。
實心點 = Φ8 能感染的 4 株（其中 2 株是抗性株），空心點 = 兩個 Φ8 lysate 都不產生 plaque 的 3 株。

- Φ8（中位數 0%）和 `e1`（中位數 12%）都幾乎完全壓住菌落；`e40`、`e281` crude lysate 貼近
  無效果線（67%、53%）。
- **`e1` 是逐株跟著 Φ8 走的**：7 株中有 6 株兩者都低於 40%；唯一 Φ8 失效的 9-1-1（157%），
  也正是 `e1` 唯一失效的一株（114%）。
- 這個一致性是本實驗最強的訊號，但同時也是最強的干擾：如果活性是從 phage 原液帶過來的，
  表現會完全一樣。
- 這個 assay 裡的抑制**不需要感染** — Φ8 在三株不能形成 plaque 的菌株中，有兩株也清掉了菌落。
  所以宿主範圍分組切不開這批資料，圖上保留只是為了完整。

每株 1 盤、單一濃度，菌落以影像自動分割計數；9-1-1 只有一盤，所以標出來而不當成已確立的例外。

## 這三張圖怎麼配

1. `fig_spot_test.png` — 原始照片 + 絕對菌落數。**證明資料是真的**，讀者看得到每一滴。
2. `fig_spot_test_hostrange.png` — 逐株、逐處理的數字表。**查表用**，附錄或 supplementary。
3. `fig_spot_test_normalised.png` — 用每盤自己的對照正規化。**結論圖**，放正文。

如果只能放一張，放第 3 張，再把第 1 張的照片縮成一條放在旁邊當佐證。
