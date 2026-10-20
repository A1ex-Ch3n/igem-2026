# Collection page — Phage Φ8 surface-polysaccharide toolkit (draft)

The six parts as one set. Paste this into the Registry collection page.
Chinese version: [`COLLECTION_zh.md`](COLLECTION_zh.md).

---

## Title

**Phage 9-2-1 Φ8 surface-polysaccharide toolkit: three virion proteins and an ancestral series
of their glycoside hydrolase**

## Summary

Six basic parts from a single soil phage, **9-2-1 Φ8**, isolated and sequenced by our team from
a *Pseudomonas* host. Three are the phage's own virion proteins, taken straight from the
genome. Three are reconstructed ancestors of one of them. Together they are a set for one
question: **can an ancestral enzyme act on bacterial surface sugars that its modern descendant
cannot reach?**

| Part | Registry ID | What it is | Evidence grade |
|---|---|---|---|
| CDS12_WT | `BBa_267WQM51` | GH5 glycoside hydrolase, a free standalone enzyme | template-confirmed |
| CDS11_WT | `BBa_26DKNAEC` | tail-spike β-helix depolymerase body | fold-level only |
| CDS10_WT | `BBa_269KJB8G` | virion fiber | function unknown |
| CDS12_ANC_Node1 | `BBa_26TWEX42` | reconstructed ancestor of CDS12, nearest | computational design |
| CDS12_ANC_Node40 | `BBa_26EK89VW` | reconstructed ancestor, deeper | computational design |
| CDS12_ANC_Node281 | `BBa_26LHLSLW` | reconstructed ancestor, deepest of the three | computational design |

## Why these six belong together

**The problem.** Phage therapy fails when a host changes the surface sugar the phage binds.
The phage's depolymerases are specialists, each tuned to one host's polysaccharide — tailspike
depolymerases are what set a phage's capsular-type range (Popova *et al.* 2021). That
specificity is the useful property and the failure mode at once.

**The hypothesis.** Reconstructed ancestors of enzyme families are repeatedly found to be more
**promiscuous** than their modern descendants (Risso *et al.* 2018), and in at least one case a
resurrected ancestor accepts a substrate its modern descendant cannot convert at all
(Hendrikse *et al.* 2018). If that holds for a phage depolymerase, an
ancestral form of it may cleave polysaccharides the modern enzyme cannot — including those of
hosts that have escaped the phage.

**The design.** CDS12_WT is the modern enzyme; the three ancestral nodes are reconstructions
along the path from it to the root of its GH5 phylogeny. CDS11_WT and CDS10_WT are the other
two surface-contacting proteins from the same virion, included because the question is about
the phage's whole surface-recognition apparatus, not one enzyme in isolation.

**The panel is not evenly spaced,** and that is deliberate. Over the 361 aa mature insert,
Node1 is **77.8 %** identical to CDS12_WT, while Node40 and Node281 are **52.6 %** and
**51.0 %** to the wild type but **87.3 %** to each other. So the set is *wild type + one near
relative + one distant sister pair*. Node1 is the conservative test: if even that ancestor
behaves differently, the effect is unlikely to be an artefact of sequence distance.

## What is established

- **All three ancestors fold to the same GH5 TIM barrel as the wild type.** ESMFold v1,
  single sequence: backbone RMSD 0.28 / 0.50 / 0.52 Å for Node1 / Node40 / Node281 against the
  CDS12_WT model, all far inside the 2 Å equivalence criterion. The reconstruction changed the
  surface, not the fold.
- **That modelling method is itself validated here.** Folding the wild type the same way and
  superposing it on Prof. Espinoza's AlphaFold3 model of the same region gives **0.28 Å over
  2139 atoms**, so the ancestral models are not single-sequence artefacts.
- **Catalytic machinery is intact in all three** — the GH5 acid/base glutamate sits in the
  conserved NEP motif with the conserved SPHEY block downstream.
