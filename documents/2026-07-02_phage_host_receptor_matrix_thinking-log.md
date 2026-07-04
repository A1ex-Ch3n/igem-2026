# Phage–host receptor interaction matrix — thinking log

**Started:** 2026-07-02 (PI task) · **Status:** planning + foundation built · **Code:** `code/0703_phage_host_matrix/`

A retrospective record of how we're approaching the PI's "interaction matrix" task — the
reasoning, the dead-ends we ruled out, the data facts we established, and the decisions
made. Purpose: so we (or future related tasks) can reload the thought process quickly.
Builds directly on the PharBP-query task ([`2026-07-01_pharbp_query_report.md`](2026-07-01_pharbp_query_report.md)).

## 1. The PI's initial task (Cesar Espinoza, WhatsApp, 2026-07-02)

Proposed a 4-step workflow:
1. Download all the predicted receptors for known Pseudomonas phages (~6000)
2. Identify all unique hosts (~60)
3. Predict/identify the shared receptors with our genomes (BLAST is fine now)
4. Make a giant interaction table

Follow-up when we flagged the receptor-vs-RBP problem (below), the PI clarified:
> "yes I know, but this would give us good clues … we won't know to which receptor for
> sure, but we know if a particular bacteria has a receptor."

So the PI **accepts a clue-level (presence/homology) analysis** — he is NOT asking for
exact RBP↔receptor binding.

## 2. The core reasoning chain (why the task is shaped this way)

Goal: **which phages could infect our 3 sequenced isolates?** Can't be answered directly
(our isolates are novel, no known phage, absent from every database), so we step back:

```
Q0 which phages infect our strains?           ✗ novel isolates, no known phage
Q1 which phages' RBPs bind receptors WE have?  ✗ no DB stores RBP↔receptor; needs folding
Q2 which phages' HOSTS share receptors with us? ✓ computable by BLAST  ← the PI's clue level
```

