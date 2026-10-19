# Registry part IDs — entered 2026-10-18

Six parts created on registry.igem.org, all **Draft**, none sent for screening.
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
**Basic Part**, host organism **_Escherichia coli_** (species, txid562), licence **CC BY 4.0**
(the form default), authors Chun-Yu Chen, Xiaokuan Wang, Yan Yan, Julio Cesar Ignacio Espinoza
with CRediT roles (PI: Conceptualisation · Methodology · Supervision). Sequences are the
`ATG` + own CDS + stop versions from `registry_parts.ffn`; no vector leader, no CDS11 linker.

## Decisions still open before *Send for Screening*

Sequence, authors and licence lock permanently at screening, and authorship can only be edited
while the part is in Draft.

- **Licence** — left at the default CC BY 4.0 on all six. Change it now if the team wants
  CC0 / MIT / Apache-2.0.
- **His6 policy** — the drafts assume the tag is *not* part of the part. Confirm.
- **Two UNDONE fields in each ancestral part** — the reconstruction program, alignment and tree,
  and where nodes 1 / 40 / 281 sit on that tree. Both are flagged in the *design* entry of each
  ancestral part as "still to be filled in by the PI".
- **Collection page** for the six parts as one toolbox — not created.

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

CDS10_WT and CDS11_WT were not spotted; their pages are unchanged.

**Wording that must survive the paste:** the active agent is **not** claimed to be the protein.
Expression is still unconfirmed, and the imidazole elution buffer was never spotted on its own,
so the vehicle control is outstanding.

---
*Log — 2026-10-18: parts entered on registry.igem.org from the drafts; drafts left unsent.*
