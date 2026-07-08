# 9-2-1 Φ8 — RBP variable region & how it binds the receptor on 9-2-1

*Overnight analysis, 2026-07-08. Sequence-level, done entirely locally (novel phage sequences were
deliberately NOT sent to any external service). Structure prediction is teed up for Laguna — see the
runbook at the end. Confidence is flagged throughout: some of this is solid, some is hypothesis to test.*

## TL;DR
- The phage is a **short-tailed podovirus** whose receptor-binding proteins (RBPs) are a cluster of
  **tail fibers/spikes** (CDS_0014–0018), dominated by **two tailspikes** (CDS_0015, CDS_0016).
- Each RBP has the classic modular layout: a **conserved N-terminal domain that anchors it to the
  virion**, and a **variable C-terminal domain that is the receptor-binding domain (RBD)** — this
  C-terminal RBD is "the variable region" you asked about.
- The tailspikes have the amino-acid signature of **β-helix depolymerases**, so the most likely
  receptor on 9-2-1 is its **LPS O-antigen** (a rhamnose-containing O-antigen — the host has the full
  biosynthesis locus). The tailspike RBD binds and probably enzymatically **cleaves the O-antigen**
  to walk the phage down to the cell surface. A protein receptor (an outer-membrane porin/TBDR) is the
  secondary hypothesis, most plausibly for the small **tail fiber CDS_0018**.
- **To confirm:** fold the RBPs on Laguna (β-helix + active-site groove = depolymerase → LPS), and
  genetically/biochemically the O-antigen link. Inputs are prepared (`fold/`).

---

## 1. The RBP repertoire — the tail module (CDS_0014–0020)

The phage's structural genes run head → tail in one block; the receptor-facing genes are:

| CDS | aa | pharokka call | PHROG | note |
|---|---:|---|---|---|
| 0014 | 477 | hypothetical (pre-tail) | 4137 | adaptor/tail-completion, sits just upstream of the spikes |
| **0015** | **547** | **tail spike** | **4636** | tailspike #1 — shares a conserved N-term with 0017 |
| **0016** | **402** | **tail spike** | **4636** | tailspike #2 — strongest tailspike hit (e=1.8e-71); most fibrous |
| **0017** | **917** | **tail protein** | 2871 | large; conserved N-term (attachment), long variable C-term |
| **0018** | **118** | **tail fiber** | 8469 | small fiber — best candidate for a *protein* receptor |
| 0019 | 577 | internal virion protein | 511 | **ejection protein — a Podoviridae hallmark** |
| 0020 | 212 | virion structural | 17319 | |

The **internal virion / ejection protein (0019)** plus the short tail with multiple **tailspikes** is
the signature of a **short-tailed podovirus** (T7/P22/N4-like). In podoviruses the tailspikes are the
primary RBPs and they typically target **surface polysaccharide (LPS O-antigen or capsule)**, often
enzymatically. *(Confidence: high — architecture is unambiguous.)*

## 2. The variable region = the C-terminal receptor-binding domain

Two independent lines of local evidence place the variable region at the **C-terminus** of each RBP:

