# Judging Form — the final text, field by field

Form: `https://teams.igem.org/6317/judging-form/edit` · **freezes 2026-10-21 08:00 PDT**,
which is **tomorrow morning**.

Everything below is the text to put in, in the order the form asks for it. The field-by-field
transcription and the history of how each answer was reached live in
[`2026-10-18_judging_form_draft.md`](2026-10-18_judging_form_draft.md); this file is what to
work from at the keyboard.

**"Save and submit" means submit.** The page says "Saving submits your form to iGEM. You can
edit it until Oct 21, 08:00 PDT." Editable after saving, but the first save is a submission.
Nothing has been saved yet.

**Type plain ASCII into every field.** No `Φ`, no en dashes, no `×`. The form has not been
tested for encoding and a mojibake abstract is a bad way to meet a judge.

---

## 1 · Project Title

```
Phagenomics
```

Already the wiki's title and the public branding. No reason to change it the day before freeze.

---

## 2 · Abstract

Hard limit: **150 words**. The text below is **148**, counted. It is the corrected version —
the species error is fixed and the Greek letter and en dashes are gone. Paste it exactly.

```
Phage therapy's bottleneck is host range: each phage binds a specific receptor on a specific
strain, so matching phage to target means screening, not design. We isolated our own system
from soil at the California Botanic Garden: Pseudomonas capeferrum and an unnamed relative in
the Pseudomonas putida group, with their co-occurring phages. Phage Phi8 is novel: 62,339 bp,
80 CDS, no database match, no virulence or resistance genes. Modelling then redirected the
project. Structure prediction and protein language models showed the recognition step is not
protein-protein: the receptor-binding apparatus is branched, and one accessory protein is a
depolymerase degrading the bacterial polysaccharide layer. The key interaction is
protein-sugar. We therefore asked whether ancestral depolymerases were more generalist,
reconstructing ancestors of the phage's GH5 glycoside hydrolase, scoring them with an
enzyme-conditioned language model, and expressing modern and ancestral enzymes in E. coli,
reporting what worked and what did not.
```

**Why it had to be retyped.** The version typed into the form on 2026-10-18 said
"*Pseudomonas capeferrum* and *P. putida*". **We have no *P. putida*.** Our own data says so
twice: sourmash/GTDB places four of the five isolates in ***Pseudomonas_E* sp013179515**, an
unnamed species, with only 8-10-2 in *P. capeferrum*; and synthesis row A5 records **89.4 % ANI
to *P. putida***, far below the 95 % species threshold, the closest public relative being
*Pseudomonas* sp. CM27 at ~99.2 %. *P. putida* enters this project only as the **surrogate
host** in the receptor-overlap analysis (KT2440), which is almost certainly where the drift
came from. It matters for the story too: the phage's host is **Strain 2 (9-2-1 / 9-6-2) =
sp013179515**, not *capeferrum*.

"An unnamed relative in the *Pseudomonas putida* group" is the honest phrasing and is what the
line above says. *P. capeferrum* is itself in that group, so the sentence is consistent.

---

## 3 · Bronze — all three required

### B1 · Competition Deliverables

Checkbox: *"I confirm that my team has and will fully complete the required deliverables"* —
Wiki, Judging Form, Presentation Video, Judging Session.

→ **Tick.** Wiki is live, this form is being filled, the Judging Session is scheduled for
**Nov 13, 07:35–08:00 PST**.

⚠️ The **Presentation Video is due Oct 28 and has not been started**. The confirmation reads
"has and will", so ticking is honest only if the video actually gets made. It is the one
checkbox on this form that is a promise rather than a report.

### B2 · Project Attributions

Checkbox: *"I confirm that my team will fully and accurately complete the Attributions Form on
time."*

→ **Tick.** The form is Saved / Received; a few PI answers are still outstanding, which is what
"will fully complete" covers.

### B3 · Contribution

Optional Part-name field — for documentation added to *someone else's* part. We are not doing
that: **leave empty**.

Required link:

