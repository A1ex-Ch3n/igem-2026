# What is still not done — 2026-10-18

Built from the 2026-10-18 morning meeting transcript with Prof. Ignacio-Espinoza,
checked against what the repo actually contains. Ordered by deadline, not by size.

**Both of the PI's action items from that meeting are already delivered.** The
computational write-up is `2026-10-18_prof_documents/LooseEndsiGEM.docx` (A1–A3)
and Jasmin's letter is `2026-10-18_prof_documents/IBCReviewLetter.docx`. Nothing
is blocked on him for the 10/21 items — except the people/sponsor questions below.

**Verify the wiki freeze time before planning around it.** Everything below is
anchored to the Parts/Attributions freeze, 2026-10-21 08:00 PDT = 15:00 UTC.
The wiki and Safety Form deadlines were not confirmed in this session; check
`api.igem.org/v1/competitions/<uuid>/deliverables`.

---

## Tier 0 — today, 2026-10-18

**0.1 Chase the PI for the five unanswered questionnaire items.**
C1 (Weitao's affiliation), C2 (anyone else in the lab), C3 (Phoebe), D1 (Twist:
sponsorship or purchase), D4 (other sponsors). The Attributions Form freezes in
three days and these are the only fields we cannot write ourselves. The meeting
said sponsors are "none, maybe KGI" — that is an answer to D4 but it needs to come
from him in writing before we enter it.

**0.2 Unblock the six ancestral-part UNDONE fields — now answerable, no one blocking.**
Each of `CDS12_ANC_Node1/40/281.md` carries two UNDONE fields; today's handover
closes both:
- *Reconstruction method*: MUSCLE in SeaView over the top 1000 nr hits to CDS_12,
  manually curated; PhyML (WAG, p-inv fixed 0.1, 100 bootstraps); ancestral states
  in IQ-TREE, same WAG matrix, midpoint-rooted. Full text in
  `2026-10-18_pi_questionnaire_answers.md` A1.
- *How to name the node*: the labels are **arbitrary**, not tree depth. The
  authoritative order is 1, 2, 38, 39, 40, 42, 267, 277, 281, most recent to most
  ancestral. So e1 = nearest to the extant enzyme, e281 = deepest of the three we
  ordered. Say exactly that and nothing about "mid node".
- Sequences to check the drafts against: `code/1018_prof_asr_zymctrl/all_nodes.fa`.

**0.3 Prepare the IBC rationale for the PI (his deadline is 10/24, his revision
needs our data).** The one open IBC condition is a scientific rationale that the
work will not alter phage host range, bacterial virulence, or antibiotic
resistance. We hold the evidence: 0 VFDB and 0 CARD hits across the Φ8 genome
(`code/0708_phage_assembly`), the resistant-mutant WGS showing only a host-side
capsule-cluster SNP with the O-antigen untouched
(`2026-10-10_resistant_mutant_summary_for_PI.md`), and the meeting's own framing —
we express isolated proteins and do not engineer the phage genome. Half a page,
sent to him, is the highest-leverage thing we can do for him this week.

## Tier 1 — tomorrow, 2026-10-19

**1.1 The botanic garden interview happens tomorrow, Weitao conducts it.**
Required afterwards, same day: the interviewee's name, institution and what they
contributed, entered into External Contributions on the Attributions Form, and
the interview written up in the human-practices format below. One day of slack
before the freeze, so the write-up cannot wait until the 21st.

## Tier 2 — by 2026-10-21 freeze

**2.1 Human practices — the single largest gap. The repo contains no
human-practices document at all.** Five interactions are owed, each in the format
the PI asked for, *person → what was discussed → what changed as a result*:
- **Ilia** — how experimental plans were modified. The concrete change named in
  the meeting: moving away from purification and large-scale production toward
  smaller-scale experiments and targeted blots.
- **Ashley** — pathogen and health framing, project impact.
- **Jasmin** — the IBC review interaction and the specific question her letter
  raised. **Compliance caution from the meeting**: her revised document is not
  yet fully approved, so describe the interaction and the question, not an
  approval we do not have. We have conditional approval and no approval number.
