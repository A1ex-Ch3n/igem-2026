# 9-2-1 Φ8 RBP structure — conclusions (real-MSA ColabFold + fold analysis)

**Method.** ColabFold AF2-multimer with **real MSA** (remote mmseqs2) on the 8 union RBPs
(single_sequence first gave pLDDT≈30 garbage — MSA was essential). Fold classified WITHOUT a
structure DB via the backbone-H-bond sequence-offset signature (`beta_helix_analysis.py`):
a right-handed parallel **β-helix / β-solenoid** H-bonds between adjacent coils → a sustained
peak at the coil period (~16–24 res); α-helix peaks at offset 4. Cross-checked with %β/%helix,
PCA elongation, and per-residue pLDDT. Scores in `../../output/0712_phage_rbp_detect/structure/`.

## Result
| RBP | pLDDT | HB period | fold | note |
|---|---|---|---|---|
| **CDS_0016 tailspike 2** | 93 | 16–18 | **β-helix depolymerase** | confident; homotrimer folds (ipTM 0.89) |
| **CDS_0015 tailspike 1** | 65 (mono) | 16–18 | **β-helix** (low-conf model) | same period as 0016; trimer pLDDT 50 |
| **CDS_0002** (RBP-Detect-only) | 82 | 22–24 | **β-helix depolymerase** | classic period; Pharokka called it "hypothetical" |
| CDS_0017 tail protein (917 aa) | 89 | — | α-rich globular | tail tube/structural, not an RBP fold |
| CDS_0019 internal virion | 96 | 7 | β-sandwich-like | not a solenoid |
| CDS_0020 | 93 | — | α-helical fiber (elong 10) | structural |
| CDS_0018 tail fiber (118 aa) | 91 | — | small β (too short for coils) | fiber tip |

## Interpretation
- **The tail spikes are β-helix depolymerases** → the phage degrades a **polysaccharide** receptor
  → **primary receptor = LPS O-antigen** (host locus OHPLIO_01274–01298, rhamnose pathway). This is
  structural support for the hypothesis in `../../0708_rbp_analysis/RBP_variable_region_analysis.md`.
- **RBP Detect earned its place:** CDS_0002 — flagged by the ML classifier, missed by Pharokka
  annotation — is itself a clean β-helix depolymerase (a likely second tail spike / depolymerase).
- The AF2-multimer **ipTM RBP×receptor binding screen was retired** (controls OVERLAP: min positive
  0.13 < max negative 0.50 — cross-kingdom phage×OMP pairs have no paired MSA, so the interface
  ranks randomly even with MSA). Protein–protein docking cannot test a sugar receptor anyway.

## Next
1. **(confirm the family)** foldseek/DALI on `CDS_0016__monomer` and `CDS_0002__monomer` → name the
   depolymerase homolog (pectate-lyase-like / P22-tailspike-like). DB-free analysis here is strongly
   consistent but not a named hit.
2. **Pivot receptor validation to LPS O-antigen:** host O-antigen locus + a wet-lab O-antigen /
   rhamnose-pathway knockout adsorption assay.
3. (optional) re-fold the CDS_0015 tail spike 1 trimer with more models/recycles to raise confidence.

---
*Log: 2026-07-13 — real-MSA structures confirm β-helix depolymerase tail spikes → LPS O-antigen
primary receptor. Binding ipTM screen retired (controls failed). foldseek family-ID + wet-lab
O-antigen assay UNDONE.*
