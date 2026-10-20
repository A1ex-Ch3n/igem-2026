# Collection - Phage 9-2-1 Phi8 surface-polysaccharide toolkit

Paste-ready. Same convention as the six part files: plain ASCII, no Greek letters, no en or em
dashes, no percent sign, no markdown bold inside the bodies. Built 2026-10-20 from
`../COLLECTION.md` aligned against the six live part pages as applied on 2026-10-19.

The collection page already exists on registry.igem.org - created 2026-10-19, UUID
3edc6bca-7c2b-4c01-b38f-c6ed3b6743ad - and its five entries carry the pre-dot-blot
text. These bodies are the replacements. The parts list was still empty while the six
parts were in Draft; all six went to published on 2026-10-20, so they can be added now.

## Collection-level fields

**Title:** Phage Phi8 surface-polysaccharide toolkit

**Summary:** Six basic parts from one soil phage, 9-2-1 Phi8: three of its own virion proteins
and three reconstructed ancestors of its GH5 glycoside hydrolase. Grouped to test one question,
whether an ancestral enzyme can act on bacterial surface sugars that its modern descendant
cannot reach.

**Affiliation:** Claremont CA (2026)

**Parts to add:** BBa_267WQM51 (CDS12_WT), BBa_26DKNAEC (CDS11_WT), BBa_269KJB8G (CDS10_WT),
BBa_26TWEX42 (CDS12_ANC_Node1), BBa_26EK89VW (CDS12_ANC_Node40), BBa_26LHLSLW
(CDS12_ANC_Node281).

## design

**title:** Why these six parts are one set

The problem. Phage therapy fails when a host changes the surface sugar the phage binds. A
phage's depolymerases are specialists, each tuned to one host's polysaccharide, and tailspike
depolymerases are what set a phage's capsular-type range (Popova et al. 2021). That specificity
is the useful property and the failure mode at once.

The hypothesis. Reconstructed ancestors of enzyme families are repeatedly found to be more
promiscuous than their modern descendants (Risso et al. 2018), and in at least one case a
resurrected ancestor accepts a substrate the extant enzyme cannot convert at all (Hendrikse et
al. 2018). If that holds for a phage depolymerase, an ancestral form of it may cleave
polysaccharides the modern enzyme cannot, including those of hosts that have escaped the phage.

The design. CDS12_WT is the modern enzyme; the three ancestral nodes are reconstructions along
the path from it to the root of its GH5 phylogeny. CDS11_WT and CDS10_WT are the other two
surface-contacting proteins from the same virion, included because the question is about the
phage's whole surface-recognition apparatus and not one enzyme in isolation.

The panel is deliberately not evenly spaced. Over the 361 aa mature insert, node 1 is 77.8
percent identical to CDS12_WT, while node 40 and node 281 are 52.6 and 51.0 percent to the wild
type but 87.3 percent to each other. The set is therefore wild type, one near relative, and one
distant sister pair. Node 1 is the conservative test: if even that ancestor behaves
differently, the effect is unlikely to be an artefact of sequence distance alone.

What the structures establish. All three ancestors fold to the same GH5 TIM barrel as the wild
type. ESMFold v1, single sequence, no MSA, no template: backbone RMSD 0.28, 0.50 and 0.52
Angstrom for node 1, node 40 and node 281 against the CDS12_WT model, all well inside the 2
Angstrom equivalence criterion. The reconstruction changed the surface, not the fold. That
modelling method is validated here rather than assumed: folding the wild type the same way and
superposing it on Prof. Espinoza's AlphaFold3 model of the same region gives 0.28 Angstrom over
2139 atoms. The catalytic machinery is intact in all three, the GH5 acid/base glutamate sitting
in the conserved NEP motif with a conserved SPHEY block downstream.

The two virion fibers are related to each other. CDS10_WT and CDS11_WT share an N-terminal
Calx-beta virion-attachment anchor, 42 percent identity over 107 aa, the anchors superposing at
0.50 Angstrom over 446 atoms: paralogous fibers built on a common attachment module.

Reconstruction method, as recorded by the PI on 2026-10-18. Top 1000 NCBI nr hits to CDS_0012;
MUSCLE alignment in SeaView, manually curated; PhyML with the WAG matrix, p-inv 0.1 and 100
bootstraps; ancestral states in IQ-TREE on the same matrix, midpoint-rooted. Every node on the
path from CDS_0012 to the root was reconstructed. The node labels are arbitrary identifiers and
not depths: from most recent to most ancestral they run 1, 2, 38, 39, 40, 42, 267, 277, 281,
which agrees with the sequence identities above.

References, each checked against its PubMed record.

