# Prompt for the Engineering-page session — number consistency after the Parts pass

Copy everything inside the quote block.

---

> I have just corrected the Parts page (`wiki/pages/parts.html`, commit `b4dcae0`
> on `main`) against the repository's own outputs. Four numbers moved, and three of
> them also appear on your Engineering page. **Right now `engineering.html`
> contradicts itself**, so please check these before the freeze.
>
> **1. The rung periods. Your Figure 6 caption and your prose disagree.**
>
> The caption of Figure 6 says, correctly: *"A at period 23 and B–C at 16–17 are
> prisms with countable coils, E at period 6 is a single helical rod, and D at
> period 34 is a barrel"*.
>
> But the Cycle 2 prose above it still says:
>
> - CDS_0011 *"rung period 15–18 residues"* → the authoritative value is **16–17**
> - CDS_0024 *"rung period 22–24"* → the authoritative value is **23**
>
> The source of truth is
> `code/output/0712_phage_rbp_detect/structure/beta_helix_analysis.tsv`, which is
> the file the figure is generated from. In it, our CDS_0015 has period 17, our
> CDS_0016 has period 16 (those two are the PI's CDS_0011), and our CDS_0002 has
> period 23 (the PI's CDS_0024). `15–18` and `22–24` are from an earlier run and
> are not reproducible from anything now in the repo. Parts now says 16–17 and 23.
>
> **2. pLDDT 88–94 for CDS_0011 is not what the models say.**
>
> Your Cycle 2 prose says the tail spike *"folds with pLDDT 88–94"*. The two
> fragment models actually return **93.2** (our CDS_0016) and **64.7** (our
> CDS_0015). The range 88–94 excludes the weaker one entirely.
>
> This matters more than a number: Figure 6 panel C is the 64.7 model, and its
> low-confidence regions are visibly orange in the figure you are already showing.
> A reader who takes "88–94" from the prose and then looks at panel C sees a
> contradiction. Parts now names both values explicitly and says the disagreement
> is why the period is quoted as a range rather than a single number.
>
> **3. The ancestral protein length is 362 aa, not 382 aa.**
>
> Your Cycle 3 text says the four CDS_0012-family constructs *"express a 382 aa
> protein"*. 1086 bp of insert is 362 codons, and
> `code/output/1018_construct_structures/registry/registry_parts.faa` gives 362 aa
> for CDS12_WT and for all three ancestors. The Registry entries say 362 too. This
> was wrong in eight places on Parts and is now fixed there; `engineering.html` has
> one instance.
>
> **4. One thing that is now settled, in case you reference it.**
>
> Parts used to carry a callout saying it was still an open question whether the
> pET-28a `MGSSHHHHHHSSGLVPRGSHM` leader goes into the submitted sequence. It is
> not open: decided 2026-10-18 (the leader is **not** included), and the sequences
> locked permanently when all six parts cleared screening on 2026-10-20. CDS_0011's
> designed `GGSGGGGS`-His6-`ENLYFQ`-`GGGGSGGGGS` purification linker is excluded
> from its submitted sequence as well. If Engineering says anything about what is
> in the submitted sequences, it should match that.
>
> **Please do not change Figure 6's caption** — it is the one place these numbers
> were already right.

---

## Why this file exists

The two pages are judged together: Engineering is the Silver S1 URL and also
feeds Best Model, and Parts is the Best New Basic Part URL. A judge who reads
both will see the same proteins described with different numbers.

| claim | Engineering prose | Figure 6 caption | authority | now on Parts |
|---|---|---|---|---|
| CDS_0011 rung period | 15–18 | **16–17** | 16 and 17 | 16–17 |
| CDS_0024 rung period | 22–24 | **23** | 23 | 23 |
| CDS_0011 pLDDT | 88–94 | — | 93.2 and 64.7 | both named |
| ancestral protein | 382 aa | — | 362 aa | 362 aa |

Authority column = `beta_helix_analysis.tsv` for the periods and pLDDT,
`registry_parts.faa` for the length.

---
*Log — 2026-10-20: written after the Parts correction pass (`b4dcae0`). The
Engineering figure was already carrying the right numbers; its prose was not.*
