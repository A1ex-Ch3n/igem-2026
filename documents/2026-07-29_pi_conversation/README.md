# 2026-07-29 — notes from the conversation with Prof. Espinoza

> Chat of 2026-07-29, 10:50–11:17. Five questions went out, three came back, and
> two new work items arrived that were not on anyone's list before.
>
> This is the shared record of what was agreed, what is now on each side's plate,
> and what still needs an answer. Verbatim quotes are kept so the reading can be
> checked. Chinese version: [`README_zh.md`](README_zh.md). Raw transcript:
> [`transcript.md`](transcript.md).

---

# To do

## Alex

| # | Item | From | Note |
|:--|:-------------------------------|:-----------------|:----------------|
| A1 | ~~Identify the date of the host-range entry~~ → **it is the 2026-07-04 entry** | "I will need help identifying the date" | ⚠️ the date was already in the 10:53 message, so possibly what is needed is the page rather than the date |
| A2 | **Digitize every notebook entry after 06-12** | "once I land in Ontario" | the 07-04 page is in that batch |
| A3 | **Draw the virion cartoon** in the style of Latka 2019 group D | "You can draw a similar cartoon to that" | must "justify this with synteny and similarity" |
| A4 | **Fold the virion proteins and turn them into printable objects** | "we could print the proteins and assemble it" | colour: baby blue |
| A5 | Read up on [phagos.com](https://www.phagos.com/) | "basically what we are trying to do" | |
| A6 | Shortlist of to-dos + updated figures and summary for review | | |
| A7 | **Parts list for the fluorometer** | "remember we are going to print a fluorometer" | to be ordered once Alex is back |

## Prof. Espinoza

| # | Item | Status |
|:--|:-------------------------------|:----------------|
| P1 | Retrieve the **host-range table** (the 2026-07-04 entry) | this week |
| P2 | Build the **GH5 tree + ancestral state reconstruction**, then express the ancestral enzymes | in progress |
| P3 | **Express CDS_0010** to characterise it | constructs ordered |
| P4 | Work through the **MGnify** search results | "a lot of sequences! have not been able to digest" |

## Analysis side

| # | Item | Why |
|:--|:-------------------------------|:--------------------------|
| C1 | Change **CDS_0010 to "unknown protein"** across the repository | the glycosidase reading has been withdrawn |
| C2 | **Rename our copies of the three constructs**, and keep C-terminal-tag detection out of downstream design | tags are N-terminal by design; the filenames say otherwise |
| C3 | Build the **synteny + similarity evidence** for the group D assignment | required before the cartoon |
| C4 | Confirm the structural-module assignment of CDS_20/08/09/13/14 | these are what make the podovirus call without TEM |
| C5 | ~~Check whether CDS_0010 carries a T4gp10-like fragment~~ → **done: it does not** | `code/0729_t4gp10_check/`; group D now rests on architecture + synteny |
| C6 | Update the host-range statements once the table arrives | we currently record "never tested", which is really "we do not have it" |

---

# What was settled

## 1. Construct tagging — deliberate; only our filenames are wrong ✅

> **Cesar:** I have placed the order for the first 3 constructs
> **Cesar:** Yeah I don't want a c terminal tag on any of them
> **Cesar:** All of them have an n terminal tag
> **Cesar:** Cleaved by two different enzymes

This matches the sequences exactly:

| Construct | N-terminus | Cleavable by |
|:-----------|:-----------------------------------------|:-----------------------------|
| CDS_0011 | pET-28a leader + designed `GGSGGGGS`-His6-`ENLYFQ` | **thrombin** (vector LVPR↓GS) + **TEV** (ENLYFQ↓) |
| CDS_0010 | pET-28a leader only | thrombin |
| CDS_0012 | pET-28a leader only | thrombin |

So "two different enzymes" is CDS_0011 carrying both the vector's thrombin site
and the designed TEV site, letting the tag come off in two stages.

The design also agrees with our 0716 analysis, which recommended an N-terminal
tag because res 921–941 looks like a trimerization foldon. **The only problem is
that `CDS11_WT_CTERM_HIS6TAG` is named for the opposite of what it contains, and
both `NOTAG` constructs do carry the vector's N-terminal His6.** We will rename
our copies; the constructs themselves are right.

## 2. CDS_0010 is an unknown protein ✅

> **Cesar:** Yeah I dont know what CDS 10 is
> **Cesar:** I thought it was a hydrolyase but not sure
> **Cesar:** I am expressing so maybe we can characterize it
> **Cesar:** but for now the focus is CDS11 and 12

This closes the question and agrees with our template analysis — the only hit on
the CDS_0010 body is a weak IspD match over res 361–456, with no template at all
over the remaining ~460 aa. We will record it as **unknown, expression pending**.

## 3. Metagenome sequences without hosts ✅

> **Cesar:** The metagenome side doesnt matter if they are not associated to any host

Agreed, and this is the same conclusion our 07-12 methodology review reached.

> **Cesar:** I was looking earlier and I think we can go bigger
> **Cesar:** and I did MGnify … to search for more sequences
> **Cesar:** a lot of sequences! have not been able to digest

For our own planning we are treating the MGnify set as a way to deepen the
alignment rather than as a route to host assignment, since those sequences are
unlabelled too — but you may well have other uses for it in mind, so we have not
assumed either way. Which analysis to run is still open (below).

---

# New direction: ancestral GH5 depolymerases

> **Cesar:** My current hypothesis (and this is how science works, directional changes ocurr)
> **Cesar:** is that CDS_12 (depolymerase) could improve host range by breaking different glycans
> **Cesar:** SO I am building a tree with all GH5 sequences and reconstruct acestrtal states to express them
> **Cesar:** if we challenge the affinity of the tail fiber and the differetn depolymerases in trans
> **Cesar:** maybe there affinity changes
> **Cesar:** all of this is under the caveat that the affinity ~ biding ~ infection
> **Cesar:** whihc is a safe assumption and we can make it clear

As we understand it:

1. **Hypothesis** — CDS_0012 (GH5) can broaden host range by cleaving different glycans.
2. **Method** — a tree over all GH5 sequences → **ancestral state reconstruction** → express the ancestral enzymes.
3. **Experiment** — combine the tail fibre with different depolymerases **in trans** and see whether affinity changes.
4. **Stated caveat** — this assumes `affinity ~ binding ~ infection`, to be made explicit in writing.

This changes the role CDS_0012 plays in our story. It had been a supporting
character — a separate protein, not a domain of the tail spike — and it now
becomes the engineerable one: the tail spike decides *who* is recognised, the
depolymerase decides *what can be cut open*.

It also connects to the O-antigen result. The three host strains carry three
non-homologous O-antigen cassettes in the same genomic slot, so if the
depolymerase determines which glycan can be processed, **swapping the
depolymerase is a plausible route to swapping host range** — which is the space
the ancestral reconstruction would be sampling.

---

# New task: the virion cartoon and the group D assignment

> **Cesar:** Our phage is a T7-like podophage
> **Cesar:** Basically looks similar to group D,
> **Cesar:** the long one is the tail (CDS 11) and short one (at least one) is the depolymerase
> **Cesar:** You can draw a similar cartoon to that
> **Cesar:** you need to justify this with synteny and similarity
> **Cesar:** basically CDS 20, 08, 09, 13, 14 … maybe not 20
> **Cesar:** 20, 8, 9, 13, 14 really tell (without TEM) that it is a podo/t7 like
> **Cesar:** by syntenic assumptions (10,11,12) are the ones that hang from the base and recognize the host

| CDS | Assignment in the conversation | Our annotation (canonical `UUAIURNK_`) |
|:-----|:-------------------------|:-----------------------------------------|
| 0020 | funnel / base plate ("maybe not 20") | portal protein, 742 aa |
| 0008 | as above | internal virion protein, 577 aa |
| 0009 | as above | tail fiber protein, 118 aa |
| 0013 | as above | virion structural protein, 201 aa |
| 0014 | as above | structural protein, 232 aa |
| 0010 | hangs from the base, recognises the host | tail protein, 917 aa — **unknown function** |
| 0011 | "the long one" = tail | tail spike, 941 aa — β-helix depolymerase |
| 0012 | "the short one" = depolymerase | GH5 TIM barrel, 477 aa |

## An observation that may be worth following up

The cartoon comes from **Latka, Leiman, Drulis-Kawa & Briers (2019),
*Front. Microbiol.* 10:2649, "Modeling the Architecture of
Depolymerase-Containing Receptor Binding Proteins in *Klebsiella* Phages"**
(DOI [10.3389/fmicb.2019.02649](https://doi.org/10.3389/fmicb.2019.02649)).

In that paper, **group D is defined by its first RBP lacking an enzymatic or
receptor-binding domain and carrying instead an N-terminal anchor that includes
a T4gp10-like fragment, while the second tail fibre is a full-featured RBP.**

Mapped onto our genes:

- **CDS_0010** has the Calx-β anchor (42% identical over 107 aa to the anchor of
  CDS_0011) and no template over its body → this is what group D's first RBP is
  supposed to look like.
- **CDS_0011** has the anchor plus a β-helix depolymerase body → the
  full-featured second RBP.

**If that holds, the group D assignment itself predicts that CDS_0010 has no
enzymatic domain** — which is where our template analysis and your own reading
independently arrived.

**We have now tested the T4gp10 part of that definition, and it does not hold**
([`code/0729_t4gp10_check/`](../../code/0729_t4gp10_check/)). Neither `phmmer`
against T4 gp10 and gp9 (nothing at E ≤ 10 across all 80 proteins) nor
structural superposition against gp10 D2/D3 (5iv5, fully modelled) finds
anything: every gp10 comparison lands at 5.6–8.7 Å RMSD, inside the band set by
deliberate negative controls (6.7–7.6 Å), while a true positive control against
a real Calx-β structure gives 1.54 Å over 88 residues.

So our anchors are **Calx-β, not the T4gp10-bearing anchor family** those
*Klebsiella* phages use — two different domain families doing the same job,
which is unsurprising across that phylogenetic distance.

This does not refute group D. Group D is defined by an *architecture* —
truncated first RBP, full-featured second — and that still holds. It does mean
**the assignment has to be argued from architecture and synteny rather than
from the T4gp10 marker**, which is what you asked for anyway. One caveat before
this goes in print: Latka used HHpred, a profile method, and we could only run
sequence search and rigid-body structural alignment, so an HHpred or foldseek
run would be worth doing to match their method exactly.

---

# 3D printing

- **To print**: the funnel and base plate (CDS 20/08/09/13/14), and the fibres
  and depolymerase (CDS 10/11/12)
- **Colour**: baby blue
- **Source**: your AF3 folds; Alex will also fold a set independently
- **Separate project**: the fluorometer — Alex prepares a parts list, to be
  ordered once he is back

---

# Still open

| Question | Status |
|:----------------------------------|:--------------------------------|
| **Which three isolates did you mean?** | not answered — see the note below |
| **Conservation, or specificity-determining positions?** | agreed that unlabelled metagenome sequences cannot answer it, but not yet decided which analysis to run |
| Anything notable in the MGnify results? | not yet worked through |
| **Where does the second depolymerase, CDS_0024, sit in this model?** | not discussed — it is outside the 10/11/12 cluster |

> **On "our three isolates".** Five isolates were sequenced and by ANI they
> collapse to three distinct strains: {8-5-2, 10-10-2}, {9-2-1, 9-6-2}, and
> 8-10-2 on its own (*P. capeferrum*, a different species). "The three
> representatives" could mean either the three strain representatives
> (8-5-2 / 9-2-1 / 8-10-2) or the three originally sequenced site isolates
> (9-6-2 / 9-2-1 / 10-10-2) — but two of the latter are the same strain at 100%
> ANI. The analysis covers all five either way; it only changes what a figure
> legend should say.

> **On CDS_0024.** Our RBP classifier found a second β-helix depolymerase that
> the Pharokka annotation had missed (score 0.998, H-bond rung period 22–24). It
> sits away from the 10/11/12 cluster. If the phage carries two depolymerases,
> that is an extra variable in the in-trans design worth accounting for.

---

# Images

![Latka et al. 2019, *Front. Microbiol.* 10:2649, Figure 2 — domain architecture of depolymerase-containing RBPs (A) and the four virion arrangements (B). Our phage was described as resembling **group D**. Reproduced for internal reference; CC-BY attribution required for any external use.](images/frontiers_2019_rbp_architecture_groups.png)

![Structure render shared in the conversation — several chains (black / blue / green / yellow / red) over a translucent surface. **Is this the assembled virion model, and how was it put together?** If so it would feed directly into the cartoon (A3) and the printable set (A4), so we would like to know how you built it.](images/virion_structure_render.png)

---

*Log — 2026-07-29: created. Records the 2026-07-29 conversation. Settled: the
construct tagging is deliberate and only our filenames are wrong; CDS_0010 is an
unknown protein; metagenome sequences without host association cannot answer the
variable-region question. New: the ancestral GH5 depolymerase direction, and a
virion cartoon in the style of Latka 2019 group D to be justified by synteny and
similarity. Noted that group D's own definition may predict CDS_0010's lack of an
enzymatic domain, pending a check for the T4gp10-like fragment. Left open: which
three isolates, which variable-region analysis, and where CDS_0024 fits.*
