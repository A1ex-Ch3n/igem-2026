# Design system — annotations to return to Claude Design

Reply to `Phagogram-design-system.pdf` (generated 2026-10-25, 18 pages), using
its own convention: an ID, then what to change. Everything not named here stays
as it is.

Paste the whole of **§1 onward** back into Claude Design. §0 is for Alex.

---

## §0 — Read this first (not for pasting)

Two findings that are larger than any single annotation.

**The system was built from the wrong repository.** The cover records
`A1ex-Ch3n/iGEM_Claremont_2026@ecb9b7a`. This repository is
`A1ex-Ch3n/igem-2026`. What it read is a dry-lab pipeline that predicts which
phages lyse which *Xanthomonas* strains and publishes a "digital phagogram":
seven numbered steps, six biophysical features, ESM-2 embeddings, AUROC. Its
example hosts are *X. citri* 306, *X. campestris* 33913, *X. oryzae*
KACC10331. That workstream is real and belongs to the team — O-03 attributes
it to a teammate — but it is not the project the presentation video tells,
which is *Pseudomonas*, phage 9-2-1 Φ8, four DBTL cycles, wet lab and dry lab
together.

**It is also the wrong kind of system.** This is a documentation and interface
system: surface levels, focus rings, status chips, table rules. Two components,
StatusTag and PhagogramTable. There is no motion section, no stroke
definition, no layout grid, no drawing primitive. The layer the animations need
does not exist in it at all.

The recommendation is not to discard it. Its tokens are careful, and they are
already close to the palette the animations use:

| its token | its value | what the animations use |
| --- | --- | --- |
| `phage` | `#0d6b6b` | `#2D6A6A` |
| `chart-phage` | `#c1432e` | `#B4542E` |
| `xanthos` | `#e2a019` | `#C9A227` |

So: **one system, two layers.** Keep C/T/S/R/D/V/M as the team's documentation
and wiki layer, correct the identity and the colour semantics, and add a whole
motion and drawing layer for the video. Wiki, deck and video then share one
palette. The cost is retuning `code/1025_presentation_deck/anim_style.py` to
these hexes and re-rendering — a few minutes of compute.

**Two assumptions made below, both reversible.**

1. The project name is written **Phagenomics**, because that is what line 22 of
   `2026-10-25_presentation_video_script.md` says and that line is being
   recorded. Verify against the live wiki before this is final.
2. The *Xanthomonas* pipeline stays in the system, scoped into a section of its
   own rather than deleted. It is a second workstream, not a mistake.

---

## §1 · A — Identity

**A-01** The name is wrong. This is not "Phagogram". The project is
**Phagenomics**, by **iGEM Claremont-CA**, a first-year team in California.
Set the cover to the project name and the team name. "Phagogram" is the
deliverable of one dry-lab workstream and belongs in §W, not on the cover.

**A-02** The tagline is wrong. "Predicting which phages lyse which host
strains" describes that one workstream. The project's question is narrower and
more concrete: **why a phage can infect one bacterial strain and not its close
relative.** Tagline: *"What decides which bacteria a phage can infect."*

**A-03** Replace the cover artwork. An 8×6 interaction matrix is a poor cover
for this project specifically: the interface-score matrix is the method we
**retired**, and the story's pivot is why it could not work. Putting it on the
cover states the opposite of our finding. Use instead the single image the
whole project turns on — a phage spike meeting a sugar chain, not a protein.

**A-04** The core premise is wrong at the level of organism. Amber is justified
as "*Xanthomonas* is named for its yellow xanthomonadin pigment". Our host
genus is ***Pseudomonas***. That reasoning does not transfer and the colour
pair must be re-derived. See C-09 and B-02.

**A-05** Keep. No logo, name set in `display` type. Correct.

**A-06 (new)** Add a line naming what the system has to serve, because it is
not only a wiki: a 14-minute presentation video assembled from roughly 22
hand-drawn explainer animations, an 85-slide deck, the team wiki, and the
project's figures. Anything that cannot be used in all four is scoped to the
one it belongs to.

