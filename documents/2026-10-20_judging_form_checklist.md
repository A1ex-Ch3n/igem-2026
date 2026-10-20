# Judging Form — the tick-as-you-go sheet

Form: `https://teams.igem.org/6317/judging-form/edit` · **freezes 2026-10-21 08:00 PDT**.
Full reasoning: [`2026-10-20_judging_form_final.md`](2026-10-20_judging_form_final.md).

**The first save IS the submission.** It stays editable until the freeze, but there is no
"save as draft". Everything below should be right before you press it.

---

## A · Text fields

| # | Field | Value | Done |
|---|---|---|---|
| A1 | Project Title | `Phagenomics` | ☐ |
| A2 | Abstract | the 148-word text in §B below | ☐ |
| A3 | G1 Part Name | `BBa_26TWEX42` | ☐ |

## B · Abstract, 148 of 150 words — paste exactly

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

No `Φ`, no en dashes, no `×`. If the field shows "*P. putida*" on its own anywhere, it is the
old text — replace the whole thing.

## C · The five links — open each FROM INSIDE the form

The form marks a link "Unseen" until it is clicked there, and an unseen link blocks its
confirmation checkbox. All five return 200 (checked 2026-10-20).

| # | Criterion | Link | Clicked |
|---|---|---|---|
| C1 | B3 Contribution | `https://2026.igem.wiki/claremont-ca/contribution` | ☐ |
| C2 | S1 Engineering | `https://2026.igem.wiki/claremont-ca/engineering` | ☐ |
| C3 | S2 Human Practices | `https://2026.igem.wiki/claremont-ca/human-practices` | ☐ |
| C4 | G1 Best New Basic Part | `https://2026.igem.wiki/claremont-ca/parts` | ☐ |
| C5 | G2 Best Software | `https://2026.igem.wiki/claremont-ca/software` | ☐ |
| C6 | G3 Best Model | `https://2026.igem.wiki/claremont-ca/model` | ☐ |

## D · The eight checkboxes — each is a declaration the team makes

| # | Box | What you are declaring | Tick |
|---|---|---|---|
| D1 | **B1** Deliverables | Wiki ✅ live · Judging Form ✅ being filled · Judging Session ✅ Nov 13, 07:35–08:00 PST · **Presentation Video ❌ due Oct 28, not started.** The wording is "has and will", so this is a promise | ☐ |
| D2 | **B2** Attributions | Form is Saved / Received; a few PI answers outstanding, which "will fully complete" covers | ☐ |
| D3 | **B3** Contribution | the `/contribution` page presents the evidence | ☐ |
| D4 | **S1** Engineering Success | one full design cycle is documented | ☐ |
| D5 | **S2** Human Practices | the page is now 36 kB after the rewrite | ☐ |
| D6 | **G1** confirmation | Best New Basic Part | ☐ |
| D7 | **G2** confirmation | Best Software | ☐ |
| D8 | **G3** confirmation | Best Model | ☐ |

**Leave B3's optional Part-name field empty** — it is for documentation added to someone
else's part. **Leave S1's optional Part-name field empty** too.

## E · The three prizes

| Slot | Prize | List |
|---|---|---|
| G1 | Best New Basic Part | General Bio Engineering |
| G2 | Best Software | Specializations |
| G3 | Best Model | General Bio Engineering |

Legal: two from General Bio Engineering, one Specialization. Fewer than three forfeits Gold.

## F · Last look before Save and submit

- ☐ Summary line no longer says "3 selected but not confirmed"
- ☐ Abstract word count is 148, and the species sentence reads "an unnamed relative in the
  Pseudomonas putida group"
- ☐ G1 Part Name is `BBa_26TWEX42`, not `BBa_26DKNAEC`
- ☐ All five links show as seen

Then **Save and submit**.

## G · Not on this form, but before the same freeze

| | What | Who |
|---|---|---|
| G-a | `/parts` still says the six parts are "still in Draft… must be submitted before the freeze" and Table 1 still reads "BBa_— pending submission". Fix is written, in the cloned wiki repo; needs a gitlab push | Alex |
| G-b | Eight wiki pages render `wiki-todo` boxes to judges, four on `/parts` alone, one of which says "confirm … before freeze". One-line kill switch documented at `static/style.css:705` | Alex decides |
| G-c | Presentation Video, due Oct 28 — the only thing D1 promises that does not exist | team |

---
*Log — 2026-10-20: written as the fill-in sheet. Link status, part status and abstract word
count all verified live the same morning.*
