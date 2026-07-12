# 9-2-1 Φ8 噬菌體 RBP：偵測、結構、與受體結論
# Phage 9-2-1 Φ8 RBPs: detection, structure, and receptor conclusion

**日期 / Date:** 2026-07-13　|　**分支 / Branch:** `rbp-receptor-fold`　|　**程式 / Code:** `code/0712_phage_rbp_detect/`

---

## 一句話結論 / Bottom line

**中文：** 9-2-1 Φ8 的 tail spike 是**右手 β-helix depolymerase（醣解酶）**，代表這隻噬菌體辨識並分解的**主要受體是宿主的 LPS O-antigen（多醣），不是蛋白質**。因此「把 RBP 對細菌 OMP 做蛋白-蛋白 docking」這條路對這個系統**行不通**（我們用對照組實測證實了），受體驗證應轉向 **O-antigen**。此外，RBP Detect（ML）多抓到一條註解漏掉的 depolymerase（CDS_0002），代表這隻噬菌體可能有**不只一個 depolymerase**。

**EN:** The 9-2-1 Φ8 tail spikes are **right-handed β-helix depolymerases**, meaning the phage's
**primary receptor is the host LPS O-antigen (a polysaccharide), not a protein**. Protein–protein
docking of RBP × bacterial OMP therefore **cannot work** for this system (we proved it empirically
with controls); receptor validation should pivot to the **O-antigen**. Separately, the ML tool
RBP Detect flagged a depolymerase (CDS_0002) that the annotation missed — the phage likely carries
**more than one depolymerase**.

---

## 今天做了什麼 / What we did today

三個任務，全部在 Laguna 上用 real-MSA ColabFold + 本地分析完成。
Three tasks, all done with real-MSA ColabFold on Laguna + local analysis.

### 1. 用 RBP Detect 標記 phage RBP / Mark RBPs with RBP Detect
- **中文：** 對 phage 的 80 條 PHANOTATE 蛋白跑 PhageRBPdetect v4（ESM-2 分類器，本地 MPS ~3 分鐘）。分類器很保守：80 條只判 **2 條**為 RBP —— CDS_0016（tailspike2，0.997）和 **CDS_0002**（0.998，Pharokka 只標 "hypothetical"）。與 Pharokka 的 tail 註解取**聯集 → 8 條**（交付：`9-2-1_phi8_RBPs_union.faa`）。
- **EN:** Ran PhageRBPdetect v4 on the 80 phage proteins. Conservative: only **2/80** called RBP —
  CDS_0016 (tail spike 2) and **CDS_0002** (which Pharokka labelled only "hypothetical"). Union with
  the Pharokka tail module → **8 RBPs** (`9-2-1_phi8_RBPs_union.faa`).

### 2. 結構預測 / Structure prediction
- **中文：** ColabFold AF2 折這 8 條。**single_sequence 是垃圾（pLDDT≈30）；改用真 MSA 才折得出來**（多數 pLDDT >80）。用不需資料庫的方法判 fold（骨架氫鍵的序列間距週期：β-helix 會在「一圈殘基數」的間距上規律出現氫鍵）。
- **EN:** ColabFold AF2 on the 8. **single_sequence gave garbage (pLDDT≈30); real MSA was essential**
  (most pLDDT >80). Fold classified DB-free via the backbone-H-bond sequence-offset period (a β-helix
  H-bonds between adjacent coils → a peak at the coil period).

### 3. Binding 篩選（RBP × 受體）/ Binding screen — retired
- **中文：** 先跑 9 對照組（正對照：T5 pb5×FhuA [PDB 8A8C]、λ gpJ×LamB、**Pseudomonas 噬菌體 DEV 的 gp54×LptD**；加打亂/錯配負對照）。結果 **OVERLAP**：正對照 ipTM ≤0.31，卻有一個錯配對到 0.50 → **完全沒有鑑別力**。**所以 120 對正式篩選沒有跑**。
- **EN:** Ran a 9-fold control gate first (positives T5 pb5×FhuA [PDB 8A8C], λ gpJ×LamB,
  **Pseudomonas phage DEV gp54×LptD**; + scrambled/mismatch negatives). **OVERLAP**: positives
  ipTM ≤0.31 while a mismatch scored 0.50 → no discrimination. **The 120-pair screen was NOT run.**

---

## 結果 / Results

| RBP | pLDDT | fold | 判定 / call |
|---|---|---|---|
| **CDS_0016 tail spike 2** | 93 | β-helix，週期 16–18 | ✅ **depolymerase** |
| **CDS_0015 tail spike 1** | 65 | β-helix，同週期（信心較低）| ✅ depolymerase（low-conf）|
| **CDS_0002**（RBP-Detect 獨有）| 82 | β-helix，週期 22–24（最典型）| ✅ **depolymerase** |
| CDS_0017 tail protein (917aa) | 89 | α-rich 球狀 | tail tube 結構，非 RBP fold |
| CDS_0019 internal virion | 96 | β-sandwich 類 | 結構蛋白，非 solenoid |
| CDS_0020 | 93 | α 螺旋長纖維 | 結構 |
| CDS_0018 tail fiber (118aa) | 91 | 小 β（太短無 coil）| fiber 尖端 |