---

## §2 · B — Brand book

**B-01** Rewrite. The paragraph describes a dry-lab pipeline publishing a
digital phagogram. Replace with: *A visual language for a project about
bacteriophage host range — why a phage infects one* Pseudomonas *strain and
not its neighbour. It covers the team wiki, the presentation video and its
animations, the slide deck, and every figure the project publishes. It serves
both a wet lab and a dry lab, and it must not make one look more authoritative
than the other.*

**B-02** The two-colour premise must be re-derived. Amber-as-host-biology
depended on *Xanthomonas*. Replace with the semantics the animations already
use, which carry the story rather than the organism:

- `teal` — our own work, and a result that held.
- `rust` — a negative result, a failure, a warning, a verdict. **This project's
  pivot is a method that did not work**, so rust is load-bearing, not an
  accent, and it must never read as an error state to be hidden.
- `amber` — a highlighted detail inside a drawing: a tagged residue, a
  hydrogen bond, a His-tag. Never a whole field.
- `purple` — a third category where two will not do: a different sugar, a
  different strain, an insoluble fraction.
- `ink` — every outline and all body text. Never black.

A reader who learns these five should be able to read any figure in the
project by colour. Keep that sentence from B-02; change what it points at.

**B-03** Keep as written. English first, Traditional Chinese second, headings
with a slash, one `body` style for both. This matches how the team works. It
also applies to a planned Chinese voice track for the video.

**B-04** Scope it. "interaction matrix", "digital phagogram" and
"Step 3 — Feature weighting" are vocabulary of the *Xanthomonas* workstream.
Keep them, but under §W's own heading, and say so. Add the vocabulary this
project actually needs, in §W.

**B-05** Keep. Accessions, file paths and factor IDs in `accession` or `code`,
NCBI case preserved. Applies unchanged to our accessions and CDS identifiers —
and note that CDS numbering is load-bearing here: see W-new-04.

**B-06** Keep and extend. "Report a metric with its name and precision, not a
verdict" is exactly right for us. Extend the predicted/confirmed distinction to
a third word this project cannot do without: **retired** — a method that was
tested, failed its controls, and was abandoned on purpose. That is not a gap in
the work; it is a finding, and the video is built on one. Give it a word, a
token and a glyph like the others.

**B-07 through B-11** Keep. Surface levels, hairline versus border-control,
focus ring, contrast floors. Sound, and they apply to the wiki unchanged.

**B-12 through B-14** See §4.

**B-15 through B-17** Keep. The 4px scale, the radii, borders-not-depth.

**B-18** Keep. Add the team's official iGEM and college marks when available.

**B-19** Extend. "The `Diagrams` asset group holds the pipeline figures" is now
too narrow — see X-02. Also add the rule that matters most for us: **a figure
that shows real data is never redrawn by hand.** A gel, a spot test, a
phylogeny, a scored matrix goes on screen as itself. Redrawing one in a nicer
hand misrepresents a result, and that is precisely what gets scored.

**B-20** Update once the system points at this repository.

---

## §3 · C — Colour

Keep the structure, the contrast measurements and the dual themes. Three
changes.

**C-09, C-10, C-11** Rename `xanthos` / `xanthos-deep` / `on-xanthos`. The name
encodes *Xanthomonas*, which is not our organism. Keep the hexes — `#e2a019`
and `#734d07` are close to the `#C9A227` the animations already use, and
either value is fine. Rename to `accent` / `accent-deep` / `on-accent`, and
rewrite the usage: a highlighted detail inside a drawing — a tagged residue, a
hydrogen bond, a His-tag — not a field, and not the host side of anything.

**C-12, C-13** Keep `phage` and `on-phage` as the teal, but rewrite the usage.
It is not "the computational teal". In this project teal means **our own work,
and a result that held** — which is sometimes computational and sometimes a
spot test. Consider renaming it `ours` or `signal` so nobody infers that teal
means in-silico.

