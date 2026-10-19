# Judging Form — every field, and what we put in it

Form: `https://teams.igem.org/6317/judging-form/edit` · **freezes 2026-10-21 08:00 PDT**.
Status before today: **Not Started**. The draft record has now been created.

**Read this first: on that form, "Save and submit" means submit.** The page says
"Saving submits your form to iGEM. You can edit it until Oct 21, 08:00 PDT." So
it is editable after saving, but the first save is a submission. Nothing has been
saved yet.

**Topology decision applied here (2026-10-18):** per Alex, we default to the PI's
assembly being correct — the genome is reported as a **circular contig of
62,339 bp** (62,416 bp with the 77 bp overhang still on). The wiki currently says
"linear, 62,338 bp, 77 bp direct terminal repeat" on `/description` and needs
changing to match. The open question is recorded in
[`2026-10-18_genome_topology_conflict.md`](2026-10-18_genome_topology_conflict.md).

---

## The form, field by field

### Project

**Project Title\*** (free text) — `Phagenomics`
Already the wiki's title and public branding; no reason to change it now.

**Abstract\*** — **hard limit: "Abstract must contain up to 150 words."** The
text now in the form is 142 words:

> Phage therapy's bottleneck is host range: each phage binds a specific receptor
> on a specific strain, so matching phage to target means screening, not design.
> We isolated our own system from soil at the California Botanic Garden:
> *Pseudomonas capeferrum* and an unnamed relative in the *P. putida* group, with
> their co-occurring phages. Phage Φ8 is
> novel: 62,339 bp, 80 CDS, no database match, no virulence or resistance genes.
> Modelling then redirected the project. Structure prediction and protein
> language models showed the recognition step is not protein–protein: the
> receptor-binding apparatus is branched, and one accessory protein is a
> depolymerase degrading the bacterial polysaccharide layer. The key interaction
> is protein–sugar. We therefore asked whether ancestral depolymerases were more
> generalist, reconstructing ancestors of the phage's GH5 glycoside hydrolase,
> scoring them with an enzyme-conditioned language model, and expressing modern
> and ancestral enzymes in *E. coli*, reporting what worked and what did not.

(Typed without the Greek Φ and en dashes, to avoid encoding surprises in the
form: "Phi8", "protein-protein", "protein-sugar".) The corrected text is **148
words**, still under the 150-word limit.

> ⚠️ **Corrected 2026-10-19 — species misassignment. The text above is the fixed
> version; what is currently typed into the form is not.** The abstract said
> *"Pseudomonas capeferrum* and *P. putida*". **We have no *P. putida*.** Our own
> data says so twice over: sourmash/GTDB places four of the five isolates in
> ***Pseudomonas_E* sp013179515**, an *unnamed* species, and only 8-10-2 in
> *P. capeferrum* (`data/bacteria_genome/*/*sourmash-genome-species.csv`); and
> synthesis row A5 records **89.4 % ANI to *P. putida***, far below the 95 %
> species threshold, with the closest public relative being *Pseudomonas* sp.
> CM27 at ~99.2 %. *P. putida* enters this project only as the **surrogate host**
> in the receptor-overlap analysis (row D4, KT2440) — that is almost certainly
> where the drift came from. It also matters for the story: the phage's host is
> **Strain 2 (9-2-1 / 9-6-2) = sp013179515**, not *capeferrum*, which is
> Strain 3. **Whoever saves the form must re-type the abstract.**

### Medals — Bronze (all three required)

