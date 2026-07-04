#!/usr/bin/env python3
"""
RBP family × receptor ipTM heatmap — the final RBP × receptor deliverable.

Reads binding_matrix.csv (rbp_id, rec_id, iptm, ...) + probe_map.tsv + receptor_map.tsv
(for labels/order) and renders a single heatmap: rows = RBP families, cols = receptors
(grouped by category), colour = ipTM (0-1). Rows sorted by best ipTM (top binders first).

Usage: python3 fold_heatmap.py [binding_matrix.csv]   (default: binding_matrix.csv in this dir)
"""
import csv
import os
import sys
from collections import defaultdict

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
MATRIX = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "binding_matrix.csv")


def load_map(path, key):
    return {r[key]: r for r in csv.DictReader(open(path), delimiter="\t")}


def main():
    fmap = load_map(os.path.join(HERE, "probe_map.tsv"), "rbp_id")
    rmap = load_map(os.path.join(HERE, "receptor_map.tsv"), "rec_id")
    scores = {}
    for r in csv.DictReader(open(MATRIX)):
        try:
            scores[(r["rbp_id"], r["rec_id"])] = float(r["iptm"])
        except (KeyError, ValueError):
            pass

    # columns: receptors grouped by category then rec_id
    recs = sorted(rmap, key=lambda c: (rmap[c]["category"], c))
    # rows: RBP families by best ipTM (top binders first)
    best = {f: max((scores.get((f, c), 0) for c in recs), default=0) for f in fmap}
    fams = sorted(fmap, key=lambda f: -best[f])

    M = np.full((len(fams), len(recs)), np.nan)
    for i, f in enumerate(fams):
        for j, c in enumerate(recs):
            v = scores.get((f, c))
            if v is not None:
                M[i, j] = v

    fig, ax = plt.subplots(figsize=(max(9, len(recs) * 0.22), max(8, len(fams) * 0.13)))
    im = ax.imshow(M, aspect="auto", cmap="viridis", vmin=0, vmax=1)
    ax.set_xticks(range(len(recs)))
    ax.set_xticklabels([f"{c} · {rmap[c]['category']}" for c in recs], rotation=90, fontsize=4)
    ax.set_yticks(range(len(fams)))
    ax.set_yticklabels([f"{f} [{fmap[f]['types']}] {fmap[f]['phages'][:24]}" for f in fams],
                       fontsize=3.2)
    # category separators on x
    cats = [rmap[c]["category"] for c in recs]
    for j in range(1, len(recs)):
        if cats[j] != cats[j - 1]:
            ax.axvline(j - 0.5, color="white", lw=0.8)
    ax.set_xlabel("our receptor (grouped by class)", fontsize=9)
    ax.set_ylabel("candidate phage RBP family", fontsize=9)
    ax.set_title(f"RBP family × receptor — ColabFold ipTM  ({len(fams)}×{len(recs)})\n"
                 "monomer×monomer approximation; high ipTM = wet-lab priority", fontsize=9, pad=8)
    fig.colorbar(im, ax=ax, fraction=0.02, pad=0.01).set_label("ipTM")
    fig.tight_layout()
    out = os.path.join(HERE, "rbp_receptor_iptm_heatmap.png")
    fig.savefig(out, dpi=170, bbox_inches="tight")
    print(f"{len(fams)}×{len(recs)} -> {out}")
    top = sorted(((best[f], f) for f in fams), reverse=True)[:8]
    print("top RBP families by best ipTM:")
    for s, f in top:
        print(f"  {f}  best_ipTM={s:.2f}  [{fmap[f]['types']}]  {fmap[f]['phages'][:40]}")


if __name__ == "__main__":
    main()
