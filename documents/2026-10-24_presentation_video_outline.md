# Presentation Video — 三幕大綱（v1，無真人出鏡）

需求與評分依據見 [`2026-10-24_presentation_video_plan.md`](2026-10-24_presentation_video_plan.md)。
那份是規格與條件總表，**這份只管內容**。表格裡的 `B2`、`C4`、`D4` 等代號指該文件 §3B 的條目。

- **形式**：Hamburg 2023 式純投影片加旁白，三幕結構加幕卡。v1 不拍真人。
- **目標**：成品檔 13:30–14:30。下面的時間軸合計 **14:00**。
- **旁白**：英文，約 1,650 字（130 wpm）。階段 1 由 Alex 一人錄完。

---

## 0. 先講這版的賭注

評審回饋（plan §3C）告訴我們，光「完整」只有 4 分，要 5 分以上得有**讓評審記得住的東西**。

這支片押在一件事上：**我們有一個罕見的、可以教別人的負面結果 —— 蛋白質結構預測在什麼情況下會失效。**

不是「我們的實驗失敗了」，而是「我們用對照組證明了一個被廣泛使用的方法，在一整類生物學問題上不適用，而且我們知道為什麼」。這同時命中：

- **B2**（technical data，modeled 結果明確算數）
- **C1**（DBTL：Cycle 1 推翻假設 → Cycle 2）
- **D4**（失敗要講成設計驅動，不是 troubleshooting）
- handbook p.83 對 Software 的提問：「Has the team documented **what didn't work, why, and what others should watch out for**?」

所以第二幕不是「我們走了冤枉路」，是全片的轉折與最強的一段。

---

## 1. 視覺規範（照 Hamburg）

| 項目 | 規則 |
|---|---|
| 底色 | 白底 |
| 標題列 | 色塊橫條，**三幕三色**（見下），幕內統一 |
| 每頁 | 右上角 iGEM logo，右下角頁碼 |
| 畫面文字 | 只有短標題加圖。**文字補充旁白，不重複旁白**（D6） |
| 數據圖 | 真實圖；目標條帶／關鍵點用**紅框**框出；對照組在圖上標明（C4） |
| 流程 | 圖示加箭頭的流程圖，不用純文字條列 |
| 學名 | *Pseudomonas*、*Gervaisevirus* 一律斜體（B5，§3C #14） |
| 出處 | 每張外部圖右下角小字標來源；PI 的工作標在標題列右側（B5） |
| 示意圖 | 角落標 `schematic`，和真實數據區隔（A7） |
| 配色 | 沿用 `code/0811_promo_video/src/theme.ts` 的莫蘭迪色 |

**三幕配色**（待 Alex 從 theme.ts 指定實際色碼）：

- Act I：暖灰綠 —— 設定、背景
- Act II：暗紅褐 —— 轉折、失敗、重新定向
- Act III：深藍 —— 解法、數據、結論

**視覺主線**：**β-helix tail spike 的渲染圖**，三幕各出現一次、意義不同 ——
第一幕當作「鑰匙」（我們以為的蛋白），第二幕它的**摺疊**揭穿真相，第三幕它是我們表達的酵素。
這是 Hamburg 用同一張 ferritin 圖貫穿全片的做法。

**幕卡**：全幅色底，置中大字 `ACT I — THE BOTTLENECK`，下一行一句話副標。停留 2.5 秒。

---

## 2. 三幕總表

| 段 | 時間 | 長度 | 核心句 |
|---|---|---|---|
| Cold open | 0:00–0:50 | 0:50 | 噬菌體能殺死細菌，但幾乎總是只殺得死一種 |
| **ACT I — The Bottleneck** | 0:50–4:20 | 3:30 | 宿主範圍是瓶頸；我們從校園挖出了材料；第一條線索在醣上 |
| **ACT II — The Wrong Key** | 4:20–8:00 | 3:40 | 我們用了標準方法，對照組推翻了它，而摺疊告訴我們真正的受體 |
| **ACT III — The Enzyme** | 8:00–12:20 | 4:20 | 把賭注放在 depolymerase 上：復活祖先序列、表達、測試 |
| Coda | 12:20–13:30 | 1:10 | 知道什麼、不知道什麼、下一步 |
| Credits | 13:30–14:00 | 0:30 | 字卡 |

