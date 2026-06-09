# Protocols — markdown staging

Markdown drafts of all lab protocols, source-of-truth for porting to Benchling. Each protocol is sourced **strictly** from `lab_notebook/digitalized/*.md` and the existing `protocol/*.docx|pdf` references — no invented procedures.

**Authoring rules:** [`_TEMPLATE.md`](_TEMPLATE.md) defines required sections, the `## Checklist` storage block, and the quick-lookup table format. When sources disagree on a value (team's as-run vs prof's vs kit default), **preserve all versions side-by-side** rather than picking one.

**Status legend:** 📝 draft • 🔍 review • ✅ confirmed • 🚀 ported to Benchling • 🔴 deprecated (content preserved for historical reference; do not run)

---

## Media & Buffer (7)

| # | Protocol | Status | Source notebook entries / source docs | Used by |
|---|---|---|---|---|
| 1 | [LB Broth](media/lb_broth.md) ★ | 🔍 review | [5-27](../../lab_notebook/digitalized/2026-05-27_dna-quantification-pia-plates.md), [6-1](../../lab_notebook/digitalized/2026-06-01_lb-agar-phage-buffer.md), [6-3](../../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md) | #2, #13, #8, #16, #17, #18 |
| 2 | [LB Agar](media/lb_agar.md) ★ | 🔍 review | [6-1](../../lab_notebook/digitalized/2026-06-01_lb-agar-phage-buffer.md) (1 %), [6-3](../../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md) (0.7 % + 0.8 % lesson), [6-4](../../lab_notebook/digitalized/2026-06-04_second-phage-plaque-assay-prep.md) (0.7 %) | #17, #18, #21, #23 |
| 3 | [PMM (Pseudomonas Minimum Media)](media/pmm.md) ★ | 🔍 review | [5-21](../../lab_notebook/digitalized/2026-05-21_pmm-agar-plates.md); `../PMM_ProtocoL (1).docx`; `../PseudomonasClassAppendixes.pdf` | #12, #7 |
| 4 | [PIA (Pseudomonas Isolation Agar)](media/pia.md) ★ | 🔍 review | [5-27](../../lab_notebook/digitalized/2026-05-27_dna-quantification-pia-plates.md) | #8, #19 |
| 5 | [Phage Buffer](media/phage_buffer.md) ★ | 🔍 review *(modified)* | [6-1](../../lab_notebook/digitalized/2026-06-01_lb-agar-phage-buffer.md); `../Genomic_And_Phage_Work.docx` | #16, #17, #18, #22, #23 |
| 6 | [50 % Glycerol Solution](media/glycerol_50pct.md) ★ | 🔍 review | [5-29](../../lab_notebook/digitalized/2026-05-29_optical-density-bacteria-stock.md) | #10 |
| 7 | [Quick-DNA Miniprep Kit (Zymo)](media/quick_dna_miniprep_kit.md) ★ | 📝 draft *(new)* | `../_d3024_d3025_quick-dna_miniprep_kit.pdf` | #14, #20 |

## Techniques (5)

| # | Protocol | Status | Source notebook entries / source docs | Used by |
|---|---|---|---|---|
| 8 | [Three-Phase Streak Plate](techniques/three_phase_streak.md) | 🔍 review | [5-22](../../lab_notebook/digitalized/2026-05-22_streak-test-trial.md) (practice), [5-26](../../lab_notebook/digitalized/2026-05-26_streak-soil-enrichment.md) (real run) | #12, #24 |
| 9 | [Single-Colony Inoculation](techniques/single_colony_inoculation.md) ★ | 🔍 review *(modified)* | [5-28](../../lab_notebook/digitalized/2026-05-28_inoculation-2nd-dna-extraction.md), [6-2](../../lab_notebook/digitalized/2026-06-02_inoculation-phage-isolation.md); `../Genomic_And_Phage_Work.docx` | #19, #22, #23 |
| 10 | [OD₆₀₀ Measurement](techniques/od600_measurement.md) ★ | 🔍 review | [5-29](../../lab_notebook/digitalized/2026-05-29_optical-density-bacteria-stock.md) (diluted t22 + undiluted t26) | log-phase decisions |
| 11 | [Glycerol Stock Storage](techniques/glycerol_stock_storage.md) ★ | 🔍 review | [5-29](../../lab_notebook/digitalized/2026-05-29_optical-density-bacteria-stock.md) | bank cultures; reverse = #24 |
| 24 | [Revive Bacteria from −80 °C Glycerol Stock](techniques/revive_bacteria_from_glycerol_stock.md) | 📝 draft *(new)* | [6-1](../../lab_notebook/digitalized/2026-06-01_lb-agar-phage-buffer.md) (Procedure ③) | reverse of #11; −80 stock → streak → fresh [[lb_agar]] plates |

