---
title: Dot Blot — His-Tag Detection on Nanocellulose Membrane
type: workflow
purpose: Spot lysates and purification fractions directly onto membrane and detect the His tag with an HRP-conjugated antibody, without a gel or any size separation.
references:
  - "[[iptg_induction_and_protein_extraction]]"
  - "[[his_tag_purification_ni_spin_column]]"
  - "[[pbs]]"
source:
  - protocol/printed_2026-10-20/Dot Blot Protocol.pdf
  - lab_notebook/digitalized/2026-10-19_dot-blot-his-tag.md
estimated_time: ≈ 2 h 45 min (1 h block + 15 min washes + 1 h antibody + 20 min development)
---

# Dot Blot — His-Tag Detection on Nanocellulose Membrane

## Purpose
Ask one question — **is the His tag present in this sample?** — without running a gel. Samples are
spotted directly onto nanocellulose membrane, blocked, probed with a **single-step HRP-conjugated
anti-His antibody**, and developed to a visible dot. Used on 2026-10-19 on rough lysates and one
Ni-column flow-through; it is the assay that reframed the failed *e281* purification from an
expression problem into a capture problem.

> [!note] Provenance — a complete digital source, unlike the rest of this set
> Transcribed from [`Dot Blot Protocol.pdf`](../../printed_2026-10-20/Dot%20Blot%20Protocol.pdf), a
> Google Docs export supplied with the printed bench documents on **2026-10-20**. Unlike the other
> four protocols in this batch, this one is **complete** — no missing pages, no handwriting to
> interpret. Its text is reproduced in full below.

> [!warning] A dot blot reports the tag, not the protein
> There is no size separation, so this assay **cannot** distinguish full-length product from a
> truncation or from free tag. It does not settle the 10/01 `CDS11` question (a band at ~43 kDa
> against an expected 72.0 kDa). Read it as presence/absence of the His epitope and nothing more.

## Quick-lookup table — the four solutions

| Solution | Recipe | Notes |
|---|---|---|
| **Blank (blocking) buffer** | **25 mL 1× PBS + 1.25 g Blotting-Grade Blocker** | = **5 % w/v** blocker |
| **PBST 5 % buffer** | `[TBD: the document names it but gives no recipe.]` | `==CONFIRM: whether "5 %" here is the blocker carried into PBST, or the Tween figure (5 % Tween would be ~50× the usual 0.1 %).==` |
| **HRP conjugate antibody** | **15 mL PBS + 15 µL antibody** (= **1:1000**) | **Reusable within two weeks**, kept at **4 °C** |
| **Detection buffer** | **13.5 mL MilliQ + 1500 µL diluent + 300 µL substrate**, from the **Opti-4CN Substrate Kit** | 15.3 mL total |

## Materials & equipment
- **Nanocellulose membrane**
- Plastic plate large enough to hold the membrane flat
- Orbital shaker, room temperature
- **P20** for spotting
- Falcon tube for recycling the antibody solution
- 4 °C fridge

## Reagents
- **1× PBS** — see [[pbs]]
- **Blotting-Grade Blocker**
- **PBST**
- **HRP-conjugated anti-His antibody** `[TBD: supplier and catalogue number.]`
- **Opti-4CN Substrate Kit** (diluent + substrate)
- Samples, plus **both a positive and a negative control**

## Procedure
1. **Load sample.** Cut the membrane to a suitable size and put it in a plastic plate. Use a **P20**
   to load protein samples onto the membrane, **2 µL per dot**; increase the volume if the solution
   is viscous. ★ **Include both positive and negative controls.**
2. **Block.** Pour blank buffer into the plate to cover the membrane. **Incubate on a shaker at room
   temperature for 1 hour.**
3. **Wash — PBST.** Discard the blank buffer. Pour **PBST 5 % buffer** into the plate to cover the
   membrane and shake for **3 minutes**. **Repeat this process twice** (i.e. three washes in total).