**C-18, C-19, C-20** The two-series scheme does not fit most of our figures.
`chart-phage` versus `chart-host` assumes every figure compares a phage
quantity against a host quantity. Ours compare: our result against a control;
three bacterial strains against each other; a present-day enzyme against three
reconstructed ancestors; a method against the controls that retired it. Replace
with a four-token scheme and say what each means:

- `series-ours` — our measurement, our construct, our strain. Teal.
- `series-control` — the control, the baseline, the parent. Neutral, dashed,
  directly labelled, recessive on purpose. Keep C-20's reasoning.
- `series-fail` — the series that did not separate, the retired method, the
  negative result. Rust.
- `series-alt` — a third category when two will not do. Purple.

Keep C-05's rule that the pair must survive greyscale and colour-vision
deficiency; apply it to all four.

**C-21, C-22** Keep, and keep the warning. `heat-high` and `heat-low` sit only
1.03:1 apart in lightness and are told apart by hue alone. This is not
hypothetical for us: the 7,182-pair interface-score heatmap uses that ramp, and
it appears in the video. Every instance needs a value legend and cell labels,
as V-11 and V-12 already say. Raise it from a note to a rule.

**C-23 (new)** Add `status-retired`, with its word and glyph, to go with B-06.

---

## §4 · T, S, R, D — Type, spacing, radius, depth

**T-01 through T-10** Keep the scale. Two notes.

**T-11 (new)** The specimens are set in the other workstream's vocabulary —
"Digital phagogram", "Step 3 — Feature weighting", "Six features per
phage–host pair", "Mean CAI against the host codon table". Reset them in this
project's language so the specimens teach the right words: *"Why one strain and
not its neighbour"*, *"Cycle 2 — Ask the protein what it is"*, *"The spike is
an enzyme, and it reads a sugar"*, *"263 of 264 reads carry the mutation"*.

**T-12 (new)** IBM Plex Sans is right for the wiki and the deck. It is **not**
right for the hand-drawn animations, where it reads as a technical figure —
the exact note already given twice on the deck. The animation layer needs its
own face: a humanist sans with slightly rounded terminals, legible on a
projector from the back of a room. Define it in the new §N as `hand`, and say
where the boundary between `sans` and `hand` falls.

**S-01 through S-08, R-01 through R-04, D-01, D-02** Keep. The 4px scale and
the radii carry over. D's "separate with borders, not depth" is also the right
instruction for the animations, where no shadow is allowed at all — say so.

---

## §5 · V — Data visualization

**V-01** Rewrite the premise with C-18's four-token scheme. "Every figure
compares a phage quantity against a host quantity" is not true of this project.

**V-02 through V-04** Replace with `series-ours`, `series-control`,
`series-fail`, `series-alt`. Keep V-04's reasoning about the recessive series
word for word; it is the best paragraph in the section.

**V-05, V-06** Keep.

**V-07, V-08** Scope to §W. Factor-versus-affinity scatters and overlaid factor
distributions belong to that workstream.

**V-09 through V-13** Keep, and harden V-11 and V-12 into rules per C-21.

**V-14, V-15** Scope to §W.

**V-16 (new)** Add rules for the figure types this project actually publishes,
because they are the ones that reach the judges:

- **Gel** — never recoloured, never redrawn, never cropped past its ladder.
  Annotate over the photograph. State which lanes are missing; ours lack a
  BL21 control lane on eight assays, and the caption says so.
- **Spot test** — always normalised to its control, with the control shown.
- **Phylogeny** — reconstructed nodes marked distinctly from observed tips;
  never imply a node is an extant sequence.
- **Structure render** — a reference for drawing, not evidence. Any render
  shown as a figure carries its method and its confidence measure.
- **Score matrix** — a value legend and labelled cells, always, per C-21.

---

