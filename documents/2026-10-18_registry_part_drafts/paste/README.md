# paste/ - the text to put into the Registry

One file per part. **This is the only directory to copy from when filling
registry.igem.org.** Everything here is plain ASCII: no Greek letters, no en or em
dashes, no `%` sign, no markdown bold - matching the convention the live pages
already use, so nothing turns into mojibake in the form.

Each file holds the Functional Description, then the five documentation entries
with the **title** to use for each.

[`COLLECTION.md`](COLLECTION.md) is the seventh file: the collection page, same
convention, added 2026-10-20. It is built from the six part files above rather
than from a live page, because the collection does not exist on the Registry yet.

## Where this came from

Base is the **live Registry text, harvested 2026-10-19** (kept verbatim in
`../live_snapshot_1019/`), not the drafts in the parent directory. The live pages
had been rewritten by Alex and another session into flowing ASCII prose and were
ahead of the drafts in wording, so overwriting them from the drafts would have
thrown that work away.

Onto that base, the 2026-10-19 anti-His dot blot was merged in the same prose
style. Nothing else was touched.

## What changed per part

| part | Functional Description | documentation | titles |
|---|---|---|---|
| `CDS12_ANC_Node281` | yes | experiment, characterisation | **both changed** |
| `CDS12_ANC_Node1` | yes | experiment, characterisation, discussion | - |
| `CDS12_ANC_Node40` | yes (strengthened, was not wrong) | experiment, characterisation, discussion | - |
| `CDS12_WT` | no | experiment, characterisation, discussion | - |
| `CDS11_WT`, `CDS10_WT` | no | **unchanged** - verbatim live text | - |

`CDS11_WT` and `CDS10_WT` were not on the 2026-10-19 membrane, so their files are
the live text copied through unaltered, present only so one directory holds all six.

## Induction temperature - corrected 2026-10-19

Every one of the six pages said **IPTG induction at 16-20 C**. That number is the
**DepoCatalog paper's recommendation**, recorded in
`../../2026-09-21_depocatalog_paper_reading_notes.md`, not a condition we ran. Per
Alex it is **~30 C**, and that is what these files now say. This is the one change
that touches all six parts, `CDS11_WT` and `CDS10_WT` included.

Two things to know:

- `CDS10_WT` has never been expressed; its sentence reads "IPTG induction at ~30 C
  **planned**". It was changed for consistency - revert it to 16-20 C if the plan
  for that part really is the low-temperature condition.
- The lab notebook does not agree with ~30 C either. The 2026-09-10 entry records
  the cultures going back into a **37 C** incubator, twice, and the 09-15 and 09-27
  inductions have no temperature written down at all. `~30 C` is Alex's figure, and
  it is the one on these pages; the notebook discrepancy is left standing rather
  than quietly reconciled.

`live_snapshot_1019/` deliberately still reads 16-20 C - it is the verbatim record
of what the live pages said on 2026-10-19, and the live pages still need this fix.

## Applied status

These files are no longer a to-do list for the documentation entries: all thirteen
were applied to the live Registry on 2026-10-19 and verified by reading them back
through the API. What is still outstanding is the **Functional Description** on two
parts, which cannot be saved without ticking the Contributor License Agreement.
See [`../REGISTRY_APPLIED.md`](../REGISTRY_APPLIED.md) for the per-entry record.

## Not in these files

The parent directory's drafts keep the `==CONFIRM==` / `==UNDONE==` markers, the
reasoning and the Chinese versions. Those are the working record and are
deliberately **not** reproduced here, because they must not be pasted into the
Registry.

---
*Log - 2026-10-19: built from the live snapshot plus the dot blot. Licence settled
as CC0 1.0 on all six; sequence, authorship and licence still lock permanently at
Send for Screening.*
