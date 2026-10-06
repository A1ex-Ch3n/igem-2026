---
title: Depolymerase Activity Assay — Spot Test on a Bacterial Lawn
type: workflow
purpose: Detect capsule/EPS-degrading activity of a purified recombinant depolymerase by spotting serial dilutions onto a dried bacterial lawn and scoring halo zones.
references:
  - "[[lb_broth]]"
  - "[[lb_agar]]"
  - "[[single_colony_inoculation]]"
  - "[[od600_measurement]]"
  - "[[pbs]]"
  - "[[phage_buffer]]"
  - "[[plaque_assay_layered_plate]]"
  - "[[media_disposal]]"
source:
  - documents/2026-09-21_depocatalog_paper_reading_notes.md
  - "Otwinowska A et al. DepoCatalog. Nat Commun 17, 6724 (2026). doi:10.1038/s41467-026-73570-7 — Methods, 'Depolymerase activity assay'"
  - "Supplementary Information PDF p.63 (Supplementary Fig. 12 — halo reference images)"
estimated_time: Day 1 ≈ 2 hr hands-on (lawn + spotting) · Day 2 read · Day 3 final read
---

# Depolymerase Activity Assay — Spot Test on a Bacterial Lawn

> [!warning] Provenance — this is the repo's first literature-derived protocol
> Every other protocol here is transcribed from `lab_notebook/digitalized/` or from
> `protocol/*.docx|pdf`. **This one is not.** It is transcribed from the Methods of a
> published paper on *Klebsiella*, at Prof. Espinoza's instruction (2026-09-21:
> *"Please read the methods: Specifically to 'Depolymerase activity assay' … That's the
> next big experiment. We will be doing these spot tests."*).
>
> Consequences, stated up front:
> - **The team has never run this.** Status is 📝 draft until a first run exists.
> - The source values are for ***Klebsiella pneumoniae* + TSA + 37 °C**. Our system is
>   environmental ***Pseudomonas* + LB + 30 °C**. Both sets of values are carried
>   side-by-side below; nothing has been silently substituted.
> - Several steps are **genuinely underspecified in the paper** and are flagged
>   `==CONFIRM==`. They are not omissions in this transcription.

> [!note] Not the same as the archived `spot_testing.md`
> [`archived/spot_testing.md`](../../../archived/spot_testing.md) spotted **phage** on a
> soft-agar overlay to screen host range, and was deprecated 2026-06-06. This protocol
> spots **purified protein** on a dried lawn to score enzymatic capsule degradation.
> Different input, different plate format, different readout.

## Purpose
Determine whether a purified recombinant depolymerase degrades the surface polysaccharide
of a given bacterial strain. A positive result is a **halo**: a translucent/matte zone
where the polysaccharide layer has been stripped but the bacteria are **still alive**.
This distinguishes the assay from a plaque assay, where the bacteria are killed.

The readout is **qualitative — presence vs absence**. The source paper states this
explicitly and does not attempt quantitative comparison between enzymes.

---

## ★ Prerequisite — the paper's protein expression condition

> [!important] **Induction: 16–20 °C for 16 h. Never 37 °C.**
> This is the single most transferable number in the paper for us, because our
> 2026-09-15 expression gels were inconclusive and induction temperature is the first
> variable to change. Two levels of detail, both from the paper:
>
> | Source | Condition |
> |---|---|
> | **Methods, main text** (applies to all 90 proteins) | *"Recombinant protein expression was induced at* **16–20 °C for 16 h** *by adding IPTG to a final concentration of 0.2–1 mM."* Induced at **OD₆₀₀ 0.5–1.0**, in 500 mL LB. |
> | **Supplementary Data 5** (per-protein, n = 90) | Temperature: **16 °C × 44, 18 °C × 41, 20 °C × 5**. IPTG: 0.5 mM × 44, 1 mM × 41, 0.2 mM × 5. Strain: BL21 (DE3) STAR × 81, BL21 (DE3) × 9. |
>
> **Not one of the 90 proteins was induced at 37 °C.** The 16 h duration comes from the
> main text only; Supplementary Data 5 has no duration column, so 16 h is the blanket
> value, not a per-protein one.
>
> **What to use for our six pET-28a constructs:** the 16 °C / 0.5 mM group is the pET30a
> subset — kanamycin, N-terminal His — which is the closest architecture to our pET-28a.
> So: **16 °C, 0.5 mM IPTG, 16 h, BL21 (DE3) STAR, induce at OD₆₀₀ 0.5–1.0**.
>
> Rationale: β-helix depolymerases trimerise slowly. Fast induction at 37 °C drives them
> into inclusion bodies. Full purification conditions are in the reading notes §4.

