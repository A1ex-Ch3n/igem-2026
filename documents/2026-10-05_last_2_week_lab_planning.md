---
title: Last 2 Weeks — Lab Planning (2026-10-06 → 2026-10-20)
type: planning
status: 📝 draft — Track A set, Track B pending
---

# Last 2 Weeks — Lab Planning

> **Schedule lives in [`2026-10-06_week_schedule.xlsx`](2026-10-06_week_schedule.xlsx)** — 10/06 → 10/10, colour-coded by track, with an expected-output column and a Spot-assay tab.
> This file explains *what each step is and why*. The spreadsheet says *when* and *what comes out*.
> `2026-10-05_last_2_week_schedule.xlsx` is superseded — delete once this one is agreed.

## Materials — confirmed in the lab 2026-10-06

| Item | Form | Location | Note |
|---|---|---|---|
| 6 × resistant-clone gDNA | extracted 2026-07-09 | 4 °C fridge | 9-2-1 R1–R3, 9-6-2 R1–R3. 90 µL each |
| 9-2-1 Φ8 lysate | pure lysate, 1 bottle | 4 °C fridge | titre **never measured**; untouched since 2026-07-15 |
| 9-6-2 Φ8 lysate | pure lysate, 1 bottle | 4 °C fridge | same |
| BL21(DE3) *E. coli* | — | — | no-plasmid control for the induction gels |
| Empty pET-28a | **not available** | — | use plain BL21(DE3) instead |

## Open
- [ ] Plasmidsaurus bacterial WGS input spec (volume, tube type) — needed before aliquoting
- [ ] Which CDS is wild-type depolymerase — blocks Track B plate layout
- [ ] Fall break start: 10/16 or 10/17 — plan assumes last work day 10/20
- [ ] Φ8 lysate viability — unknown until the first plate. Step 0 answers it

## Hard dates
| Date | Item |
|---|---|
| Tue 10/06 | Ship gDNA. Pour plates. Revive strains. |
| Wed 10/07 | Team photo 4:30 PM, uniform + lab coat. Safety form final submit. |
| Tue 10/20 | Last work day. |
| Wed 10/21 | Wiki, software, judging form, attribution, project description. |

---

# Track A — Bacterial WGS

**Goal:** sequence the phage-resistant clones and compare each against its own already-sequenced parent → find the resistance locus → predict the surface sugar the depolymerase acts on. Feeds the wiki genome section + software deliverable.

> [!important] Not the wild-type hosts
> 9-2-1 and 9-6-2 already have complete annotated genomes from June (9-2-1 = GCA_059295275.1; 9-6-2 assembled + annotated on disk, not deposited). Re-sequencing them would buy nothing. The parents are the **reference**, not the sample.

## Order
| Field | Value |
|---|---|
| Samples | **2, 4 or 6** — Prof's choice. gDNA from phage-resistant clones |
| Candidates | 9-2-1 R1/R2/R3, 9-6-2 R1/R2/R3 |
| Service | Bacterial whole genome sequencing — **not** plasmid |
| Vendor | Plasmidsaurus |
| Ordered by | Prof, before drop-off |
| Drop-off | Caltech, 10/06, by car |

**What each count buys**
- **2** — one clone per host. Confirms a mutation exists in each lineage; cannot separate causal from passenger.
- **4** — two per host. First chance to see the same gene hit twice independently.
- **6** — three per host. A gene hit 2–3× is strong evidence for the resistance locus.

**Do not pool.** The clones differ from the parent by a handful of SNPs and from each other by fewer. A pooled assembly collapses to one consensus and loses which clone carries which mutation; a variant in 1 of 6 sits near 17% allele frequency, inside the error band. Per-sample barcoding is the thing being bought.

## Sample concentrations — `code/0710_quantification.ipynb`

| Sample | ng/µL | Volume | Mass |
|---|---:|---:|---:|
| 9-2-1 R1 | 55.8 | 90 µL | 5.0 µg |
| 9-2-1 R2 | 457.2 | 90 µL | 41.1 µg |
| 9-2-1 R3 | 81.4 | 90 µL | 7.3 µg |
| 9-6-2 R1 | 124.6 | 90 µL | 11.2 µg |
| 9-6-2 R2 | 1192.8 | 90 µL | 107.4 µg |
| 9-6-2 R3 | 261.1 | 90 µL | 23.5 µg |

⚠️ All six read **above the 30 ng/µL top standard** — order-of-magnitude only. **Dilute and re-read before aliquoting.** Flagged `UNDONE` since 2026-08-29.

## What the clones actually are
Picked 2026-07-07 as "3 dots" growing **inside the plaque zone** of the 9-2-1 and 9-6-2 Φ8 1:1000 plates; inoculated 7/08; pelleted, extracted and Qubit'd 7/09 (notebook p.75–p.77).

- **R1/R2/R3 are pick numbers, not identities.** Nothing records which dot came from which plate position.
- **Never verified as resistant.** The notebook says *"not sure if contamination or real colonies"*; PIA plates were streaked to check, but **no PIA readout was ever recorded**.
- **Plate provenance is contradictory**: `code/0710_quantification.ipynb` cell 7 says "picked from DIFFERENT PLATES"; notebook p.75 is ambiguous. If different plates, the clones are independent and convergence across them is meaningful. Both readings preserved.
- **No glycerol stock was made.** The only possible live material is the 7/07–7/08 PIA plates, 12 weeks at 4 °C. If they are dead, resistant clones must be re-isolated before any spot assay on them.

