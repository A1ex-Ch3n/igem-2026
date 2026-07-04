# Phage–host receptor matrix — findings so far (Steps 0–2)

**Date:** 2026-07-03 · **Code:** `code/0703_phage_host_matrix/` · **Companion:**
process/reasoning log = [`2026-07-02_phage_host_receptor_matrix_thinking-log.md`](2026-07-02_phage_host_receptor_matrix_thinking-log.md)

A findings summary (results, not reasoning) for each step done so far. Goal of the whole
task: predict which known Pseudomonas phages could infect our isolates, bridged by shared
receptor repertoire (a clue, not proof — phages read variable surface loops).

## Output files (`code/output/0703_phage_host_matrix/`)
| file | what |
|---|---|
| `receptor_by_strain.{tsv,md}` | Step 0 — our receptors × our 5 isolates (presence) |
| `pharbp_pseudomonas_hosts.{tsv,md}` | Step 1 — 54 PharBP hosts → 43 NCBI genomes |
| `host_overlap_matrix.tsv` | Step 2 — our 144 receptors × 43 host genomes (best % identity) |
| `host_overlap_summary.{tsv,md}` | Step 2 — hosts ranked by receptors shared with us |
| `host_receptor_overlap.tsv`, `host_receptor_counts.tsv` | Step 2 — long form + host repertoires |
| `receptor_host_presence.{tsv,md}` | our receptors → which host strains carry them |

---

## English

**Step 0 — our receptor repertoire.** Clustering our 441 receptor proteins (mmseqs 90%/80%)
across the 5 sequenced isolates gives **144 receptor groups**. 43 are core (in all 5); **46
are 8-10-2-specific** (P. capeferrum is the genuinely distinct isolate — the other four,
9-6-2/9-2-1/10-10-2/8-5-2, are *Pseudomonas_E* sp013179515 and near-identical). Dominant
classes: porin, TBDR, TolC/efflux-OM.

**Step 1 — PharBP hosts → genomes.** Filtering PharBP by the **host** field
(`host=Pseudomonas`, reproducing the DB's **6,376** host-containing records; + Stutzerimonas)
gives **54 distinct host strains → 43 downloadable NCBI genomes** (26 strain-exact, 27
species-reference, 1 unresolved). *Lesson:* filter by host, not phage name; PharBP's host
field is coarse (6k+ RBP records collapse to ~54 host names, dominated by lab strains, mostly
*P. aeruginosa* / *P. syringae*).

**Step 2 — host × our-receptor overlap.** Downloaded the 43 genomes, mined **3,850 host
receptors**, and mmseqs'd our 144 reps against each. The result cleanly separates hosts by
how much they resemble us:
- **P. putida is the standout** — max identity **99.4%**, 57–68 of our receptors shared at
  ≥90%. Crucially **P. putida KT2440 has 71 phages** in PharBP. Secondary near-relatives:
  taiwanensis (26 shared ≥90%, 3 phages), plecoglossicida (24, 3 phages).
- **P. aeruginosa is far** — max only **81.7%**, **0** receptors shared at ≥90%, despite
  carrying ~108 receptors of its own and dominating PharBP's phage records. Its phages are
  therefore low-value leads for us.
This reproduces the 0623 surrogate-host conclusion by an independent (PharBP-based) route.

**Our receptors → host strains.** Of our **144** receptors, **76** are present in ≥1 PharBP
host at ≥90% identity, **131** at ≥50%, and **13 are "our-specific"** (found in no PharBP
Pseudomonas host even at ≥50% — mostly porins; candidates for genuinely distinctive receptors).
The receptors shared at ≥90% are shared almost exclusively with the **P. putida group**
(putida / KT2440 / S12 / taiwanensis / plecoglossicida / lactis …), never with aeruginosa.

**Takeaway.** Following the receptor-overlap logic converges hard on **P. putida (especially
KT2440) as the surrogate host** — it is the only host that is both highly receptor-similar to
us (~99%) and phage-rich (71 phages). Its phages are the top candidates to test / to fold
against our receptors next.

---

## 中文

**Step 0 — 我們的 receptor repertoire。** 把 5 株的 441 個 receptor 用 mmseqs(90%/80%)跨株分群 →
**144 個 receptor group**。43 個為 core(5 株都有);**46 個是 8-10-2 獨有**(P. capeferrum 是真正
不同的那株;其他 4 株 9-6-2/9-2-1/10-10-2/8-5-2 是 *Pseudomonas_E* sp013179515,幾乎相同)。
主要 class:porin、TBDR、TolC/efflux-OM。

**Step 1 — PharBP host → 基因體。** 用 **host** 欄位篩(`host=Pseudomonas`,重現 DB 的 **6,376** 筆;
+ Stutzerimonas)→ **54 個 distinct host strain → 43 個可下載 NCBI 基因體**(26 strain-exact、
27 species-reference、1 unresolved)。*教訓:* 要用 host 篩、不要用 phage 名篩;PharBP 的 host 欄位很粗
(6 千多筆 RBP 塌縮到 ~54 個 host 名,多為實驗室株,大宗是 *P. aeruginosa* / *P. syringae*)。

**Step 2 — host × 我們receptor 的 overlap。** 下載 43 個基因體、挖出 **3,850 個 host receptor**、
把我們 144 個 rep 比對過去。結果乾淨地把宿主按「跟我們像不像」分開:
- **P. putida 是標竿** —— max identity **99.4%**,我們有 57–68 個 receptor 跟它 ≥90% 相同。關鍵是
  **P. putida KT2440 在 PharBP 有 71 個 phage**。次要近緣:taiwanensis(≥90% 共享 26,3 phage)、
  plecoglossicida(24,3 phage)。
- **P. aeruginosa 很遠** —— max 只有 **81.7%**、**0** 個 receptor ≥90% 相同,儘管它自己有 ~108 個
  receptor、又佔 PharBP 最多 phage 記錄。所以它的 phage 對我們參考價值低。
這用獨立的(PharBP)路徑重現了 0623 surrogate-host 的結論。

**我們的 receptor → 出現在哪些 host strain。** 我們 **144** 個 receptor 裡,**76** 個在 ≥1 個 PharBP
host 身上 ≥90% 相同,**131** 個 ≥50%,而 **13 個是「我們獨有」**(在任何 PharBP Pseudomonas host
都找不到 ≥50% 的同源;多為 porin,可能是我們較獨特的 receptor)。而那些 ≥90% 共享的 receptor,
幾乎只跟 **P. putida group**(putida / KT2440 / S12 / taiwanensis / plecoglossicida / lactis…)
共享,從不跟 aeruginosa。

**結論。** 沿著 receptor-overlap 的邏輯,強烈收斂到 **P. putida(尤其 KT2440)= surrogate host**
—— 它是唯一「跟我們 receptor 極像(~99%)、又 phage 多(71 個)」的宿主。它的 phage 就是下一步
最該拿去測試 / 對我們的 receptor 做 fold 的頭號候選。

---
*Log — 2026-07-03: Steps 0–2 findings summary (bilingual). Next = pull PharBP RBP sequences
for the P. putida-group hosts → RBP × receptor layer.*