---

## ⚠️ Step 0 — Go / no-go pre-test (do this before anything else)

Halos are easy to see on *Klebsiella* because its capsule is thick and mucoid. Our
*Pseudomonas* hosts may not produce enough surface polysaccharide for a halo to be
visible at all, and the receptor for 9-2-1 Φ8 is an **LPS sugar**, not a capsule
(see [`documents/2026-07-13_why_protein_protein_binding_fails.qmd`](../../../documents/2026-07-13_why_protein_protein_binding_fails.qmd)).

**Pre-test:** spot undiluted phage filtrate (9-2-1 Φ8) on a lawn of its host and look for
a **halo around the plaques**, not just the plaques.

| Pre-test outcome | What it means | Action |
|---|---|---|
| Plaques **with** halo | The host's polysaccharide is degradable and the halo is visible on our plates | Proceed with the full protocol |
| Plaques, **no** halo | Either no degradable layer or the halo is below visual contrast | Do **not** expect protein spots to work. Switch to a biochemical readout (see Notes) |
| No plaques | Wrong host / dead lysate | Fix that first |

This costs one plate and answers whether the whole assay is viable.
**UNDONE** — not yet done. `photos/` holds only the 0529 and 0605 batches, and no
digitised notebook entry records plaque morphology, so the answer is not in the archive.

---

## Quick-lookup table — what goes on the plate

| Spot | Volume | Content | Purpose |
|---|---|---|---|
| Sample | **10 µL** | Purified enzyme, two-fold serial dilution series in PBS | The test |
| Negative control | **10 µL** | PBS alone | Buffer/spotting artefact control |
| Positive control | **10 µL** | Phage filtrate, **10⁷–10⁸ PFU/mL** | Proves the host's polysaccharide *is* degradable |
| Vehicle control *(added by us)* | **10 µL** | Elution buffer incl. imidazole, at the same dilution as the top enzyme spot | Rules out imidazole/salt killing the lawn |

The vehicle control is **not in the source paper**. It is added because our enzyme will
come straight off Ni-NTA in 500 mM imidazole, which the paper's PBS-based samples did not
contain.

## Quick-lookup table — source vs our system

| Parameter | Paper (*Klebsiella*) | Ours (*Pseudomonas*) — proposed |
|---|---|---|
| Medium | **TSA** plates, TSB culture | **LB agar** — see [[lb_agar]]. We have no TSA. `==CONFIRM: buy TSA or accept LB==` |
| Lawn culture density | **OD₆₀₀ = 1.0** | Same. See [[od600_measurement]] |
| Lawn volume | **1 mL** poured directly on the plate | Same |
| Incubation 1 | **37 °C overnight** | **30 °C overnight** (project default for our isolates) `==CONFIRM==` |
| Incubation 2 | **room temp, additional 24 h** | Same. Do not skip |
| Replicates | ≥ **biological triplicate** | Same |

---

## Materials & equipment
- Pre-poured agar plates, normal thickness (see [[lb_agar]]; paper used TSA)
- Sterile spreader or the plate-tilting technique
- P20 / P200 pipettes + sterile tips
- Sterile 1.5 mL tubes or a 96-well plate for the dilution series
- Spectrophotometer for OD₆₀₀ — see [[od600_measurement]]
- Incubator at 30 °C (ours) or 37 °C (paper)
- Laminar flow hood or still bench for lawn drying
- Marker (grid the back of the plate before spotting)