**(a) Conserved N-terminal, divergent C-terminal.** CDS_0015 and CDS_0017 share a clear N-terminal
homology block — ~250 aligned aa at 32% identity (local-align score 191), strongest over the first
~100 aa (up to 56% identity in a 25-aa window). Past that block their sequences diverge. That shared
N-terminal module is the **particle-attachment domain** (it plugs into the tail hub, so it is
conserved across the phage's own tail proteins); everything C-terminal of it is free to vary and is
the **receptor-binding domain**. Approximate splits (to be refined by structure):
- **CDS_0015:** attachment ≈ aa 1–160, **variable RBD ≈ aa 161–547**
- **CDS_0017:** attachment ≈ aa 1–254, **variable RBD ≈ aa 255–917** (long — a fiber + tip)
- **CDS_0016:** a standalone tailspike; short N-anchor then a **β-helix RBD** over most of its length
- **CDS_0018:** 118 aa, essentially all fiber/tip

**(b) Fibrous β-helix composition.** Every tail protein is strongly enriched in Gly/Ser/Thr/Ala/Asn/Asp
(40–53%) and depleted in aromatics (5–12%) — the hallmark composition of **β-helix / β-solenoid fibers**,
the fold used by tailspike depolymerases. Tailspike #2 (0016) is the most extreme (53% GSTAND), i.e.
the strongest β-helix depolymerase candidate. *(Confidence: medium-high — composition is diagnostic of
the fold class; structure prediction will confirm the actual β-helix and any active-site groove.)*

Two tailspikes of the same PHROG family but different sequence = **two receptor specificities** on one
phage — a common way phages broaden or tune host range. That is exactly where "variable region"
matters: swapping/mutating these C-terminal RBDs is what changes what the phage can bind.

## 3. How it binds the receptor on 9-2-1

**Primary hypothesis — LPS O-antigen (glycan receptor), engaged by tailspike depolymerase.**
- The tailspikes' β-helix-depolymerase signature means they most likely recognize a **repeating sugar**
  — i.e. the **O-antigen** of the host LPS — rather than a protein.
- The host 9-2-1 has a **complete rhamnose-containing O-antigen biosynthesis locus** (≈1.41–1.44 Mb,
  OHPLIO_01274–01298): O-antigen chain-length regulator (*wzz*), oligosaccharide flippase (*wzx*),
  the dTDP-L-rhamnose pathway (*rmlABCD* incl. RfbA/OHPLIO_01298), and UDP-sugar–modifying enzymes
  that build an unusual amino-uronic-acid sugar — plus LPS core (heptosyltransferases, RfaG/RfaP) and
  O-antigen ligase (*waaL*). So there is a real, defined O-antigen for a tailspike to target.
- **Model:** the tailspike RBD (C-terminal β-helix) binds a specific O-antigen sugar repeat and its
  active-site groove **cleaves the O-antigen**, letting the virion descend to the outer membrane and
  eject its DNA. This is the standard podovirus-tailspike mechanism. *(Confidence: this is the
  best-supported model, but it is a hypothesis — it rests on fold-class inference + the host having the
  substrate, not yet on structure or a binding assay.)*

**Secondary hypothesis — an outer-membrane protein receptor.**
- Some podoviruses use a protein (TBDR or porin) as the terminal/irreversible receptor after the
  initial LPS contact. The small **tail fiber CDS_0018** is the best candidate to read a *protein*
  surface. 9-2-1 offers the usual suspects: OprD-family porins (OHPLIO_00213/01741/01844), major porins
  (00247/00860/00777/01322/01918), and TonB-dependent receptors (00246/00535/00940/01643, FoxA/00129).
- This is exactly what the existing binding screen was built to test — but that screen used *junk*
  literature/predicted RBPs. It can now be re-run with the **real** 9-2-1 Φ8 RBPs (inputs prepared).

**Caveat that matters for the computational screen:** if the true receptor is **LPS (a glycan)**, then
folding RBP × OMP protein complexes (the ipTM binding screen) **will not capture the real interaction** —
you'd need glycan docking or, better, wet-lab validation (O-antigen mutants / LPS extraction + binding).
So treat the protein-receptor fold screen as a test of the *secondary* hypothesis, not the primary one.

## 4. What's solid vs what to test
- **Solid:** short-tailed podovirus; the tail module & 2 tailspikes + tail fiber; modular
  conserved-N-term / variable-C-term RBD layout; fibrous β-helix composition; host has a rhamnose
  O-antigen locus; no virulence/AMR genes.
- **Hypothesis (to test):** LPS O-antigen as the primary receptor via tailspike depolymerase; the exact
  RBD boundaries; whether CDS_0018 reads a protein; which O-antigen sugar is recognized.

## 5. Morning runbook — confirm on Laguna
Everything is prepared in [`fold/`](fold/) (see [`fold/README_RUN.md`](fold/README_RUN.md)). Reuses the
ColabFold pipeline you already run.
1. **Fold the 4 RBP structures** (`fold/structure_monomers.csv`) + the **two tailspike homotrimers**
   (`fold/structure_tailspike_trimers.csv`). Cheap (6 folds), most decisive: a right-handed β-helix with
   a groove = depolymerase → LPS receptor; it also pins the real RBD boundary and the active site.
2. **Binding screen with the REAL RBPs** (`fold/binding_screen_pairs.csv`, 60 pairs = 4 RBP probes ×
   15 shortlisted OMP/TBDR receptors) — tests the protein-receptor (secondary) hypothesis by ipTM,
   upgrading the old junk-RBP screen.
3. **If structures say "depolymerase":** pivot receptor validation to the **O-antigen** — the folded
   RBD groove tells you the sugar chemistry to look for; cross-check against the host O-antigen locus
   genes above; plan an LPS/O-antigen binding or O-antigen-mutant assay in the wet lab.

---
*Log: 2026-07-08 — created overnight. All analysis local; structure prediction deferred to Laguna.
Boundaries and the LPS-vs-protein call are hypotheses to confirm with the folds + wet lab.*
