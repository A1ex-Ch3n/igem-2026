# MRA00793-26 — revision

Decision letter 2026-07-31 (Annette Rowe, editor), forwarded by Cesar 2026-08-01.
**60 days → resubmit by roughly 2026-09-29.**

| File | What it is |
|:--|:--|
| `decision_letter.pdf` | The decision letter and both reviewer reports, as forwarded |
| `manuscript_submitted.docx` / `.pdf` | The manuscript **as submitted** — line-numbered; every reviewer comment cites these line numbers |
| `manuscript_revised.docx` | The revision. Produced by editing `manuscript_submitted.docx` in place, so the formatting is the journal file's own |
| `response_to_reviewers.md` | **The specification.** Point-by-point responses above a `NOT FOR SUBMISSION` divider; internal notes, open questions and the word budget below it |
| `response_to_reviewers.docx` | The submission copy, rendered from the `.md` and stopping at the divider |
| `response_to_reviewers_alex_first_draft.docx` | Alex's own opening paragraph, 2026-08-08, superseded |
| `workplan.md` | How the revision was scoped: the four blockers, the evidence for each reviewer point, and where each fact came from |

Generators: `code/0809_patch_mra_manuscript.py` and `code/0809_response_letter_to_docx.py`.
Both are **provenance only** — each rebuilds its output from scratch, so re-running
after a hand edit in Word silently discards it.

## State

Three isolates: **8-5-2, 9-2-1, 8-10-2**. Assemblies public as GCA_059295255.1,
GCA_059295275.1 and GCA_059295235.1 (BioProject PRJNA1482863); reads under
PRJNA1483221. Revised Announcement is 494/500 words, abstract 47/50.

**One blocker.** Table 1's read count for 8-10-2 (546,337 / 3,220 Mb) is roughly
double the deposited run SRR39379360 (272,751 / 1,530 Mb), while the other two
isolates match theirs to the base pair. Those three cells are highlighted
`[PENDING]` in `manuscript_revised.docx` and the question to Cesar is drafted at
the end of `response_to_reviewers.md`.

Before submitting, work the checklist at the end of `response_to_reviewers.md` —
in particular, delete the highlighted working note from the manuscript, clear the
yellow highlighting, and produce the marked-up file with Word → Review → Compare
(`manuscript_submitted.docx` against `manuscript_revised.docx`).

---

*Log: 2026-08-09 — Folder created when the revision files were consolidated out of the repo root and `documents/`. Previous names: `review_manuscript.pdf` → `decision_letter.pdf`; `MRA00793-26-Manuscript_Text_File.{docx,pdf}` → `manuscript_submitted.{docx,pdf}`; `2026-08-09_MRA00793-26_Manuscript_REVISED.docx` → `manuscript_revised.docx`; `2026-08-08_MRA_response_to_reviewers_FLAT.md` → `response_to_reviewers.md`; `2026-08-09_MRA00793-26_Response_to_Reviewers.docx` → `response_to_reviewers.docx`; `(CHEN)Response_to_Reviewers.docx` → `response_to_reviewers_alex_first_draft.docx`; `2026-08-08_mra_revision_workplan.md` → `workplan.md`. References were rewritten in both generator scripts and both markdown files, and each generator re-run against the new paths to confirm.*