```
https://2026.igem.wiki/claremont-ca/contribution
```

✅ live, 21 kB. Open it from inside the form — the form marks every link "Unseen" until it is
clicked there, and an unseen link blocks the confirmation.

→ **Tick** the confirmation after opening it.

---

## 4 · Silver — both required, plus Bronze

### S1 · Engineering Success

Optional Part name — may name a part. Suggest leaving it empty: the engineering cycle we
document is the modelling-to-construct loop, not a single part, and naming one here invites the
same "does it work" question that G1 already has to answer.

Required link:

```
https://2026.igem.wiki/claremont-ca/engineering
```

✅ live, 30 kB. → **Tick** after opening it from the form.

### S2 · Human Practices

Required link:

```
https://2026.igem.wiki/claremont-ca/human-practices
```

✅ live, **36 kB** — the rewrite landed. It was 6.5 kB and the thinnest page on the wiki when
this was last assessed on 2026-10-19; it is now one of the larger ones.

→ **Tick** after opening it from the form.

---

## 5 · Gold — three special prizes

Rules: at least one from **General Bio Engineering**, at least one from **Specializations**,
third from either. All three are scored; fewer than three forfeits Gold outright.

| slot | prize | list | required link | state |
|---|---|---|---|---|
| **G1** | **Best New Basic Part** | General Bio Engineering | `https://2026.igem.wiki/claremont-ca/parts` | ✅ live, 42 kB |
| **G2** | **Best Software** | Specializations | `https://2026.igem.wiki/claremont-ca/software` | ✅ live, 21 kB |
| **G3** | **Best Model** | General Bio Engineering | `https://2026.igem.wiki/claremont-ca/model` | ✅ live, 28 kB |

Legal: Model and Basic Part are General Bio Engineering, Software is a Specialization.
Confirmed by Alex 2026-10-19.

### G1 needs a part number — and the choice is worth five minutes

Selecting Best New Basic Part opens a required `Part Name*` field that only accepts a `BBa_`
name. **All six are now `published`, so any of them is accepted. Enter:**

```
BBa_26TWEX42
```

**Decided 2026-10-20 by Alex**, replacing `BBa_26DKNAEC` (CDS11_WT, the tail-spike body), which
was entered on 2026-10-19 as the headline part but has no experimental evidence behind it.

**The dot blot has since changed the evidence picture, and the criterion is explicit:**
*"Winning parts come with thorough documentation **and experimental data showing the part
works**."*

| candidate | documentation | experimental evidence |
|---|---|---|
| `BBa_26DKNAEC` CDS11_WT | strong — structure-led domain boundaries, trimer, foldon | **none at all.** No band at 72.0 kDa in three gels; not on the dot-blot membrane |
| `BBa_26TWEX42` Node1 | strong — full ASR method, 0.28 Å to the WT model | **the most in the project**: anti-His positive at 2.4x, and the only activity signal we have (12 % colony suppression) |
| `BBa_267WQM51` CDS12_WT | strong — 4/4 AF3 templates are GH5 endoglucanases, pLDDT 95–98 | one induction-dependent band at the predicted mass; the dot blot did not reproduce it |

**Decided: G1 is `BBa_26TWEX42`.** It is the only part with both halves of what
the criterion asks for, and the ancestral story — a sequence that exists nowhere in nature,
reconstructed, synthesised, expressed, and carrying the one activity signal in the project — is
more memorable than a fiber fragment with no data. The caveat is honest and already written on
the part page: that activity is not yet attributed to the protein, because phage carry-over has
not been excluded.

**Against the switch:** CDS11_WT is what the `/parts` page is built around and what the
narrative leads with, so a judge following the link lands on the tail spike's story, not
node 1's. If the page is not going to be re-pointed tonight, consistency may be worth more than
evidence.

`/parts` is still built around the tail spike, so a judge following the G1 link lands on
CDS11_WT's story rather than node 1's. That is the cost of the switch and it is accepted: the
page documents all six and the node 1 entry carries the evidence.

