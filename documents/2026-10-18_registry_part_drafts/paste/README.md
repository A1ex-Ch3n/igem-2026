# paste/ - the text to put into the Registry

One file per part. **This is the only directory to copy from when filling
registry.igem.org.** Everything here is plain ASCII: no Greek letters, no en or em
dashes, no `%` sign, no markdown bold - matching the convention the live pages
already use, so nothing turns into mojibake in the form.

Each file holds the Functional Description, then the five documentation entries
with the **title** to use for each.

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

## Not in these files

The parent directory's drafts keep the `==CONFIRM==` / `==UNDONE==` markers, the
reasoning and the Chinese versions. Those are the working record and are
deliberately **not** reproduced here, because they must not be pasted into the
Registry.

---
*Log - 2026-10-19: built from the live snapshot plus the dot blot. Licence settled
as CC0 1.0 on all six; sequence, authorship and licence still lock permanently at
Send for Screening.*
