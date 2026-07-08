---
title: DNA Extraction Inventory
purpose: Master inventory of every bacteria/phage/DNA item, organized by storage location (4 °C / −20 °C / −80 °C / sent), with what it is, date created, and sequencing status. Quantification details kept as a reference appendix.
last_updated: 2026-06-13
sources:
  - lab_notebook/digitalized/2026-05-20_dna-extraction-soil-enrichment.md
  - lab_notebook/digitalized/2026-05-27_dna-quantification-pia-plates.md
  - lab_notebook/digitalized/2026-05-28_inoculation-2nd-dna-extraction.md
  - lab_notebook/digitalized/2026-05-29_optical-density-bacteria-stock.md
  - lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md
  - lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md
  - lab_notebook/digitalized/2026-06-08_metagenomic-extraction-dna-concentration-quantification.md
  - lab_notebook/digitalized/2026-06-10_pellet-prep-genome-extraction-plaque-assay.md
  - data/assays/0529_OD.xlsx
  - data/bacteria_genome/
  - code/0605_quantification.ipynb
  - code/0608_quantification.ipynb
---

# DNA Extraction Inventory

Organized by **storage location**. Each section is one table — **ID · what it is · date created · status (sent / not sent for sequencing)**. Per-sample concentrations/masses live in the [Quantification details](#quantification-details-reference) appendix. Physically re-checked **2026-06-13**.

See [[metagenomic_dna_extraction]] and [[bacteria_genome_extraction]] for method; [[dna_quantification_qubit]] for the assay; [[week_3_bacteria_list]] for the strains still to be worked.

---

## 4 °C — DNA extracts + phage picks

| ID | What it is | Date created | Status |
|---|---|---|---|
| 9-1-1 | Bacteria genome extract (Round 2) | 2026-06-10 | not sent |
| 6-8-1 | Bacteria genome extract (Round 2) | 2026-06-10 | not sent |
| 9-10-1 | Bacteria genome extract (Round 2) | 2026-06-10 | not sent |
| 6-2-1 | Bacteria genome extract (Round 2) | 2026-06-10 | not sent |
| 8-10-2 | Bacteria genome extract (Round 2) | 2026-06-10 | not sent |
| 9-9-2 | Bacteria genome extract (Round 2) | 2026-06-10 | not sent |
| 6-8-2 | Bacteria genome extract (Round 2) | 2026-06-10 | not sent |
| 6-10-2 | Bacteria genome extract (Round 2) | 2026-06-10 | not sent |
| 6-3-2 | Bacteria genome extract (Round 1) | 2026-06-05 | not sent |
| 8-5-2 | Bacteria genome extract (Round 1) | 2026-06-05 | not sent |
| 8-2-2 | Bacteria genome extract (Round 1) | 2026-06-05 | not sent |
| 10-9-2 | Bacteria genome extract (Round 1) | 2026-06-05 | not sent |
| 9-2-2 | Bacteria genome extract (Round 1) | 2026-06-05 | not sent |
| 8-3-1 ⚠ | Bacteria genome extract (Round 1) — **label likely `8-5-1`** (see [Discrepancies](#discrepancies--miswrites-to-fix)) | 2026-06-05 | not sent |
| 8-3-2 | Bacteria genome extract (Round 1) | 2026-06-05 | not sent |
| Metagenome site 1 (Round 3) | Metagenome extract, concentrated | 2026-06-08 | not sent |
| Metagenome site 6 (Round 3) | Metagenome extract, concentrated | 2026-06-08 | not sent |
| Metagenome mix_1 | Metagenome extract (R1+R2 combined) | 2026-05-28 | not sent |
| Metagenome mix_3 | Metagenome extract (R1+R2 combined) | 2026-05-28 | not sent |
| Metagenome mix_4 | Metagenome extract (R1+R2 combined) | 2026-05-28 | not sent |
| Metagenome mix_7 | Metagenome extract (R1+R2 combined) | 2026-05-28 | not sent |
| Metagenome site 2 (1st batch) | Metagenome extract | 2026-05-20 | not sent |
| Metagenome site 5 (1st batch) | Metagenome extract | 2026-05-20 | not sent |
| Metagenome site 6 (1st batch) | Metagenome extract | 2026-05-20 | not sent |
| Metagenome site 8 (1st batch) | Metagenome extract | 2026-05-20 | not sent |
| Metagenome site 9 (1st batch) | Metagenome extract | 2026-05-20 | not sent |
| Metagenome site 10 (1st batch) | Metagenome extract | 2026-05-20 | not sent |
| 9-6-2 Φ8 | Phage pick / lysate (plaque-picked into phage buffer) — week-1 hit | 2026-06-10 | not sent |
| 9-2-1 Φ8 | Phage pick / lysate (plaque-picked into phage buffer) — week-1 hit | 2026-06-10 | **sent** — see [Sent for sequencing — phage](#sent-for-sequencing--phage-results-back-2026-07-08) |

*The two phage picks are the "two successful 06/05 plates" (Φ8 on hosts `9-6-2` and `9-2-1`), cored and eluted on [2026-06-10](../lab_notebook/digitalized/2026-06-10_pellet-prep-genome-extraction-plaque-assay.md) ⑤. The hosts `9-6-2`/`9-2-1` also have bacterial genome extracts (sent for sequencing — see below) and remain as −80 glycerol stocks.*

---

## −20 °C — bacteria pellets

| ID | What it is | Date created | Status |
|---|---|---|---|
| 9-1-2 | Bacteria pellet (washed, awaiting extraction) | 2026-06-10 | not sent |
| 8-1-2 | Bacteria pellet (washed, awaiting extraction) | 2026-06-10 | not sent |

*Banked as pellets because the Quick-DNA kit's last 8 spin columns were used on the 8 Round-2 extractions; these 2 wait for new columns. ([2026-06-10](../lab_notebook/digitalized/2026-06-10_pellet-prep-genome-extraction-plaque-assay.md) ②)*

---

## −80 °C — glycerol stocks (28)

All 28 stocks physically confirmed 2026-06-13 (Alex found batch-1 ×13; R found batch-2 ×15 — exactly the two `Stock Solutions` sub-lists in [`0529_OD.xlsx`](assays/0529_OD.xlsx)). **Batch-2 (6-x onward) = the "likely *P. aeruginosa*" candidates.** Created 2026-05-29 ([2026-05-29](../lab_notebook/digitalized/2026-05-29_optical-density-bacteria-stock.md) ②). Glycerol stocks are the permanent backup — not themselves sent for sequencing.

| ID | What it is | Date created | Status |
|---|---|---|---|
| 10-10-1 | Glycerol stock (batch-1) | 2026-05-29 | not sent (stock) |
| 10-9-1 | Glycerol stock (batch-1) | 2026-05-29 | not sent (stock) |
| 10-7-2 | Glycerol stock (batch-1) | 2026-05-29 | not sent (stock) |
| 8-2-2 | Glycerol stock (batch-1) | 2026-05-29 | not sent (stock) |
| 10-9-2 | Glycerol stock (batch-1) | 2026-05-29 | not sent (stock) |
| 9-6-2 | Glycerol stock (batch-1) | 2026-05-29 | not sent (stock) |
| 8-3-2 | Glycerol stock (batch-1) | 2026-05-29 | not sent (stock) |
| 10-10-2 | Glycerol stock (batch-1) | 2026-05-29 | not sent (stock) |
| 8-5-1 | Glycerol stock (batch-1) | 2026-05-29 | not sent (stock) |
| 9-2-1 | Glycerol stock (batch-1) | 2026-05-29 | not sent (stock) |
| 9-2-2 | Glycerol stock (batch-1) | 2026-05-29 | not sent (stock) |
| 8-5-2 | Glycerol stock (batch-1) | 2026-05-29 | not sent (stock) |
| 6-3-2 | Glycerol stock (batch-1) | 2026-05-29 | not sent (stock) |
| 6-2-1 | Glycerol stock (batch-2, likely *P. aeruginosa*) | 2026-05-29 | not sent (stock) |
| 6-2-2 | Glycerol stock (batch-2, likely *P. aeruginosa*) | 2026-05-29 | not sent (stock) |
| 6-6-1 | Glycerol stock (batch-2, likely *P. aeruginosa*) | 2026-05-29 | not sent (stock) |
| 6-6-2 | Glycerol stock (batch-2, likely *P. aeruginosa*) | 2026-05-29 | not sent (stock) |
| 6-7-2 | Glycerol stock (batch-2, likely *P. aeruginosa*) | 2026-05-29 | not sent (stock) |
| 6-8-1 | Glycerol stock (batch-2, likely *P. aeruginosa*) | 2026-05-29 | not sent (stock) |
| 6-8-2 | Glycerol stock (batch-2, likely *P. aeruginosa*) | 2026-05-29 | not sent (stock) |
| 6-10-2 | Glycerol stock (batch-2, likely *P. aeruginosa*) | 2026-05-29 | not sent (stock) |
| 8-1-2 | Glycerol stock (batch-2, likely *P. aeruginosa*) | 2026-05-29 | not sent (stock) |
| 8-7-1 | Glycerol stock (batch-2, likely *P. aeruginosa*) | 2026-05-29 | not sent (stock) |
| 8-10-2 | Glycerol stock (batch-2, likely *P. aeruginosa*) | 2026-05-29 | not sent (stock) |
| 9-1-1 | Glycerol stock (batch-2, likely *P. aeruginosa*) | 2026-05-29 | not sent (stock) |
| 9-1-2 | Glycerol stock (batch-2, likely *P. aeruginosa*) | 2026-05-29 | not sent (stock) |
| 9-9-2 | Glycerol stock (batch-2, likely *P. aeruginosa*) | 2026-05-29 | not sent (stock) |
| 9-10-1 | Glycerol stock (batch-2, likely *P. aeruginosa*) | 2026-05-29 | not sent (stock) |

*Note: each glycerol stock is the permanent source; reviving one and pelleting/extracting it does **not** consume the −80 stock, so strains can appear here **and** in the 4 °C / −20 °C tables.*

---

## Sent for sequencing — 2026-06-08

Results returned ~2026-06-12 (in [`bacteria_genome/`](bacteria_genome/) — Cal_Bot_9_2_1, 9_6_2, 10_10_2).

| ID | What it is | Date created | Status |
|---|---|---|---|
| Metagenome #8 | Metagenome extract (Round 3, concentrated, diluted for submission) | 2026-06-08 | **sent** |
| Metagenome #9 | Metagenome extract (Round 3, concentrated, diluted for submission) | 2026-06-08 | **sent** |
| 9-2-1 | Bacteria genome extract (Round 1) | 2026-06-05 | **sent** |
| 9-6-2 | Bacteria genome extract (Round 1) | 2026-06-05 | **sent** |
| 10-10-2 | Bacteria genome extract (Round 1) | 2026-06-05 | **sent** |

*Submission details (conc / volume / mass) in the [Quantification details](#quantification-details-reference) appendix. Metagenomes #8/#9 were diluted (38 µL DNA + 50 µL kit buffer); the 3 bacterial genomes — see Discrepancy #3.*

---

## Sent for sequencing — phage (results back 2026-07-08)

Results returned 2026-07-08 (raw + host-removed paired-end fastq, now in [`phage_genome/9-2-1/`](phage_genome/9-2-1/)). `[TBD: exact submission date — not recorded anywhere; only the results-back date is known.]`

| ID | What it is | Date created | Status |
|---|---|---|---|
| 9-2-1 Φ8 | Phage pick / lysate (plaque-picked into phage buffer) — week-1 hit | 2026-06-10 | **sent — assembled + annotated** |

*Vendor submission code `3NKSC3`. Only the `9-2-1` Φ8 pick has come back so far — the companion `9-6-2 Φ8` pick (same 06/05 plate pair, still listed as "not sent" above) has not. **Assembled + annotated 2026-07-08**: complete ~62.4 kb novel phage — a **linear genome with a ~77 bp DTR** (confirmed vs the PI group's 62,416 bp assembly; our SPAdes contig is 62,338 bp with one DTR copy trimmed + RC/rotated). Temperate, safe (0 virulence / 0 AMR), carries RBPs; our own host removal found ~15% host vs the vendor's 1.9%. Full write-up: [`phage_genome/9-2-1/assembly/NOTES.md`](phage_genome/9-2-1/assembly/NOTES.md).*

---

## Discrepancies / miswrites to fix

1. **`8-3-1` ≈ `8-5-1`.** The 6/5 extract labelled `8-3-1` is **not** one of the 28 glycerol stocks. `8-5-1` *is* (batch-1 #9) and was a host in the 6/3 plaque assay ([2026-06-03](../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md) ②) yet appears nowhere else as an extract — so `8-3-1` is almost certainly **`8-5-1` mislabelled**. Label kept as written (user); **verify the physical tube** and relabel. *(This is why the not-yet-worked set is 8, not 9 — see [[week_3_bacteria_list]].)*
2. **6/3 pellet list `8-5-2 ×2`.** The 6/3 bacteria-pellet list recorded `8-5-2` twice and no `8-5-1` — same root cause as #1; one banked `8-5-2` is really `8-5-1`.
3. **Bacterial sequencing "diluted".** The 6/13 recheck noted the 3 sent bacterial genomes (`9-2-1`/`9-6-2`/`10-10-2`) as "diluted for sequencing", but the 6/8 submission was earlier confirmed **not diluted** (only the metagenomes were diluted). Recorded here as sent, undiluted — confirm which is right.
4. **Metagenome Round-1 (5/20) count.** Digitized as "all 10 (#1–#10)"; the 6/13 physical check finds **6** tubes (sites 2, 5, 6, 8, 9, 10) — the rest apparently consumed (into the M-mixes / quant).

*All bacteria IDs except `8-3-1` trace cleanly to the 28-stock list.*

---

## Quantification details (reference)

Per-sample numbers behind the tables above. Concentrations marked **⚠** are **extrapolated** above the standard curve's top point (approximate). Volumes are post-Qubit "remaining" estimates.

### Bacteria genome — Round 1 (extracted 2026-06-05, ~90 µL each; total ≈ 140.7 µg) — [`0605_quantification.ipynb`](../code/0605_quantification.ipynb)

| Sample | Conc (ng/µL) | Mass (µg, ~90 µL) |
|---|---:|---:|
| 8-2-2 | 263.98 ⚠ | 23.76 |
| 8-5-2 | 245.51 ⚠ | 22.10 |
| 9-6-2 | 194.53 ⚠ | 17.51 |
| 8-3-1 ⚠(≈8-5-1) | 156.82 ⚠ | 14.11 |
| 10-10-2 | 140.44 ⚠ | 12.64 |
| 9-2-1 | 139.29 ⚠ | 12.54 |
| 10-9-2 | 125.31 ⚠ | 11.28 |
| 9-2-2 | 102.25 ⚠ | 9.20 |
| 6-3-2 | 101.66 ⚠ | 9.15 |
| 8-3-2 | 93.34 | 8.40 |

### Bacteria genome — Round 2 (extracted 2026-06-10) — **not yet quantified**

8 extracts at 4 °C (`9-1-1, 6-8-1, 9-10-1, 6-2-1, 8-10-2, 9-9-2, 6-8-2, 6-10-2`); conc/volume/mass *pending* (deferred to "next week"). 2 pellets (`8-1-2`, `9-1-2`) at −20 °C. ([2026-06-10](../lab_notebook/digitalized/2026-06-10_pellet-prep-genome-extraction-plaque-assay.md))

### Metagenome — Round 2 (extracted 2026-05-28, ~80 µL each) — quantified [2026-06-05](../lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md)

| Sample | Conc (ng/µL) | Mass (µg, ~80 µL) |
|---|---:|---:|
| #1 | 1.62 | 0.130 |
| #3 | 0.18 | 0.015 |
| #4 | 1.16 | 0.093 |
| #7 | 0.36 | 0.029 |
| M1 mix | 1.78 | 0.142 |
| M3 mix | 0.14 | 0.011 |
| M4 mix | 0.74 | 0.059 |
| M7 mix | 0.45 | 0.036 |

*M-mixes = round-1 (5-20) + round-2 (5-28) eluates combined. Round-2 total ≈ 0.5 µg. Standalone #1/#3/#4/#7 appear consumed into the mixes (only the mixes were found 6/13).*

### Metagenome — Round 3 (extracted 2026-06-08; before/after concentration) — [`0608_quantification.ipynb`](../code/0608_quantification.ipynb)

| Site | Unconc (ng/µL) | Concentrated (ng/µL) | Fold |
|---|---:|---:|---:|
| #1 | ≈ 0 (below blank) | ≈ 0 | — |
| #6 | 0.21 | 3.58 | ~17× |
| #8 | 20.76 | **290.23** ⚠ | ~14× |
| #9 | 5.91 | **160.69** ⚠ | ~27× |

*Concentrated eluate ≈ 40 µL curated (38 µL after 2 µL quant). `[TBD: confirm final concentrated volume.]` #8/#9 diluted + sent for sequencing; #1/#6 retained at 4 °C.*

### Metagenome — Round 1 (extracted 2026-05-20) — ✗ quant failed

All sites quantified [2026-05-27](../lab_notebook/digitalized/2026-05-27_dna-quantification-pia-plates.md): only **#10** above detection; no numeric ng/µL recorded. 6 tubes (sites 2,5,6,8,9,10) remain at 4 °C.

### Sent-for-sequencing submission masses (2026-06-08)

| Sample        | Type             | Diluted?                           | Submitted conc (ng/µL) | Volume (µL) | DNA sent (µg) |
| ------------- | ---------------- | ---------------------------------- | ---------------------: | ----------: | ------------: |
| Metagenome #8 | metagenome       | yes (38 µL DNA + 50 µL kit buffer) |                 125.33 |          88 |         11.03 |
| Metagenome #9 | metagenome       | yes (38 µL DNA + 50 µL kit buffer) |                  69.39 |          88 |          6.11 |
| 9-2-1         | bacterial genome | no (see Discrepancy #3)            |                 139.29 |        ≈ 90 |         12.54 |
| 9-6-2         | bacterial genome | no (see Discrepancy #3)            |                 194.53 |        ≈ 90 |         17.51 |
| 10-10-2       | bacterial genome | no (see Discrepancy #3)            |                 140.44 |        ≈ 90 |         12.64 |

*Metagenome mass sent = pre-dilution conc × 38 µL; bacterial = conc × ≈ 90 µL (`[TBD]` if less than full eluate).*

---

## Log
- 2026-06-10 — Initial compilation (by type: metagenomic / bacterial / sequencing) from the digitized lab notebook (5-20 / 5-27 / 5-28 / 6-5 / 6-8) and the 0605 / 0608 notebooks.
- 2026-06-10 — Corrected the 6-5 bacterial Set A: the 26,136.76 RFU reading is `8-3-1` (not a second `8-3-2`), per user.
- 2026-06-12 — Added Bacterial Round 2 (6-10): 8 extracted + 2 pellets; spin-column note.
- 2026-06-13 — **Restructured to a by-storage-location layout** (4 °C / −20 °C / −80 °C / sent), each a single table (ID · what · date · status), from the user's physical re-check. Added the −80 glycerol-stock table (all 28), the 2 week-1 phage picks (`9-6-2 Φ8` / `9-2-1 Φ8`) at 4 °C, and the older metagenome extracts (1st-batch sites 2/5/6/8/9/10, mixes mix_1/3/4/7). Moved per-sample conc/mass into a **Quantification details** appendix (nothing lost). Added a **Discrepancies** section (8-3-1≈8-5-1 — label kept per user; 6/3 `8-5-2 ×2`; bacterial "diluted" wording; 5/20 "all 10"→6). Added sources (5-29 OD, 6-3 entry, `0529_OD.xlsx`, `bacteria_genome/`). Created companion [[week_3_bacteria_list]].
- 2026-07-08 — First phage sequencing results back: `9-2-1 Φ8` (vendor code `3NKSC3`, raw + host-removed paired-end fastq) landed in `data/phage_genome/9-2-1/`. Marked `9-2-1 Φ8` **sent** in the 4 °C table and added a new **Sent for sequencing — phage** section. Submission date not recorded anywhere in the notebook/inventory — flagged `[TBD]` rather than guessed. Companion `9-6-2 Φ8` pick still shows "not sent" — no data for it yet.
- 2026-07-08 — `9-2-1 Φ8` **assembled + annotated** (Laguna, [`code/0708_phage_assembly/`](../code/0708_phage_assembly/)): one 62,338 bp circular novel phage genome (temperate, safe, carries RBPs). Updated its status to "assembled + annotated" in both phage tables. Write-up: [`phage_genome/9-2-1/assembly/NOTES.md`](phage_genome/9-2-1/assembly/NOTES.md).