## Workflows (13 active; 2 archived)

| # | Protocol | Status | Source notebook entries / source docs | Notes |
|---|---|---|---|---|
| 12 | [Soil Sample Collection](workflows/soil_sample_collection.md) | 🔍 review | [5-19](../../lab_notebook/digitalized/2026-05-19_soil-sample-collection.md) | Field method (probe + GPS-labelled zip-bags) |
| 13 | [Soil Enrichment — Bacteria](workflows/soil_enrichment_bacteria.md) | 🔍 review | [5-20](../../lab_notebook/digitalized/2026-05-20_dna-extraction-soil-enrichment.md) | PMM-based; refs [[pmm]] |
| 14 | [Soil Enrichment — Phage](workflows/soil_enrichment_phage.md) ★ | 🔍 review | [6-1](../../lab_notebook/digitalized/2026-06-01_lb-agar-phage-buffer.md) | LB-based (not PMM); refs [[lb_broth]] |
| 15 | [Metagenomic DNA Extraction](workflows/metagenomic_dna_extraction.md) | 🔍 review *(modified)* | [5-20](../../lab_notebook/digitalized/2026-05-20_dna-extraction-soil-enrichment.md), [5-28](../../lab_notebook/digitalized/2026-05-28_inoculation-2nd-dna-extraction.md), [6-5](../../lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md), [6-8](../../lab_notebook/digitalized/2026-06-08_metagenomic-extraction-dna-concentration-quantification.md) | Quick-DNA Miniprep (13-step transcription) — refs [[quick_dna_miniprep_kit]]; 6-8 small-biomass (0.12 g/tube) + pooling → feeds #25 |
| 16 | [DNA Quantification (Portelite BDR / Qubit 4)](workflows/dna_quantification_qubit.md) ★ | 🔍 review *(modified)* | [5-27](../../lab_notebook/digitalized/2026-05-27_dna-quantification-pia-plates.md), [6-5](../../lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md), [6-8](../../lab_notebook/digitalized/2026-06-08_metagenomic-extraction-dna-concentration-quantification.md); Portelite BDR PDF | Standards + samples + raw-RFU mode; 6-point + 7-point + 6-8 smaller-volume 4-point series |
| 17 | [Phage Isolation](workflows/phage_isolation.md) ★ | 🔍 review *(modified)* | [6-2](../../lab_notebook/digitalized/2026-06-02_inoculation-phage-isolation.md); `../Genomic_And_Phage_Work.docx` | Variant A bulk filtration (team) only; Variant B daily aliquot **deprecated 2026-06-06** |
| 18 | [Plaque Assay — Soft-Agar Overlay](workflows/plaque_assay_soft_agar.md) ★ | 🔍 review | [6-3](../../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md) (failed @ 0.7 %) | Doc the failure + 0.8 % lesson |
| 19 | [Plaque Assay — Layered-Plate](workflows/plaque_assay_layered_plate.md) ★ | 🔍 review | [6-4](../../lab_notebook/digitalized/2026-06-04_second-phage-plaque-assay-prep.md) | Hard-agar base + 0.7 % overlay |
| 20 | [Bacteria Pellet for Sequencing](workflows/bacteria_pellet_for_sequencing.md) ★ | 🔍 review *(modified)* | [6-3](../../lab_notebook/digitalized/2026-06-03_phage-plaque-assay.md) (Procedure ③); `../Genomic_And_Phage_Work.docx` Part 1 | PBS wash + −20 °C; team 3000 rpm / prof 4000 rpm variants |
| 21 | [Bacteria Genome Extraction](workflows/bacteria_genome_extraction.md) ★ | 📝 draft *(new)* | [6-5](../../lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md); Zymo kit PDF p.4 | Quick-DNA on bacterial pellet; team edits pending |
| 22 | [Phage Purification (iterative re-isolation)](workflows/phage_purification.md) ★ | 📝 draft *(new)* | `../Genomic_And_Phage_Work.docx` Part 4 | Single-plaque pick + re-plate × ≥ 3 rounds (team not yet run) |
| 23 | [Media Disposal](workflows/media_disposal.md) | 🔍 review | [6-4](../../lab_notebook/digitalized/2026-06-04_second-phage-plaque-assay-prep.md) (Procedure ③) | Bleach + DI rinse |
| 25 | [DNA Concentration / Cleanup (Spin-Column)](workflows/dna_concentration.md) | 📝 draft *(new)* | [6-8](../../lab_notebook/digitalized/2026-06-08_metagenomic-extraction-dna-concentration-quantification.md) (Procedure ⑤ / p.35) | Re-bind dilute eluate → elute small; refs [[metagenomic_dna_extraction]], [[dna_quantification_qubit]]; downstream of #15 |