- **CDS10_WT and CDS11_WT share an N-terminal Calx-β anchor** (42 % identity over 107 aa,
  anchors superposing at 0.50 Å over 446 atoms): paralogous fibers on a common
  virion-attachment module.
- **Two of the six carry positive anti-His evidence.** On the 2026-10-19 dot blot the Node1
  induced lysate was His-positive at **2.4×** the negative control and the Node281 Ni-NTA
  flow-through at **2.9×**, with the positive control at about 18×. A tagged product is present
  in both; a dot blot reports the tag, not size or activity.

## What is not established

Stated plainly, because it is most of what a reuser needs to know:

- **No product has been assigned by size for any of the six.** A dot blot cannot tell
  full-length protein from a truncation or from free tag. Three SDS-PAGE sessions
  (2026-09-15, 09-29, 10-10) gave one induction-dependent band at the predicted mass for
  CDS12_WT and one unassigned 45–50 kDa band for `e1`, and the 2026-10-19 blot did **not**
  reproduce an induction-dependent signal for CDS12_WT. Node40 gave no signal on either of its
  two spots, on a membrane where its two siblings were positive — a like-for-like negative, but
  not proof of absence: every 1:10 dilution on that membrane fell to background, so the
  detection floor is high. CDS10_WT and CDS11_WT were not on it and have **no expression
  evidence at all**. The untransformed-BL21(DE3) control lane and a size-resolved anti-His
  western are both still outstanding.
- **One purification in the project recovered protein, and it is `e1`.** On 2026-10-01 all six
  constructs went over Ni-NTA across two gels; only the node 1 construct eluted, at ~41 kDa
  against a predicted 41.9 kDa. That is why the `e1` spot-test preparation sits in an imidazole
  elution buffer. CDS11_WT eluted a band at ~43 kDa the same day, ~29 kDa short of its predicted
  72.0 kDa and unexplained. The second round, `e281` on 2026-10-10, failed: blank elutions, the
  flow-through indistinguishable from the load. The dot blot then found that flow-through
  His-positive, so that failure is **capture, not expression**.
- **The four CDS_0012-family proteins cannot be told apart by SDS-PAGE** — all within 0.43 kDa
  (1.0 %) of each other. Identification needs sequencing or intact-mass MS.
- **One activity result exists and it is unattributed.** In a spot test on 2026-10-16, the
  `e1` preparation suppressed colony growth inside the drop to a median of 12 % of the
  same-plate sterile-PBS control, against 0 % for phage Φ8 and 53–67 % for the crude `e40` and
  `e281` lysates. But `e1` tracks the phage strain by strain, including their shared failure on
  one strain, so **carry-over of infectious phage from the Φ8 stock is still the leading
  alternative explanation**. A plaque assay of the preparation itself is the experiment that
  would settle it, and it has not been run. The anti-His signal for `e1` does not close this:
  a tag in the lysate does not make this protein the active species, and the imidazole elution
  buffer the preparation sits in was never spotted on its own.
- **No ancestor-versus-modern comparison has been made.** CDS12_WT was not in that spot test.
- **The inserts are not codon-optimised** and carry mammalian-like codon bias, which is the
  first thing to suspect behind a missing band. Rosetta or BL21-CodonPlus is the obvious next
  host.

## How to reuse this collection

The set is designed to be taken as a whole or in two halves.

- **For a phage-therapy project:** CDS12_WT plus the three ancestors is a ready-made
  modern-versus-ancestral panel for any depolymerase activity assay. The fold and catalytic
  residues are checked, and two of the four have anti-His evidence of a tagged product; what is
  missing is a size-assigned product, purified material and any attributed activity, so the
  panel is a starting point rather than a result.
- **For an ancestral-sequence-reconstruction project:** the three nodes are a worked example
  with the full method recorded — top 1000 NCBI nr hits, MUSCLE in SeaView, manual curation,
  PhyML (WAG, p-inv 0.1, 100 bootstraps), ancestral states in IQ-TREE, midpoint-rooted — plus
  the structural validation of the resulting sequences.
