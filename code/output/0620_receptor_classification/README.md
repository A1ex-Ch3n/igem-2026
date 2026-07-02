# Pseudomonas receptors → Moriniere 2026 receptor classes

Classify the surface/outer-membrane proteins annotated in three environmental *Pseudomonas* strains (`9-2-1`, `9-6-2`, `10-10-2`) into the receptor classes of Moriniere et al. 2026 (EcoliPhage / GenoPHI) by **sequence homology**, so they share one receptor vocabulary with the phage side in [`../0619_literature_rbp_database/`](../0619_literature_rbp_database/).
Built by [`../../0620_receptor_classification.ipynb`](../../0620_receptor_classification.ipynb). (中文:[`README_zh.md`](README_zh.md))

## Method (one line)
**Receptor-vs-receptor** homology — MMseqs2 of our curated Pseudomonas OMPs against the **13 canonical *E. coli* K-12 receptor proteins that define the paper's classes**; best hit passing the gate → that class, else `Unclassified`.
> ⚠️ **Not** BLAST receptors vs the RBP database: a receptor is the "lock", an RBP (phage tail fiber) is the "key" — they're non-homologous, so that comparison returns ~all Unclassified.

## Files

| File | Contents |
|---|---|
| `receptor_classification.tsv` | **Main result** — one row per receptor (237): strain, locus, annotation, curated category, `curation` (kept / rescued-by-homology), `assigned_class`, `fold_family`, best E. coli hit, %identity, coverage, e-value, bitscore, confidence, basis |
| `class_summary.tsv` | counts per class × strain |
| `excluded_log.tsv` | the 305 entries dropped as non-receptors, with reason — and **confirmed to contain zero gate-passing homolog** (nothing real silently dropped) |
| `pseudomonas_receptors_curated.fasta` | the annotation-curated "pure receptors" list (233 seqs) |
| `ecoli_receptor_refs.fasta` | the 13 E. coli K-12 reference receptors (= search target) |
| `ecoli_receptor_refs_meta.tsv` | gene / UniProt accession / length of the 13 refs |
| `blast_raw_hits.m8` | raw MMseqs2 hits for all 542 (re-threshold without re-running) |

## How to read `receptor_classification.tsv`

The hierarchy first:
```
542 surface proteins
├── 237 pure receptors (= this table)
│     ├── 81  classified (mapped to a Moriniere class)
│     └── 156 Unclassified (a receptor, but no E. coli 13-class match across genus)
└── 305 non-receptors (in excluded_log.tsv, not in this table)
```

Each row = one pure receptor. Key columns:

| Column | How to read it |
|---|---|
| `assigned_class` | the Moriniere class hit (`fhuA`/`ompA`/`tolC`/`tsx`…); `Unclassified` = a receptor with no match to the 13 classes |
| `fold_family` | **read this one** — the honest level (TBDR / OmpA-family / TolC-family / porin…). Cross-genus you can't tell fhuA vs btuB reliably, so **trust the family, not the member name** |
| `confidence` | `family-level` = passed the gate, family is reliable; `none` = Unclassified |
| `curation` | `kept` = annotation judged it a receptor; `rescued-by-homology` = annotation had excluded it but homology overrode (4 rows) |
| `curated_category` | the annotation-based first-pass bin (auditable) |
| `best_ref_gene` / `pct_identity` / `query_cov` / `evalue` / `bitscore` | the homology evidence vs the best E. coli reference; use these to re-threshold |
| `basis_note` | one-line rationale (incl. rescue note, or why an Unclassified row failed) |

Reading tips:
- **`Unclassified` ≠ not a receptor** — it's still a pure receptor, just with no E. coli 13-class match (typically OprD-family porins). The actual non-receptors are in `excluded_log.tsv`.
- **Class is a homology/family annotation, not a binding prediction** (same fold ≠ same phage binds).
- To see only the mapped ones → filter `assigned_class != Unclassified` (81); to see one family → filter on `fold_family`.

## Where the 13 classes come from
**The list is from the paper** (p.5–6, 15: of the ~60–180 OMPs in E. coli K-12, only 13 ever act as receptors):
`Tsx, FadL, OmpA, OmpF, OmpW, OmpC, FhuA, BtuB, LptD, NupG, LamB, TolC, YncD`.
**The sequences are from UniProt** (the paper deposits no receptor FASTA — only gene identities): fetched by `gene + E. coli K-12 (taxid 83333) + Swiss-Prot`, accession and length verified at fetch time. All 13 are used (not just the 8 with phage RBPs in the DB) so TolC/OmpA etc. have a reference.