幕名備選（Alex 挑）：
- Act II：`The Wrong Key` / `When the Model Breaks` / `Ten Folds That Killed Seven Thousand`
- Act III：`The Enzyme` / `The Real Key` / `Resurrecting the Ancestor`

---

## 3. 逐拍大綱

### Cold open — 0:00–0:50

| | |
|---|---|
| 畫面 | promo 的 plaque assay 動畫：菌苔鋪滿 → 噬菌體落下 → 溶菌圈長出來。接著同一支噬菌體滴在另外兩株菌上，**什麼都沒發生**。 |
| 旁白 | 噬菌體是會殺死細菌的病毒，而且精準。問題也在這裡：一支噬菌體通常只對一株細菌有效，換一株就失效。要把噬菌體當藥用，這是真正的瓶頸。 |
| 服務 | D1 故事、§3C #1 先講 why、§3C #2 hook 要切題 |
| 素材 | `code/0811_promo_video/`（plaque assay 場景） |

⚠️ **不要**用泛泛的抗藥性死亡人數開場。V1 評審 #4 就是因為開場例子和後面脫節被扣分。

---

### ACT I — The Bottleneck（0:50–4:20）

**幕卡 0:50–0:53** ｜ `ACT I — THE BOTTLENECK` ／ 副標：*Why one phage only kills one host*

#### I.1 問題（0:53–1:50）

| | |
|---|---|
| 畫面 | 示意圖：噬菌體要先**吸附**才能注入 DNA；吸附認的是細菌表面。有莢膜／O-antigen 的細菌，表面被一層多醣包住。 |
| 旁白 | 感染的第一步是吸附，而吸附認的是細菌表面長什麼樣。對有莢膜的細菌來說，表面不是蛋白質，是一層厚多醣。所以「這支噬菌體能感染誰」，很大程度上就是「它能不能處理那層糖」。 |
| 服務 | B1 目標、D2 big picture 先行、§3C #10 機制要講清楚 |
| 素材 | promo 的吸附 3D（`Membrane3D.tsx`） |

#### I.2 我們的材料（1:50–2:50）

| | |
|---|---|
| 畫面 | 校園採樣點地圖（**確認沒有國旗**，A6）→ 三株 *Pseudomonas_E* sp013179515 → Φ8 基因體圖，tail 模組標色 |
| 旁白 | 我們從校園附近的水和土裡分離出三株 ANI 上互相區分的 *Pseudomonas*，以及感染其中一株的噬菌體 Φ8。基因體約 62 kb，和已知噬菌體幾乎沒有共享的 ortholog —— 是新的。三株細菌的基因體已經發表在 Microbiology Resource Announcements。 |
| 服務 | B2 真實數據、C8 記錄完整、B5 標註 |
| 素材 | `code/0729_prof_figures/plot_bacterial_genomes.py`、`plot_phage_genome_map.py` |
| 畫面標註 | MRA doi `10.1128/mra.00793-26`；assembly accession；**基因體組裝與註解：Prof. J. Cesar Ignacio Espinoza**（B5） |

⚠️ 拓撲只講長度，**不要說 circular 也不要說 linear**（E1，兩方證據衝突）。分類講成暫定。

#### I.3 第一條線索（2:50–4:00）

| | |
|---|---|
| 畫面 | 三株菌的 O-antigen 基因座並排：同一個 `ihfB` 兩側的槽位，裝的是三套**互不同源**的 cassette。45 個 ortholog cluster 只有 4 個共享。旁邊標內部對照：兩組 clone pair 100.0% 一致。 |
| 旁白 | 比對三株菌的時候出現了一件事：同一個基因座位置上，三株各帶一套完全不同源的 O-antigen 合成基因。既然噬菌體認的是那層糖，這直接預測 Φ8 不會感染另外兩株。 |
| 服務 | B2、C4 對照、§3C #6 區分關聯與因果 |
| 素材 | `code/0727_o_antigen_comparison/` |
| 畫面標註 | **`prediction — not yet tested`**（E1，§3C #6） |

#### I.4 標準做法（4:00–4:20）