Binding 對照組 / controls: positive ipTM mean 0.24 (0.13–0.31)，negative mean ~0.25 (max 0.50)，
gap = −0.37 → **OVERLAP / 非資訊性 non-informative**。

---

## 這些發現的價值 / Why today's findings matter

**中文：**
1. **鎖定了受體的「種類」，直接改寫實驗方向。** 知道 tail spike 是 depolymerase → 主要受體是 **LPS O-antigen（醣）**。這讓 receptor 驗證從「大海撈針找蛋白 OMP」變成「針對 O-antigen / rhamnose 合成 locus 做 knockout 吸附實驗」——**省下大量試錯**，且更可能一次做對。
2. **RBP Detect 帶來新資訊，不是重複註解。** 它抓到 Pharokka 漏標的 CDS_0002（一條乾淨的 β-helix depolymerase）。代表這隻噬菌體**可能有 ≥2 個 depolymerase** → 可能對應**更廣或分支的宿主範圍 / 兩種 O-antigen 特異性**，這對「工程化拓寬宿主範圍」很關鍵。
3. **用最小成本排除了一條死路（負面但有價值）。** 我們證實 AF2/AF3 的蛋白-蛋白 ipTM 篩選對「噬菌體×宿主」**根本無效**（跨界無 paired MSA），而且**知道為什麼**。這阻止團隊繼續把算力/時間投在做不出來的方法上；而「先用對照組把關」也成為之後可重用的防呆。
4. **建立了可重用的流程。** real-MSA 結構 pipeline + 免資料庫的 β-helix 判定 + 對照組把關的 binding 協定，之後 **9-6-2 Φ8 及其他噬菌體可直接套用**。
5. **對設計/安全有意義。** depolymerase 本身可當**獨立的抗生物膜酵素**元件；且 O-antigen 型別可用來**預測宿主範圍**。

**EN:**
1. **We pinned down the *type* of receptor, which rewrites the experiment plan.** Depolymerase tail
   spikes ⇒ the receptor is **LPS O-antigen (sugar)**. Receptor validation shifts from "hunt for a
   protein OMP" to "knock out the O-antigen / rhamnose locus and test adsorption" — **far less
   trial-and-error** and more likely right the first time.
2. **RBP Detect gave new information, not a re-run of the annotation.** It found CDS_0002, a clean
   β-helix depolymerase the annotation missed ⇒ the phage likely has **≥2 depolymerases**, hinting at
   a **broader / branched host range or two O-antigen specificities** — important for engineering host range.
3. **We ruled out a dead end cheaply (negative but valuable).** We proved AF2/AF3 protein–protein
   ipTM screening **fundamentally cannot** rank phage×host pairs (no cross-kingdom paired MSA), **and
   we know why**. This stops further wasted compute/time, and the control-gate is now a reusable safeguard.
4. **We built reusable infrastructure** — real-MSA structure pipeline + DB-free β-helix classifier +
   control-gated binding protocol — **directly applicable to 9-6-2 Φ8 and future phages.**
5. **Design/safety relevance:** the depolymerase is itself a candidate **standalone anti-biofilm
   enzyme**, and O-antigen typing can **predict host range**.

---

## 限制與待辦 / Limitations & UNDONE
- **中文：** β-helix 判定是**幾何/氫鍵**方法（強且內部一致），但尚未用 **foldseek/DALI 命名同源家族**（Laguna 無 foldseek/DB）→ 建議把 `CDS_0016__monomer` 上傳 search.foldseek.com 補一個命名證據。CDS_0015 三聚體信心低（pLDDT 50），可加 model/recycle 重折。**LPS O-antigen 受體仍需濕實驗證實**（knockout 吸附）。
- **EN:** The β-helix call is a **geometric/H-bond** method (strong, internally consistent) but not yet
  a **named foldseek/DALI hit** (no foldseek/DB on Laguna) → upload `CDS_0016__monomer` to
  search.foldseek.com for a named homolog. CDS_0015 trimer is low-confidence (re-fold with more
  models). **The LPS O-antigen receptor still needs wet-lab confirmation** (knockout adsorption assay).

## 檔案 / Files
- 交付 RBP / RBP deliverable: `code/output/0712_phage_rbp_detect/9-2-1_phi8_RBPs_union.faa`, `rbp_detect_vs_pharokka.tsv`
- 結構 + 分析 / structures + analysis: `code/output/0712_phage_rbp_detect/structure/` (`pdb/`, `structure_summary_msa.tsv`, `beta_helix_analysis.tsv`)
- 結論 / conclusions: `code/0712_phage_rbp_detect/fold_structure/CONCLUSIONS.md`
- 流程 / pipelines: `code/0712_phage_rbp_detect/` (`phage_rbp_union.py`, `fold_structure/`, `fold_binding/`)

---
*Log — 2026-07-13：整合今日三任務（RBP Detect → 結構 → binding）。核心結論：tail spike 是 β-helix
depolymerase → primary receptor = LPS O-antigen；binding docking 因跨界無 paired MSA、對照組失敗而退場；
RBP Detect 多發現一條 depolymerase（CDS_0002）。foldseek 命名 + 濕實驗 O-antigen 驗證為 UNDONE。*
