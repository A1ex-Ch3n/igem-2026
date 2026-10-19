# Which three special prizes we should nominate

Gold is decided by three Special Awards named on the Judging Form. **All three
must pass** — a judge's rubric score for each becomes their Gold vote. So the
right question is not "which three are most ambitious" but "which three are we
least likely to lose". At least one from General Bio Engineering, at least one
from Specializations.

Assessed 2026-10-19 against the live wiki and the repository, not from memory.

## Recommendation

| | prize | list | confidence |
|---|---|---|---|
| **1** | **Best Model** | General Bio Engineering | **high** |
| **2** | **Best Software** | Specializations | **high — the licence objection was wrong; one upload left** |
| **3** | **Best New Basic Part** | General Bio Engineering | medium |

Confirmed by Alex on 2026-10-19. The Judging Form has been updated accordingly.

---

## Best Model — our strongest claim

Criterion: *"build or apply a model and use it to inform design, predict
behavior, or interpret results, before or alongside their experimental work."*

That is literally what happened. `/model` (11.7 kB) tells it as four tracks that
each exist because of what the previous one returned:

- **A receptor catalogue** — 441 surface receptors across five isolates, 178
  ortholog clusters, cross-referenced against PharBP (6,376 *Pseudomonas* host
  entries) to find *P. putida* KT2440 as the informative surrogate host.
- **A screen we retired, with the controls that killed it** — 114 RBPs × 63
  receptors = 7,182 ESMFold pairs; scores correlated with protein size
  (*r* = +0.58); a nine-fold control validation showed the interface score is
  non-informative for cross-kingdom pairs. Retired and documented.
- **The structure work that replaced it** — and which changed the project:
  the recognition step is protein–sugar, not protein–protein.
- **An O-antigen comparison** answering the host-range question that followed.

Why this wins points other teams lose: most teams show a model that agreed with
them. We show a model with a **quantified failure mode, a control experiment
against our own method, and a decision that followed from it**. That is the
behaviour rubrics reward.

**One honesty point to manage.** The ancestral reconstruction and the ZymCTRL
scoring are the PI's work (his questionnaire answer A1), and judges score "how
much of the project was initiated and led by the students" separately. The
`/model` page should lead with the four student-run tracks and present the ASR
and language-model scoring as the PI's contribution. Do not centre the
nomination on ZymCTRL.

## Best Software — the best return on two hours of work

Criterion: *"Born out of practical need, these tools can be surprisingly useful
for others, and they don't have to be large or complex… This award finds and
honors such 'nuggets' of computational work."* That is an unusually good match
for what we actually have.

`/software` (6.4 kB) is already live and already written the way the criterion
asks: 14,516 lines across 126 files, honest about how much is project glue, and
**four units ranked by how much work it would take someone else to use them** —
the SDS-PAGE densitometry tool (ladder calibration, lane detection, apparent-MW
estimate; only PIL, NumPy, SciPy), the O-antigen locus comparator (works from any
Bakta or Prokka annotation, where PAst is *P. aeruginosa*-only and Kaptive has no
*Pseudomonas* database), the resistant-mutant workflow, and `phagecheck`.

**The licence objection was wrong** (checked 2026-10-19): `software/LICENSE` is
already **MIT**, and `software/README.md` already explains that the split from the
repository's CC BY 4.0 exists precisely because Best Software requires an
OSI-approved licence. Earlier notes in this repository, and the memory entry
behind them, said the CC BY 4.0 licence blocked this award. It does not. The root
`README.md` wording has been corrected to stop implying that the analysis code is
CC BY 4.0 across the board.

**One blocker remains: the code is not submitted.** The Software deliverable on
the dashboard reads **"No Submissions"**, and the rules require the source on the
dedicated iGEM repository at `gitlab.igem.org`. That is an upload, not work.

**One correction to make first.** `software/README.md`, `phagecheck/dtr.py` and
`software/docs/architecture.md` all claim the DTR check "corrected our own call
on phage 9-2-1 Φ8 — reported circular, actually linear with a 77 bp DTR". That
check returned *circular*, and we have now decided the PI's circular assembly
governs. Shipping a headline provenance claim that is backwards into a software
nomination is the kind of thing a judge finds. Fix or remove it.

## Best New Basic Part — good documentation, thin evidence

`/parts` is the largest page on the wiki (16.9 kB) and the six drafts are
thorough. Three of them are sequences that exist nowhere in nature, which is
genuinely distinctive.

**But the criterion says in the form itself:** *"Winning parts come with thorough
documentation **and experimental data showing the part works**."* We cannot show
that. The expression record is 0915 inconclusive, 0929 two unassigned bands, and
1010 the e281 Ni-NTA elutions came back as a blank gel — with no BL21 control
lane after three gels. The documentation is strong; the "it works" half is not
there.

It also needs a registered `BBa_` number before the form will accept it, which
depends on the Registry upload finishing.

Keep it as the third nomination — the documentation really is good and the
ancestral panel is memorable — but it is the one of the three most likely to
cost us Gold.

## Best Integrated Human Practices — high ceiling, unproven

`/human-practices` is 6.5 kB, the thinnest page on the wiki, and is being
rewritten tonight. The raw material is genuinely good: Ilia's feedback moved the
wet lab away from purification and large-scale production toward small-scale
targeted blots, and the IBC review raised a specific question we have to answer.
That is exactly the loop the criterion wants — *"How did that feedback enter your
work throughout the Competition?"*

The problem is timing. This page has to be strong anyway, because it is also the
Silver S2 criterion. Nominating it adds a Gold dependency on work not yet done.
Decide after tonight's rewrite, not before.

## Ruled out

- **Best Part Collection** — the collection page does not exist, and it inherits
  the same "does it work" weakness as Best New Basic Part.
- **Best Measurement** — underrated on the evidence (EOP susceptibility matrix,
  OD600 growth curves across a dozen notebooks, the fluorometer work, and the
  gel densitometry tool is a measurement method with calibration and units) but
  `/measurement` does not exist and there are two days left.
- **Safety and Security** — the Safety Check-in Form shows "Deadline Missed" on
  our own dashboard, where a judge can see it.
- **Best Education, Inclusivity, Sustainable Development, Entrepreneurship,
  Hardware, Alternative Platform** — no evidence in the repository at all.

## What this changes on the Judging Form

The form currently holds Best New Basic Part / Best Integrated Human Practices /
Best Model, entered 2026-10-18 and **not saved**. The recommendation swaps
Integrated Human Practices for Best Software. Still legal: Model and Basic Part
are General Bio Engineering, Software is a Specialization.

Swap made 2026-10-19. The form still holds the selections unsaved.

---

**Log**

- 2026-10-19 — assessed against the live wiki and the 2026 criteria text.
