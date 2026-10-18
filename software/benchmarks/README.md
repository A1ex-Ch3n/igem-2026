# benchmarks — a method of ours that failed, with its control data

We spent several weeks building an RBP × outer-membrane-protein docking screen: fold each phage
receptor-binding protein against each candidate host receptor with AlphaFold2-multimer (ColabFold,
real MSAs), rank the pairs by ipTM, call the top hit the receptor. It was rebuilt three times and
run on a GPU cluster.

**It does not work, and the controls say so.**

- Positive controls — known interacting phage-RBP/receptor pairs from the literature — did not
  score above the negative controls.
- The failure reproduced with a **second, independent** tool (Boltz-2), so it is not a ColabFold
  artefact.
- Mechanistically it could not have worked: cross-kingdom pairs have **no paired MSA**, which is
  what AF-multimer's interface signal is built on.
- And the biology was against it from the start: the receptor for our phage is an **LPS O-antigen
  sugar**, not a protein. A protein–protein docking screen cannot find a protein–sugar interaction.

We publish this because the 2026 rubric credits *"test data, or benchmarking"*, and because the
most useful thing we can hand the next team is the control experiment that saves them the same
weeks. The full write-up, with the control ipTM distributions and the figure, is
[`../../documents/2026-07-13_why_protein_protein_binding_fails.qmd`](../../documents/2026-07-13_why_protein_protein_binding_fails.qmd);
the screen's own code stays in the project repository under `code/0703_phage_host_matrix/fold/`,
`code/0712_phage_rbp_detect/fold_binding/` and `data/processed_genome/binding_screen/`, and is
deliberately **not** packaged as a tool.

**Use this as a negative control, not as a pipeline.** If a future ipTM-ranking screen of this
shape is proposed, run these positive and negative controls first; if they do not separate,
the ranking is noise.
