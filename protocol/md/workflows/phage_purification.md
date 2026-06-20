---
title: Phage Purification — Iterative Single-Plaque Re-Isolation
type: workflow
purpose: Take a positive plaque from a plaque assay and purify it to a clonal (axenic) phage by iterative single-plaque pick → elute → re-plate, repeated ≥ 3 times. The output is a single-phage lysate ready for DNA extraction + sequencing.
references:
  - "[[lb_agar]]"
  - "[[phage_buffer]]"
  - "[[single_colony_inoculation]]"
  - "[[plaque_assay_soft_agar]]"
  - "[[plaque_assay_layered_plate]]"
source:
  - protocol/Genomic_And_Phage_Work.docx
  - lab_notebook/digitalized/2026-06-10_pellet-prep-genome-extraction-plaque-assay.md
  - lab_notebook/digitalized/2026-06-12_plaque-assay-extracted-phage.md
estimated_time: ≈ 1 hr per round + overnight incubation; ≥ 3 rounds total ≈ 4–5 days
---

# Phage Purification — Iterative Single-Plaque Re-Isolation

> [!note] Status — first plaque-pick recorded 2026-06-10 / 2026-06-12
> The team has now performed its **first single-plaque pick → elute → re-plate** (one round), so the iterative protocol is no longer purely on-paper. Steps still drafted from the prof's `Genomic_And_Phage_Work.docx` (Part 4); the team's as-run pick technique is folded into Notes. **This is at most round 1 of the ≥ 3 rounds** required for a clonal lysate. `==CONFIRM: which candidate counts toward purification depends on the 6/10–6/12 phage lineage (see the as-run note + the [6-10 entry](../../../lab_notebook/digitalized/2026-06-10_pellet-prep-genome-extraction-plaque-assay.md) Notes).==` Part 4 (steps 27–30) was **not** affected by the 2026-06-06 update that deprecated `[[spot_testing]]` and `[[phage_amplification]]` — phage purification remains an active part of the simplified pipeline.

## Purpose
A single plaque on a first-round plaque assay is **not yet proof of a single phage clone** — it may have formed from multiple phages that happened to co-localise. To get a **clonal (axenic)** lysate suitable for phage DNA extraction and sequencing, the plaque must be re-isolated multiple times: pick a single plaque → suspend it → plate on a fresh bacterial lawn → pick a single new plaque → repeat.

**Three rounds is the convention.** By round 3, the lysate is statistically dominated by a single phage genotype and the downstream sequencing read pile assembles cleanly into one phage genome.

## Quick-lookup table — per-round volumes

| Component | Volume | Notes |
|---|---|---|
| [[phage_buffer]] for plaque elution | **100 µL** | Vortex the punched-out agar core to release phages |
| Overnight bacterial host culture | **250 µL** | Same host strain as the original assay |
| Eluted / diluted phage from the picked plaque | **10 µL** | Added to the agar + bacteria mix |
| Molten 0.7 % LB soft agar (50 °C) | **3 mL** | See [[lb_agar]] |
| **→ Pour onto** | one hard agar plate | See [[plaque_assay_layered_plate]] for the layered-plate setup |

## Materials & equipment
- Sterile pipette tips (large enough to **punch out a soft-agar core** from a plaque)
- [[phage_buffer]] aliquots (~100 µL per plaque per round)
- Microcentrifuge tubes (for elution + storage)
- Vortex
- Falcon tubes (for the molten-agar + bacteria mix per re-plate)
- 50 °C water bath (keep soft agar molten)
- 30 °C incubator
- Pre-poured 1 % LB hard agar plates (one per round per phage) — see [[lb_agar]]