## §6 · W — Pipeline and vocabulary

**W-01 through W-24** Keep, but move the whole section under a heading that
names it as one workstream: *"Workstream — phage–host infectivity
prediction"*. The seven steps, the six factors, the `f<NN>_<description>`
namespace, PHANOTATE/Prodigal, the phagogram vocabulary — all correct for that
line of work, all specific to it.

**W-25, W-26** Promote out of that section. The bilingual rules are
project-wide.

**W-new-01** Add the navigation this project uses, with the same weight the
seven steps are given. The work is told in **four Design–Build–Test–Learn
cycles**, and they are named the way the video names them:

| cycle | name | what it produced |
| --- | --- | --- |
| 1 | The wrong question | A 7,182-pair interface screen, retired by its controls |
| 2 | Ask the protein what it is | The spike is an enzyme reading a sugar, not a protein |
| 3 | Build the enzymes | Six constructs, three of them reconstructed ancestors |
| 4 | Let the bacteria answer | Resistant mutants sequenced; one mutation survives |

Name a cycle by number and title together, as W-01 does for steps.

**W-new-02** Terms to keep fixed, written exactly, in prose and in labels:

- **host range** — which strains a phage can infect. The project's subject.
- **O-antigen** — the sugar the tail spike reads. Not "the sugar coat" in a
  figure label.
- **tail spike** — the protein that reads it. Not "RBP" in prose; RBP is fine
  in code and filenames.
- **ancestral reconstruction** — inferring a sequence at an internal node.
  Never "ancestor protein" as though one were isolated.
- **retired** — a method tested, failed on its controls, abandoned on purpose.
  Per B-06.

**W-new-03** Attribution. Our weakest judging question two years running is
attribution. Make it a rule rather than a courtesy: any figure, method or idea
that came from an advisor, a PI or another team carries that credit in its
caption, in `body-sm` and `ink-muted`, in the same place every time.

**W-new-04** The one naming rule that has already caused an error. **CDS_0011
and CDS_0012 are two different proteins.** CDS_0012 is a TIM barrel matched to
endoglucanase 1ECE, with a different substrate from the O-antigen the CDS_0011
tail spike reads. All three reconstructed ancestors are CDS_0012's. Never draw
or describe them as domains of one protein. Use the PI's canonical `UUAIURNK_`
CDS index, never our earlier `FHABPWTM_` numbering.

---

## §7 · M — Components

**M-01 StatusTag** Keep. Add the `retired` state from B-06 and C-23.

**M-02 PhagogramTable** Keep, scoped to §W.

**M-new** The video is the project's largest deliverable and the system
currently builds nothing for it. Needed, each with a live preview:

*Drawing primitives* — bacterial envelope as three soft bands; a beaded sugar
chain and a field of them; a visibly different branched sugar; a capsule lying
over the chain tops; a hole being digested open through a layer; a
bacteriophage with head, collar, tapered spike and genome thread; a protein
blob with an optional tag dot; a chromatography column packed with resin beads;
a gel lane with and without a band; a dot-blot spot, light and dark; a row of
genes with flanking markers; a phylogenetic tree with tips and internal nodes;
a bar histogram; a matrix of scored cells; a curved pointer that extends into
place with its label; a verdict line, bold and underlined rather than boxed.

*Deck components* — eyebrow label, statement slide, figure slide with caption
and attribution line, card row.

The three hardest, and the ones to build first because every other animation
is easier than they are: the **rung-period histogram**, the **7,182-pair
matrix**, and the **cassette gene row**.

---

## §8 · X — Assets

**X-01** Keep the framing rule.

**X-02** Replace. `pipeline-workflow.jpeg` belongs to §W. The asset group this
project needs is already assembled and ready to upload:
`documents/2026-10-25_video_assets/`, **32 figures**, each one labelled in its
README with where it came from and which beat of the video uses it.

**X-04 (new)** Carry the README's own distinction into the system, because it
decides how an asset may be used:

