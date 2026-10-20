# Registry part IDs — entered 2026-10-18

**All six were sent for screening on 2026-10-20 and the API now reports every one as
`published`.** Sequence, authorship and licence are locked. Everything below from "Decisions
still open" is kept as the record of how they were settled, not as a to-do list.

Six parts created on registry.igem.org 2026-10-18, entered as **Draft**.
Each carries the five documentation entries (design / experiment / characterisation /
application / discussion) written from
[`2026-10-18_registry_part_drafts/`](2026-10-18_registry_part_drafts/).

| Part | Registry ID | URL |
|---|---|---|
| CDS12_WT — Phi8 GH5 glycoside hydrolase (CDS_0012 res 117–477) | `BBa_267WQM51` | https://registry.igem.org/parts/bba-267wqm51 |
| CDS11_WT — tail-spike β-helix depolymerase body (CDS_0011 res 305–941) | `BBa_26DKNAEC` | https://registry.igem.org/parts/bba-26dknaec |
| CDS10_WT — virion fiber, unknown function (CDS_0010 res 105–917) | `BBa_269KJB8G` | https://registry.igem.org/parts/bba-269kjb8g |
| CDS12_ANC_Node1 — `Phi8-GH5-ancN1` | `BBa_26TWEX42` | https://registry.igem.org/parts/bba-26twex42 |
| CDS12_ANC_Node40 — `Phi8-GH5-ancN40` | `BBa_26EK89VW` | https://registry.igem.org/parts/bba-26ek89vw |
| CDS12_ANC_Node281 — `Phi8-GH5-ancN281` | `BBa_26LHLSLW` | https://registry.igem.org/parts/bba-26lhlslw |

Common fields as entered: role **CDS** (`SO:0000316`), topology **Linear**, composition
**Basic Part**, host organism **_Escherichia coli_** (species, txid562), licence
**CC0 1.0 Universal** (see the licence note below — this is *not* the form default),
authors Chun-Yu Chen, Xiaokuan Wang, Yan Yan, Julio Cesar Ignacio Espinoza
with CRediT roles (PI: Conceptualisation · Methodology · Supervision). Sequences are the
`ATG` + own CDS + stop versions from `registry_parts.ffn`; no vector leader, no CDS11 linker.

## Decisions still open before *Send for Screening*

Sequence, authors and licence lock permanently at screening, and authorship can only be edited
while the part is in Draft.

- **His6 policy — DECIDED 2026-10-18: the tag is *not* part of any part.** The vector's
  N-terminal `MGSSHHHHHHSSGLVPRGSHM` leader stays out of all six sequences, and no part carries
  a C-terminal tag. Every draft and the collection page state this. Nothing to change on the
  entered sequences — they were already submitted this way.
- **Licence — SETTLED 2026-10-19: CC0 1.0 Universal, confirmed by Alex.** Verified on the live
  page for `BBa_26LHLSLW`, which reads "Creative Commons Zero v1.0 Universal". The recommendation
  below was taken. Licence locks permanently at screening, so confirm the field reads CC0 on each
  of the six before *Send for Screening*. Original reasoning: (1) a part is a DNA
  sequence, and CC BY's attribution requirement is unenforceable and awkward once a sequence is
  copied into someone else's construct, which is why CC0 is the norm for biological parts;
  (2) it removes any licence-compatibility question for a team that wants to combine our parts
  with theirs; (3) judges read maximal openness as a contribution, and we lose nothing — the
  Attributions form and the part page credit us regardless. (The form did offer CC0, so the
  CC BY 4.0 fallback this note once described never applied.) **This is separate from the
  repository's code licence**, which must become OSI-approved (MIT or Apache-2.0) for Best
  Software; CC BY 4.0 does not qualify there.
- **Two UNDONE fields in each ancestral part** — RESOLVED 2026-10-18 from the PI's handover.
- ~~**Licence — reported changed to CC0, not independently verified.**~~ **Closed 2026-10-19:**
  verified on `BBa_26LHLSLW`'s live page and confirmed by Alex. All six should read CC0 1.0.