## Reagents
- A **plaque-positive plate** from a previous round ([[plaque_assay_soft_agar]] / [[plaque_assay_layered_plate]] for round 1; this protocol's own output for rounds 2 and 3) — *[`spot_testing` was a possible round-1 source per the original prof's doc but was archived 2026-06-06; see [`/archived/spot_testing.md`](../../../archived/spot_testing.md)]*
- [[phage_buffer]] (for elution and dilution)
- Overnight bacterial host culture — see [[single_colony_inoculation]]
- Molten 0.7 % LB soft agar at 50 °C — see [[lb_agar]]
- Pre-poured hard agar plates (1 % LB agar) — see [[lb_agar]]

## Procedure (per round — repeat ≥ 3 times)

### Step A — Pick a single plaque
1. Identify a **single, well-isolated cleared plaque** on the source plate. Avoid plaques near the edge or near other plaques — the goal is a plaque that almost certainly originated from one phage particle.
2. Using a sterile pipette tip, **punch out and pick up the soft agar gel** at that plaque (a "plaque core"). The tip cores the agar like a hole-punch.

### Step B — Elute the plaque
3. **Dissolve the agar core** into **100 µL of [[phage_buffer]]** in a microcentrifuge tube.
4. **Vortex well** to release the phages into suspension.
5. **Store at 4 °C** — note: do **not** store this crude elution for extended periods before proceeding to step C. Same-day use is best.

### Step C — Re-plate on a fresh bacterial lawn
6. In a Falcon tube, combine:
   - **250 µL** of overnight host bacterial culture
   - **10 µL** of the dissolved / diluted phage from Step B
7. Add this mix to **3 mL of molten 0.7 % LB soft top agar** (50 °C water bath).
8. **Immediately pour** the mixture over a pre-solidified hard agar plate.
9. Tilt to cover; wait for the soft agar to solidify.

### Step D — Incubate & evaluate
10. Incubate the plate **inverted (lid on bottom)** at **30 °C overnight** to allow new plaques to form.
11. Next day, check for new plaques. If present, **return to Step A** with a single new well-isolated plaque from this plate and start the next round.

### Step E — Repeat until clonal
12. **Repeat steps A–D at least 3 consecutive times** to ensure you have isolated a completely **clonal, axenic** phage strain. The output of the third successful round is the lysate to feed phage DNA extraction → sequencing.

## Notes / common deviations
- **Team's as-run pick technique (6-10 / 6-12).** Mark the target plaque on the **back** of the plate first. Then **insert a (cut/wide) pipette tip vertically into the soft agar at the marked plaque** — as vertical as possible — to core out the plaque plug, **pipette the gel plug into phage buffer, and vortex thoroughly** to elute. The eluate is the phage source for the next re-plate (per [[plaque_assay_layered_plate]], 200 µL eluate/plate on 6-12). *(6-10 used 20 mL-pipette tips for a wide bore; the prof's Part 4 below specifies a sterile pipette tip / loop.)* `==CONFIRM: phage-buffer volume per pick — 6-10 reads "2 mL" into a 1.5 mL Eppendorf, likely 1 mL.==`
- **First candidates picked:** `6-8-1` Φ3 and `8-1-2` Φ6, off the **6-10 ϕ3/5/6 plaque assay** (run on the 10 newly revived hosts; see the [6-10 entry](../../../lab_notebook/digitalized/2026-06-10_pellet-prep-genome-extraction-plaque-assay.md) Notes) — these are the live re-isolation candidates. A **separate Φ8 pick** was also taken on 6-10 from the two successful **06/05 plates** — **host `9-6-2` Φ8** and **host `9-2-1` Φ8** (the only week-1 phage hits; those plates used the *old* 06/03-banked hosts). Both picks are stored at 4 °C (see [[dna_extraction_inventory]], [[week_3_bacteria_list]]). The 6-11 Φ8/9/10 screen — on the new hosts — produced no plaques, **but whether that screen used these 6-10 eluates or the fresh 06/09 ϕ8/9/10 filtrate is unconfirmed** (so "the 6-10 pick failed" is not established). `==CONFIRM==`
- **Why three rounds?** Statistically, after one round you might still have multiple phage variants if the original plaque was mixed. Each subsequent round geometrically reduces the chance of co-isolation — three rounds is the field-standard convention for clonality.
- **Mixed-lysate symptoms** in sequencing assembly: poor contig N50, chimeric assemblies, ambiguous variant calls. If sequencing assembly fails despite three rounds, add a fourth round before re-extracting.
- **Plaque morphology consistency** across rounds is informative — a plaque that looks the same (size, edge sharpness, turbidity) across all three rounds is more likely truly clonal than one that varies between rounds.
- **Don't pick a plaque that grew at the edge of another plaque** — those may have shared metabolites or even physically merged.
- The crude elution from Step B is **not stable** — process to Step C the same day (or at most the next day, refrigerated).