| | |
|---|---|
| 畫面 | 鎖與鑰匙示意：RBP（蛋白）對上外膜蛋白（蛋白）。**第一次出現 β-helix tail spike 渲染圖**，標成「the key?」 |
| 旁白 | 於是問題變成：Φ8 的哪一個 receptor-binding protein，認的是哪一個受體？這個領域的標準做法，是把兩個蛋白折在一起，用界面分數排序。我們就這麼做了。 |
| 服務 | C1 設計、鋪第二幕 |

---

### ACT II — The Wrong Key（4:20–8:00）

**幕卡 4:20–4:23** ｜ `ACT II — THE WRONG KEY` ／ 副標：*Ten control folds decided the fate of 7,182*

> 這一幕是全片的賣點。節奏要穩，不要急著認錯；先讓方法看起來合理，再讓對照組把它推翻。

#### II.1 篩選（4:23–5:10）

| | |
|---|---|
| 畫面 | 矩陣示意：114 RBP × 63 受體 = **7,182 對**；跑在 L40S GPU 上。旁邊是我們建的 1,673 條 RBP 資料庫來源（三篇文獻）。 |
| 旁白 | 我們建了一個 1,673 條噬菌體 RBP 的資料庫，把其中的 Pseudomonas 序列對上候選受體，一共 7,182 組配對，用 AlphaFold 類的模型把每一組折成複合物，再用 ipTM —— 界面信心分數 —— 排序。這正是 AlphaFold-Multimer 在蛋白交互作用篩選上的標準用法。 |
| 服務 | B2、C1、C2（軟體） |
| 素材 | `code/0619_literature_rbp_database/`、`code/0712_phage_rbp_detect/fold_binding/` |

#### II.2 對照組（5:10–6:20）

| | |
|---|---|
| 畫面 | 對照組設計圖：三個**已知會結合**的正對照（T5 pb5 × FhuA，PDB 8A8C；λ gpJ × LamB，PDB 8XCJ；*Pseudomonas* 的 DEV gp54 × LptD），加上**打亂**與**錯配**負對照。→ 切到 `2026-07-13_binding_controls_comparison.png`，紅框框住重疊區。 |
| 旁白 | 在相信任何排序之前，我們先問一個問題：這個方法分得出已知會結合和已知不會結合嗎？我們放了三組有共結晶結構的正對照，加上序列打亂和配錯受體的負對照。<br><br>結果：黃金標準 pb5 對 FhuA 得 0.137。**同一個受體，把序列打亂，得 0.136。**差 0.001。<br><br>我們換了工具重跑，這次用真的 MSA。這次更糟 —— 一組**配錯**的組合拿到 0.50，高過每一個真正的結合對。 |
| 服務 | **B2、C4 對照（§3C #3 兩年都被點名的弱點，這裡正面回答）** |
| 素材 | `documents/2026-07-13_binding_controls_comparison.png`、`code/output/0703_phage_host_matrix/fold/control_validation.png` |

> 關鍵數字（來源 `documents/2026-07-13_why_protein_protein_binding_fails.qmd`）：
> ESMFold 正對照平均 0.136、打亂 0.122、錯配 0.123，差距 +0.014 小於雜訊 sd 0.026。
> ColabFold AF2 正對照 0.130–0.310（平均 0.243），錯配最高 **0.500**。

#### II.3 為什麼（6:20–7:15）

| | |
|---|---|
| 畫面 | 兩層原因。**上層**：pTM 在打亂後從 0.55 崩到 0.17，但 ipTM 幾乎不動 —— 用兩條並排的柱子演。**下層**：paired MSA 示意 —— 噬菌體蛋白的同源都在噬菌體裡，細菌蛋白的同源都在細菌裡，**兩者永遠不會出現在同一個基因組**。 |
| 旁白 | 有趣的是，模型知道打亂過的序列不合理：整體折疊信心從 0.55 掉到 0.17。但界面分數幾乎不動 —— 代表它從來就沒有在讀一個真正的界面。<br><br>原因是這樣：AlphaFold 這類模型擺放界面，靠的是 paired MSA，也就是同一個生物體裡兩條鏈的同源序列，讓模型看出哪些殘基一起演化。但噬菌體和細菌是跨界配對，它們的同源序列永遠不會出現在同一個基因組裡。沒有共演化訊號，界面分數就是雜訊。<br><br>**這不是可以調參數救回來的 bug，是整類宿主—病原配對的通性。** |
| 服務 | **B2 modeled result、D4、C1** |