- **reference** (11) — the animator looks at it and draws something new. A
  rendered protein surface never appears on screen as a PNG, but the animated
  shape must have its proportions.
- **on-screen** (21) — real data that appears as itself. Gels, spot tests,
  phylogenies, scored matrices. Per B-19, these are never redrawn.

**X-05 (new)** Still missing, and both come from the team rather than the
repository: California Botanic Garden interview footage and site photographs,
and the closing credits card.

---

## §9 · O — Open questions, answered

**O-01** IBM Plex Sans TC is on Google Fonts. Keep the bilingual stack. For the
animation layer this is moot — see T-12; that layer needs its own face.

**O-02** Answered: the name is **Phagenomics**, the team is **iGEM
Claremont-CA**. Per A-01.

**O-03** Attribution should be the team, not a person. Per W-new-03,
individual credit belongs in captions where it is specific.

**O-04** Keep the ramp, keep published figures as they are, and harden the
legend and cell-label requirement into a rule. Re-rendering published figures
this close to the deadline is not worth the risk. Per C-21.

**O-05** Answered by C-18: four semantic series, not three categorical ones.
`series-control` stays recessive and dashed for the reason C-20 gives.

**O-06** Team marks to follow.

**O-07** Answered by M-new. The next components are not FactorCard and a wiki
header — they are the drawing primitives, because 22 animations are blocked on
them.

---

## §10 — Sections to add

Four sections the system does not have, in the order they are needed. Together
they are the layer that makes 22 separately generated animations look like one
hand drew them.

### N · Hand and stroke

The animations are hand-drawn whiteboard, flat vector, white ground. Define:

- `hand` — the animation typeface. Humanist sans, slightly rounded terminals.
  Legible on a projector from the back of a room. Where `sans` ends and `hand`
  begins.
- Two stroke weights — one structural, one for detail inside a structure.
- The wobble: amplitude and frequency of the irregularity, as a number, so
  every generator produces the same hand.
- Round caps and round joins everywhere. No pure black; all outlines `ink`.
- No gradient, no shadow, no texture, no 3D. D's reasoning extended.
- Nothing axis-aligned and perfectly regular: a chain leans, a band undulates,
  a box is a little out of square.

### L · Animation layout

The grid the whole video is composed on. **1920 × 900, 30 fps, white ground.**

This is the section the first test clip most needed. It placed the drawing in
the left third and the text in the right third and left the middle dead. Over
22 clips that reads as slack. Define: a drawing zone, a label zone, margins,
how large a subject should be relative to the frame, what to do when a drawing
is wide versus tall, and where a verdict line sits. A label never sits over a
drawing.

### P · Drawing primitives

The list in M-new, each with a static preview and the parameters that vary:
how far a hole has opened, how far a bar has grown, how far a pointer has
extended. Every clip is assembled from these and nothing else.

### Q · Motion

Durations, easing curves by name, and the patterns. Named patterns needed:
enter and exit; a label replaced by the next label; a pointer extending to its
target; a group appearing one after another, staggered; something travelling
from A to B; emphasis on something already on screen; a value growing into a
bar.

Rules:

- Nothing moves at constant speed. Ease in and out, always.
- One idea moves at a time. Never two motions competing.
- The previous callout leaves before the next arrives.
- A drawing holds still long enough to be read after it finishes moving.
- Colour carries meaning. Never recolour for variety alone.

Write Q so that a prompt saying *"animate the phage adsorption sequence using
this system"* produces a clip that cuts together with the other 21 without
adjustment.

---

_Log: written 2026-10-25 against `Phagogram-design-system.pdf`, 18 pp.,
generated 2026-10-25 from `A1ex-Ch3n/iGEM_Claremont_2026@ecb9b7a`. Two
assumptions stated in §0: the spelling **Phagenomics**, and keeping the
Xanthomonas workstream scoped rather than deleted. Both need Alex to confirm._