## Checklist — where do the outputs go?
- [ ] Crude eluted plaques (in 100 µL phage buffer) → **4 °C fridge** for same-day re-plating; do not bank for long.
- [ ] Re-plated incubation plates → **30 °C incubator**, inverted.
- [ ] Confirmed-clonal lysate (after round 3) → **4 °C fridge** for short-term, ready for phage DNA extraction → sequencing. *(For longer-term storage, follow lab's standard phage-stock banking protocol — `[TBD]`.)*
- [ ] Source plates after picking → [[media_disposal]] (bleach + DI rinse) once finished with.

## Source
- [`../Genomic_And_Phage_Work.docx`](../../Genomic_And_Phage_Work.docx) — Part 4: Phage Purification (steps 27–30).
- Lab notebook: [2026-06-10](../../../lab_notebook/digitalized/2026-06-10_pellet-prep-genome-extraction-plaque-assay.md) (Procedure ⑤ — first plaque pick/elute) and [2026-06-12](../../../lab_notebook/digitalized/2026-06-12_plaque-assay-extracted-phage.md) (Procedure ② — re-plate of picked plaques).

---
## Log
- 2026-06-05 — Initial draft from prof's `Genomic_And_Phage_Work.docx` Part 4. Project has not executed this protocol yet — no team-recorded values to fold in. Maps to the scheme's UNDONE "re-isolation round 2" + "round 3" bullets.
- 2026-06-06 — Updated `spot_testing` cross-ref in Reagents section to point at `archived/spot_testing.md` (the protocol was archived after prof's update crossed out spot-testing steps 21–26). Reagents `[[spot_testing]]` wiki-link removed; references frontmatter cleaned.
- 2026-06-08 — Proofread cleanups (**#11** + **#14** + **#15**): converted prose `> **Status:** …` to `> [!note] Status — as of 2026-06-08` callout to match project convention; `estimated_time` uses `≈` instead of `~` for consistency; added this Log entry to record the 6-06 archive update + this 6-08 cleanup.
- 2026-06-12 — **Status update:** team performed its first single-plaque pick → elute → re-plate (6-10 pick/elute, 6-12 re-plate) — protocol is no longer purely on-paper. Added the team's as-run pick technique (mark on back → vertical tip core → elute in phage buffer → vortex) to Notes, the first picked candidates (`6-8-1` Φ3, `8-1-2` Φ6), and 6-10/6-12 to `source:`. Flagged with `==CONFIRM==` (round counting depends on the 6/10–6/12 phage lineage; phage-buffer volume per pick). No prof-protocol steps changed.
- 2026-06-12 — **User correction:** clarified that the ϕ8/9/10 pick is from the *old* 06/05 plates while both of the week's plaque *assays* (ϕ3/5/6 6/10, ϕ8/9/10 6/11) ran on the **10 newly revived hosts**; reworded the "First candidates picked" note so the new-host screen isn't conflated with the old-plate pick.
- 2026-06-13 — **User-confirmed** the two week-1 hits / 06/05 successful plates: **`9-6-2` Φ8** + **`9-2-1` Φ8** (picks now at 4 °C); named them in the "separate Φ8 pick" note. Cross-linked to the new [[dna_extraction_inventory]] + [[week_3_bacteria_list]].