- **Ren** — no detail captured in the transcript; needs reconstructing from
  whoever met them.
- **Botanic garden interview** (Tier 1).

**2.2 Registry parts — drafts are written, the parts are not submitted.**
All six drafts exist under `2026-10-18_registry_part_drafts/` with the seven
registry sections. Still outstanding:
- The six UNDONE fields from 0.2 written in.
- The **collection page** tying the six parts together — marked UNDONE in that
  folder's README, never started.
- The characterisation tier the PI asked for: AlphaFold models and their
  interpretation, **plasmid maps** showing how each part sits in pET-28a, and an
  explicit rationale for why these parts and what remains unknown. Plasmid maps
  do not exist anywhere in the repo.
- Actually creating the pages on the Registry. Drafts in git are not a submission.

**2.3 Wiki — no wiki content exists in this repository.** Everything below is
only on teams.igem.org, so it cannot be reviewed here:
- The software/modelling narrative, rewritten as *what we learned and how it
  changed direction*, not "we ran X". The worked example from the meeting: early
  AlphaFold / ESM3 / "Modimor" work indicated the key interaction is
  protein–sugar, not protein–protein, which reframed the system around a
  depolymerase and a sugar — and is why the RBP×OMP binding screen was retired.
  The PI's A1 text supplies the LLM half: an external model trained on large-scale
  metagenomics, our sequences scored against it, and more ancestral sequences
  scoring as more canonical.
- Figures. The meeting asked specifically for plate photographs, graphical
  abstract(s), and protein visuals tied to the simulations. The repo already holds
  usable material: `2026-10-18_prof_documents/iGEM_main_figure.pdf` (four panels),
  `phage_groupA.svg` (editable virion schematic),
  `2026-07-30_graphical_abstract_design.md`, and `photos/`.
- Links from the wiki to the code repository and the quantification notebooks.
  This is also what the Best Software entry needs — note the separate blocker
  recorded in `project_igem_submission_prep`: the CC BY 4.0 LICENSE is not an
  OSI-approved software licence.
- Negative results stated plainly as evidence of current limits — the meeting
  explicitly endorsed this. We have real ones: the failed e281 Ni-NTA
  purification, the retired binding screen, three inconclusive gels.

**2.4 Attributions Form — saved, not final.** Beyond the PI's missing answers:
add the 10/19 interviewee to External Contributions; frame the team as leading
the project and the PI mainly as funding and support; include safety training and
the Jasmin interaction. Verbatim text for the funding and CARC acknowledgements is
in `2026-10-18_pi_questionnaire_answers.md` A5 and D3.

**2.5 Safety Form.** Officer is Jasmine Yu, Chair, IBC, Keck Graduate Institute.
Status is conditional approval, dated 2026-10-15, **no approval number**. State it
that way. Add the safety training record.

## Tier 3 — after the freeze, or genuinely unblocked

- **Resolve the circular-vs-linear genome conflict** with the PI. His A2 text says
  circular, our analysis says linear + 77 bp DTR. Not on the critical path for the
  21st unless a wiki page states a topology — if one does, it moves to Tier 2.
- **Fill the placeholders in his method text**: the `XX ng` DNA input in A2 and the
  AlphaFold webserver version in A3, both needed before any of it is published.
- **Rafael continues expressing all proteins**, ongoing, no completion date. Deeper
  characterisation — affinity and biochemical assays — is aspirational and should
  be described as such, not promised.
- **CheckV and formal taxonomy** for the phage genome. A3's Foldseek assignment
  (Bcep22-like podovirus, *Gervaisevirus*, via Ralstonia phage GP4 NC_054964)
  partly closes this, tentatively.

---

**Log**

- 2026-10-18 — compiled from the morning transcript against repo state; deadlines
  anchored to the 2026-10-21 Parts/Attributions freeze, wiki freeze unverified.
