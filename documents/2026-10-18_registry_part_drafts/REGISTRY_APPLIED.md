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

`BBa_26LHLSLW`'s **Functional Description was already updated by Alex** before this
session and was left alone.

## Not applied - needs a human

Editing a part's **Functional Description** means pressing **Save Part**, and that
form will not submit unless the **Contributor License Agreement** box is ticked:
*"I am the original author ... the information provided is accurate ... this
submission will become part of the permanent scientific record ... I agree to the
Contributor License Agreement."* That is a declaration the team makes, so it was
left unticked and these two edits are **outstanding**:

- **`BBa_26TWEX42` (Node1)** - replace the closing sentence
  *"Expression has not been confirmed; see the documentation entries."* with:
  > Anti-His dot blot on 2026-10-19 gave a positive signal for this construct's induced lysate, at 2.4 times the negative control; the product has not been assigned by size. See the documentation entries.
- **`BBa_26EK89VW` (Node40)** - the existing sentence is not wrong; this only
  strengthens it from an isolated negative to a like-for-like one:
  > Expression has not been demonstrated: on the 2026-10-19 anti-His dot blot this construct gave no signal on a membrane where two sibling constructs were positive. See the documentation entries.

## Before Send for Screening

Sequence, authorship and licence lock permanently. Confirm on each of the six that
the licence reads **CC0 1.0 Universal**, and that every author including the PI has
opted in and signed the CLA - authorship cannot be edited once a part leaves Draft.

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