### Archived (moved 2026-06-06 to [`../../archived/`](../../archived/README.md))

| Was # | Archived file | Reason |
|---|---|---|
| ~~22~~ | [`spot_testing.md`](../../archived/spot_testing.md) | Prof crossed out steps 21–26 of `Genomic_And_Phage_Work.docx`. Replaced by [[plaque_assay_layered_plate]]. Team never executed. |
| ~~23~~ | [`phage_amplification.md`](../../archived/phage_amplification.md) | Prof crossed out steps 15–17 of `Genomic_And_Phage_Work.docx`. Entire host-amplification routine removed. Team never executed. |

★ = has a `## Quick-lookup table` section (either concentration / use-case variants, or a per-batch recipe table).

---
## Log
- 2026-06-05 — Index seeded with all 20 planned protocols.
- 2026-06-05 — All 20 drafts written from lab-notebook + existing `protocol/` source docs. Status advanced to 🔍 review. 38 `[TBD]` / `==CONFIRM==` markers across the set — see [open-items list](#open-items-for-review) below.
- 2026-06-05 — Fixed two `/verify` FAIL findings: (1) added `## Reagents` section to all 14 protocols that were missing it (techniques + workflows), and (2) corrected ★ markers in the index — all 15 files with a quick-lookup table now carry the ★. Legend definition broadened to match.
- 2026-06-05 — Renamed parent folder `protocal/` → `protocol/` (spelling fix); updated all references across project (5 .md files + Obsidian workspace). Resolved Qubit-kit identity to Portelite (AAT Bioquest); rewrote `workflows/dna_quantification_qubit.md` (6-point custom standard curve 0/1/3/10/30/100 ng/µL, 0.2 mL PCR tubes, PI extrapolation-beyond-100 guidance).
- 2026-06-05 — **Corrected** Qubit-kit variant: it's the **BDR** (Broad Dynamic Range) kit (cat. **17665**) not the HS kit (17660/17661). User had initially pointed at the wrong PDF. `dna_quantification_qubit.md` updated with BDR-specific specs: Component D = 100 ng/µL (so Std 5 = Component D undiluted), excitation 480 / emission 530 nm, **linear regression** fit (not log-log), 0.2–100 ng/µL optimized range.
- 2026-06-05 — **Folded in `Genomic_And_Phage_Work.docx` and the Zymo kit PDF.** Counts: **20 → 25** protocols. **5 new** (`quick_dna_miniprep_kit`, `bacteria_genome_extraction`, `spot_testing`, `phage_amplification`, `phage_purification`). **4 modified, preserving all variants** (`phage_buffer` ← added prof's molar recipe + pH 7.5; `bacteria_pellet_for_sequencing` ← added prof's 4000 rpm variant; `single_colony_inoculation` ← added prof's 10 mL row; `phage_isolation` ← restructured into bulk + daily-aliquot variants). Cross-ref graph: `quick_dna_miniprep_kit` ← used by `metagenomic_dna_extraction` + `bacteria_genome_extraction`; `phage_isolation` → `phage_amplification` → plaque assays → `phage_purification` (× 3 rounds) → UNDONE phage DNA extraction + sequencing.
- 2026-06-06 — **Prof updated `Genomic_And_Phage_Work.docx`:** crossed out steps 15–17 (host amplification + daily sampling) and steps 21–26 (spot-testing execution); also indicated step 14 (Filtering) should now be done twice. **Impact on `protocol/md/`:** marked **`workflows/spot_testing.md`** and **`workflows/phage_amplification.md`** as **🔴 deprecated** (content preserved as historical reference; both protocols team had never executed). Removed Variant B daily-aliquot from **`workflows/phage_isolation.md`** (now deprecated within that file). Updated "Downstream pipeline" notes in `phage_isolation` to the simplified path `phage_isolation → plaque_assay_layered_plate → phage_purification (× 3 rounds)`. **Step 14 "filter 2×" update deliberately NOT yet applied** — pending team discussion before adoption. README status legend gained 🔴 deprecated.
- 2026-06-06 — **Moved the 2 deprecated protocols to [`/archived/`](../../archived/) at the project root** (`spot_testing.md` + `phage_amplification.md`). Workflows count `14 → 12 active + 2 archived`. Index split into an active section + an "Archived" section linking to the new home. Each archived file's full content + `[!failure] DEPRECATED` callout preserved verbatim — the archive directory has its own `README.md` recording provenance.
- 2026-06-08 — **New technique: [Revive Bacteria from −80 °C Glycerol Stock](techniques/revive_bacteria_from_glycerol_stock.md)** — drafted from the 6-1 entry (Procedure ③ "Streak bacteria stock"). Fills a real gap: the revival direction (−80 stock → streak → fresh plates) previously had no protocol, only the freezing direction (#11). **Appended as #24** rather than inserting as a new #12 — the index's "Used by" column cross-references protocol numbers, so renumbering would ripple; #24 keeps existing refs intact (rows now run 8–11, 24 in the Techniques table). Techniques count `4 → 5`.
- 2026-06-08 — **Integrated the 2026-06-08 session.** New workflow **[DNA Concentration / Cleanup (Spin-Column)](workflows/dna_concentration.md)** drafted from the 6-8 entry (p.35) — re-bind a dilute eluate and elute small; fills a gap (the concentration step had no protocol). **Appended as #25** (same out-of-sequence convention as #24 — avoids renumbering the cross-referenced workflow rows). Workflows count `12 → 13 active`. **Modified #15** [metagenomic_dna_extraction] — replaced the thin "follow the kit" procedure with the 13-step transcription from the printed kit page (`0608/IMG_4411.png`) + 6-8 run params (≈0.12 g/tube, 40 min vortex L3, 4-tubes-pooled), and resolved its UNDONE "Planned next" row to the executed 6-8 small-biomass + pooling trial (sites #1/6/8/9; 0.12 g/tube confirmed, ~8× down from the prior 1 g/tube; before/after worked — #6 ~17×, #8 ~14×, #9 ~27×). **Modified #16** [dna_quantification_qubit] — added the 6-8 smaller-volume 4-point standard series alongside the existing 6-/7-point series (preserve-all-versions). Kit catalog for #15/#25 left `[TBD]`.

---

## Open items for review

Missing values and ambiguities surfaced during drafting. Each protocol carries inline `[TBD: …]` or `==CONFIRM: …==` markers; the list below is a quick triage view.

### Brand / catalog confirmations (one-time fill, then constant)
- **LB broth powder** brand + catalog — [`media/lb_broth.md`](media/lb_broth.md)
- **Agar powder** brand + catalog — [`media/lb_agar.md`](media/lb_agar.md)
- **PIA base medium** brand + catalog — [`media/pia.md`](media/pia.md)
- ~~**Phage buffer reagents** — exact forms of Tris / MgSO₄ / CaCl₂ (anhydrous vs hydrate)~~ → ✅ **Resolved 2026-06-05** by reverse-checking team's gram weights against prof's molar concentrations: **MgSO₄·7H₂O** (heptahydrate) + **CaCl₂·2H₂O** (dihydrate) + Tris adjusted to **pH 7.5**.
- ~~**Soil DNA extraction kit** brand~~ → ✅ **Quick-DNA™ Miniprep Kit (Zymo Research)** (confirmed 2026-06-05). Catalog # = **D3024 / D3025** ([`media/quick_dna_miniprep_kit.md`](media/quick_dna_miniprep_kit.md)). Lot still `[TBD]` from the physical box.
- ~~**Qubit dye** chemistry (BR vs HS)~~ → ✅ **Neither standard Qubit dye** — actual kit is **Portelite™ Fluorimetric DNA Quantitation Kit with Broad Dynamic Range** (AAT Bioquest, cat. **17665**, Helixyte™ Green BR dye) read on Qubit 4, green channel (480 / 530 nm). Resolved 2026-06-05; protocol rewritten.

### Standardization decisions (notebook has multiple values; need to pick one)
- **LB broth autoclave cycle** — 30 min (5-27) vs 1 hr (6-1) — [`media/lb_broth.md`](media/lb_broth.md)
- **LB agar autoclave cycle** — same divergence — [`media/lb_agar.md`](media/lb_agar.md)
- **PMM pour volume per plate** — 7 mL (5-21) vs 12 mL (5-22) — [`media/pmm.md`](media/pmm.md)
- **MiniQ vs DI water** for LB broth — 5-27 used MiniQ, 6-1 used DI — [`media/lb_broth.md`](media/lb_broth.md)
- **Bacteria-pellet harvest spin** — team's 3000 rpm + 10,000 g two-stage scheme vs prof's 4000 rpm one-stage — both kept side-by-side in [`workflows/bacteria_pellet_for_sequencing.md`](workflows/bacteria_pellet_for_sequencing.md); team can pick one as canonical later.
- **Single-colony inoculation volume** — team's 5 mL vs prof's 10 mL (sequencing prep) — both rows in [`techniques/single_colony_inoculation.md`](techniques/single_colony_inoculation.md) quick-lookup table.

### Missing notebook values (notebook didn't record; need team)
- **Soil mass + broth volume per flask** for [[soil_enrichment_bacteria]] (5-20 entry trails off) — [`workflows/soil_enrichment_bacteria.md`](workflows/soil_enrichment_bacteria.md)
- **Enrichment incubation temp + duration** — both bacteria and phage tracks — [`workflows/soil_enrichment_bacteria.md`](workflows/soil_enrichment_bacteria.md), [`workflows/soil_enrichment_phage.md`](workflows/soil_enrichment_phage.md)
- **Bleach concentration + contact time** — [`workflows/media_disposal.md`](workflows/media_disposal.md)
- **50 % glycerol** — autoclave / filter-sterilize step (not in 5-29) — [`media/glycerol_50pct.md`](media/glycerol_50pct.md)
- **Latitude** (notebook records only longitude + altitude) — [`workflows/soil_sample_collection.md`](workflows/soil_sample_collection.md)
- **Final sentence of [`plaque_assay_layered_plate`](workflows/plaque_assay_layered_plate.md) step 8** — 6-4 trails off mid-sentence
- **Bacteria genome extraction — team modifications** to the Zymo Whole Blood protocol (resuspension buffer + volume + any incubation tweaks) — [`workflows/bacteria_genome_extraction.md`](workflows/bacteria_genome_extraction.md). User will share specifics.
- **Phage buffer aliquot volume** — [`media/phage_buffer.md`](media/phage_buffer.md)
- **Phage purification — long-term banking** of confirmed-clonal lysate — [`workflows/phage_purification.md`](workflows/phage_purification.md) (after round 3)
- **Glycerol-stock revival — incubation temp + time, and scrape amount** (6-1 entry doesn't record either; project default is 30 °C overnight) — [`techniques/revive_bacteria_from_glycerol_stock.md`](techniques/revive_bacteria_from_glycerol_stock.md)
- **Metagenomic 6-8 run** — ~~input mass~~ ✅ confirmed **0.12 g/tube**; **"mix 4 tubes into 1" pooling ratio** still `[TBD]` — [`workflows/metagenomic_dna_extraction.md`](workflows/metagenomic_dna_extraction.md)
- **DNA concentration 6-8** — kit catalog, starting pooled volume, and elution volume (p.35) — [`workflows/dna_concentration.md`](workflows/dna_concentration.md)
- **Qubit 6-8** — ~~four unconcentrated #1/6/8/9 RFU readings~~ ✅ resolved (119.87 / 195.94 / 3600.46 / 1139.16; before/after now computed). Still open: blurry p.36 standard/sample digits (S0/S1/C1/C8/C9), the concentration-factor calc, and the bacterial sequencing submitted-volume (≈90 µL assumed) — see [6-8 entry](../../lab_notebook/digitalized/2026-06-08_metagenomic-extraction-dna-concentration-quantification.md) + [`typos.md`](../../lab_notebook/digitalized/typos.md)

### `==CONFIRM==` items (flagged inline)
- **`8-5-2` × 2 vs `8-3-2` × 2** in the 6-3 pellet list vs 6-5 Set A — physical freezer rack to verify — [`workflows/bacteria_pellet_for_sequencing.md`](workflows/bacteria_pellet_for_sequencing.md), [`lab_notebook/digitalized/2026-06-05_…md`](../../lab_notebook/digitalized/2026-06-05_plaque-assay-r3-dna-extraction-quantification.md) Procedure ③
- **#2 vs #3 enrichment-sample mismatch** between bacteria and phage tracks — [`workflows/soil_enrichment_phage.md`](workflows/soil_enrichment_phage.md)
- **5-mL vs 2.75-mL per-plate mix volume** on 6-3 — [`workflows/plaque_assay_soft_agar.md`](workflows/plaque_assay_soft_agar.md)

### Closed-out (was deferred)
- ~~**`Genomic_And_Phage_Work.docx` integration**~~ → ✅ **Resolved 2026-06-05.** Folded into 4 existing protocols (preserving all variants) + 3 new workflows (`spot_testing`, `phage_amplification`, `phage_purification`).

### Pending team decisions
- **Step 14 "filter 2×" update** to [[phage_isolation]] Variant A — prof's 2026-06-06 update suggests filtering the soil-enrichment supernatant **twice** through 0.22 µm rather than once. Team did a single filter on 6-2. Not yet applied to the protocol — pending team discussion before adoption.