## 10/06 — ship
| Time | Action | Purpose |
|---|---|---|
| — | Dilute and re-Qubit the six tubes | real concentrations, not extrapolated |
| — | Aliquot to vendor spec, label, print sample list | — |
| — | Drive to Caltech | ship today |

## Risk
Bench time < 1 day on every path. The wait is the risk.

**Data back after 10/16 → no analysis time → Track A contributes nothing to the wiki.**

- [ ] Ask turnaround today, not at drop-off
- [ ] Check previous submission's actual turnaround in the digitised notebook

## Analysis — 4–8 h once data lands
assemble → annotate → locate surface sugar biosynthetic cassettes → circle-plot them on the genome figure. **UNDONE**

---

# Track A × B — resistant strain × ancestral enzymes

| Step | Action |
|---|---|
| 1 | Revive resistant strains from the **−80 °C freezer** |
| 2 | Grow lawns |
| 3 | Spot E1 / E40 / E281 / wild-type / phage |

**Tests:** halo from an ancestral node where wild type gives none = ancestral host range is broader. Central hypothesis, direct evidence.

**Why first:** does not depend on sequencing turnaround. Makes the genome a bonus, not a prerequisite.

**Controls:** resistant + phage must be negative. Sensitive parent strain, same batch. PBS, phage-positive, imidazole vehicle.

**Blocked on:** whether live resistant cells still exist. gDNA is in hand, but no glycerol stock was banked — only the 7/07–7/08 PIA plates, 12 weeks at 4 °C. If dead, re-isolate: plate host + Φ8 at high MOI, pick colonies from inside the clearing, bank glycerol stocks immediately. 2–3 days, and it needs live phage.

---

# Track B — protein + spot assay

**UNDONE — pending.** Carry forward:

- Assay is a 3-day cycle: spot → 30 °C overnight → room temp 24 h → read. Last useful spotting date **10/14**, or 10/16 if someone reads plates during break.
- **Step 0 go/no-go first.** Spot phage on host lawn, look for halo *around* plaques. Receptor is an LPS sugar, not a capsule — halo visibility is not guaranteed. One plate decides the whole track.
- Induction 16–20 °C, 0.5 mM IPTG, 16 h. Never 37 °C. Protein by Thursday evening requires IPTG in **Wednesday evening**.
- Plate layout: breadth (5 spots × many strains) or depth (7-step dilution series × one strain). Not both on one plate.
- Imidazole vehicle control mandatory — enzyme elutes in 500 mM imidazole.
- **Gel lanes per construct:** construct −IPTG, construct +IPTG, BL21(DE3) −IPTG, BL21(DE3) +IPTG (crude), plus one lane of **pooled** purified elutions. No empty pET-28a exists, so plain BL21(DE3) is the host-background control.
- **Pool the elution fractions.** One tube, one lane — not E1/E2/E3 separately. (Note the name clash: elution fractions E1/E2/E3 vs ancestral nodes E1/E40/E281.)
- Keep kanamycin in the passage and starter cultures — serial passage without selection loses the plasmid and looks exactly like failed expression.
- The uninduced arm only feeds a gel lane; 25–50 mL is enough. Only the induced arm needs 500 mL.
- **Protein priority:** batch 1 = CDS12 wild type + E1. Batch 2 = E40 + E281. Batch 3 = CDS 10 & 11 (likely future work).
- **Lawn panel, 6 strains:** 9-2-1, 9-6-2 (hosts) · 9-2-1 R1, R2 (resistant) · 8-10-2, 10-10-2 (clean non-hosts on the 7/04 matrix, **both with annotated genomes** — phenotype and genotype in one figure). Avoid the site-6 group (6-2-1, 6-2-2, 6-6-1, 6-6-2, 6-7-2, 6-8-2, 6-3-2): the 7/14 control was designed to test whether they are contamination or prophage, and was never read.
- **Φ8 amplification + titring is a new critical-path item.** The assay wants 10⁷–10⁸ PFU/mL; no titre has ever been measured and amplification was never run.
- Biological triplicate.
- Homework: protein quantity needed per spot. **UNDONE**

---

# 10/06 parallel — all paths

Plate stock is the critical path. Old LB plates were discarded.

- [ ] Pour LB plates in bulk, ~27 cultures' worth
- [ ] Streak original isolates from the **−80 °C freezer** (OG, not transformants)
- [ ] Streak resistant strains from the **−80 °C freezer**
- [ ] Overnight culture of transformants (second set, no kanamycin)
- [ ] Confirm 16 °C capacity and whether 500 mL inductions fit
- [ ] Buy bleach

Vivi, possibly Vincent: media and plates, freeing the core team for biochemistry.

---

## Log
- 2026-10-05 — Created after the deliverables call. Track A set: 2 samples (9-6-2, 9-2-1), bacterial WGS, Plasmidsaurus, Prof orders, Caltech drop-off 10/06. Three storage-outcome paths. Crossover experiment flagged. Track B **UNDONE** pending CDS identity and Step 0 result. 4 open questions, 5 UNDONE items.
- 2026-10-05 — Split the schedule out into `2026-10-05_last_2_week_schedule.xlsx` (58 rows, 10/05 → 10/21, colour-coded A / B / both / deadline, Legend tab carries the open questions and fixed constraints). This file is now the explanation; the spreadsheet is the calendar. Track B rows in the spreadsheet are **provisional** — they assume the Step 0 go/no-go passes and are not yet agreed.
- 2026-10-05 — Rewritten to time / action / purpose format. Attributions, quotes and references stripped. Corrected: the Friday-drop / Tuesday-pickup delay was **Scripps**, not Caltech — Caltech pickup removed as an open question.