#### II.4 摺疊說了實話（7:15–8:00）

| | |
|---|---|
| 畫面 | 放棄 docking，改折 RBP 本身。**β-helix tail spike 渲染圖第二次出現**，這次標出右手 β-helix 的氫鍵週期。→ 一個分解多醣的動畫：酵素在糖鏈上切開一條路。 |
| 旁白 | 所以我們不再折複合物，改折 RBP 自己。結果 tail spike 是右手 β-helix —— 那是多醣分解酵素的招牌摺疊。<br><br>這一下，整件事翻轉了：如果 tail spike 是一個**酵素**，那麼受體根本不是蛋白質，是糖。我們從頭到尾在找的那把蛋白質鎖，不存在。<br><br>受體的身分不是 docking 給的，是**摺疊**給的。而且這回頭對上了第一幕那三套不同的 O-antigen。 |
| 服務 | C1 的轉折、D1 故事、B1 |
| 素材 | `code/0712_phage_rbp_detect/fold_structure/` |

⚠️ **待確認**：這段出現的 CDS 編號。`2026-07-13` 那份用的是我們自己的 `FHABPWTM_` 索引（CDS_0016、CDS_0002），但 0716 之後**正本是 PI 的 `UUAIURNK_` 索引**。上字幕前必須換算，不然畫面上的編號會和 wiki、Registry 對不起來。

---

### ACT III — The Enzyme（8:00–12:20）

**幕卡 8:00–8:03** ｜ `ACT III — THE ENZYME` ／ 副標：*If the ceiling is set by the enzyme, raise the enzyme*

#### III.1 新的假說（8:03–8:50）

| | |
|---|---|
| 畫面 | 一句話假說框（Hamburg 1:00 的做法）：<br>**In capsulated bacteria, the substrate range of the depolymerase — not the identity of the RBP — sets the ceiling on host range.**<br>下面一行：現存的窄專一性，是從更廣的祖先活性演化來的。 |
| 旁白 | 第二幕把問題換掉了。如果決定宿主範圍上限的不是 RBP 的身分，而是那個酵素能處理多少種糖，那該測的就不是結合，是**受質範圍**。而如果今天的窄專一性是從更廣的祖先活性演化來的，那麼最有意思的實驗，是把祖先找回來。 |
| 服務 | **B1（全片的目標句）**、C1 |
| 畫面標註 | **Hypothesis: Prof. J. Cesar Ignacio Espinoza**（B5，§3C 出處題是兩年最弱項） |

#### III.2 目標蛋白（8:50–9:30）

| | |
|---|---|
| 畫面 | Φ8 基因體圖放大到 tail 模組：CDS_0010（unknown protein）、CDS_0011（tail fibre）、CDS_0012（**GH5 depolymerase**）。附 AF3 pTM。 |
| 旁白 | Φ8 的 tail 模組裡，CDS_0012 是一個 GH5 家族的醣苷水解酶，這是我們的主角。CDS_0011 是 tail fibre。CDS_0010 目前仍然是**未知功能蛋白** —— 我們把它一起表達，就是為了弄清楚。 |
| 服務 | B2、E1 |
| 畫面標註 | AF3 模型來自 PI；CDS 編號用 `UUAIURNK_` 索引 |

#### III.3 復活祖先（9:30–10:30）

| | |
|---|---|
| 畫面 | 系統發生樹（promo 的由末端往回合併動畫）→ 標出被選中的節點 → 身分矩陣：Node1 對 WT **77.8%**，Node40 **52.6%**，Node281 **51.0%**，Node40 對 Node281 **87.3%**。→ ZymCTRL perplexity 隨節點越祖先而越低。 |
| 旁白 | PI 用 MUSCLE 對齊、PhyML 建樹，再用 IQ-TREE 做祖先序列重建，沿著從 CDS_0012 回到根部的路徑把每個節點的序列算出來，並用蛋白質語言模型 ZymCTRL 打分。越祖先的節點，perplexity 越低。我們挑了三個節點合成出來。 |
| 服務 | B2（modeled）、C2、**B5 署名** |
| 畫面標註 | **Phylogeny, ASR and ZymCTRL scoring: Prof. J. Cesar Ignacio Espinoza**（整段標題列掛著） |

