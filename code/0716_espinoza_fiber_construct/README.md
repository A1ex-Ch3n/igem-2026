# 0716 — which piece of CDS_0011 do we actually clone? (Prof. Espinoza's AF3 folds)

Provenance — Prof. Espinoza sent three **AlphaFold3 Server** folds + the three tail-cluster
sequences on **2026-07-14/15**, and said he wants to **order the first plasmid that week**:

> CDS 11 is the fiber (the part that matters to use and we will clone) … from lit, there is a
> general arrangement of three domains, from N to C, first domain joins to the base of the capsid,
> the second and third domains recognize the sugars and hydrolyze them … but it looks like in our
> phage the catalytic region is shared with other two proteins, CDS10 and CDS12 … What I don't know
> is if the enzymes also have a role in host recognition … **using CDS 11, removing the first 300ish
> bases so everything after the first long beta-sheet barrel**

**All numbering here is HIS (`UUAIURNK_`)** — canonical for this phage as of 2026-07-16. Convert
legacy `FHABPWTM_` numbers via `../0713_espinoza_structural_mapping/cds_lookup.tsv`.

## Run
```bash
# unzip his 3 zips into data/phage_genome/9-2-1/folds_espinoza/ first (gitignored, 51 MB → 460 MB)
python3 code/0716_espinoza_fiber_construct/analyze_fiber_folds.py
```
Outputs → `code/output/0716_espinoza_fiber_construct/`: `template_hits.tsv`, `domain_map.tsv`,
`model_rmsd.tsv`, `construct_options.{tsv,faa,ffn}`.

## What "the first long beta-sheet barrel" is — answered
All four AF3 templates for CDS_0011 map to **res 9–110 and nothing else** (`template_hits.tsv`);
all four are **Calx-β / NCX Ca²⁺-binding β-sandwich** domains (3US9, 3EAD, 2FWU, 2KLT). The other
**830 aa have no template at all** — that part of the fiber is novel.

**300 bases = 100 codons**, and the β-sandwich is res 1–110. His arithmetic is self-consistent →
he means **res ~111–941 (831 aa, 2496 bp)**. ⚠️ He wrote **"bases"**, not "residues" — a 3×
difference. Confirm the start residue explicitly before anything ships.

## Domain map of CDS_0011 (941 aa, folded as the trimer he says it forms)
| res | what | evidence |
|---|---|---|
| **1–110** | **Calx-β β-sandwich** — his "joins to the base of the capsid" | 4 templates; internal PAE 3–11 |
| 121–160 | small helical unit | internal PAE 2–6 |
| 161–200 | disordered | pLDDT 33 |
| 201–280 | compact β unit | internal PAE 3–7; no template |
| **301–941** | **the fiber body** — β-helix depolymerase + RBD | pLDDT 88–94; H-bond rung period 15–17 |

The rung period 15–17 matches our 0712 calls for the same protein (period 16/17), so the β-helix
depolymerase reading is unchanged — see `../0712_phage_rbp_detect/`.

## The cut site — his words leave ~190 aa of undefined shaft
Superposing his 5 AF3 models **on the body (res 301–941)** (`model_rmsd.tsv`):

| region | RMSD across the 5 models |
|---|---|
| body 301–941 | **0.44–0.99 Å** (rigid, reproducible) |
| Calx-β 1–110 | **50–92 Å** |
| shaft 111–300 | **41–52 Å** |

The body is a hard, self-trimerizing structure; **everything N-terminal of ~301 is an unplaced,
floppy appendage** (AF3 drops it somewhere different in every model, and PAE from any of res 1–300
to the body is ~31–32 = maximum uncertainty). Whole-trimer ipTM 0.64 is dragged down by that
appendage, **not** by a bad interface — inter-chain PAE min ≈ 2 Å, and res 321–941 carry the
trimer contacts. There is also a 1.94 Å inter-chain CA–CA clash at res 237 (pLDDT 68), i.e. a
modelling artifact inside the floppy region.

So the three candidates (`construct_options.{tsv,faa,ffn}`, ready to order):

| construct | length | note |
|---|---|---|
| **res 111–941** | 831 aa / 2496 bp | **his words**; keeps ~190 aa of shaft AF3 cannot place |
| res 301–941 | 641 aa / 1926 bp | clean, self-contained, trimeric β-helix body |
| res 391–941 | 551 aa / 1656 bp | his **0713** claim that the RBD is "the C-terminal ~550 aa" |

⚠️ **His own two cut sites disagree by 280 residues** (0713: "RBD = last 550 aa" → res 391;
0715: cut at ~111). Keep the C-terminus intact either way — res 921–941 is a helical,
heavily trimer-contacting element that looks like a trimerization foldon, so an **N-terminal tag
is the safer choice**.

## His glycosidase model — one confirmed, one not
| his claim | verdict | evidence |
|---|---|---|
| **CDS_0012 = glycosidase** | ✅ **confirmed** | all 4 templates are **GH5 endoglucanases** — 1ECE (*Acidothermus* endocellulase E1 **with cellotetraose bound**), 1VRX, 4TUF, 2ZUM — over res 118–475, pLDDT 95–98. It is a **CBM + GH5 TIM barrel** |
| **CDS_0010 = glycosidase** | ⚠️ **not supported** | only template on the body is a weak IspD hit (4MYB, res 361–456); the other ~460 aa have none |

**This closes the 0713 open question.** Our 0712 H-bond test called CDS_0012 (= our old CDS_0014)
"α-rich" and that was never a contradiction — **a TIM barrel *is* α/β**, and correctly is not a
β-helix. The two methods agree. **CDS_0010 is the one to press him on**, not CDS_0012.

## New: CDS_0010 and CDS_0011 are paralogous fibers
Their N-terminal Calx-β domains are **42% identical over 107 aa** (and hit the same PDBs), while
CDS_0012 shares nothing (18–19 aa at ~32% = noise). So CDS_0010 and CDS_0011 carry **the same
virion-attachment module** with different business ends — which is exactly his "first domain joins
to the base of the capsid", and explains why the three genes sit together and why we have three
where other podoviruses have one or two.

## UNDONE
- **Confirm the cut site with him before the order ships** — "bases vs residues", and 111 vs 391.
- **Ask for his evidence on CDS_0010** being a glycosidase (his foldseek hit table).
- His open question — *do the enzymes also recognize the host, or only degrade the sugar?* —
  **cannot be answered from these three folds**; needs an experiment or a different analysis.

---
*Log — 2026-07-16: filed Prof. Espinoza's 3 AF3 folds (2026-07-14/15) + the construct analysis.
"First long beta-sheet barrel" identified as the Calx-β β-sandwich res 1–110 → his construct is
res ~111–941; two ambiguities flagged for him (bases-vs-residues, 111-vs-391). 0713's open question
RESOLVED: CDS_0012 is a GH5 TIM barrel (confirmed), CDS_0010 unsupported. Adopted his `UUAIURNK_`
numbering repo-wide. UNDONE: cut site confirmation, CDS_0010 evidence.*
*Log — 2026-07-30: both remaining UNDONE items are now closed by the 2026-07-29 PI conversation.
Cut site = res **305** (he chose it; see `documents/2026-07-27_twist_construct_order/`). CDS_0010
evidence: the PI **withdrew the glycosidase call** — it is an **unknown protein**, being expressed
for functional characterization. Body text left as the 0716 record. See
`documents/2026-07-29_pi_conversation/`.*