Risso VA, Sanchez-Ruiz JM, Ozkan SB (2018). Biotechnological and protein-engineering
implications of ancestral protein resurrection. Curr Opin Struct Biol 51:106-115.
doi:10.1016/j.sbi.2018.02.007. Review; resurrected ancestors repeatedly show substrate and
catalytic promiscuity. The core citation for this collection's hypothesis.

Hendrikse NM, Charpentier G, Nordling E, Syren P-O (2018). Ancestral diterpene cyclases show
increased thermostability and substrate acceptance. FEBS J 285:4660-4673.
doi:10.1111/febs.14686. A resurrected ancestor accepts a substrate the extant enzyme does not
convert. The closest precedent for what we are testing.

Chen X, Dou Z, Luo T, Sun Z, Ma H, Xu G, Ni Y (2022). Directed reconstruction of a novel
ancestral alcohol dehydrogenase featuring shifted pH-profile, enhanced thermostability and
expanded substrate spectrum. Bioresour Technol 363:127886. doi:10.1016/j.biortech.2022.127886.
Quantified substrate-spectrum expansion in an ancestor.

Chiang C-H, Wang Y, Hussain A, Brooks CL, Narayan ARH (2024). Ancestral sequence reconstruction
to enable biocatalytic synthesis of azaphilones. J Am Chem Soc 146:30194-30203.
doi:10.1021/jacs.4c08761. ASR used to obtain a more soluble, stable and promiscuous enzyme;
also the solubility argument for our constructs.

Castro-Fernandez V, Herrera-Morande A, Zamora R, et al. (2017). Reconstructed ancestral enzymes
reveal that negative selection drove the evolution of substrate specificity in ADP-dependent
kinases. J Biol Chem 292:15598-15610. doi:10.1074/jbc.M117.790865. A bifunctional ancestor
specialising into a narrow modern enzyme: the direction we are trying to reverse.

Popova AV, Shneider MM, Arbatsky NP, et al. (2021). Specific interaction of novel Acinetobacter
baumannii phages encoding tailspike depolymerases with corresponding capsular types. J Virol
95:e01714-20. doi:10.1128/JVI.01714-20. Tailspike depolymerases determine phage specificity for
a capsular type. The statement of the problem.

Chen C-Y, et al. (2026). Microbiol Resour Announc doi:10.1128/mra.00793-26. Our own genome
announcement for the Pseudomonas isolates, including 9-2-1, the host this phage was isolated
on.

## experiment

**title:** Cloning, three gels, a failed purification and an anti-His dot blot

Common to all six. Each part was cloned into pET-28a(+) by NdeI/XhoI, synthesised by Twist
Bioscience, and expressed in E. coli BL21(DE3) under kanamycin with IPTG induction at ~30 C.
The expressed construct carries the vector's N-terminal MGSSHHHHHHSSGLVPRGSHM leader, which is
not part of any of these parts' sequences; CDS11_WT's own construct additionally carries a
designed GGSGGGGS-His6-ENLYFQ-GGGGSGGGGS linker, also not part of the submitted sequence. No
part carries a C-terminal tag. None of the six inserts was codon optimised for E. coli and all
carry a mammalian-like codon bias, which is the first thing to suspect behind a missing band;
Rosetta or BL21-CodonPlus are the obvious alternative hosts.

SDS-PAGE, three sessions: 2026-09-15, 2026-09-29 and 2026-10-10. Two bands came out of them and
neither is an identification. CDS12_WT gave an induction-dependent band at its predicted mass,
and the node 1 construct gave an unassigned band at 45-50 kDa. The node 40 lane on gel 1 was
essentially not loaded and no usable lane has been run for it since. CDS11_WT showed no band at
its expected 72.0 kDa in any session, and on 2026-09-29 no undiluted lane was run for it, so
that absence is not interpretable. CDS10_WT, predicted at 91.6 kDa tagged, has never been
expressed in earnest and no gel carries an interpretable lane for it. The untransformed
BL21(DE3) control lane that would let any of these bands be assigned is still outstanding
across all three sessions. A further caution for the CDS_0012 family: all four of those
proteins fall within 0.43 kDa, 1.0 percent, of one another, so SDS-PAGE cannot tell them apart
at all. Identification needs sequencing or intact-mass MS.

Ni-NTA purification, 2026-10-10, node 281. This is the one purification in the project with a
gel, and it failed. Elutions E1 and E2 were blank gel: peak prominence 0.011 against a measured
noise floor of 0.020, with lane totals inside the never-loaded range. The flow-through was
indistinguishable from the load, the same 40-44 kDa band in both. No purified protein from any
of the six exists.