- **Collection page** — drafted 2026-10-18:
  [`2026-10-18_registry_part_drafts/COLLECTION.md`](2026-10-18_registry_part_drafts/COLLECTION.md)
  (中文：`COLLECTION_zh.md`). **Created on registry.igem.org 2026-10-19**, UUID
  `3edc6bca-7c2b-4c01-b38f-c6ed3b6743ad`
  (registry.igem.org/collections/3edc6bca-7c2b-4c01-b38f-c6ed3b6743ad), curated by Chun-Yu Chen
  under Claremont CA (2026). All five documentation entries are live: Design "Why these six
  parts are one set", Experiment "Cloning, expression trials and the first spot test",
  Characterisation "One activity signal, and what it is not yet attributed to", Application
  "How to reuse this collection", Discussion "What this set does and does not yet show".
  **Parts list filled 2026-10-20** — all six are in the collection, verified through
  `api.registry.igem.org/v1/parts/collections/<uuid>/items` (6 items, each `published`).

## Documentation to re-paste on registry.igem.org

The *characterisation* entry of four parts was rewritten on 2026-10-18 with the
**2026-10-16 spot test** result ([`../code/1016_spot_test_result.ipynb`](../code/1016_spot_test_result.ipynb),
figure in `code/output/1016_spot_test_result/`). The live pages still carry the earlier text,
so each has to be edited on registry.igem.org. Documentation is editable while a part is in
Draft; only sequence, authorship and licence lock at screening.

| Part | Registry ID | What changed in *characterisation* |
|---|---|---|
| CDS12_ANC_Node1 (`e1`) | `BBa_26TWEX42` | "None yet" → first activity data: colony growth inside the drop suppressed almost as completely as by phage Φ8 (median 1 vs 14 for the sterile-PBS control), on 6 of 7 strains |
| CDS12_ANC_Node40 (`e40`) | `BBa_26EK89VW` | "None" → crude lysate gave only a slight reduction (median 10 vs 14); not evidence of inactivity |
| CDS12_ANC_Node281 (`e281`) | `BBa_26LHLSLW` | "None" → same, median 9 vs 14 |
| CDS12_WT | `BBa_267WQM51` | adds that the wild type was **not** in this run and is the missing ancestor-versus-modern comparator |

Three further edits came out of the 2026-10-18 team review of the live pages:

| Part | Registry ID | What changed |
|---|---|---|
| CDS10_WT | `BBa_269KJB8G` | *design*: the sentence "…and that is why the protein is being expressed" did not follow from what precedes it. Rewritten so the reason is explicit: the function of a tail-module protein with no structural template can only be settled experimentally. The rest of that paragraph stays — the withdrawn glycosidase call is worth recording. |
| CDS11_WT | `BBa_26DKNAEC` | *characterisation*: dropped the "we report this honestly, as the Registry asks" framing, which reads as filler. Added that the 2026-10-16 spot test covered only the three ancestral variants and **not** this part, so the planned assay is still only planned. |
| CDS12_WT | `BBa_267WQM51` | *characterisation*: same filler sentence removed. |

**On "planned" entries:** a planned readout is a statement of intent, not a commitment to
upload a follow-up. Nothing has to be added later for those sentences to stay accurate. What
*would* need an edit is a planned assay that has since been run — which is why CDS11_WT now
says explicitly that it was not in the 2026-10-16 run.

**Wording that must survive the paste:** the active agent is **not** claimed to be the protein.
Expression is still unconfirmed, and the imidazole elution buffer was never spotted on its own,
so the vehicle control is outstanding.

---
*Log — 2026-10-18: parts entered on registry.igem.org from the drafts; drafts left unsent.*
*Log — 2026-10-20: all six sent for screening and now `published`, updated between 07:12 and
07:27 UTC. Verified through `api.registry.igem.org/v1/parts?search=<id>`. All six share
`licenseUUID 5b2a6fd4-f5fa-4626-a37f-35f1ea89eec7`, the licence the live page for
`BBa_26LHLSLW` shows as CC0 1.0 Universal, which closes the last pre-screening item. The
collection was updated at 07:33 and its parts list now holds all six. **Not verified:** whether
the collection's five documentation entries carry the post-dot-blot text from
`2026-10-18_registry_part_drafts/paste/COLLECTION.md` — the API exposes no documentation
endpoint for collections and the browser extension was offline, so that one needs an eyeball.*