**B1 · Competition Deliverables.** A checkbox: "I confirm that my team has and
will fully complete the required deliverables" — Wiki, Judging Form,
Presentation Video (after freeze day), Judging Session.
→ **Tick.** Wiki is live, this form is being filled, the Judging Session is
already scheduled for **Nov 13, 07:35–08:00 PST**. The Presentation Video is due
Oct 28 and has not been started — the confirmation is forward-looking ("has and
will"), so ticking is honest only if we actually make the video.

**B2 · Project Attributions.** Checkbox: "I confirm that my team will fully and
accurately complete the Attributions Form on time."
→ **Tick.** The form is Saved / Received; a few PI answers are still outstanding.

**B3 · Contribution.** "Describe how and why you chose your iGEM project. Make a
useful contribution for future iGEM teams."
- optional: an existing Part name, if the contribution is documentation added to
  someone else's part. We are not doing that — leave empty.
- **required link: `https://2026.igem.wiki/claremont-ca/contribution`**
- checkbox: "I confirm that the required link presents the evidences…"

→ **Unblocked as of 2026-10-19: the page now returns 200** (6.9 kB). The form
still marks the link "Unseen" until someone opens it from inside the form — that
is a click, not a piece of work.

What it should contain, from material we already have: the `phagecheck` package
(the DTR-versus-circularity check and the rest of the software inventory), the
six documented parts, the negative results worth warning future teams about —
the RBP×OMP folding screen that failed with two tools and no paired MSA, and the
Ni-NTA purification that came back blank — and the pipelines for assembling and
annotating a phage from soil.

### Medals — Silver (both required, plus Bronze)

**S1 · Engineering Success.** "at least one iteration of the engineering design
cycle."
- optional Part name field — we can name a part here.
- required link: `https://2026.igem.wiki/claremont-ca/engineering` (**exists**)
- checkbox confirmation.
→ **Tick** once someone opens the link in the form.

**S2 · Human Practices.** "Explain how you have determined your work is
responsible and good for the world."
- required link: `https://2026.igem.wiki/claremont-ca/human-practices` (**exists**,
  thinnest page on the wiki, being rewritten tonight)
- checkbox confirmation.
→ **Tick** after tonight's rewrite.

### Medals — Gold (three special prizes)

Three dropdowns, G1 / G2 / G3. At least one from General Bio Engineering, at
least one from Specializations, third from either. All three must impress the
judges or Gold is lost; fewer than three forfeits Gold outright.

**Proposed, and this is the team's call, not mine:**

| | prize | list | why |
|---|---|---|---|
| G1 | **Best New Basic Part** | General Bio Engineering | Six documented parts, three of them computationally designed ancestral sequences that exist nowhere in nature, with structure predictions and a stated design rationale. Our strongest claim. **Selecting it opens a required `Part Name*` field that only accepts a BioBrick name (`BBa_…`) — so it is blocked until the Registry upload produces part numbers.** The form asks for "your one best Basic Part"; the criterion text says winning parts come with "thorough documentation and experimental data showing the part works". |
| G2 | ~~Best Integrated Human Practices~~ → **Best Software** (swapped 2026-10-19) | Specializations | The only Specialization we can realistically reach in three days. Depends entirely on tonight's rewrite, and the criterion wants stakeholder input that visibly changed the project — which we have: the shift away from purification toward small-scale targeted blots. |
| G3 | **Best Model** | General Bio Engineering | AlphaFold/ESMFold structures, the ZymCTRL perplexity series across ancestral nodes, the Foldseek structural taxonomy — and a modelling result that genuinely redirected the project, which is exactly what the criterion rewards. Required link `https://2026.igem.wiki/claremont-ca/model` **exists**. |

Alternatives considered and rejected for now: **Best Measurement**
(`/measurement` 404s), **Safety and Security** (the Safety Check-in Form shows
"Deadline Missed", which a judge can see).

> **Superseded 2026-10-19.** This paragraph also listed **Best Software**
> ("`/software` 404s and the CC BY 4.0 licence is not OSI-approved") and **Best
> Part Collection** ("needs the collection page, which does not exist"). Both
> readings were wrong by the time they were written: `/software` is live and
> `software/LICENSE` is MIT, and the collection page now exists. Best Software
> is the **G2 nomination** in the table above. Kept here so the reasoning trail
> is legible, not as a current statement.

### Awards we are already in, no action needed

The form's summary lists these as Eligible by default: **Best Foundational
Advance Project** (our village), **iGEM Spirit Award**, **Best Project Promotion
Video**, **Best Presentation**, **Best Wiki**, **iGEMers Prize**.

Note that Best Presentation and Best Wiki are scored on the same ballot questions
as the Presentation and Wiki sections of the general project ballot — so the
Presentation Video and the wiki carry weight beyond Bronze.

## The general project ballot, for context

Every team is scored on these, whether or not they appear on the form:

1. How well were engineering principles used (design-build-test cycle,
   standards, modularity)?
2. Did the team design a project based on synthetic biology and standard
   components?
3. Did the project work, or is it likely to work?
4. How competent was the team, collectively, at answering judge questions?
5. How well did the team's data — modelled and/or experimentally measured —
   support their claims?
6. Is the project likely to have an impact?
7. How well did the team demonstrate that their Human Practices work influenced
   the design, execution, application and/or other aspects of their project?
8. To what extent did they convince you that their Human Practices activities
   helped create a project that is responsible and good for the world?
9. Are the project components well documented on the team's Wiki/Registry pages
   (parts must be documented in the Registry)?
10. How much of the project was initiated and led by the students?

Questions 7 and 8 are both Human Practices. Question 10 is why the Attributions
Form frames the PI as funding and support.

**Update 2026-10-19.** G2 is now **Best Software**, and `BBa_26DKNAEC` is entered
as the Best New Basic Part. Reasoning and what each prize still needs:
[`2026-10-19_special_prize_assessment.md`](2026-10-19_special_prize_assessment.md)
and [`2026-10-19_special_prize_gaps.md`](2026-10-19_special_prize_gaps.md).

## What is in the form right now

Title, abstract and the three prize selections are entered. **Nothing has been
saved, so nothing has been submitted.** Every confirmation checkbox is
deliberately left unticked — each one is a declaration the team makes to the
judges ("I confirm that…"), and two of them depend on work that does not exist
yet. The summary line currently reads "Not eligible for any medal · no special
prize (3 selected but not confirmed)".

To finish it, a team member needs to: open each required link from inside the
form (the form tracks them as "Unseen" until clicked), tick B1, B2, B3, S1, S2
and the three prize confirmations, enter the `BBa_` part name under G1, and
press **Save and submit**.

## Blockers, in order

1. ~~`/contribution` does not exist~~ — **resolved 2026-10-19**, the page is live.
2. **The six Registry parts are still in Draft** — numbers exist
   (`BBa_26DKNAEC` is entered on the form) but a Draft part is not screened and
   not publicly visible. They must be submitted before the freeze.
3. The **three special prizes** need the team's agreement before the form is
   saved.
4. **Human Practices** rewrite (tonight) before S2 and G2 are honest — the same
   page backs both.
5. The **Presentation Video** must actually be made for B1 to be honest.

---

**Log**

- 2026-10-18 — form record created on teams.igem.org, every field transcribed,
  answers drafted. Nothing saved or submitted.