Anti-His dot blot, 2026-10-19. Eleven samples were spotted directly onto membrane and probed
with a single-step anti-His HRP conjugate; the positive control reached about 18 times the
negative control, so the detection chemistry worked. A dot blot reports the His tag, not size
or activity, and this membrane's detection floor is high: every 1:10 dilution on it fell to
background, so an absent signal here is weak evidence of absence. Four of the six constructs
were on it, the whole CDS_0012 family; CDS10_WT and CDS11_WT were not. The node 1 induced rough
lysate was His-positive at 2.4 times the negative control. The node 281 Ni-NTA flow-through was
His-positive at 2.9 times. The node 40 construct was spotted twice, as induced rough lysate and
at 1:10, and gave no signal either time, at -0.2 and 0.7 against a negative control of 3.9.
CDS12_WT did not reproduce an induction-dependent signal.

Spot test, spotted 2026-10-12 and read 2026-10-16. Seven Pseudomonas strains were grown as
double-layer lawns, 200 microlitres of culture in 3 millilitres of soft agar. Each plate
received five 7 microlitre drops: phage Phi8 stock as the positive control, sterile 1x PBS as
the negative control, and the e1, e40 and e281 preparations, each diluted 1 in 10 in that same
sterile PBS. CDS12_WT was not in this run.

## characterisation

**title:** What the dot blot settled, and the one activity signal it did not

Expression, per construct, after the 2026-10-19 blot. Two of the six now have positive evidence
of a tagged product and one has a meaningful negative.

Node 1 (BBa_26TWEX42): the induced lysate is His-positive at 2.4 times the negative control,
the third strongest signal on the membrane. A tagged product is present. Because a dot blot
carries no size information it cannot tell full-length protein from a truncation or from free
tag, so it does not on its own assign that construct's unexplained 45-50 kDa band.

Node 281 (BBa_26LHLSLW): the flow-through is His-positive at 2.9 times the negative control,
the second strongest signal. That settles the purification: the protein was expressed and it
did not bind the resin, so the failure is capture and not expression. The next move is the
binding conditions, meaning imidazole carried into the load, binding time and resin choice,
rather than a repeat of the same run.

Node 40 (BBa_26EK89VW): no signal on either spot. This is a like-for-like negative rather than
an isolated one, because two sibling constructs were positive on the same membrane, but it is
not proof of absence for the detection-floor reason given in the Experiment entry.

CDS12_WT (BBa_267WQM51): no induction-dependent signal reproduced, so its single gel band is
still its only expression evidence and is still unassigned.

CDS10_WT (BBa_269KJB8G) and CDS11_WT (BBa_26DKNAEC): not on the membrane. These two have no
expression evidence at all.

Activity. One activity result exists in the whole set and it is not yet attributed. In the
2026-10-16 spot test no drop produced a clear lysis zone, phage Phi8 included; the readout was
colony growth inside the drop. Sterile PBS drops reproducibly developed discrete colonies, a
median of 14 per drop, and that baseline varied from plate to plate between 7 and 17, so each
drop is reported as a percentage of the PBS drop on its own plate. On that scale the medians
are Phi8 0 percent, e1 12 percent, e281 53 percent, e40 67 percent. The e1 preparation
suppressed colony growth almost completely on six of the seven strains, as did the phage.

Why that is not yet an activity for the protein. Across the seven strains e1 tracks the phage
almost exactly: both fall below 40 percent on six strains, and the single strain where the
phage failed, 9-1-1 at 157 percent, is the one where e1 failed, at 114 percent. Carry-over of
infectious phage from the Phi8 stock would produce precisely that agreement and remains the
leading alternative explanation. The anti-His result does not close the gap either: a tag in
the lysate does not make this protein the active species, and the imidazole elution buffer the
e1 preparation sits in was never spotted on its own. The deciding experiment is a plaque assay
of the e1 preparation itself on a sensitive lawn, and it has not been run.

The two weaker variants are not shown to be inactive. The e40 and e281 drops were crude lysates
in which no enzyme is enriched, and both were spotted at 1 in 10, the same dilution that fell
below the detection floor on the dot blot. How much protein was in those drops is unknown, so
the experiment cannot distinguish a missing activity from a diluted one.

No ancestor-versus-modern comparison has been made. CDS12_WT, the modern arm the whole design
asks for, was not in the spot test.

## application

**title:** How to reuse this collection

The set is designed to be taken as a whole or in two halves.

