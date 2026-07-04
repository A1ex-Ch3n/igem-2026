"""
Pre-fold deliverables: the two condensed axis lists + an EMPTY heatmap scaffold.

- condensed_rbps.tsv      the 114 RBP families (rows of the matrix)
- condensed_receptors.tsv the 63 receptor panel (columns of the matrix)
- rbp_receptor_iptm_heatmap_EMPTY.png  the 114×63 grid, axes labelled, no values yet
  (swap in binding_matrix.csv after the Laguna fold via fold_heatmap.py to fill it)

Run: python code/0703_phage_host_matrix/fold/make_condensed_and_empty.py
"""

import csv
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
FOLDOUT = os.path.join(HERE, "..", "..", "output", "0703_phage_host_matrix", "fold")


def load(path, key):
    return list(csv.DictReader(open(os.path.join(FOLDOUT, path)), delimiter="\t"))


def main():
    fam = load("probe_map.tsv", "rbp_id")
    rec = load("receptor_map.tsv", "rec_id")

    # --- condensed RBP list (rows) ---
    with open(os.path.join(FOLDOUT, "condensed_rbps.tsv"), "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["rbp_id", "rbp_type", "n_members", "length", "hosts", "example_phages"])
        for r in fam:
            w.writerow([r["rbp_id"], r["types"], r["n_members"], r["len"], r["hosts"],
                        r["phages"][:80]])

    # --- condensed receptor list (columns) ---
    rec_sorted = sorted(rec, key=lambda r: (r["category"], r["rec_id"]))
    with open(os.path.join(FOLDOUT, "condensed_receptors.tsv"), "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["rec_id", "category", "our_strains", "locus_tag", "product"])
        for r in rec_sorted:
            w.writerow([r["rec_id"], r["category"], r["our_strains"], r["locus_tag"], r["product"]])

    # --- EMPTY heatmap (structure only) ---
    fams = [r["rbp_id"] for r in fam]
    cols = [r["rec_id"] for r in rec_sorted]
    cats = [r["category"] for r in rec_sorted]
    M = np.full((len(fams), len(cols)), np.nan)
    cmap = plt.get_cmap("viridis").copy(); cmap.set_bad("#ececec")

    fig, ax = plt.subplots(figsize=(max(9, len(cols) * 0.22), max(8, len(fams) * 0.13)))
    im = ax.imshow(M, aspect="auto", cmap=cmap, vmin=0, vmax=1)
    ax.set_xticks(range(len(cols)))
    ax.set_xticklabels([f"{c} · {cats[j]}" for j, c in enumerate(cols)], rotation=90, fontsize=4)
    ftype = {r["rbp_id"]: r["types"] for r in fam}
    fph = {r["rbp_id"]: r["phages"] for r in fam}
    ax.set_yticks(range(len(fams)))
    ax.set_yticklabels([f"{f} [{ftype[f]}] {fph[f][:22]}" for f in fams], fontsize=3.2)
    for j in range(1, len(cols)):
        if cats[j] != cats[j - 1]:
            ax.axvline(j - 0.5, color="white", lw=0.9)
    ax.set_xlabel("our receptor (grouped by class)", fontsize=9)
    ax.set_ylabel("candidate phage RBP family", fontsize=9)
    ax.set_title(f"RBP family × receptor — EMPTY scaffold ({len(fams)}×{len(cols)})\n"
                 "awaiting ColabFold ipTM (fill via fold_heatmap.py after the Laguna run)",
                 fontsize=9, pad=8)
    cb = fig.colorbar(im, ax=ax, fraction=0.02, pad=0.01); cb.set_label("ipTM (empty)")
    fig.tight_layout()
    out = os.path.join(FOLDOUT, "rbp_receptor_iptm_heatmap_EMPTY.png")
    fig.savefig(out, dpi=170, bbox_inches="tight"); plt.close(fig)

    print(f"condensed_rbps.tsv: {len(fam)} RBP families")
    print(f"condensed_receptors.tsv: {len(rec)} receptors")
    print(f"empty heatmap: {len(fams)}×{len(cols)} -> {os.path.basename(out)}")


if __name__ == "__main__":
    main()