### What each nomination rests on, if a judge asks

**G3 Best Model** — our strongest. Four tracks on `/model`: a 441-receptor catalogue across
five isolates cross-referenced against PharBP; a 7,182-pair ESMFold screen that we **retired**
after a nine-fold control showed the interface score is non-informative for cross-kingdom pairs
and correlates with protein size (*r* = +0.58); the structure work that replaced it and
redirected the project to protein–sugar; and an O-antigen comparison. A model with a quantified
failure mode and a decision that followed from it is what the rubric rewards.
*Honesty point:* the ASR and the ZymCTRL scoring are the PI's work. Lead with the four
student-run tracks; do not centre the nomination on ZymCTRL.

**G2 Best Software** — `/software`, 14,516 lines across 126 files, honest about how much is
project glue, with four units ranked by how much work it would take someone else to use them:
the SDS-PAGE densitometry tool, the O-antigen locus comparator, the resistant-mutant workflow,
and `phagecheck`. `software/LICENSE` is **MIT** — the old CC BY 4.0 objection was wrong.

**G1 Best New Basic Part** — six parts, all `published` as of this morning, three of them
sequences that exist nowhere in nature. The documentation is genuinely thorough. The "it works"
half is thin and the pages say so.

---

## 6 · Awards we are in by default — no action

Best Foundational Advance Project (our village), iGEM Spirit Award, Best Project Promotion
Video, Best Presentation, Best Wiki, iGEMers Prize.

Best Presentation and Best Wiki are scored on the same ballot questions as the Presentation and
Wiki sections of the general ballot, so the video and the wiki carry weight past Bronze.

---

## 7 · Before anyone presses Save and submit

**Two things on `/parts` are judge-visible and wrong.** It is the G1 link; a judge will open it.

1. **Table 1 still reads `Part number: BBa_— pending submission` / `Name: To fill in`** — on
   the headline part's own record table. The number is `BBa_26DKNAEC`.
2. **A paragraph still says the six are "still in Draft status… not yet submitted for biosafety
   screening and are not publicly visible… They must be submitted before the freeze."** As of
   this morning that is false: all six are `published`. Left standing, it tells a judge our
   parts are not submitted.

**One date to check.** `/parts` says "the 10-01 gels show e1 eluting at its predicted mass".
Our own records have gels on 2026-09-15, 09-29 and 10-10, and the 10-10 Ni-NTA on e281 came
back blank. If 10-01 is a typo it should be fixed; if there is a 10-01 gel the rest of the
repository does not know about it, that is worth knowing tonight.

**Then, in the form:** open each of the five required links from inside the form so they stop
reading "Unseen", tick B1 / B2 / B3 / S1 / S2 and the three prize confirmations, enter the
`BBa_` name under G1, and press **Save and submit**.

The summary line should stop reading *"Not eligible for any medal · no special prize
(3 selected but not confirmed)"*.

## Blockers, current

| was | now |
|---|---|
| ~~`/contribution` does not exist~~ | resolved 2026-10-19, live at 21 kB |
| ~~six Registry parts still in Draft~~ | **resolved 2026-10-20 — all six `published`, licence CC0 on all six, collection holds all six** |
| ~~Human Practices page too thin for S2/G2~~ | rewritten, 36 kB |
| three special prizes need the team's agreement | confirmed by Alex 2026-10-19; G1's **part number** is the one open choice |
| Presentation Video must actually be made | **still open** — due Oct 28, not started, and B1 promises it |
| `/parts` placeholders and the "still in Draft" paragraph | **still open — fix before saving** |

---

**Log**

- 2026-10-20 — written as the paste-ready version. Wiki link status, part status, licence and
  collection membership all re-checked live this morning rather than carried over: five
  required links return 200, `/measurement` and `/safety` still 404 (neither is nominated), all
  six parts report `published`. Abstract word count verified at 148. The G1 part choice is
  reopened because the 2026-10-19 dot blot gave two parts evidence that `BBa_26DKNAEC` does not
  have.