⚠️ **不要**把三個節點叫成 deep / mid / shallow（E1）。只講身分百分比。

#### III.4 建構與結構檢查（10:30–11:10）

| | |
|---|---|
| 畫面 | 六個 pET-28a 建構一覽（Twist 合成，全部 N 端 His6）→ ESMFold 折出來的三個祖先疊在 WT 上：aligned RMSD **0.28 / 0.50 / 0.52 Å**。→ 跨方法檢查：我們的 ESMFold WT 對 PI 的 AF3 模型，**0.28 Å / 2,139 atoms**。 |
| 旁白 | 六個建構由 Twist 合成，全部帶 N 端 His6。在進濕實驗之前我們先問：這些祖先序列還折得出同一個酵素嗎？三個都疊回同一個 TIM barrel，aligned RMSD 在 0.5 Å 以內。我們也用兩種不同方法折同一條野生型序列互相檢查，差 0.28 Å。 |
| 服務 | B2、C4（跨方法當作對照） |
| 素材 | `code/1018_construct_structures/` |

⚠️ 引用 **aligned RMSD**，不是 CSV 裡那個 residue-index-paired 的 3.8–4.6 Å。

#### III.5 濕實驗：照實講（11:10–12:00）

| | |
|---|---|
| 畫面 | 膠圖，目標位置紅框。**畫面上直接寫出對照狀態**：<br>`IPTG −/+ : present` ｜ `BL21 empty-vector lane: ABSENT` ｜ `n = 1` |
| 旁白 | 表達這一段，我們沒有得到乾淨的結果，我說清楚是哪一種不乾淨。<br><br>九月底的膠上，CDS_0012 在加了 IPTG 的條件出現 40 到 43 kDa 的帶。但我們**到現在仍然沒有跑過 BL21 空載體的對照**，所以沒有東西能把這條帶和宿主背景分開。<br><br>十月的 Ni-NTA 純化失敗：沖提道是空的，流穿和上樣一樣 —— 蛋白沒有結上管柱。<br><br>這兩件事都還沒解決，而缺的那個對照是最便宜的一步。 |
| 服務 | **C4、B2、D4、§3C #3 和 #12 兩年都被點名** |
| 素材 | 膠圖 notebook（`*_gel_annotation.ipynb`） |

> 這段的語氣照 EPFL 的句型：**假說 → 做了什麼 → 結果 → 結論**，不要寫成失敗清單（D4）。

#### III.6 抗性突變與安全（12:00–12:20）

| | |
|---|---|
| 畫面 | 9-6-2 r1 的定序：Stealth CR3 **F126L**，read pileup 證實；O-antigen 基因座**未變動**。→ 安全：IBC 條件式核准、**0 VFDB / 0 CARD**。 |
| 旁白 | 另一條線我們做出了乾淨的結果：對 Φ8 產生抗性的突變株，定序後找到莢膜型別基因上的一個點突變，在 reads 層級確認。而 O-antigen 基因座沒有變動。<br><br>安全方面，Φ8 的基因體沒有任何毒力因子或抗藥基因的命中，我們的工作也取得了 IBC 的核准。 |
| 服務 | **C7（§3C #9 兩年都被點名「沒講安全」）**、B2 |
| 素材 | `code/1010_*`、resistant mutant WGS |

⚠️ spot test 的 R1 表型 **inconclusive**（連親代都沒有清除），這裡不要宣稱抗性表型已驗證（E1）。

---

### Coda — What we know and what we don't（12:20–13:30）

