---
title: Revive Bacteria from −80 °C Glycerol Stock
type: technique
purpose: Recover a banked bacterial strain from its −80 °C glycerol stock by streaking onto LB agar, producing fresh single-colony plates for downstream culture and plate work.
references:
  - "[[glycerol_stock_storage]]"
  - "[[three_phase_streak]]"
  - "[[lb_agar]]"
  - "[[single_colony_inoculation]]"
source:
  - lab_notebook/digitalized/2026-06-01_lb-agar-phage-buffer.md
estimated_time: ≈ 2 min per stock streaked + overnight incubation
---

# Revive Bacteria from −80 °C Glycerol Stock

## Purpose
Bring a strain back from cryo-archive: take a −80 °C glycerol stock (banked via [[glycerol_stock_storage]]), scrape a small amount **without fully thawing the tube**, and streak it onto an [[lb_agar]] plate to grow fresh isolated colonies. The revived plates feed downstream liquid culture ([[single_colony_inoculation]]) and plate-based work (e.g. lawns for plaque assay). This is the reverse of [[glycerol_stock_storage]] — that protocol freezes a culture down; this one brings it back up.

## Materials & equipment
- LB agar plates (1.0 %) — see [[lb_agar]]. The 6-1 run used **8 mL** plates.
- Ice bucket (to keep stocks cold during transit and while scraping)
- Inoculation loops or sterile pipette tips — one per stock (avoid cross-contamination)
- Bunsen burner (for flame sterilization between streak blocks, if using reusable loops)
- Marker for plate labels

## Reagents
- −80 °C glycerol stock(s) of the strain(s) to revive — output of [[glycerol_stock_storage]]
- LB agar plates — see [[lb_agar]]

## Procedure
1. Take the glycerol stock(s) out of the −80 °C freezer and place them **directly in an ice bucket** — keep them cold; do **not** let them thaw fully.
2. Label each LB agar plate with the **stock ID** (`sample_site.duplicate.plate_half` format — see [2026-05-22](../../../lab_notebook/digitalized/2026-05-22_streak-test-trial.md) for the label convention) and the **date**, on the bottom edge.
3. With a sterile loop (or pipette tip), **scrape a small amount of frozen culture from the surface** of the stock — do not melt the whole tube.
4. Return the stock to the −80 °C freezer **immediately** while there is still material on it (never thaw-and-refreeze a glycerol stock — see [[glycerol_stock_storage]] Notes).
5. Streak the scraped material onto the LB agar plate. Use the three-phase streak method ([[three_phase_streak]]) if you want isolated single colonies; a simple lawn streak is fine if you only need bulk growth.
6. Replace the lid and incubate (see Checklist).

## Notes / common deviations
- **As-run record (6-1).** On [2026-06-01](../../../lab_notebook/digitalized/2026-06-01_lb-agar-phage-buffer.md) (Procedure ③) the team revived **10 stocks** — `8-2-2`, `10-9-2`, `9-6-2`, `8-3-2`, `10-10-2`, `8-5-1`, `9-2-1`, `9-2-2`, `8-5-2`, `6-3-2` — streaking each onto one of the **8 mL** LB agar plates made the same day (Procedure ④, 10 plates total).
- **Don't thaw the stock.** Pulling and refreezing degrades viability; scrape from the surface and return to −80 °C right away. (Carried over from [[glycerol_stock_storage]].)
- **One loop/tip per stock** to avoid cross-contaminating strains.
- `[TBD: incubation temperature & time — not recorded in the 6-1 entry. Project default for bacterial plates is 30 °C overnight, inverted (see [[three_phase_streak]] / [[plaque_assay_layered_plate]]). Confirm with the team.]`
- `[TBD: how much frozen material to scrape — the 6-1 entry doesn't specify. A small loopful is typical.]`

## Checklist — where do the outputs go?
- [ ] Streaked revival plates → **30 °C incubator**, inverted (lid on bottom). `[TBD: confirm temp/time.]`
- [ ] Glycerol stocks → back to **−80 °C freezer** immediately after scraping.
- [ ] After overnight growth + inspection → **4 °C fridge**, sealed, until colonies are picked ([[single_colony_inoculation]]) or used for plate work.
- [ ] Contaminated / failed plates → [[media_disposal]].

## Source
- Lab notebook: [2026-06-01](../../../lab_notebook/digitalized/2026-06-01_lb-agar-phage-buffer.md) (Objective 3 + Procedure ③ "Streak bacteria stock", and ④ for the 8 mL plate prep).
- Label convention: [2026-05-22](../../../lab_notebook/digitalized/2026-05-22_streak-test-trial.md).

---
## Log
- 2026-06-08 — Initial draft from the 6-1 lab-notebook entry (Procedure ③). Fills a gap: the revival direction (−80 stock → streak → fresh plates) previously had no dedicated protocol — only the freezing direction ([[glycerol_stock_storage]]). Incubation temp/time and scrape amount left as `[TBD]` (not recorded on 6-1).
