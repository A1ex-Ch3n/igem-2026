# What each of the three nominated prizes still needs

Nominations now on the Judging Form (entered, **not saved**):
**Best New Basic Part** · **Best Software** · **Best Model**.
Two from General Bio Engineering, one Specialization — the rule is satisfied.

Each prize has one required wiki link that a team member must **open from inside
the form** before its checkbox counts. The form marks them "Unseen" until then.
All three pages already exist.

Freeze: **2026-10-21 08:00 PDT**.

---

## 1 · Best New Basic Part → `/parts`

Required link: `https://2026.igem.wiki/claremont-ca/parts` ✅ live, 16.9 kB —
the largest page on the wiki.
Part entered on the form: **`BBa_26DKNAEC`** — the Φ8 tail-spike β-helix
depolymerase, CDS_0011 residues 305–941. Chosen because it is the project's
headline part, its domain boundaries came from structure prediction rather than
guesswork (Calx-β anchor and flexible shaft excluded; rigid trimeric body kept
from residue 305, 0.44–0.99 Å model RMSD), and it is the one a judge can see a
reason behind. Change it if the team prefers an ancestral part.

**Blocking, and nothing else matters until it is done:**

- **All six parts are still in Draft on the Registry.** The `/parts` page says so
  itself: "a draft is created, not submitted… They must be submitted before the
  freeze." A Draft part is not screened for biosafety and is not publicly
  visible, so a judge cannot read it. The form's own text requires the part to be
  "fully documented in the Registry".

**Needs writing:**

- **Table 1 on `/parts` still has placeholders** — `Part number: BBa_— pending
  submission` and `Name: To fill in`. The real numbers exist
  (`BBa_26DKNAEC`, `BBa_269KJB8G`, `BBa_26TWEX42`, `BBa_26LHLSLW`,
  `BBa_267WQM51`, `BBa_26EK89VW`). Fill them in; a placeholder on the page a
  judge is sent to is the most avoidable loss on this list.
- **The honest "does it work" paragraph.** The criterion, in the form's own
  words: *"Winning parts come with thorough documentation **and experimental data
  showing the part works**."* We cannot claim that. What we can do is state
  plainly what the expression record shows — 2026-09-15 inconclusive, 2026-09-29
  two unassigned bands at 40–43 kDa and 45–50 kDa, 2026-10-10 the e281 Ni-NTA
  elutions came back blank — say that no BL21 control lane has yet been run
  across three gels, and say what the next experiment is. Judges score candour
  far better than silence; the Results page already takes this tone.
- **Plasmid maps.** Asked for directly in the 2026-10-18 meeting, and they exist
  nowhere in the repository. Six pET-28a constructs, each with an N-terminal
  His6 leader — one figure covers all six.

## 2 · Best Software → `/software`

Required link: `https://2026.igem.wiki/claremont-ca/software` ✅ live, 6.4 kB.
Criterion, from the form: *"impactful software tools or computational methods…
To be eligible, your software must be well-documented and made available under
an **OSI-approved open-source license**."*

**The licence is already fine.** `software/LICENSE` is MIT; only the non-code
content is CC BY 4.0, and `software/README.md` explains the split. An earlier
note in this repository said the licence blocked this award — that was wrong, and
it has been corrected along with the root `README.md` wording.

**Blocking:**

- **The Software deliverable reads "No Submissions."** The rules require the
  source code on the dedicated iGEM repository at `gitlab.igem.org`. This is an
  upload, not work, and it is the only thing standing between us and eligibility.

**Needs writing:**

- **Fix the provenance claim, first.** `software/README.md`,
  `software/phagecheck/dtr.py` and `software/docs/architecture.md` all say the
  DTR check "corrected our own call on phage 9-2-1 Φ8 — reported circular,
  actually linear with a 77 bp DTR". That check returned *circular*, and we have
  since decided the PI's circular assembly governs. A headline claim that is
  backwards, in the one artefact a Best Software judge will read closely, is a
  real risk. Rewrite it as what actually happened: the check distinguishes two
  cases an assembler reports identically, and on our own genome it returned
  circular, which is the call we now stand behind.
- **The six judging aspects** the 2026 criteria name, which the page does not yet
  address one by one: synbio-standards compatibility (SBOL, RFCs, data formats) ·
  how well validated, including *test data or benchmarking* · usefulness to other
  projects · integrability (APIs, packages) · user-friendliness · how well written
  and documented for future groups, specifically naming **architecture diagrams**
  and **installation and execution scripts**. We already hold most of the
  evidence — `benchmarks/` is literally a control study, `environment.yml` and
  `examples/` exist, 23 of ~30 code directories carry a README, and
  `docs/architecture.md` is a diagram. The page needs to *say* so against each
  aspect.
- **One worked example per tool**, input to output, so a reader can see the thing
  run without cloning anything.

## 3 · Best Model → `/model`

Required link: `https://2026.igem.wiki/claremont-ca/model` ✅ live, 11.7 kB, and
already the best-structured page on the wiki.
Criterion: *"build or apply a model and use it to inform design, predict
behavior, or interpret results, before or alongside their experimental work."*

Nothing blocks this one. Two things would strengthen it:

- **Lead with the student-run tracks, and attribute the rest.** The ancestral
  reconstruction and the ZymCTRL scoring are the PI's work — his own answer A1
  says so. The four tracks the students ran (receptor catalogue, the retired
  binding screen with its controls, the RBP structure work, the O-antigen
  comparison) are the nomination. Judges score "how much of the project was
  initiated and led by the students" as a separate ballot question, so an
  unattributed ZymCTRL section costs points twice.
- **Say the decision out loud.** The page tells the four tracks as a sequence,
  which is right, but the single most persuasive sentence is not yet prominent:
  *the model told us the interaction we had designed the project around does not
  exist, we ran a nine-fold control to confirm it, we retired the screen, and we
  rebuilt the project around protein–sugar recognition.* That is a modelling
  result that changed a wet lab, which is exactly what the award is for. Put it
  at the top.
- Optional, cheap: the Foldseek evidence behind the Bcep22-like *Gervaisevirus*
  assignment, and the ZymCTRL perplexity figure (panel D of the PI's main figure)
  — both already in hand, both clearly marked as the PI's.

---

## Everything above, as a to-do list

1. **Submit the six Registry parts out of Draft.** Blocks Best New Basic Part and
   the Registry deliverable both.
2. **Push the code to `gitlab.igem.org`.** Blocks Best Software eligibility.
3. **Fix the backwards DTR provenance claim** in three files under `software/`.
4. **Fill the `BBa_` numbers into Table 1 on `/parts`** and delete "To fill in".
5. **Write the expression-results paragraph on `/parts`**, negative results
   included.
6. **Draw the plasmid maps.**
7. **Re-order `/model`** to lead with the decision and the student tracks, with
   the PI's contribution marked.
8. **Answer the six Best Software aspects explicitly on `/software`.**
9. In the form: open all required links, tick the eight confirmations, press
   **Save and submit**.

Items 1, 2 and 9 are the ones that lose medals if missed. The rest are points.

---

**Log**

- 2026-10-19 — written after the prize swap; nominations are Basic Part,
  Software, Model.
