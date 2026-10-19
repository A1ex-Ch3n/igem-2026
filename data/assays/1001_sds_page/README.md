# 2026-10-01 SDS-PAGE — first His-tag purification

Two gels run on 2026-10-01, with the fractions from the NEBExpress Ni spin column
purification described in `lab_notebook/digitalized/2026-10-01_protein-purification.md`.

| File | Gel | Constructs |
|---|---|---|
| `gel1_cds11-cds12-e1-e281_annotated.jpeg` | Gel 1 | CDS11, CDS12, e1, e281 — FT / E1 / E2, with Bradford A595 per lane |
| `gel2_cds10-e40_annotated.jpeg` | Gel 2 | CDS10, e40 — Raw / Raw 1:2 / W3 / E1 / E2, no Bradford |

Both files are **annotated composites**, not raw gel photographs: the lane map, the dashed
expected-size boxes and the tables are overlaid on the photo. They arrived by WhatsApp on
2026-10-01 at 16:54. The raw photographs are not in the repo, and the annotation was not
produced by anything under `code/` — unlike `0915` / `0929` / `1010`, there is no
`*_lane_quant.tsv` and no ladder calibration behind these numbers.

## What the gels show

**Gel 1 — the only purification of the project with eluted protein.**
- `e1` E1 and E2: bands at ~41 kDa against an expected 41.9 kDa. This one matches.
- `CDS11` E1 and E2: bands at ~43 kDa against an expected **72.0 kDa**. Something eluted, but
  it is roughly 29 kDa smaller than the construct. Degradation, a truncation, or a co-purifying
  contaminant are all still open; the gel alone does not settle it.
- `CDS12` and `e281`: no bands in either elution.
- Bradford, BSA quadratic curve (R² = 0.998, 125–1500 µg/mL): e1 E1 above the top standard
  (>1,500 µg/mL, needs dilution and a re-read); CDS12 E2 and e281 E2 below the LLOQ.

**Gel 2 — nothing eluted.** `CDS10` and `e40` give lysate bands in Raw and Raw 1:2, and nothing
at the expected size in W3, E1 or E2. The gel corner at lanes 10–12 tore near the wells; the
resolving region of every lane is intact.

This 10-01 result is what the 10-10 `e281` Ni-NTA run was meant to follow up, and that run
failed outright — see `code/1010_gel_annotation.ipynb`.
