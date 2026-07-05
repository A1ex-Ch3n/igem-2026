# RBP × receptor folding 篩選 — 完整推論總結（0703 task）

> 這份文件把「用結構折疊預測 phage RBP × 我們 Pseudomonas receptor 結合」這條線**從動機到結論的完整推理**記下來,並附**每個交付檔案怎麼看**。結論:**folding 這一層確認無效(嚴謹的 negative result);主線 receptor-repertoire overlap 不受影響。**

---

## 0. 一句話結論

我們把 7,182 對 phage RBP × Pseudomonas receptor 全折了、也用黃金正對照驗了,**證明 MSA-free ESMFold 的 pseudo-ipTM 分不出真結合 vs 隨機** —— 分數其實在量「蛋白多大、多好折」,不是「這對有沒有結合」。因此**這張矩陣不當結合證據用**,但它是一個乾淨、可寫進報告的 negative result。

---

## 1. 檔案導覽（每個檔案是什麼、怎麼看）

### 結果與圖 — `code/output/0703_phage_host_matrix/fold/`
| 檔案 | 是什麼 | 怎麼看 |
|---|---|---|
| **`binding_matrix.csv`** | 完整 7,182 對的分數表 | 欄位:`rbp_id, rec_id, iptm, ptm, interchain_pae_min, interchain_pae_mean, plddt_mean, len, status`。`iptm`=界面分數(0–1,本來想當結合排序),`ptm`=整體折疊品質,`interchain_pae_min`=跨鏈最低 PAE(越低=界面越有把握),`status`=`OK`/`SKIP_TOOLONG`。**6,358 OK + 824 SKIP**。 |
| **`rbp_receptor_iptm_heatmap.png`** | 主熱圖(左)+ 大小假訊號散點(右) | 左:列=RBP、欄=receptor,**都按長度排序**;顏色=ipTM。幾乎一片均勻藍綠 → 沒有專一結構。左上角紅框=「最小 RBP × 最小 receptor」最亮(假訊號)。右:散點證明 **ipTM 跟複合物長度 +0.58 相關** → 分數在量大小。 |
| **`control_validation.png`** | 對照組決定性圖(**給教授看這張**) | 左:3 對正對照(綠)vs 打亂 receptor(紅,同長度)vs 錯配(粉),灰帶=背景。綠≈紅≈背景 → 分不開。右:打亂時 **pTM(藍)大跌**但 **ipTM(橘)不動** → 界面分數沒在讀真界面。 |
| **`control_scores.csv`** | 9 折對照組原始分數 | 3 正對照 + 3 打亂 + 3 錯配。對照 `control_key.tsv` 看每列屬於哪類。 |
| `control_pairs.tsv` / `control_key.tsv` | 對照組的輸入序列 / 分類標籤 | `_key` 標 positive/scrambled/mismatch + 合併長度。 |
| `probes.fasta` / `receptors_panel.fasta` | 篩選的輸入:114 RBP families / 63 receptors | RBP id `RBP0001..0114`、receptor id `REC001..063`。 |
| `truncated_rbps.txt` | 被 C 端截斷的 6 個大 RBP | RBP0004/0026/0081/0096/0100/0110(>1000 aa),截成 C 端 700 aa 才折得下。 |

### 程式碼 — `code/0703_phage_host_matrix/fold/esmfold/`
| 檔案 | 作用 |
|---|---|
| `esmfold_run.py` | 核心:每對 `RBP + 25×G linker + receptor` 折成複合物、算 pseudo-ipTM、可續跑、標 OOM/太長 |
| `make_esm_pairs.py` | 生 7,182 對輸入(含大 RBP 的 C 端截斷) |
| `split_esm.py` / `collect_esm.py` | 切塊送 Slurm array / 收集成 binding_matrix.csv |
| `esmfold.sbatch` | Laguna array job(`--num-recycles 1`) |
| `setup_esmfold.sh` / `run_smoke_esm.sh` / `GUIDE.md` | 安裝 / smoke / 完整操作指南 |

### 文件 — `documents/`
| 檔案 | 內容 |
|---|---|
| `2026-07-04_folding_tool_odyssey.md` | 工具三跳六坑(ColabFold→Boltz→ESMFold)的完整史 |
| `2026-07-04_folding_tool_recommendation.md` | 21-agent 研究報告:為什麼留 ESMFold + §6 早就預警這個失敗模式 |
| `2026-07-05_esmfold_matrix_note_for_PI_EN.md` | **給 Cesar 的英文說明**(含對照組結果表) |
| `2026-07-05_phage_host_matrix_reasoning_summary.md` | 本文件 |

---

## 2. 完整推論鏈（我們是怎麼一步步得到結論的）

### 第 0 步 — 為什麼要 folding
教授要我們找「phage 打的是哪個 receptor」。定序回來的 phage 還沒有,所以無法直接知道 RBP。折衷:把**已知會感染 Pseudomonas 的 phage 的 RBP** × **我們基因體上的 surface receptor** 折成複合物,用結合分數當**線索**(教授接受「線索級」:不確定綁哪個,但知道某菌有沒有某 receptor)。→ 需要一個能跑 7,182 對的結合預測。