| | |
|---|---|
| 畫面 | 三欄：**Established** ／ **Predicted, not tested** ／ **Open**。每欄下面接一行下一步。 |
| 旁白 | 把話說清楚。<br><br>**已經確立的**：三株菌的基因體和一個新噬菌體的基因體，都已公開；三套互不同源的 O-antigen cassette；tail spike 是 β-helix depolymerase；跨界界面 docking 在對照組下不帶訊號；一個經 read 確認的抗性突變。<br><br>**預測但未驗證的**：Φ8 不會感染另外兩株；祖先酵素的受質範圍比較廣。<br><br>**還沒解決的**：乾淨的表達與純化、酵素活性測定、基因體拓撲。<br><br>最便宜的下一步是那個空載體對照，最關鍵的一步是 O-antigen 剔除的吸附實驗 —— 那才是真正的證明。 |
| 服務 | **D4、§3C #5、C3、B1 回扣第三幕的假說** |

#### HP 要插在哪裡（待填）

§3C #7 的評審說 HP 不要關在一個區塊。這版把 HP 拆成三處，**內容待從 wiki Human Practices 頁填入**，每處固定句型 **誰 → 說了什麼 → 我們改了哪一個決定**，各約 15 秒：

- `[HP-1]` 插在 I.1 之後 —— 為什麼宿主範圍是真問題（臨床或產業端的意見）
- `[HP-2]` 插在 II.4 之後 —— 誰的意見支持了轉向 depolymerase
- `[HP-3]` 插在 III.6 —— 安全與責任（IBC 條件、生物安全考量）

⚠️ 我不知道團隊實際做了哪些 HP 活動，**這三段必須由 Alex 從 wiki 填**，不能編。填完後總長會增加約 45 秒，Coda 相應壓縮。

---

### Credits — 13:30–14:00

照 Hamburg 14:00 那張：團隊成員、PI、advisors、Twist 與其他贊助、**Artlist 音樂的曲名/作者/授權**、工具（Claude、ESMFold、ColabFold、IQ-TREE、ZymCTRL…）。**停留 ≥ 2 秒**（A5）。

---

## 4. 這版怎麼回答評分

| 題 | 在哪裡回答 |
|---|---|
| B1 目標／設計／結果 | 一句話假說框（III.1）；Coda 三欄回扣 |
| B2 技術數據 | 對照組圖（II.2）、身分矩陣與 RMSD（III.3/III.4）、膠圖（III.5）、突變 reads（III.6） |
| B3 視覺設計 | β-helix 渲染圖貫穿三幕；三幕三色；紅框 |
| B4 engaging | 三幕戲劇結構；第二幕的轉折 |
| B5 出處 | **兩年最弱項** → PI 署名出現三次（I.2、III.1、III.3）、每張外部圖標來源、學名斜體、字卡 |
| C1 DBTL | Cycle 1（II）被對照組推翻 → Cycle 2（III） |
| C3 會不會成功 | Coda 三欄 |
| C4 數據支持 claim | 畫面直接寫出對照狀態，包含缺的 |
| C6 HP 影響設計 | `[HP-1~3]` 分散插入 |
| C7 責任與安全 | III.6 |
| C9 學生主導 | 三處 PI 署名反襯其餘為學生工作；字卡列分工 |

**刻意留給 Judging Session 的**（§3C：兩年都稱讚現場答問）：GH5 的機制細節、資料庫建置方法、metagenome pipeline、ZymCTRL 的參數。片中點到為止。

---

## 5. 開工前要確認的事

1. **CDS 編號換算**（II.4）—— `FHABPWTM_` 的 CDS_0016 / CDS_0002 對應到 `UUAIURNK_` 的哪兩個？不換算會和 wiki 對不起來。
2. **因果順序**（II.4 → III.1）—— PI 的 depolymerase 假說，是在 0713 的摺疊結果**之後**形成的，還是他本來就有？目前稿子寫成「摺疊結果指出受體是糖，這把 depolymerase 推到中心」，沒有宣稱是我們的失敗導致他提出假說。**請和 PI 確認這個順序再定稿。**
3. **`[HP-1~3]` 的實際內容** —— 從 wiki Human Practices 頁取，我不編。
4. **三幕的實際色碼** —— 從 `theme.ts` 指定。
5. **Act II / III 幕名**二選一。
6. **採樣點地圖**要確認畫面中沒有任何國旗（A6）。

---

## Log

- 2026-10-24 — 初稿。三幕結構，以「蛋白質結構預測何時失效」的對照組負面結果為第二幕轉折；時間軸合計 14:00；視覺規範照 Hamburg 2023；HP 留三個待填位；列出六項開工前待確認事項
