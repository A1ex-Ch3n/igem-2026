#!/usr/bin/env python3
"""
Compare the extracted O-antigen cassettes across isolates.

Product strings alone are a weak basis for calling genes shared or unique --
Bakta will happily give two unrelated glycosyltransferases the same label.  So
orthology here is decided by sequence: MMseqs2 clusters the cassette proteins,
and an all-vs-all search supplies the identity values.

Outputs -> code/output/0727_o_antigen_comparison/
    ortholog_clusters.tsv      cluster id -> members
    gene_content_matrix.tsv    cluster x isolate presence/absence
    all_vs_all_hits.m8         MMseqs all-vs-all hits (consumed by plot_loci.py)
    pair_identity.tsv          best-hit-per-query identity for every isolate pair
                               (one-directional -- NOT reciprocal best hits)
    shared_unique_summary.tsv  per strain-group: shared / unique cluster counts
"""
from __future__ import annotations

import subprocess
from itertools import combinations
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "code/output/0727_o_antigen_comparison"
TMP = OUT / "mmseqs_tmp"   # name matches the .gitignore pattern

ISOLATES = ["9-2-1", "9-6-2", "8-5-2", "10-10-2", "8-10-2"]
STRAIN_OF = {
    "9-2-1": "Strain 2", "9-6-2": "Strain 2",
    "8-5-2": "Strain 1", "10-10-2": "Strain 1",
    "8-10-2": "Strain 3",
}

# Cross-strain orthologs of sugar enzymes diverge fast; 30% identity over half
# the length is the usual floor for calling them the same gene.
MIN_ID, MIN_COV = "0.30", "0.50"


def run(cmd: list[str]) -> None:
    # MMseqs re-invokes itself internally and mishandles paths containing
    # spaces (this repo lives in ".../iGEM 26"), so every call is made from
    # inside OUT with relative paths only.
    proc = subprocess.run(cmd, cwd=OUT, capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit(f"{' '.join(cmd)}\n{proc.stdout[-2000:]}\n{proc.stderr[-2000:]}")


def main() -> None:
    TMP.mkdir(parents=True, exist_ok=True)

    combined = OUT / "all_locus_proteins.faa"
    with combined.open("w") as fh:
        for iso in ISOLATES:
            fh.write((OUT / f"locus_{iso}.faa").read_text())

    # ---- cluster -------------------------------------------------------
    run(["mmseqs", "easy-cluster", "all_locus_proteins.faa",
         "mmseqs_tmp/clust", "mmseqs_tmp/wd",
         "--min-seq-id", MIN_ID, "-c", MIN_COV, "--cov-mode", "0"])

    memb = pd.read_csv(TMP / "clust_cluster.tsv", sep="\t", header=None,
                       names=["representative", "member"])
    memb["isolate"] = memb["member"].str.split("|").str[0]
    memb["locus_tag"] = memb["member"].str.split("|").str[1]

    reps = {r: f"OG{ i + 1:03d}" for i, r in enumerate(sorted(memb["representative"].unique()))}
    memb["cluster"] = memb["representative"].map(reps)

    products = (pd.read_csv(OUT / "locus_table.tsv", sep="\t", dtype=str)
                  .set_index("locus_tag")["product"].to_dict())
    memb["product"] = memb["locus_tag"].map(products)
    memb.sort_values(["cluster", "isolate"]).to_csv(
        OUT / "ortholog_clusters.tsv", sep="\t", index=False)

    # ---- presence / absence -------------------------------------------
    mat = (memb.pivot_table(index="cluster", columns="isolate",
                            values="locus_tag", aggfunc="count")
               .reindex(columns=ISOLATES).fillna(0).astype(int))
    # label each cluster by the most common product among its members
    mat.insert(0, "product", memb.groupby("cluster")["product"]
               .agg(lambda s: s.value_counts().index[0]))
    mat.to_csv(OUT / "gene_content_matrix.tsv", sep="\t")

    # ---- per-strain-group sharing --------------------------------------
    groups = sorted(set(STRAIN_OF.values()))
    present = {g: set(mat.index[(mat[[i for i in ISOLATES
                                      if STRAIN_OF[i] == g]] > 0).any(axis=1)])
               for g in groups}
    summary = []
    for g in groups:
        others = set().union(*(present[o] for o in groups if o != g))
        summary.append({
            "strain_group": g,
            "isolates": ",".join(i for i in ISOLATES if STRAIN_OF[i] == g),
            "n_clusters": len(present[g]),
            "unique_to_group": len(present[g] - others),
            "shared_with_any_other": len(present[g] & others),
        })
    core = set.intersection(*present.values())
    summary.append({"strain_group": "CORE (all 3)", "isolates": "-",
                    "n_clusters": len(core), "unique_to_group": "-",
                    "shared_with_any_other": "-"})
    sdf = pd.DataFrame(summary)
    sdf.to_csv(OUT / "shared_unique_summary.tsv", sep="\t", index=False)

    # ---- pairwise identity ---------------------------------------------
    # NB: this is best-hit-per-query in one direction, not RBH.  It also uses a
    # looser cutoff (20% id / 40% cov) than the clustering above (30%/50%), so
    # these counts are deliberately not comparable with the cluster counts.
    run(["mmseqs", "easy-search", "all_locus_proteins.faa",
         "all_locus_proteins.faa", "all_vs_all_hits.m8", "mmseqs_tmp/wd2",
         "--min-seq-id", "0.20", "-c", "0.4",
         "--format-output", "query,target,fident,alnlen,evalue,bits"])
    hits = pd.read_csv(OUT / "all_vs_all_hits.m8", sep="\t", header=None,
                       names=["query", "target", "fident", "alnlen", "evalue", "bits"])
    hits["qi"] = hits["query"].str.split("|").str[0]
    hits["ti"] = hits["target"].str.split("|").str[0]
    rows = []
    for a, b in combinations(ISOLATES, 2):
        sub = hits[(hits["qi"] == a) & (hits["ti"] == b)]
        best = sub.sort_values("bits", ascending=False).drop_duplicates("query")
        rows.append({
            "isolate_a": a, "isolate_b": b,
            "strain_a": STRAIN_OF[a], "strain_b": STRAIN_OF[b],
            "n_best_hits": len(best),
            "mean_identity": round(best["fident"].mean(), 3) if len(best) else 0.0,
            "median_identity": round(best["fident"].median(), 3) if len(best) else 0.0,
        })
    pd.DataFrame(rows).to_csv(OUT / "pair_identity.tsv", sep="\t", index=False)

    print(sdf.to_string(index=False))
    print()
    print(pd.DataFrame(rows).to_string(index=False))
    print(f"\n{len(mat)} ortholog clusters across {len(memb)} cassette proteins")


if __name__ == "__main__":
    main()
