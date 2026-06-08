---
title: Spot Testing — Multi-Phage Screening on a Bacterial Lawn
type: workflow
purpose: Screen multiple phage filtrates against a single bacterial lawn by spotting 10 µL drops on a pre-marked grid — efficient detection step before committing to a full plaque assay per phage.
references:
  - "[[lb_agar]]"
  - "[[lb_broth]]"
  - "[[single_colony_inoculation]]"
  - "[[phage_isolation]]"
  - "[[phage_amplification]]"
source:
  - protocol/Genomic_And_Phage_Work.docx
estimated_time: ≈ 1.5 hr setup (excl. autoclave); overnight incubation
---

# Spot Testing — Multi-Phage Screening on a Bacterial Lawn

> [!failure] DEPRECATED 2026-06-06 — execution half removed from prof's `Genomic_And_Phage_Work.docx`
> Prof updated `Genomic_And_Phage_Work.docx` on / before 2026-06-06 and **crossed out steps 21–26** (Pouring the Lawn → Solidification → Spotting → Absorption → Incubation → Evaluation) — i.e., the entire **execution half** of the spot-testing approach. Steps 18–20 (Thin agar prep + Soft agar prep + Bacterial Lawn Mixture) are technically still in the source doc but lead nowhere without the execution steps.
>
> **What replaces it:** the team's [[plaque_assay_layered_plate]] (used 6-4 / 6-5) becomes the sole phage-screening method. Both approaches share the same general idea (bacterial lawn + phage on top) but use different plate formats — the layered-plate method has the bacteria *mixed into* the soft-agar overlay rather than just *spotted on top*.
>
> **Team status:** team **never executed** this protocol — never did either the prep half or the execution half. Content below preserved as historical reference for what was originally planned. Do not run; use [[plaque_assay_layered_plate]] instead.

## Purpose
Detect phage activity against a chosen bacterial host using a **thin-bottom hard agar plate + bacterial soft-agar overlay + grid-spotted phage drops**. Each plate can test multiple phage filtrates against a single host, making this an efficient first-pass screening method before committing to full per-phage plaque assays ([[plaque_assay_soft_agar]], [[plaque_assay_layered_plate]]).

## Quick-lookup table — per-plate composition

| Component | Volume | Notes |
|---|---|---|
| Thin hard agar (1 % LB agar) base | **5 mL** per plate | Less than the normal 8 mL base — see [[lb_agar]] for recipe |
| 0.7 % LB soft agar (molten, held at 50 °C) | **3 mL** per plate | See [[lb_agar]] 0.7 % entry |
| Overnight bacterial culture (host strain) | **250 µL** per plate | See [[single_colony_inoculation]] |
| Phage filtrate (per grid spot) | **10 µL** per spot | Multiple spots per plate on pre-marked grid |

## Materials & equipment
- Petri dishes (for thin hard-agar plates)
- 50 °C water bath (keep molten soft agar pourable)
- Small Falcon tubes (for bacterial lawn mix, one per plate)
- Pipettes + tips
- Marker (to draw the spotting grid on the back of the plate)
- 30 °C incubator (or per host's optimum)

## Reagents
- Pre-poured **thin hard-agar plates** (1 % LB agar, **5 mL** per plate — half the normal 8 mL) — see [[lb_agar]]. Can be prepared well in advance.
- **Molten 0.7 % LB soft agar**, held at 50 °C — see [[lb_agar]].
- **Overnight bacterial culture** of the host strain — see [[single_colony_inoculation]] for prep.
- **Phage filtrates** to test — output of [[phage_isolation]] (initial) or [[phage_amplification]] (enriched on host).

## Procedure

### Plate prep (do in advance)
1. **Pour thin hard agar plates:** 5 mL of 1 % LB agar per Petri dish (vs the normal 8 mL). Allow to solidify, then store at 4 °C until use.

### On the day
2. **Prepare soft top agar:** make 0.7 % LB agar per [[lb_agar]] and keep fluid in a **~50 °C water bath** so it does not solidify prematurely.
3. **Bacterial lawn mixture:** in a small Falcon tube, quickly mix:
   - 3 mL of molten soft agar
   - 250 µL of overnight bacterial culture (host strain)
4. **Pour the lawn:** mix gently with a pipette and pour immediately over the thin hard agar plate before the soft agar solidifies. Rotate the plate gently so the soft agar evenly covers the entire surface — this creates the **two-layer agar system** (hard base + bacterial soft overlay).
5. **Solidification:** wait **15–20 minutes** for the top agar layer to completely solidify.
6. **Mark spotting grid** on the **back** of the plate — one region per phage filtrate you intend to test.
7. **Spot phages:** using your phage enrichments / filtrates, gently drop **10 µL of filtrate** onto the corresponding pre-marked grid region.
8. **Absorption:** allow the plate to sit undisturbed for about **15 minutes** until the liquid droplets are fully absorbed into the agar.
9. **Incubation:** transfer the plates **inverted** (lid on the bottom) to the incubator.
10. **Evaluation (next day):** check the plate for **clear spots (zones of lysis)** at each grid region. Cleared areas indicate the presence of active phages that lyse the host strain.

## Notes / common deviations
- The 5 mL "thin" bottom is the key difference from a normal plate — it leaves more vertical room for the soft-agar overlay and makes the lysis zones easier to see.
- A successful spot is then a good candidate to take into [[phage_purification]] for clonal isolation, before phage DNA extraction and sequencing.
- This method is **complementary** to (not a replacement for) [[plaque_assay_soft_agar]] and [[plaque_assay_layered_plate]] — those run a full mixed-in-agar assay against a single phage, while spot testing screens many phages quickly against one host.

## Checklist — where do the outputs go?
- [ ] Thin hard agar plates (pre-poured, sealed in plastic bag) → **4 °C fridge** until day of use.
- [ ] Molten 0.7 % soft agar awaiting pour → **50 °C water bath** during the session.
- [ ] Inoculated + spotted plates → **30 °C incubator**, inverted (lid on bottom).
- [ ] After readout, plates with positive spots → keep at **4 °C fridge** while picking plaques for [[phage_purification]]; negatives → [[media_disposal]].

## Source
- [`../Genomic_And_Phage_Work.docx`](../../Genomic_And_Phage_Work.docx) — Part 3: Spot Testing (steps 19–26).

---
## Log
- 2026-06-05 — Initial draft from prof's `Genomic_And_Phage_Work.docx` Part 3. Project has not executed this protocol yet — no team-recorded values to fold in.
- 2026-06-06 — **DEPRECATED.** Prof crossed out steps 21–26 (the execution half of spot testing) in `Genomic_And_Phage_Work.docx`. Steps 18–20 prep half are still in the source but orphaned. Team never executed any of it. Replaced in the project pipeline by [[plaque_assay_layered_plate]] as the sole phage-screening method.