Q2 logic: phage P infects host H → P binds *some* receptor on H → if H and we share a
receptor R (high identity) → P may also bind our R → **P is a candidate**. The matrix
systematises this. Cells are **presence + % identity** ("does this phage's host carry a
receptor homologous to ours"), NOT a binding score — because binding needs simulation and
the PI is fine with the weaker clue.

## 3. The key facts we established (from the PharBP-query task + probing)

- **PharBP stores RBP → phage → host *name*. It has NO bacterial-receptor field**, and no
  RBP↔receptor pairing. → the matrix cells cannot be "downloaded"; the receptor side must
  be built ourselves from host genomes (NCBI + annotation).
- **The real Pseudomonas scope in PharBP:** by phage name, ~1,480 phages / **8,227 RBP
  records** / ~57 (messy) host strings (1,911 records have no host). *This* matches the PI's
  "~6000 / ~60" — not the 198/21 we first pulled with the narrow `host_genus=Pseudomonas`
  filter. Dominated by *P. aeruginosa* and *P. syringae*.
- **Receptor-sharing already computed in 0623** (`out_receptor_ncbi/carrier_organisms.tsv`,
  390 organisms): the hosts most similar to us at high identity (hunanensis, alloputida,
  fortuita, capeferrum…) mostly have **0 phages**; the one host that is *both* highly
  similar (99.4% id, 98 shared receptors) *and* phage-rich (**139 phages**) is **P. putida**.
  Secondary: plecoglossicida (95.9%, 7), taiwanensis (95.8%, 4). Meanwhile PharBP's dominant
  aeruginosa/syringae share with us only at 78–87% id (far). → **P. putida is the standout
  surrogate host; its phages are the top candidates.**

## 4. Where the PI's workflow was inefficient, and our corrections

1. **Wrong columns.** "6000 host receptors" is unnecessary — the receptors that matter are
   the ones WE have. Columns collapse to our own ~106–144 receptor groups; no 60-host
   genome download needed just to define columns.
2. **Lookup assumption.** "Make an interaction table" implies the interactions are
   downloadable. They aren't (no RBP↔receptor data). Cells are presence/homology now; a
   fold/ipTM layer is optional, later, only for top candidates.
3. **Redundancy.** Our 3 site isolates (9-6-2/9-2-1/10-10-2) are ~one strain; 8-10-2 is a
   distinct species (capeferrum). Reference is really ~2 receptor sets, not 3–5.

## 5. Decisions made (with the user)

- **Redo the host-receptor overlap fresh, from PharBP** (not just reuse 0623) — for clean
  data provenance and easier debugging. 0623 becomes a cross-check.
- **Self-annotate receptors at scale** (many host genomes) via code kept in the repo,
  runnable **locally or on Laguna**.
- **Keep all 5 sequenced isolates as reference columns** despite redundancy — makes it
  easier to spot clues later (core vs strain-specific receptors).
- **First concrete artifact:** a receptor × strain presence table for our isolates + a
  Markdown repertoire summary (done — see §6).

## 6. Current status

**Done:**
- `code/0703_phage_host_matrix/build_receptor_by_strain.py` — clusters our 441 receptors
  (mmseqs, 90% id / 80% cov) across all 5 isolates.
- `code/output/0703_phage_host_matrix/receptor_by_strain.tsv` — 144 receptor groups ×
  5 strains presence matrix.
- `code/output/0703_phage_host_matrix/receptor_by_strain.md` — repertoire summary
  (43 core groups shared by all 5; 46 capeferrum-specific; per-class counts).

**Done (Step 1):** `step1_pharbp_hosts.py` → `pharbp_pseudomonas_hosts.tsv` — cleaned PharBP's
Pseudomonas hosts and resolved **54 hosts → 43 distinct NCBI genomes** (26 strain-exact,
27 species-reference, 1 unresolved) via the `datasets` CLI, strain-preferred. High-value near
relatives: KT2440 (227 RBP/71 phages), fluorescens, putida, protegens Pf-5, plecoglossicida, S12, taiwanensis.

*Reliability check (user-prompted):* first cut filtered by **phage name** (`phage=Pseudomonas`),
which slightly undercounts. Re-did it by **host field** (`host=Pseudomonas` → **6,376 records**,
reproducing the DB's own count, + `host=Stutzerimonas`). Result: same **~54 hosts / 43 genomes**
— the small "missed" host strings were junk (`Pseudomonas sp.`) or multi-host entries whose
Pseudomonas part (KT2440) was already captured. Lesson: filter PharBP by HOST, not phage name;
its host field is coarse (6k+ RBP records collapse to ~54 host names, dominated by lab strains).

**Done (Step 2):** `step2_host_receptors.py` — downloaded the 43 host proteomes (datasets CLI),
mined **3,850 receptors** (reusing 0623 `classify()`), and mmseqs'd our **144 receptor reps**
vs each → **host × our-receptor overlap matrix** (144 × 43). Cross-validates 0623:
**P. putida max 99.4% id** (57–68 receptors shared ≥90%; KT2440 = 71 phages), plecoglossicida/
taiwanensis secondary, **P. aeruginosa far (81.7%, 0 shared ≥90%)** despite ~108 receptors.
Outputs: `host_overlap_matrix.tsv`, `host_overlap_summary.{tsv,md}`, `host_receptor_overlap.tsv`,
`host_receptor_counts.tsv`. (Big proteomes stay in job tmp, not git.)

**Next (planned):**
3. Join PharBP RBP sequences for the top hosts (P. putida group: KT2440 etc.) → the RBP ×
   receptor layer; the giant matrix's phage side.
4. Optional fold/ipTM on the shortlist for a direct binding signal.

## Related files
- PharBP-query report: `documents/2026-07-01_pharbp_query_report.md`
- Our receptors (canonical): `code/0623_metagenome_rbp/out_receptor_fasta/receptors_all.tsv`
- 0623 surrogate-host overlap: `code/0623_metagenome_rbp/out_receptor_ncbi/carrier_organisms.tsv`

---

# 中文版(含對話來回)

一份「我們怎麼想這個任務」的回溯紀錄:PI 的原始任務、推論如何一步步演進、確立的關鍵事實、
做過的決策。目的是之後(或相關 task)能快速回神。接續前一天的 PharBP 查詢任務
([`2026-07-01_pharbp_query_report.md`](2026-07-01_pharbp_query_report.md))。

## 1. PI 的初始任務(Cesar Espinoza,WhatsApp,2026-07-02)

四步 workflow:
1. 下載所有已知 Pseudomonas phage 的 predicted receptors(~6000)
2. 整理出所有 unique host(~60)
3. 用 BLAST 找出跟我們基因體共享的 receptor
4. 做一張大 interaction table

當我們指出「receptor vs RBP」的問題後,PI 澄清:
> 「yes I know, but this would give us good clues … we won't know to which receptor for
> sure, but we know if a particular bacteria has a receptor.」

→ PI **接受 clue 等級(存在/同源)的分析**,不是要精確的 RBP↔receptor 結合。

## 2. 對話演進(來回時間線)

1. **PI 開任務**:上面四步。
2. **Claude 研究 PharBP + API**(承前一天成果):發現 PharBP 是**噬菌體 RBP 庫**、**沒有
   receptor 欄位**、pairs 只到 phage–host、且多為電腦預測。
3. **Claude 第一版提案**(過度設計):RBP × receptor 矩陣、用 fold/ipTM 填每一格。
4. **User 澄清矩陣的軸**:列 = RBP(每 phage 多列),欄 = host receptor(每 host 多欄),
   聚焦「跟我們基因體高相似」的 receptor。
5. **Claude 指出核心卡點**:這張矩陣**無法從資料庫填**——沒有任何 DB 記錄 RBP↔receptor,
   每格都得用結構預測(fold)。「做一張 interaction table」隱含「交互作用可下載」的錯誤假設。
6. **User 把此點傳給 PI;PI 回覆**:「我知道,但這能給好線索;不會確定是哪個 receptor,
   但我們知道某菌有沒有某 receptor。」→ **確認走 clue 等級,不做 simulation。**
7. **Claude 重新框定**成「presence 線索矩陣」(格 = 該 phage 的宿主有沒有跟我們共享的
   receptor),並指出這其實就是 **0623 的 surrogate-host 分析攤成矩陣**。
8. **User 問**:60 個 Pseudomonas phage 是 PharBP 全部嗎?**Claude 查證**:不是。真正是
   **~1,480 phage / 8,227 RBP / ~57 個 host 字串**(對應 PI 的 ~6000/~60);先前的 60/21 是
   `host_genus=Pseudomonas` 窄篩的結果。
9. **User 提出**:先把宿主的 receptor 對照表做出來當核心資料。**Claude 發現** 0623 的
   `carrier_organisms.tsv` 已做了一大半(390 菌 × 共享 receptor 數 + phage 數),並指出
   **P. putida 是唯一「又跟我們高相似(99.4%)、又有 phage(139)」的標竿**;aeruginosa/
   syringae 雖多但只 78–87% 相似(遠);跟我們高相似的近緣多半 0 phage。
10. **User 細化決策**:(a) 註解 pipeline 放 repo、可本機/Laguna;(b) 為資料源乾淨,
    **從 PharBP 重做**,不吃 0623;(c) 先做 **receptor × strain 存在表 + md**;(d) 建這份
    thinking log(中英文)。
11. **Claude 執行**:重新跨 5 株 cluster 出 receptor × strain 表(144 group)+ md + 本文件。

## 3. 核心推論鏈(為什麼任務長這樣)

目標:**哪些 phage 能感染我們的分離株?** 無法直接答(我們的菌是新的、無已知 phage、不在任何
資料庫),所以一路退:

```
Q0 哪些 phage 感染我們?            ✗ 新菌、無已知 phage
Q1 哪些 phage 的 RBP 綁我們有的 receptor? ✗ 沒有 DB 記錄 RBP↔receptor;要 fold
Q2 哪些 phage 的「宿主」跟我們共享 receptor? ✓ BLAST 就能算 ← PI 接受的 clue 等級
```

Q2 邏輯:phage P 感染宿主 H → P 綁 H 上某個 receptor → 若 H 與我們共享 receptor R(高相似)
→ P 可能也綁我們的 R → **P 是候選**。矩陣格子 = **存在 + % identity**,不是結合分數。

## 4. 確立的關鍵事實

- **PharBP 記錄 RBP → phage → host 名稱,沒有 receptor 欄位**,也沒有 RBP↔receptor 配對。
  → 矩陣的 receptor 側要自己從宿主基因體(NCBI + 註解)建。
- **PharBP 真正的 Pseudomonas 規模**:依 phage 名 ~1,480 phage / **8,227 RBP** / ~57 host
  (1,911 筆沒 host)。大宗是 *P. aeruginosa* 和 *P. syringae*。
- **0623 已算過 receptor 共享**:又像我們、又有 phage 的標竿是 **P. putida**(99.4%、98 共享、
  139 phage);plecoglossicida(95.9%,7)、taiwanensis(95.8%,4)次之。

## 5. 做過的決策
- **從 PharBP 重做** host-receptor overlap(不只吃 0623),求資料源可追溯、好 debug。
- **自己大規模註解 receptor**,程式碼放 repo,可本機或 Laguna 跑。
- **5 株全留當 reference 欄位**(雖冗餘),方便日後找線索。
- **第一個產物**:receptor × strain 存在表 + repertoire 摘要(已完成,見 §6)。

## 6. 目前進度
**已完成**:`code/0703_phage_host_matrix/build_receptor_by_strain.py` →
`receptor_by_strain.tsv`(144 receptor group × 5 株存在矩陣)+ `receptor_by_strain.md`
(43 個 core、46 個 capeferrum 特有、各 class 數量)。

**下一步**:(1) 撈+清理 PharBP 全部 Pseudomonas host → 對應 NCBI 基因體;(2) 下載+註解
receptor(本機/Laguna);(3) BLAST 我們 receptor vs 各 host → host × 我們receptor 的 overlap
表(格 = % identity);(4) 對 top host 接上 PharBP 的 RBP 序列,必要時再對 shortlist 做 fold。

---
*Log — 2026-07-02: PI proposed matrix task. 2026-07-03: reasoning worked out (clue-level,
not simulation), PharBP scope corrected (~8k RBP / ~57 hosts), receptor×strain reference
table built, English + 中文(含對話來回)written. Next = host-receptor overlap from PharBP.*
