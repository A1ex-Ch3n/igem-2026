# Live Registry edits still to make - 2026-10-20

The six parts are `published`. **Documentation stays editable**; only sequence, authorship and
licence locked at screening. So everything below can still be fixed.

All of it comes from one finding: `lab_notebook/digitalized/2026-10-01_protein-purification.md`
and `data/assays/1001_sds_page/README.md` record a **Ni-NTA round over all six constructs on
2026-10-01**, two gels, which the Registry text never accounted for. `e1` eluted at about
41 kDa against 41.9 kDa predicted. The 2026-10-10 `e281` run was the **second** round, not the
only one.

Ranked. The first one is the part nominated for Best New Basic Part. **Five of the six pages are
affected** - every part except node 1 was on a 10-01 gel and none of them said so.

**Two of these need the Save Part form**, which cannot be submitted without ticking the
Contributor License Agreement, so Alex has to do them: the Functional Descriptions of node 1 and
node 281. Everything else is a documentation entry and can be edited directly.

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

## 2 - `BBa_26LHLSLW` Node281 - two purifications, not one

*Functional Description* (needs the Save Part form and the CLA tick, so Alex must do this one):
"One purification of this construct was attempted and failed" becomes "Two purification
attempts, on 2026-10-01 and 2026-10-10, both recovered nothing".

*Experiment*: new title `Cloning, two Ni-NTA purifications that recovered nothing, and the dot
blot that explains them`, and the opening sentence "This is the only construct of the six we
have attempted to purify" is replaced by the 10-01 and 10-10 account.

*Characterisation*: "The Ni-NTA attempt on 2026-10-10 recovered nothing" becomes "Neither
Ni-NTA attempt, on 2026-10-01 or 2026-10-10, recovered anything".

*Discussion*: "one purification attempt failed outright" becomes "Two purification attempts
recovered nothing".

*Design*: the two PI placeholders are replaced by the node ordering and the reconstruction
method.

## 3 - `BBa_26DKNAEC` CDS11_WT - it did elute something

*Experiment*: three SDS-PAGE sessions becomes four, and a 10-01 paragraph is added: this
construct eluted bands in E1 and E2 at about 43 kDa, roughly 29 kDa short of its predicted
72.0 kDa.

*Characterisation*: "No confirmed expression, no purified protein, and therefore no activity
assay" is replaced, because something did elute - it simply was not the construct as designed.

## 4 - `BBa_26EK89VW` Node40 - it has a gel after all

*Experiment*: new title, the predicted mass line, and the 10-01 paragraph. The old text said
"No usable lane has been run since" 2026-09-15; in fact this construct ran on the second 10-01
gel as crude lysate, 1:2, wash 3 and both elutions, with nothing at the expected 42.2 kDa.

*Discussion*: "not even a readable gel lane for this construct" is replaced for the same reason.

*Design*: the two PI placeholders are replaced.

## 5 - `BBa_269KJB8G` CDS10_WT - same omission

*Experiment*: new title, and "No gel to date carries an interpretable lane for it" is replaced
by the 10-01 paragraph; nothing at the expected 91.6 kDa in wash 3 or either elution.

*Characterisation*: "No expression, no purification, no activity data" becomes "Expression is
unconfirmed, the one purification attempt recovered nothing".

## 6 - `BBa_267WQM51` CDS12_WT - purification is no longer "not yet done"

*Experiment*: "Not yet done: ... Ni-NTA purification of this construct" was false. The 10-01
paragraph is added - no band in either elution, Bradford E2 below the limit of quantification -
and the to-do list now reads "a second purification attempt with reworked binding conditions".

*Characterisation*: "No purified protein, therefore no activity data" gains "was recovered on
2026-10-01".

## Not a Registry edit, but the same finding

`COLLECTION.md` and `paste/COLLECTION.md` said "no purified protein exists". Corrected
2026-10-20. The collection page's five entries on registry.igem.org are the pre-dot-blot text
and need replacing from `paste/COLLECTION.md` anyway; that replacement now carries the
two-rounds correction as well.

---
*Log - 2026-10-20: written after the 10-01 gel turned up while checking a date on the wiki's
`/parts` page. The wiki had it right - "the 10-01 gels show e1 eluting at its predicted mass" -
and the Registry text did not.*