- **For a phage-biology project:** CDS10_WT and CDS11_WT are two surface proteins from a novel
  62 kb phage, one with a fold-level depolymerase assignment and one genuinely unassigned.

All six are expression constructs cloned into **pET-28a(+)** via NdeI/XhoI, synthesised by
Twist Bioscience, for *E. coli* BL21(DE3) under kanamycin, IPTG induction at **~30 °C**.
**The vector's N-terminal His6 leader is not part of any of these parts' sequences**, and no
part carries a C-terminal tag — but it is that leader the anti-His dot blot detects, so the
expression evidence belongs to the construct, not to the part sequence as submitted.

## Attribution

The GH5 phylogeny, the ancestral-state reconstruction and the choice of nodes are
**Prof. J. Espinoza's work**, not the students'. The three ancestral sequences are his design.
The students contributed the phage isolation and sequencing, the structural comparison of the
variants, the cloning and expression trials, the gel densitometry, and the spot test.
Every named author, including the PI, must opt in on registry.igem.org before being credited.


## References (verified on PubMed, 2026-10-19)

- Risso VA, Sanchez-Ruiz JM, Ozkan SB (2018). Biotechnological and protein-engineering
  implications of ancestral protein resurrection. *Curr Opin Struct Biol* 51:106–115.
  doi:10.1016/j.sbi.2018.02.007 — review; resurrected ancestors repeatedly show substrate and
  catalytic promiscuity. **The core citation for this collection's hypothesis.**
- Hendrikse NM, Charpentier G, Nordling E, Syrén P-O (2018). Ancestral diterpene cyclases show
  increased thermostability and substrate acceptance. *FEBS J* 285:4660–4673.
  doi:10.1111/febs.14686 — resurrected ancestors accept a substrate the extant enzyme does not
  convert. **The closest precedent for what we are testing.**
- Chen X, Dou Z, Luo T, Sun Z, Ma H, Xu G, Ni Y (2022). Directed reconstruction of a novel
  ancestral alcohol dehydrogenase featuring shifted pH-profile, enhanced thermostability and
  expanded substrate spectrum. *Bioresour Technol* 363:127886.
  doi:10.1016/j.biortech.2022.127886 — quantified substrate-spectrum expansion in an ancestor.
- Chiang C-H, Wang Y, Hussain A, Brooks CL, Narayan ARH (2024). Ancestral sequence
  reconstruction to enable biocatalytic synthesis of azaphilones. *J Am Chem Soc*
  146:30194–30203. doi:10.1021/jacs.4c08761 — ASR used to obtain a more soluble, stable and
  promiscuous enzyme; also the solubility argument for our constructs.
- Castro-Fernandez V, Herrera-Morande A, Zamora R, et al. (2017). Reconstructed ancestral
  enzymes reveal that negative selection drove the evolution of substrate specificity in
  ADP-dependent kinases. *J Biol Chem* 292:15598–15610. doi:10.1074/jbc.M117.790865 — a
  bifunctional ancestor specialising into a narrow modern enzyme: the direction we are trying
  to reverse.
- Popova AV, Shneider MM, Arbatsky NP, et al. (2021). Specific interaction of novel
  *Acinetobacter baumannii* phages encoding tailspike depolymerases with corresponding capsular
  types. *J Virol* 95:e01714-20. doi:10.1128/JVI.01714-20 — tailspike depolymerases determine
  phage specificity for a capsular type. **The statement of the problem.**
- Chen C-Y, et al. (2026). *Microbiol Resour Announc* doi:10.1128/mra.00793-26 — our own genome
  announcement for the *Pseudomonas* isolates, including 9-2-1, the host this phage was
  isolated on.

Found via PubMed. Each entry above was checked against its PubMed record; none is inferred
from memory.

## Registry documentation entries (paste-ready, 2026-10-19)

The collection form takes the same five entry types as a part page. Create one entry per type.
Field values: **Affiliation** `Claremont CA (2026)`.

