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
infect and on the two resistant isolates. This is the pattern an enzyme acting on a surface
polysaccharide would give, and it is what the ancestral-enzyme design predicts; it also means
the suppression cannot be explained by phage carried over in the preparation. The crude `e40`
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
  這正是「作用在表面多醣的酵素」會有的樣子，也是祖先酵素設計預測的結果；同時也排除了
  「製備液裡混到 phage」這個解釋。
- `e40`、`e281` crude lysate 看不出這種分組。

兩格不要過度解讀：9-6-2 的 Φ8 那格算到的 3 是滴緣反光，不是菌落；9-1-1 是唯一 Φ8 沒有壓住的
一株（11 顆），這跟它是非宿主一致。

每株 1 盤、單一濃度，菌落以影像自動分割計數。
