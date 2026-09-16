# 五分鐘報告投影片（英文版）

- `slides.pdf` — 正式投影片，16:9，**6 頁主線 + 1 頁分隔 + 7 頁備用**，全英文。
  敘事主線是**改造噬菌體零件的 DBTL loop**（pick gene → define target → learn from evolution →
  build → test），糖是 step 2 的答案，不是開場。第 3 頁的 loop 用實線／虛線標示
  「有資料 vs 提案中」，規則沿用 `../2026-07-30_graphical_abstract_design.md`。
- `slides_notes.pdf` — 講者稿列印版（縮圖 + 逐字稿 + 每頁秒數）。
- `slides.tex` — 唯一原始檔。**英文講稿就寫在每頁的 `\note{}`，那是正本**；中文的
  [`../2026-08-21_five_minute_talk_script.md`](../2026-08-21_five_minute_talk_script.md)
  只留結構、紅線與時間分配，不再是逐字稿。
- `bash build.sh` 重建兩份 PDF。只需要 XeLaTeX（TinyTeX 已有），不需要 quarto。
  本機沒裝 quarto，qmd 在這台 render 不出來，所以走 Beamer。
  字型 Helvetica Neue（Heiti TC 只留作 CJK fallback），已 subset 嵌入 PDF，換電腦不會掉字。

**講稿長度**：652 字 —— 125 wpm 約 313 秒、135 wpm 約 290 秒。
各頁 36 / 106 / 150 / 116 / 112 / 132 字。超時先砍第 3 頁的 step-two 那句。

**與原本 5 頁骨架的差異**：依要求把開頭 context 加厚（標題頁 + 背景頁），並把第 3 頁
從「Gap + RQ + 設計」改成 **design loop**，所以主線是 6 頁。
祖先重建畫成虛線、講稿明講「not results yet」。**注意兩件不同的東西**：PI 在建的是
**GH5（CDS_0012）全序列的樹 + ancestral state reconstruction**，祖先酵素要和 fiber *in trans* 挑戰
（caveat：affinity ~ binding ~ infection，出自 `../2026-07-29_pi_conversation/README.md`）；
CDS_0011 那份 15,775 條序列的比對只能做**保守度剖面**，不是祖先重建。

`fig/` 是為了投影片裁切／加工過的衍生圖，來源圖沒有改動，也沒有重跑繪圖腳本：

| 檔 | 來源 | 做了什麼 |
|:--|:--|:--|
| `oantigen_tracks.png` | `code/output/0727_o_antigen_comparison/o_antigen_loci_comparison.png` | 去標題、去圖例、去左側小字標籤 |
| `oantigen_tracks_labeled.png` | 上一列 | 用大字重畫五條軌道的菌株標籤，並畫出兩組 clone pair 括號（投影片直接用這張） |
| `binding_controls_af2.png` | `documents/2026-07-13_binding_controls_comparison.png` | 只留 ColabFold AF2 那一半，去標題 |
| `phage_map_banner.png` | `code/output/0729_prof_figures/fig_phage_genome_map.png` | 去頂端說明文字 |
| `hostrange_cells.png` | `code/output/0727_o_antigen_comparison/fig3_hostrange_prediction.png` | 去標題，讓三個格子放大 |

其餘圖直接引用 `code/output/` 底下的原檔。

**上台前**：第 2 頁的抗藥性數字仍是紅字 `[AMR figure + source — Alex]`，投影片上看得到，
填掉它再上台。
