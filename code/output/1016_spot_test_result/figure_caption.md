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
