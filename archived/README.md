# Archived

Materials that were once part of the active iGEM 26 project but have since been superseded, deprecated, or otherwise removed from the working set. **Content is preserved here as historical reference** — do not run protocols stored here without checking why they were archived.

Each entry below records: file, when it was archived, where it came from, and the reason. Files are stored flat (no subfolder structure) — provenance lives in this README rather than in folder paths.

## Index

| Archived on | File | Original location | Reason |
|---|---|---|---|
| 2026-06-06 | [`phage_amplification.md`](phage_amplification.md) | `protocol/md/workflows/phage_amplification.md` | Prof updated `protocol/Genomic_And_Phage_Work.docx` on/before 2026-06-06 and **crossed out steps 15–17** (Enrichment Set-Up + Incubation + Daily phage Sampling) — i.e., the entire host-amplification + daily-sampling routine this protocol was drafted from. The team had **never executed** this protocol (it was a prof-only draft). The simplified phage pipeline now goes `[[soil_enrichment_phage]] → [[phage_isolation]] → [[plaque_assay_layered_plate]] → [[phage_purification]]` with no in-host amplification step. |
| 2026-06-06 | [`spot_testing.md`](spot_testing.md) | `protocol/md/workflows/spot_testing.md` | Prof crossed out **steps 21–26** of `Genomic_And_Phage_Work.docx` (the entire execution half of spot testing — Pouring Lawn → Solidification → Spotting → Absorption → Incubation → Evaluation). Steps 18–20 prep are still in the source doc but orphaned. The team had **never executed** any of it. Replaced in the project pipeline by [[plaque_assay_layered_plate]] as the team's screening method. |

## Conventions

- **Keep content intact.** Files moved here should arrive in the same state they were last in — including the `[!failure] DEPRECATED` callouts that explain why they were retired. Don't edit the archived files except to clarify the deprecation reason.
- **Update references when archiving.** If the active project (`protocol/md/`, `lab_notebook/digitalized/`, `scheme/`) had `[[wiki-link]]` references to the now-archived file, update those active files to either (a) drop the reference, or (b) annotate it as `[[name]] (archived 2026-MM-DD)` so a reader knows where to find it.
- **Don't re-import without a fresh review.** If circumstances change and an archived protocol becomes relevant again, copy it back into the active tree and re-validate against current sources — don't just `mv` it back.

---
## Log
- 2026-06-06 — Folder created. Seeded with 2 protocols deprecated after the prof's 2026-06-06 update to `Genomic_And_Phage_Work.docx`.
