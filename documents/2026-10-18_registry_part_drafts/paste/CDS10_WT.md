# CDS10_WT - BBa_269KJB8G  (bba-269kjb8g)

Paste-ready. Live registry text as of 2026-10-19 with the 2026-10-19 dot blot merged in. status=draft

## Functional Description

Residues 105-917 of CDS\_0010 of bacteriophage 9-2-1 Phi8: a virion protein whose function is genuinely unknown. It is submitted as such, as a characterisation target rather than as a protein with an assigned activity. What is solid is its relationship to the tail spike CDS\_0011: the two share an N-terminal Calx-beta virion-attachment anchor (42 percent identity over 107 aa; the two anchors superpose at 0.50 Angstrom over 446 atoms), so they look like paralogous fibers built on a common attachment module. The remaining roughly 800 residues have no structural template. This part is deliberately not called a glycosidase: an early annotation suggested one, our template analysis never supported it, and the PI withdrew that call on 2026-07-29. The construct cuts just inside the anchor so that the protein is soluble rather than an assembly component, and it is a coding sequence with its own ATG and stop codon, without the pET-28a His6 leader used in our own expression construct.

## design

**title:** A shared Calx-beta anchor, 800 residues with no template, and a withdrawn annotation

CDS\_0010 sits in the tail module of phage 9-2-1 Phi8 and shares its N-terminal Calx-beta anchor with the tail spike CDS\_0011: 42 percent identity over 107 aa, with the two anchors superposing at 0.50 Angstrom RMSD over 446 atoms, or 0.96 Angstrom by CE over 88 residues. The two look like paralogous fibers built on a common virion-attachment module, and that relationship is the best-supported thing we can say about this protein.

Everything else is open. The remaining roughly 800 residues have no structural template at all; the only hit anywhere in the chain is a weak IspD match over residues 361-456. The AlphaFold3 model is confident as a shape, with pTM 0.80, mean pLDDT 90.8 inside the cloned region and 98.3 percent of those residues above 70, but confidence in a fold is not a function.

This part is deliberately not called a glycosidase. An early annotation suggested one, our template analysis never supported it, and the PI withdrew the call on 2026-07-29. The honest statement is unknown function. We cloned and expressed it for exactly that reason: the function of a tail-module protein with no structural template can only be settled experimentally.

Keep the three wild-type parts distinct. CDS\_0010 is of unknown function. CDS\_0011 is the virion-attached tail spike, a depolymerase on fold evidence only. CDS\_0012 is the template-confirmed GH5 glycoside hydrolase, a separate free protein. Three proteins, three claims, three evidence grades.

Construct boundary. Residues 105-917 cut just inside the Calx-beta anchor (1-110), keeping the large uncharacterised region intact. The anchor is what attaches the fiber to the virion, so removing most of it should give a soluble protein rather than an assembly component. The AlphaFold3 monomer model is Prof. J. Espinoza's work.

## experiment

**title:** Cloned and queued; expression not yet attempted in earnest

Cloned into pET-28a(+) by NdeI/XhoI, synthesised by Twist Bioscience (order of 2026-07-27). Host E. coli BL21(DE3), kanamycin selection, IPTG induction at ~30 C planned.

Status: not yet attempted in earnest. This construct is batch 3 in the project's expression plan, behind CDS\_0012 and the three ancestral GH5 variants, and at a predicted 91.6 kDa for the tagged protein it is the hardest of the six to express. No gel to date carries an interpretable lane for it.

The insert was not codon optimised for E. coli, which is a live risk at this size. Anyone attempting it should plan for a soluble-versus-pellet fractionation and an untransformed-host control lane from the start.

## characterisation

**title:** No characterisation: submitted as a sequence and structure contribution

None. No expression, no purification, no activity data. The part is submitted as a sequence-and-structure contribution with an explicitly open function.

What is measured, and belongs to this part, is the structural relationship to the tail spike CDS\_0011: 42 percent sequence identity over the 107 aa Calx-beta anchor, and 0.50 Angstrom backbone RMSD over 446 atoms between the two modelled anchors. That is a dry-lab result on predicted structures, not a wet-lab measurement.

Anyone wanting to characterise this protein has an obvious first experiment: express it, then test it against the host's surface polysaccharide alongside CDS\_0012, whose activity is the comparison this fiber lacks.

## application

**title:** A characterisation target, and a source of the shared Calx-beta anchor

Two uses, both honest about the state of knowledge.

First, a functional-characterisation target. The protein is in hand as a plasmid; any team with a Pseudomonas host and a surface-polysaccharide assay could test what it does. A phage fiber of unknown function with a confident predicted structure is a reasonable target for exactly that kind of collaboration.

Second, a source of the Calx-beta anchor module. The anchor (residues 1-110 of the full-length protein, 42 percent identical to the tail spike's) is a candidate attachment part for chimeric-fiber work: it is the module that two different fibers of this phage both use. Note that the submitted part starts at residue 105 and therefore contains only the tail end of that anchor; a team wanting the anchor itself should take it from the full-length CDS, which is in the genome record cited in the source field.

## discussion

**title:** Why submit a part whose function is unknown

Limitations. Function unknown. Roughly 800 residues without a structural template. The model is confident in shape only, and a confident fold is not a function. Expression is untested, and 91.6 kDa for the tagged protein is a hard target.

Why submit it anyway. The sequence and the structural relationship are real results, and the Registry explicitly values negative and inconclusive documentation. A phage fiber that shares its virion-attachment anchor with a tail spike whose body we do call a depolymerase is a useful thing for the next team to have, precisely because its function is open.

What would settle it. Expression and a surface-polysaccharide assay, or a structure. Until then, no functional claim should be attached to this part, and in particular the withdrawn glycosidase annotation should not be reinstated from the older files that still carry it.