## Reagents
- **Purified recombinant depolymerase.** Prerequisite; no protocol in this repo yet.
  **UNDONE** — Ni-NTA purification of the six pET-28a constructs.
  ★ Express it at **16–20 °C for 16 h**, never 37 °C — see the
  [Prerequisite callout](#-prerequisite--the-papers-protein-expression-condition) above
  for the full breakdown and the values to use for our constructs.
- **PBS**, pH 7.4 — see [[pbs]]. The paper's exact recipe: 137 mM NaCl, 2.7 mM KCl,
  10 mM Na₂HPO₄, 1.8 mM KH₂PO₄.
  ⚠️ This is **not** our [[phage_buffer]] (Tris + MgSO₄ + CaCl₂, pH 7.5). Do not substitute
  without recording it as a deviation.
- **Overnight host culture** — see [[single_colony_inoculation]]
- **Phage filtrate** at 10⁷–10⁸ PFU/mL for the positive control — output of
  [[phage_isolation]] / [[phage_purification]]. `==CONFIRM: our Φ8 lysate titre==`
- **Enzyme elution buffer** for the vehicle control (whatever the purification eluted into)

---

## Procedure

### Day 1 — lawn

1. Grow the host to **OD₆₀₀ = 1.0** ([[od600_measurement]]). Not saturated overnight
   culture. Mid-to-late log.
2. Pipette **1 mL of the culture directly onto the agar plate** and spread to cover the
   whole surface.
   > This is a **dried lawn**, not a soft-agar overlay. It differs from both
   > [[plaque_assay_layered_plate]] and the archived spot-testing method.
3. **Dry the plate** until no free liquid remains.
   `==CONFIRM: the paper says only "after drying". It does not state whether excess
   liquid is poured off first, how long drying takes, or whether it is done in a hood.==`
   This is the single step most likely to fail on a first attempt. Suggested first pass:
   pour off excess, then lid-off in a laminar flow hood 15–20 min until matte. Record the
   actual time and method for the next run.

### Day 1 — spotting

4. Mark a grid on the **back** of the plate before spotting. Label every position.
5. Prepare a **two-fold serial dilution series** of the enzyme **in PBS**. Start neat.
   `==CONFIRM: the paper does not state the starting concentration or how many dilution
   steps.==` Suggested first pass: neat down to 1/64, seven spots.
   > The dilution series is not for quantifying activity. Its job is to find the highest
   > dilution still giving a halo, which is the usable comparison between constructs.
6. Spot **10 µL** of each dilution onto its grid position. Also spot, on the same plate:
   - **10 µL PBS** (negative)
   - **10 µL phage filtrate at 10⁷–10⁸ PFU/mL** (positive)
   - **10 µL elution buffer** (vehicle, our addition)
7. Let every spot absorb fully before moving the plate. Do not invert while wet.

### Day 1–3 — incubation

8. **Incubate overnight at 37 °C** (paper) / **30 °C** (our isolates).
9. Then **leave at room temperature for a further 24 h**.
   > Not optional. The paper specifies both stages and halos frequently only become
   > readable during the room-temperature stage.

### Day 3 — scoring

10. Read against a dark background with oblique light. Score **presence or absence** only:

| Observation | Interpretation |
|---|---|
| **Halo** — translucent/matte zone, bacteria still growing inside it | Depolymerase active on this strain |
| **Clear plaque ringed by a halo** | Phage control working as intended |
| Clear zone, **no** halo, at the enzyme spot | Suspect killing or buffer toxicity, not depolymerase activity. Check the vehicle control |
| Nothing at any dilution | Negative, *or* the halo is not visible on this host. See Step 0 |

11. Reference images: **Supplementary Fig. 12, p. 63** of the paper's Supplementary
    Information PDF. Panels A–C are phage titration plaques with halos; panel D is a spot
    test showing both a phage halo and a recombinant-enzyme halo.
12. Photograph every plate. Record the highest dilution still showing a halo.
13. Repeat as **biological triplicate** before reporting anything.

---

## Notes / common deviations

- **The spot assay is more sensitive than a Coomassie gel.** The paper reports clear halos
  from protein present at levels not prominently visible on SDS-PAGE. Our 2026-09-15 gels
  were inconclusive; that is not evidence the protein is absent. Do not wait for a clean
  gel before attempting this assay.
- **If no halo appears anywhere, work through these in order:** (1) Step 0 says halos
  aren't visible on this host at all; (2) no expression — redo induction at 16 °C /
  0.5 mM IPTG / 16 h with an empty-vector control and a pre-induction sample, both of
  which the 0915 gels lacked; (3) codon bias — the ordered inserts are
  `Codon Optimized: No` with mammalian-like bias (see
  [`documents/2026-09-10_twist_construct_order_second_set/README.md`](../../../documents/2026-09-10_twist_construct_order_second_set/README.md));
  (4) the CDS_0011 construct is truncated (res 305–941) whereas the paper produced every
  protein full-length.
- **Biochemical fallback, if halos are not visible.** DNS reducing-sugar assay, TLC, or
  polysaccharide gel electrophoresis on extracted LPS/EPS. ⚠️ **These are our addition.**
  The paper's Methods contain **no** biochemical activity assay of any kind; the plate
  halo is its only readout. A biochemical assay would give quantitative data the paper
  does not have, but it is an unvalidated route for us.
- **Lawn viability.** A halo requires living bacteria underneath. If the lawn is patchy or
  the plate over-dried, halos and kill zones become indistinguishable.

## Checklist — where do the outputs go?

- [ ] Spotted plates → **30 °C incubator** overnight, then **room temp bench** 24 h
- [ ] Plate photographs → `photos/<MMDD>/` + the notebook entry for that day
- [ ] Leftover purified enzyme → **4 °C** short term; **−80 °C** with glycerol for longer
      `==CONFIRM: storage condition for our constructs==`
- [ ] Leftover phage filtrate → **4 °C** — see [[phage_buffer]]
- [ ] Used plates + cultures → **media disposal** — see [[media_disposal]]

## Source
- Paper: Otwinowska A, Olejniczak S, Latka A, *et al.* **DepoCatalog: mapping diversity of
  129 recombinantly produced *Klebsiella* phage depolymerases.** *Nat Commun* **17**, 6724
  (2026). doi:10.1038/s41467-026-73570-7 — Methods, "Depolymerase activity assay".
  Open Access, CC BY 4.0.
- Halo reference images: Supplementary Information PDF, p. 63 (Supplementary Fig. 12).
- Expression conditions: Supplementary Data 5 (per-protein table, n = 90).
- Team reading notes + the *Pseudomonas* adaptation reasoning:
  [`documents/2026-09-21_depocatalog_paper_reading_notes.md`](../../../documents/2026-09-21_depocatalog_paper_reading_notes.md)
- Instruction to run this assay: Prof. Espinoza, 2026-09-21 message.

---
## Log
- 2026-09-21 — Initial draft. Transcribed from the DepoCatalog Methods paragraph; the
  paper has no standalone protocol, so steps 4, 7, 10–13 and the grid/labelling
  instructions are ordinary lab practice filling gaps the source leaves open, not values
  invented for it. Paper values and our *Pseudomonas* substitutions are kept side-by-side
  per the repo's preserve-all-versions rule. Additions beyond the source (Step 0 go/no-go,
  vehicle control, biochemical fallback) are labelled as such inline. 6 `==CONFIRM==`
  markers open. Team has not run this. [[pbs]] (#27) drafted alongside this file,
  since the assay needs PBS as both diluent and negative control.
- 2026-09-21 — Added the ★ Prerequisite callout flagging the paper's induction condition
  (**16–20 °C, 16 h**, main text) beside the per-protein Supplementary Data 5 breakdown
  (16 °C × 44 / 18 °C × 41 / 20 °C × 5), at Alex's request. No protein was induced at 37 °C.
