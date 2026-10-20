# What has actually been applied to registry.igem.org

Status as of **2026-10-19**, after the edit session that followed the dot blot.
Every line below was verified by reading the part back through
`api.registry.igem.org/v1/parts/<uuid>/documentation`, not by trusting the editor.

All six parts are still **`draft`**. Nothing has been sent for screening.

## Applied and saved

| part | entry | what changed |
|---|---|---|
| `BBa_269KJB8G` CDS10_WT | experiment | induction temperature -> `~30 C` |
| `BBa_26DKNAEC` CDS11_WT | experiment | induction temperature -> `~30 C` |
| `BBa_267WQM51` CDS12_WT | experiment | temperature, the dot blot paragraphs, and `anti-His western` -> `size-resolved anti-His western` |
| | characterisation | adds that this part was not in the 2026-10-16 spot test, so the ancestor-versus-modern comparison has no modern arm |
| | discussion | the 2026-10-19 blot did not reproduce an induction-dependent signal |
| `BBa_26TWEX42` Node1 | experiment | temperature + dot blot; lysate His-positive at 2.4x |
| | characterisation | "expression still unconfirmed" -> expression now has positive evidence |
| | discussion | limitations rewritten; the 45-50 kDa band is still unassigned |
| `BBa_26EK89VW` Node40 | experiment | temperature + dot blot; no signal either time |
| | characterisation | adds the no-signal result |
| | discussion | now a like-for-like negative, not an isolated one |
| `BBa_26LHLSLW` Node281 | experiment | temperature + dot blot; **capture failed, not expression** |
| | characterisation | expression supported, but the spot test used the 1:10 lysate |
| | **titles** | experiment -> "Cloning, a failed Ni-NTA purification, and the dot blot that explains it"; characterisation -> "First activity data, and anti-His evidence that the protein was expressed" |

## Functional Descriptions - all three applied

All three Functional Descriptions that needed the dot blot now carry it, applied by Alex through
the **Save Part** form and verified here by reading each part back through the API on 2026-10-19:

| part | closing sentence now reads |
|---|---|
| `BBa_26TWEX42` Node1 | anti-His dot blot gave a positive signal for the induced lysate at 2.4x the negative control; the product has not been assigned by size |
| `BBa_26EK89VW` Node40 | expression has not been demonstrated: no signal on a membrane where two sibling constructs were positive |
| `BBa_26LHLSLW` Node281 | the purification failed, but the flow-through was positive at 2.9x, so the protein was expressed and did not bind the resin |

That form cannot be submitted without ticking the **Contributor License Agreement**, which is a
declaration the team makes, so these three were done by Alex rather than automated.

**Authorship is confirmed correct** (Alex, 2026-10-19). It can only be edited while a part is in
Draft, so nothing further is needed there.

## Nothing has been reverted

The thirteen documentation edits and both renamed Node281 entries were re-read through the API
after the Functional Description round, to rule out one edit session overwriting another. All
thirteen are intact and no entry still carries the old `16-20 C`.

## Before Send for Screening

Sequence, authorship and licence lock permanently. **Authorship is confirmed.** The one item left
to eyeball is that the licence reads **CC0 1.0 Universal** on each of the six - the API does not
expose the licence field, so it can only be checked in the web interface.

## Note on method

The Registry body editor is rich text, so edits were made by selecting a paragraph
and retyping it rather than by character surgery, which misfired three times early
on (`CDS10`, `CDS11`, and the Node1 Functional Description, where a selection ran to
the start of the field and truncated it). Each was caught and repaired in the same
session, and every entry above was then read back through the API to confirm. The
`~30 C` figure is Alex's; the notebook records 37 C on 2026-09-10 and nothing for the
09-15 and 09-27 inductions, and that disagreement is recorded in `paste/README.md`.

---
*Log - 2026-10-19: written after applying the dot blot to the live Registry pages.*
*Log - 2026-10-19 (later): all three Functional Descriptions applied by Alex and verified; the
thirteen documentation entries re-checked and intact; authorship confirmed. The only pre-screening
item left is the licence field.*
