# Live Registry edits still to make - 2026-10-20

The six parts are `published`. **Documentation stays editable**; only sequence, authorship and
licence locked at screening. So everything below can still be fixed.

All of it comes from one finding: `lab_notebook/digitalized/2026-10-01_protein-purification.md`
and `data/assays/1001_sds_page/README.md` record a **Ni-NTA round over all six constructs on
2026-10-01**, two gels, which the Registry text never accounted for. `e1` eluted at about
41 kDa against 41.9 kDa predicted. The 2026-10-10 `e281` run was the **second** round, not the
only one.

Ranked. The first one is the part nominated for Best New Basic Part.

---

## 1 - `BBa_26TWEX42` Node1 - add the elution (G1 part, do this first)

Three changes, all in `CDS12_ANC_Node1.md` in this directory, ready to copy.

**a. Functional Description** - replace the closing sentence. It now reads:

> It is the only one of our six constructs that eluted from a Ni-NTA column at its predicted
> size, at about 41 kDa against 41.9 kDa predicted on 2026-10-01, and an anti-His dot blot on
> 2026-10-19 gave a positive signal for its induced lysate at 2.4 times the negative control.
> No product has yet been assigned by size on a calibrated gel. See the documentation entries.

**b. Experiment** - new title, and three new paragraphs between the 2026-09-29 paragraph and
the dot-blot paragraph.

New title: `Cloning, the one Ni-NTA elution of the project, and an unassigned 45-50 kDa band`

The paragraphs cover: the 10-01 run and what each of the six did; the Bradford read that put E1
above the top standard; two cautions (the gels are annotated composites with no ladder
calibration and no lane-quantification table, so 41 kDa is a read-off, not a measurement; and
it does not reconcile with the 45-50 kDa band of 09-29); and that this eluate **is** the
`e1` preparation used in the 2026-10-16 spot test.

**c. Characterisation** - replace the "It does not identify the active agent" paragraph, which
now cites both the elution and the dot blot and says plainly that neither makes this protein
the active species.

## 2 - `BBa_26LHLSLW` Node281 - one false sentence

Its *experiment* entry says:

> This is the only construct of the six we have attempted to purify

**False.** All six were purified on 2026-10-01; this construct was among those that eluted
nothing, and the 2026-10-10 run was a second attempt on it alone. Suggested replacement:

> This construct was put over Ni-NTA twice. On 2026-10-01 it was one of six constructs purified
> in a single session and gave no band in either elution. The dedicated run of 2026-10-10
> failed outright.

The rest of that entry - the blank elutions, the prominence figures, the flow-through matching
the load - is accurate and should stay.

## 3 - `BBa_26DKNAEC` CDS11_WT - "no purified protein" is wrong

Its *characterisation* entry opens:

> None. No confirmed expression (see the Experiment entry), no purified protein, and therefore
> no activity assay.

Something did elute for this construct on 2026-10-01: a band at about 43 kDa, roughly 29 kDa
short of its predicted 72.0 kDa. That is not the protein as designed, but "no purified protein"
is not what the gel says. Suggested replacement:

> No activity assay. Expression of the full-length construct is unconfirmed: no band at the
> predicted 72.0 kDa in three gels, and this part was not on the 2026-10-19 dot-blot membrane.
> A Ni-NTA elution on 2026-10-01 did produce a band, at about 43 kDa, roughly 29 kDa short of
> the prediction and unexplained - degradation, a truncation and a co-purifying contaminant are
> all still open.

Its *experiment* entry should gain the same 10-01 line, since it currently stops at the three
SDS-PAGE sessions.

## Not a Registry edit, but the same finding

`COLLECTION.md` and `paste/COLLECTION.md` said "no purified protein exists". Corrected
2026-10-20. The collection page's five entries on registry.igem.org are the pre-dot-blot text
and need replacing from `paste/COLLECTION.md` anyway; that replacement now carries the
two-rounds correction as well.

---
*Log - 2026-10-20: written after the 10-01 gel turned up while checking a date on the wiki's
`/parts` page. The wiki had it right - "the 10-01 gels show e1 eluting at its predicted mass" -
and the Registry text did not.*
