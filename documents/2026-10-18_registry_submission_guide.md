# 2026-10-18 — How to put our six parts on the iGEM Registry

> # ⏰ Deadline: **2026-10-21 15:00 UTC** — three days from today.
> `Registry Contributions` (`type: parts`, `required: true`, `freeze: true`) closes then, from
> `https://api.igem.org/v1/competitions/58a7e73a-1e25-457f-9f59-36c47b3f652a/deliverables`.
> The **Attributions Form** has the *identical* close time. The Project Safety Form already
> closed on 2026-10-07.

Help text below is quoted from the Registry's own lazy-loaded JS chunks
(`registry.igem.org/assets/how-to-submit-a-part-*.js`,
`how-to-create-a-part-collection-*.js`, `part-and-part-collection-documentation-*.js`,
`SendForScreeningPage-*.js`, `CLA-*.js`) and the public `api.registry.igem.org`, because the
site is a JS SPA. **Not verified** (login-gated): the live create form, the teams.igem.org
deliverable page body, the part-type dropdown contents.

---

## 1. Where, and who can be credited

`registry.igem.org` is the live Registry; `parts.igem.org` is "classic". Entry point:
`https://teams.igem.org/go/deliverables/registry`.

Quoted: *"you must opt-in to being listed as an author. This only has to be done once"*, then
*"read and accept our Contributor Licence Agreement"*. And: *"Only members of the selected
organisation who have opted-in will appear."*

> **This is the blocking dependency.** Every person we want credited — **including Prof.
> Espinoza** — must sign in to registry.igem.org themselves, opt in as an author, and accept the
> CLA. Nobody can be added to a part otherwise. Do this first, today.

## 2. The workflow, and what locks forever

Create Part → part type (Sequence Ontology role; ours is **CDS**, `SO:0000316`) → Title, Source,
Functional description (*"state what the part is to do"* — design intent, not results) →
Sequence → Authors + Contribution Roles → Licence → **Draft** → **Send for Biosafety
Screening** → Published.

The screening step is a gated stepper: confirm the sequence; accept or reject the
auto-generated sub-part annotation suggestions (*"Parts cannot be sent for screening while
suggestions are pending"*); confirm authors; declare the **host organism** (NCBI Taxonomy, at
least one); confirm the licence; sign the scientific-contribution attestation. A
duplicate-sequence check can block submission outright.

> **The trap:** *"Three things become permanent the moment you leave Draft mode"* — **sequence,
> authorship, licence**. *"If you discover an error later you'll have to create a new part."*
> Documentation stays editable forever. So: get the six nucleotide strings, the author list and
> the licence right **before** sending for screening; the writing can continue afterwards.

**Submission is digital-only.** No physical DNA shipment appears anywhere in the submit guide,
the screening flow or the deliverables bundle.

## 3. Sequence rules (2026)

- **RFC10 BioBrick prefix/suffix is NOT required.** Quoted: *"The system does not assume RFC10
  when adding scars. To capture the scars left by your assembly method, add a DNA sequence
  between the two parts."*
- **No illegal-restriction-site list** was found in the current help text — that rule belonged to
  classic parts.igem.org. Safety is handled by automated biosafety screening instead.
- **Basic vs composite:** basic = *"a single, continuous stretch of DNA that you enter
  directly."* **All six of ours are basic parts.**
- **Enter the CDS only — not pET-28a, and (recommended) not the vector's His6 leader.** The
  2025 exemplar `BBa_25IQCJ3B` starts `ATGGAGACTATC…` with no tag and no vector; its pET303 +
  6×His cloning is described in the *characterisation* text. Our `MGSSHHHHHHSSGLVPRGSHM` leader
  is pET-28a's, not our part. Precedent exists the other way too (`BBa_252FW60D` includes its
  PelB leader and says so in the title), so if we do include the tag, **put it in the title**.
  Either way: decide once, apply to all six.
- **Names are auto-assigned** (`BBa_26XXXXXX`). We control `title`, `description` and
  **`source`** — and `source` is the free-text field where the novel-phage provenance goes
  (isolate, assembly, "ancestral reconstruction designed by Prof. Espinoza").