## Decision logic
1. **Curate**: keyword ruleset bins the 542 into keep (OMP-receptor folds) / flag out-of-scheme surface (pili, autotransporter, flagellin, secretin) / exclude (Bam-Lol assembly, TonB-ExbBD energizers, inner-membrane transporters, efflux inner pumps & periplasmic adaptors, cytoplasmic signaling…). The `curated_category` column makes every call auditable.
2. **MMseqs2 easy-search** (`-s 7.5`) — **all 542 proteins** → 13 refs (not just the curated set, so homology can override a wrong annotation).
3. **Gate**: `e-value ≤ 1e-5` **and** `query coverage ≥ 0.50`. Across genera, e-value+coverage are reliable; raw %identity is **not** (real homologs sit at ~20–35%), so identity only sets the confidence tier, never a hard cutoff.
4. Pass → assigned the best-hit class; fail → `Unclassified` (closest reference still recorded for transparency).
5. **Homology overrides annotation**: any annotation-excluded protein that passes the gate is *rescued* into the table (`curation = rescued-by-homology`). Here that recovered **4 rows / 2 proteins** — a "Secretin/TonB short N-terminal" protein (→ `fhuA`, e=2e-17: really a TonB-dependent receptor) and OM-lipoprotein YfiB (→ `ompA`, e=8e-12). The final excluded set was then re-checked: **0 of 305 pass the gate.**

## Results

| Category | Count (3 strains) |
|---|---|
| **Classified** | **81** |
| └ TonB-dependent receptors (fhuA 41 / btuB 12 / yncD 7) | 60 |
| └ ompA | 12 |
| └ tolC | 6 |
| └ tsx | 3 |
| **Unclassified** (kept as receptor candidates) | **156** |
| (non-receptors removed at curation, separate) | 305 |

> **Strain caveat:** `9-2-1` and `9-6-2` have a near-identical product set, so the 3-strain totals roughly **double-count** the same proteins (≈ two copies + the `10-10-2` variant). Read totals as scale, not diversity; per-strain columns are in `class_summary.tsv`.

**Key scientific takeaways:**
- **Max identity is only ~40%** — *no* protein reaches close-ortholog level (>40% id); every call is `family-level`. That itself is the result: **Pseudomonas has no close ortholog of any E. coli receptor; matches are recoverable only at the fold-family level.**
- **All 81 porins are Unclassified** — Pseudomonas porins are predominantly **OprD-family**, with no E. coli OmpF/OmpC/LamB homolog *detectable above this gate with MMseqs2*. (More sensitive profile methods — HMMER/HHpred — could detect remote signal at 20–30% identity; the all-porins-Unclassified result is conditional on the search tool, not an absolute claim of no relationship.)
- **TonB-dependent receptors classify best** (60 → FhuA/BtuB/YncD family), consistent with Pseudomonas's heavy reliance on siderophore iron piracy.
- `fold_family` is the **honest level**; `fhuA`/`btuB`/`yncD`, and individual porin members, cannot be reliably distinguished across genera — read at family level.

## Important limitations (please convey to the professor)
1. The 13 classes are an **E. coli K-12 functional list** (knockout-derived), not a universal taxonomy; transferring it to Pseudomonas has an inherent gap.
2. **Class = homology/family annotation, not a binding prediction.** Same fold ≠ same phage binds (e.g. OprF is OmpA-family but its extracellular loops differ entirely from E. coli OmpA).
3. **Incomplete coverage**: type IV pili, LPS O-antigen, and flagella — common Pseudomonas phage receptors — are not in these 13 classes (polysaccharide or outside the list) and fall into out-of-scheme / Unclassified.
4. The gate (cov 0.5 / e 1e-5) is tunable — all raw numbers are in `blast_raw_hits.m8` and the main table, so re-thresholding needs no re-search.

## Reproduce
Needs `mmseqs`, `pandas`, `requests`, and internet (UniProt). Run [`../../0620_receptor_classification.ipynb`](../../0620_receptor_classification.ipynb) (or the matching `.py`); all outputs land in this folder.

---
*Log: 2026-06-20 — initial build. 542 surface proteins; all searched vs 13 E. coli refs → receptor table 237 (233 curated-kept + 4 rescued-by-homology) / 305 non-receptors (0 gate-passers). 81 classified / 156 Unclassified. Gate cov≥0.5 & e≤1e-5.*