### 第 1 步 — 工具選型的坎坷（詳見 odyssey）
- ColabFold/AF2-multimer:遠端 MSA 伺服器擋死;單序列模式精度崩(pLDDT≈28)、~3.5 min/折。✗
- Boltz-2:cuequivariance kernel 要 cuBLAS 12.5+,但 Laguna 驅動是 12.4 → 裝不起來;`--no_kernels` 能跑但 403s/折(慢 13×)。✗
- **ESMFold(HF transformers)**:純 PyTorch、無 MSA、無特製 kernel → 唯一在這台 GPU 上穩跑的。✓
  做法:`RBP + 25×G linker + receptor` 折成一條,從跨鏈 PAE 算一個 interface-pTM 代理分數。

### 第 2 步 — 第一眼就不對勁
主跑出來的分布:**median 0.127、sd 0.026、max 0.32**(真結合的 ipTM 通常 0.5–0.9)。而 top hits 被**少數蛋白霸佔**(RBP0069 一個佔 top20 的一半;REC052 反覆出現)。→ 像「單一蛋白很黏」而非「這一對專一」。

### 第 3 步 — 正規化診斷(把懷疑量化)
- **加成模型**(RBP效應 + receptor效應)就解釋了 **63.3% 的變異** → 大部分差異是「哪個蛋白」的基線,不是「這一對」。
- **ipTM 跟長度強相關**:corr(iptm, 複合物長度)=**+0.58**、corr(iptm, receptor長度)=+0.47。
- **Top hits 是「小×小」**:REC052(248 aa 短 receptor)配 RBP0025/0015/0071/0016(118–143 aa 迷你 RBP)→ 兩個小 domain 好折、PAE 低(~5)→ 假高分。扣掉長度 + per-protein bias 後,榜首還是最小的那群 → 訊號被大小徹底汙染。

### 第 4 步 — 決定性對照組(裁判)
找 3 對**文獻已知會結合**的 phage RBP–receptor(2 對有實驗共結構),各跑:真 receptor、**打亂 receptor(同長度同組成)**、錯配 receptor。走同一支 pipeline。

| 正對照 | 真 | 打亂 | 錯配 | Δ(真−打亂) |
|---|---|---|---|---|
| T5 pb5 × FhuA(PDB 8A8C) | 0.137 | **0.136** | 0.129 | **+0.001** |
| λ gpJ × LamB(PDB 8XCJ) | 0.112 | 0.102 | 0.129 | +0.010 |
| DEV gp54 × LptD(Pseudomonas) | 0.159 | 0.129 | 0.112 | +0.030 |

- 有**共結構的黃金正對照,跟自己打亂版差 0.001** —— 完全分不開。
- 平均真−打亂差 +0.014 **< 背景噪音 sd 0.026** → 差異在噪音之內。
- 正對照全落在 7,182 背景分布裡(背景 median 0.127、p95 0.157)。
- **機制鐵證**:打亂時 **pTM 大跌**(0.55→0.17、0.49→0.24、0.65→0.24)—— 模型知道打亂的不是真蛋白;**但 ipTM 不動** → 界面分數對「對面是不是真 receptor」無感 → 它根本沒在量界面。

### 第 5 步 — 結論
MSA-free、跨界(phage 蛋白 × 細菌蛋白)、又只折 monomer(RBP 其實是同源三聚體)→ 沒有共演化訊號定位界面,模型只能給「通用堆疊信心」,而那由**大小和可折性**主導 —— 正是我們觀察到的。**這個 folding 篩選對 RBP–receptor 結合不具鑑別力,不當證據用。**

---

## 3. 為什麼這是有價值的結果

> **這是嚴謹、可寫進 iGEM 報告的 negative result(附黃金正對照 + 機制解釋),比一張沒驗證的漂亮熱圖有價值得多。而主線 receptor-repertoire overlap(教授接受的線索級證據)不依賴這步,依然成立。**

具體來說:
- 我們沒有拿一張未驗證的熱圖去唬人;而是**主動用有共結構的正對照去驗自己的方法,誠實報告它失敗**。這在 iGEM 評審眼中是加分的科學態度(有 controls、有機制解釋、知道方法的極限)。
- 「pTM 會動、ipTM 不動」是一個**乾淨的機制論點**,說明**為什麼**失敗(不是模型壞,是這個任務缺共演化訊號),而不只是「分數看起來很平」。
- 它劃清了方法的適用邊界:**MSA-free 單序列折疊不能做 novel 跨界 PPI 的結合排序** —— 這對整個領域都是有用的提醒(也記進了記憶,未來不重蹈)。

---

## 4. 主線不受影響

phage–host 配對的**主證據**是 **receptor-repertoire overlap**(我們的菌有沒有某類 receptor,對照 PharBP 上打該菌的 phage)—— 教授明確接受這是「線索級」證據,而且**完全不依賴 folding 這一步**。所以 folding 失敗**不影響**我們原本的結論鏈。定論級的 receptor ID 仍然是**遺傳學**(phage-resistant mutant → 重定序),那是濕實驗的事。

---

## 5. 之後可做（非必要）

1. 把 branch `rbp-receptor-fold` 併回 `main`(程式碼 + 結果 + 文件都保留當紀錄)。
2. 若真要救結合預測:等**自己的 phage 定序回來**拿到真 RBP,或改用**遺傳學**定 receptor;結構上唯一可能有意義的是對 shortlist 用**真三聚體 + 複合物原生模型**細折,但無 MSA 大概率仍缺專一性(見 recommendation §9)。

---
*Log — 2026-07-05:0703 task 收尾。完整檔案清單見 §1;完整推理見 §2;結論=嚴謹 negative result,主線 receptor-overlap 不受影響。相關:[[project_phage_receptor_binding_screen]] 記憶已標註此 OUTCOME。*