Collection-level fields: **Title** `Phage Phi8 surface-polysaccharide toolkit`; **Summary**
"Six basic parts from one soil phage, 9-2-1 Phi8: three of its own virion proteins and three
reconstructed ancestors of its GH5 glycoside hydrolase. Grouped to test one question — whether
an ancestral enzyme can act on bacterial surface sugars that its modern descendant cannot
reach." Parts to add: BBa_267WQM51, BBa_26DKNAEC, BBa_269KJB8G, BBa_26TWEX42, BBa_26EK89VW,
BBa_26LHLSLW.

The five entry bodies are the prose sections above, reorganised as:

| Type | Title | Source section above |
|---|---|---|
| Design | Why these six parts are one set | *Why these six belong together* + *What is established* + reconstruction method + References |
| Experiment | Cloning, three gels, a failed purification and an anti-His dot blot | cloning/expression + the 2026-10-10 Ni-NTA attempt + the 2026-10-19 dot blot + the 2026-10-16 spot-test protocol |
| Characterisation | What the dot blot settled, and the one activity signal it did not | per-part dot-blot outcome + the spot-test result and the carry-over question |
| Application | How to reuse this collection | *How to reuse this collection* + practical notes |
| Discussion | What this set does and does not yet show | limitations and ranked future directions |

**Discussion ends on the ranked future directions.** An earlier draft closed with a sentence
about deliberately reporting negative results; it was cut on 2026-10-19 as editorialising.

The five bodies are written out, ASCII and paste-ready, in
[`paste/COLLECTION.md`](paste/COLLECTION.md) — **that file, not this one, is what goes into
the form**, exactly as for the six part pages.

## Resolved 2026-10-20: there were two purification rounds, not one

The live part pages contradicted each other. `BBa_26LHLSLW` (Node281) *experiment* called
itself "the only construct of the six we have attempted to purify", while its own
*characterisation* and `BBa_26TWEX42` (Node1) both described `e1` as having been through a
purification step and sitting in an imidazole elution buffer.

The lab notebook settles it. `lab_notebook/digitalized/2026-10-01_protein-purification.md`
records a **2026-10-01 Ni-NTA round over all six constructs, on two gels**:

- **`e1` eluted at ~41 kDa** against a predicted 41.9 kDa — the only purification in the
  project that recovered protein, and the source of the `e1` spot-test preparation.
- **CDS11_WT eluted a band at ~43 kDa**, about 29 kDa short of its predicted 72.0 kDa.
  Unexplained.
- `CDS10_WT`, `CDS12_WT`, `e40` and `e281` eluted nothing.

The 2026-10-10 run was a **second** round, on `e281` alone, and is the one that failed.

**Three live Registry pages now say something false and should be edited** (documentation stays
editable after screening; only sequence, authorship and licence are locked):

| part | sentence to fix |
|---|---|
| `BBa_26LHLSLW` Node281 | "the only construct of the six we have attempted to purify" — it is the second round, not the only one |
| `BBa_26DKNAEC` CDS11_WT | "no purified protein" — it eluted a 43 kDa band on 2026-10-01, 29 kDa short of prediction |
| `BBa_26TWEX42` Node1 | does not mention its own 2026-10-01 elution at all, which is the project's best expression evidence and the provenance of the spot-test material |

The wiki's `/parts` page had this right all along: "the 10-01 gels show e1 eluting at its
predicted mass".

---
*Draft — 2026-10-18. Numbers: `code/output/1018_construct_structures/` and
`code/output/1016_spot_test_result/`. Evidence grades:
[`../2026-10-18_parts_structure_comparison.md`](../2026-10-18_parts_structure_comparison.md).*
*Log — 2026-10-20: aligned with the six live part pages as applied on 2026-10-19. The
"no expression is confirmed for any of the six" claim was false after the dot blot and is
replaced; the failed `e281` Ni-NTA, the ~30 °C induction temperature and the per-part dot-blot
outcomes are written in; the entry-mapping table now routes the purification and the blot into
Experiment and Characterisation. The five bodies are written out in `paste/COLLECTION.md`.*