4. **Wash — PBS.** Discard the PBST buffer. Pour **1× PBS** to cover the membrane and shake for
   **3 minutes**.
5. **Probe.** Discard the PBS. Pour the **antibody solution** to cover the membrane and shake for
   **1 hour**.
6. **Recycle the antibody.** Return the antibody solution to its Falcon tube and put it back in the
   fridge.
7. **Develop.** Add **detection buffer** to cover the membrane to visualise the protein dots. Shake
   the plate for **around 20 minutes**, until the dots are visualised.

## Notes / common deviations
- **This protocol closes three open items on the 2026-10-19 notebook entry**, which recorded them as
  unknown at the time it was written:
  1. **Spotting volume** — the entry says *"`==CONFIRM: spotting volume per dot — not recorded.==`"*.
     The protocol specifies **2 µL per dot**.
  2. **Blocker concentration** — the entry says the figure was *"mirrored and faint — not reliably
     legible"* on the reverse of the layout sheet. The protocol specifies **1.25 g in 25 mL = 5 %**.
  3. **Substrate chemistry** — the entry narrowed it to *"precipitating TMB or 4-chloro-1-naphthol…
     which of the two was used is not recorded"*. The protocol names the **Opti-4CN Substrate Kit**,
     which is a **4-chloro-1-naphthol** substrate. `==CONFIRM: that the 10/19 blot was run from this
     document and not an earlier version of it — the resolution depends on that.==`
- **Single-step detection.** There is no separate primary and secondary antibody; the anti-His is
  already HRP-conjugated. One probe step, one hour.
- **The antibody is reused.** Recycling it (step 6) is in the protocol, which means signal strength
  is not comparable between blots run two weeks apart.
- **There is no loading normalisation anywhere in this protocol**, and there was none on 10/19.
  Intensity differences **between different constructs carry no quantitative meaning**; only the
  comparison of each spot against the negative control is safe. The 10/19 analysis used a **2×
  the negative control** threshold for calling a spot, measured against a local background annulus
  rather than by eye.
- **Put the positive control at an edge.** On 10/19 the positive control spot ran, leaving a smear
  up and to the right, and carry-over onto the neighbouring row could not be excluded from the
  photograph. The entry's own recommendation is to re-run with the positive control at an edge
  position.
- **Use a matched negative control, not a buffer blank.** The 10/19 blot used the **uninduced**
  CDS12 culture — the same construct without IPTG — which makes the induced/uninduced pair a
  result in its own right rather than just a background check.
- **Still missing: a BL21 empty-vector arm.** The 10/19 entry notes this was the fourth protein
  assay in a row without one. Nothing in this protocol distinguishes a construct-specific signal
  from host background that happens to bind the probe. The instruction to run it exists in
  handwriting on [[iptg_induction_and_protein_extraction]] §2 and has never been carried out.

## Checklist — where do the outputs go?
- [ ] Developed membrane → photograph immediately; archive under `data/assays/`
- [ ] Spot layout sheet → photograph **in the same orientation** as the membrane and archive beside it
- [ ] HRP conjugate antibody solution → **recycled to its Falcon tube, 4 °C**, usable ~2 weeks
- [ ] Spot intensities → measure, do not eyeball (see `code/1019_dotblot/quantify_dotblot.py`)

## Source
- [`Dot Blot Protocol.pdf`](../../printed_2026-10-20/Dot%20Blot%20Protocol.pdf), supplied 2026-10-20.
- As-run record and analysis:
  [10-19](../../../lab_notebook/digitalized/2026-10-19_dot-blot-his-tag.md),
  [`code/1019_dotblot/`](../../../code/1019_dotblot/).

---
## Log
- 2026-10-20 — Initial transcription. The source is a text PDF, so the procedure is reproduced
  verbatim rather than read off a photograph. Cross-checked against the 2026-10-19 entry, which it
  resolves on three points left open there (2 µL spotting volume, 5 % blocker, Opti-4CN =
  4-chloro-1-naphthol). The PBST recipe is the one value the document itself does not give.
