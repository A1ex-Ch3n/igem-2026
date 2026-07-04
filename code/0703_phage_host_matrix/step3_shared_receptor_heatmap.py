"""
Step 3 (viz): host x our-strain heatmap, colored by the number of receptors each of our
isolates shares with each PharBP host at >=90% identity.

shared(strain S, host genome H) = # of our receptor groups R such that S carries R
(receptor_by_strain) AND R has a >=90% homolog in H (host_receptor_overlap). This is the
"clue quantity": a host sharing many of our receptors + having phages = a candidate source.

Note: shared-receptors is a HOST-level quantity (all phages/RBPs of a host inherit it), so
the honest axis now is host x strain; an RBP-level heatmap waits for the fold/ipTM step.
Rows are the 43 distinct genomes (not the 54 host name strings).

Outputs (code/output/0703_phage_host_matrix/):
  shared_receptors_by_strain.tsv   matrix: genome x our 5 isolates (counts)
  shared_receptors_heatmap.png     the heatmap
"""

import csv
import os
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "output", "0703_phage_host_matrix")
STRAINS = ["9-6-2", "9-2-1", "10-10-2", "8-5-2", "8-10-2"]
TH = 90.0


def main():
    # our receptor -> which isolates carry it
    rep_strains = {}
    for row in csv.DictReader(open(os.path.join(OUT, "receptor_by_strain.tsv")), delimiter="\t"):
        rep_strains[row["cluster_rep"]] = {s for s in STRAINS if row.get(s) == "1"}

    # our receptor -> set of host genomes with a >=90% homolog; + acc metadata
    rep_hits = defaultdict(set)
    acc_org = {}
    for row in csv.DictReader(open(os.path.join(OUT, "host_receptor_overlap.tsv")), delimiter="\t"):
        acc_org[row["host_accession"]] = row["host_organism"]
        if float(row["pct_identity"]) >= TH:
            rep_hits[row["our_rep"]].add(row["host_accession"])

    # per-genome PharBP phage count (sum over the host strings that resolve to it)
    acc_phages = defaultdict(int)
    for row in csv.DictReader(open(os.path.join(OUT, "pharbp_pseudomonas_hosts.tsv")), delimiter="\t"):
        if row["ncbi_accession"]:
            acc_phages[row["ncbi_accession"]] += int(row["n_phages"] or 0)

    accs = sorted(acc_org)
    # shared[acc][strain] = count
    data = {}
    for acc in accs:
        data[acc] = {s: sum(1 for rep, ss in rep_strains.items()
                            if s in ss and acc in rep_hits.get(rep, ()))
                     for s in STRAINS}

    # readable, unique row label: organism (+ phage count)
    def label(acc):
        return f"{acc_org[acc]}  ({acc_phages.get(acc, 0)} ph)"

    df = pd.DataFrame(data).T[STRAINS]
    df.index = [label(a) for a in accs]
    df = df.sort_values(by=["9-6-2", "8-10-2"], ascending=False)

    df.to_csv(os.path.join(OUT, "shared_receptors_by_strain.tsv"), sep="\t")

    # ---- heatmap: sequential single-hue (magnitude), annotated ----
    n = len(df)
    fig, ax = plt.subplots(figsize=(6.2, max(6, 0.32 * n)))
    sns.heatmap(
        df, ax=ax, cmap="Blues", vmin=0, annot=True, fmt="d", annot_kws={"size": 7},
        linewidths=0.5, linecolor="#f0f0f0", square=False,
        cbar_kws={"label": "receptors shared ≥" + f"{int(TH)}% identity", "shrink": 0.4},
    )
    ax.set_title("Receptors our isolates share with each PharBP Pseudomonas host "
                 f"(≥{int(TH)}% id)\n43 host genomes × our 5 isolates",
                 fontsize=10, pad=10)
    ax.set_xlabel("our isolate", fontsize=9)
    ax.set_ylabel("")
    ax.tick_params(axis="y", labelsize=7)
    ax.tick_params(axis="x", labelsize=8, rotation=0)
    plt.tight_layout()
    png = os.path.join(OUT, "shared_receptors_heatmap.png")
    fig.savefig(png, dpi=200, bbox_inches="tight")
    print(f"wrote {png}  ({n} genomes x {len(STRAINS)} isolates)")
    print("top hosts (by 9-6-2 shared):")
    for idx, r in df.head(6).iterrows():
        print(f"  {idx:42} {list(r.values)}")


if __name__ == "__main__":
    main()