- Use the canonical `UUAIURNK_` CDS numbering for the 9-2-1 Φ8 proteins, never our old
  `FHABPWTM_` index.

## 4. Documentation sections

Five types, with the Registry's own descriptions:

| Section | What belongs in it |
|---|---|
| **design** | *"How the part or collection was conceived — the rationale behind it and any computational models."* → our AF3/ESMFold models, the tool table, the construct-boundary reasoning |
| **experiment** | *"Protocols, test conditions, results, and troubleshooting."* |
| **characterisation** | *"Quantitative or qualitative data on how the part behaves under particular conditions."* |
| **application** | *"How the part was used in a system — proof-of-concept work and industry use cases."* |
| **discussion** | *"Limitations, comparisons, and future directions."* |

Markdown; *"iGEM does not impose a minimum number of sections or a required length"*; a part may
carry several documents of the same type. The page must stand alone: *"anyone who finds the part
years from now should be able to understand the essentials without leaving the Registry."*

**Explicitly: *"Negative or inconclusive results are still valuable."*** That is the licence to
write our expression story honestly — the inconclusive 0915 gels, the one induction-dependent
CDS12_WT band, the failed e281 Ni-NTA, the missing BL21 control lane.

## 5. The Part Collection

Profile → Collections → **Create Collection**; give organisation, title, description; add parts
by searching their `BBa_` name; then write the collection documentation (same five section
types).

Individual parts must **still** be documented, and the division is strict: *"content should never
be duplicated. If your documentation applies to a group of parts, it belongs in the collection
documentation. Individual parts should only carry their own intrinsic documentation (for example,
sequence-specific behaviour or characterisation). Collections are the right place for shared
experimental context, design considerations, and group-level insights."*

So for us: the collection page carries the phage-targeting/lysis story, the shared methods, and
the variant → predicted-metric → measured-activity table; each part page carries only what is
specific to that sequence.

## 6. Attribution, provenance, safety

- **Contribution Roles** are per author (CRediT-style) — this is where "the GH5 phylogeny and the
  ancestral reconstruction are Prof. Espinoza's work" gets recorded honestly.
- CLA §10: we warrant we *"have the necessary rights"* and have *"complied with all applicable
  export-control, biosecurity, and data-protection regulations."* A novel unpublished phage
  sequence is fine — it is ours; the assembly context goes in `source`.
- **Default licence is CC BY 4.0** if none is chosen, and it *"may not be changed retroactively."*
- Safety is an **automated biosafety screen** at submission. Rejection is survivable: *"A
  rejected part stays visible to its authors while the iGEM team reviews… If the rejection turns
  out to be a false positive, the part can still be published."* Have our Φ8 **0 VFDB / 0 CARD**
  result ready as evidence.

---

## Do this next, in order

1. **Today — everyone, including the PI:** sign in to registry.igem.org, opt in as an author,
   accept the CLA. Nothing else can proceed until this is done.
2. **Decide the His6 policy once** (recommended: CDS only, no vector, no pET-28a leader) and
   freeze the six final nucleotide strings.
3. Create all six as **basic** parts, role **CDS**, with title / description / `source`. Leave
   them in **Draft**.
4. **Triple-check sequence, authors + contribution roles, and licence** — these three lock
   permanently at screening.
5. Send each for screening: clear the sub-part annotation suggestions, set host organism
   (*E. coli* as the expression host, our *Pseudomonas* phage as the source), confirm, sign.
6. Create the **Part Collection** — the GH5 plus its three ancestors plus the two fibers, as one
   targeting-and-lysis toolbox. Shared content on the collection page, sequence-specific content
   on the part pages, no duplication.
7. Fill the five section types per part, using
   [`2026-10-18_parts_structure_comparison.md`](2026-10-18_parts_structure_comparison.md) for the
   *design* sections and saying plainly where the wet lab stands.
8. Submit the **Attributions Form** — same 2026-10-21 15:00 UTC deadline. Draft:
   [`2026-10-18_attribution_form_DRAFT.md`](2026-10-18_attribution_form_DRAFT.md).

---
*Log — 2026-10-18: compiled from the Registry's own help text and the competition API. The one
soft spot is the His6 convention, which is precedent-based judgement, not a written rule.*