For a phage-therapy project: CDS12_WT plus the three ancestors is a ready-made
modern-versus-ancestral panel for any depolymerase activity assay. The fold and the catalytic
residues are checked, and two of the four have anti-His evidence of a tagged product. What is
missing is a size-assigned product, purified material and any attributed activity, so the panel
is a starting point rather than a result.

For an ancestral-sequence-reconstruction project: the three nodes are a worked example with the
full method recorded, from the top 1000 NCBI nr hits through MUSCLE in SeaView, manual
curation, PhyML with WAG, p-inv 0.1 and 100 bootstraps, to ancestral states in IQ-TREE,
midpoint-rooted, plus the structural validation of the resulting sequences against both an
ESMFold and an AlphaFold3 model.

For a phage-biology project: CDS10_WT and CDS11_WT are two surface proteins from a novel 62 kb
phage, one with a fold-level depolymerase assignment and one genuinely unassigned, sharing a
Calx-beta anchor that superposes at 0.50 Angstrom.

Practical notes for anyone expressing these. Plan the untransformed BL21(DE3) control lane from
the start; we did not, and it is the single reason several of our gel bands remain unassigned.
Expect the codon bias to matter and consider a codon-optimised resynthesis or a Rosetta host.
Run a soluble-versus-pellet fractionation, particularly for the two large fibers at 72.0 and
91.6 kDa tagged. For Ni-NTA on the ancestral variants, watch the imidazole carried into the
load: our one purification with a gel lost the protein to the flow-through. And do not try to
tell the four CDS_0012-family proteins apart on a gel; they are within 1.0 percent in mass.

## discussion

**title:** What this set does and does not yet show

What the set shows. A reconstructed ancestral series of a phage GH5 glycoside hydrolase can be
designed, synthesised and cloned, and the reconstruction preserves the fold: three ancestors at
77.8, 52.6 and 51.0 percent identity to the modern enzyme all model onto it within 0.52
Angstrom backbone RMSD, with the catalytic acid/base glutamate intact in its NEP motif in every
one. Two of the four CDS_0012-family constructs give positive anti-His signal, so the panel is
expressible at least in part. Alongside them sit the phage's two other surface-contacting
proteins from the same virion, one of them a fold-level depolymerase assignment and both built
on a shared Calx-beta anchor.

What it does not show. No activity has been attributed to any of these proteins. The single
suppression result belongs to the e1 preparation, not demonstrably to the e1 protein, and the
phage carry-over alternative is still open. No product has been assigned by size: the dot blot
reports a tag, and a tag is compatible with a truncation or with free His6. No purified protein
exists. The modern arm of the comparison the design is built on has never been run. And the
structural evidence throughout is modelling, not experiment: it says the fold survives the
reconstruction, not that the enzyme works.

A caution about what the parts are. The three wild-type proteins are three different things and
should not be collapsed into one. CDS_0011 is the tail spike whose body is assigned as a
depolymerase on fold evidence alone, with no named homolog. CDS_0012 is a separate, free
standing enzyme and carries the strongest evidence in the project, four of four AlphaFold3
templates being GH5 endoglucanases at pLDDT 95-98. CDS_0010 is of unknown function; an early
glycosidase annotation was withdrawn by the PI on 2026-07-29. The tail spike should never be
described as carrying a GH5 domain.

Ranked future directions.

1. A plaque assay of the e1 preparation on a sensitive lawn. Until this is run, the one
activity result in the set cannot be attributed, and everything downstream of it is provisional.

2. An untransformed BL21(DE3) control lane, run once, alongside a size-resolved anti-His
western. Together these turn the existing bands and dot-blot signals into assignments.

3. CDS12_WT into the spot test, on the same plates as the ancestors, with an
elution-buffer-only drop and a dilution series. This is the comparison the collection exists to
make.

4. Rework the Ni-NTA binding conditions for node 281, which the flow-through result points at
directly, rather than repeating the run that failed.

5. Codon-optimised resynthesis, or a Rosetta or BL21-CodonPlus host, for the constructs with no
band at all, node 40 and the two large fibers in particular.

## Attribution

The GH5 phylogeny, the ancestral-state reconstruction and the choice of nodes are Prof. J.
Espinoza's work, not the students'. The three ancestral sequences are his design. The students
contributed the phage isolation and sequencing, the structural comparison of the variants, the
cloning and expression trials, the gel densitometry, the Ni-NTA attempt, the dot blot and the
spot test. Every named author, including the PI, must opt in on registry.igem.org before being
credited.

---
*Log - 2026-10-20: written from `../COLLECTION.md` after aligning it against the six live part
pages as applied 2026-10-19. Every factual sentence here traces to a sentence in `./CDS*.md`;
the only numbers not on a part page are the collection-level ones already in the draft.*
