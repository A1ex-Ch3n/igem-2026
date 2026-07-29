#!/usr/bin/env python3
"""
Two explanatory figures for the write-up, on top of the main locus comparison.

fig2  ortholog-cluster presence/absence across the three strain groups --
      makes "only 4 of 45 clusters are core" visible instead of a number.
fig3  the host-range prediction: what has actually been tested vs what the
      cassette difference predicts.  Kept deliberately blunt so nobody reads
      the untested cells as results.

Outputs -> code/output/0727_o_antigen_comparison/
    fig2_cluster_presence.png
    fig3_hostrange_prediction.png
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "code/output/0727_o_antigen_comparison"

GROUPS = {
    "Strain 2\n(9-2-1, 9-6-2)": ["9-2-1", "9-6-2"],
    "Strain 1\n(8-5-2, 10-10-2)": ["8-5-2", "10-10-2"],
    "Strain 3\n(8-10-2)": ["8-10-2"],
}


def fig2() -> None:
    m = pd.read_csv(OUT / "gene_content_matrix.tsv", sep="\t", index_col=0)
    pres = pd.DataFrame({g: (m[c].sum(axis=1) > 0).astype(int)
                         for g, c in GROUPS.items()})
    # order: core first, then shared pairs, then singletons
    pres["_n"] = pres.sum(axis=1)
    pres = pres.sort_values(["_n"] + list(GROUPS), ascending=False).drop(columns="_n")

    fig, ax = plt.subplots(figsize=(11, 3.4))
    ax.imshow(pres.T.values, aspect="auto", interpolation="nearest",
              cmap=ListedColormap(["#ecf0f1", "#2c7fb8"]))
    ax.set_yticks(range(len(pres.columns)))
    ax.set_yticklabels(pres.columns, fontsize=10)
    ax.set_xticks([])
    ax.set_xlabel(f"{len(pres)} ortholog clusters "
                  "(MMseqs, ≥30% identity / ≥50% coverage)", fontsize=10)

    n_core = int((pres.sum(axis=1) == 3).sum())
    ax.axvline(n_core - 0.5, color="#c0392b", lw=2.5)
    # axes-relative so the label cannot fall outside the drawn area
    ax.text(n_core / len(pres) + 0.012, 1.06,
            f"← 只有 {n_core} 個 cluster 是三株共有的（全部是通用糖化學，沒有組裝機械）",
            transform=ax.transAxes, fontsize=10.5, color="#c0392b",
            ha="left", va="bottom")
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.legend(handles=[Patch(fc="#2c7fb8", label="present"),
                       Patch(fc="#ecf0f1", ec="grey", label="absent")],
              loc="upper right", bbox_to_anchor=(1.0, 1.42), ncols=2,
              frameon=False, fontsize=9)
    ax.set_title("每一格 = 一個 ortholog cluster；三株之間幾乎不重疊",
                 fontsize=13, pad=46)
    fig.savefig(OUT / "fig2_cluster_presence.png", dpi=300, bbox_inches="tight")
    print("wrote fig2_cluster_presence.png")


def fig3() -> None:
    labels = ["Strain 2\n9-2-1 / 9-6-2", "Strain 1\n8-5-2 / 10-10-2", "Strain 3\n8-10-2"]
    # 0 = tested & infects, 1 = untested (predicted negative)
    state = np.array([[0, 1, 1]])
    cell_text = ["已測試\n會裂解", "未測試\n預測不裂解", "未測試\n預測不裂解"]

    fig, ax = plt.subplots(figsize=(9, 2.9))
    ax.imshow(state, aspect="auto", interpolation="nearest",
              cmap=ListedColormap(["#27ae60", "#dfe6e9"]), vmin=0, vmax=1)
    for i, txt in enumerate(cell_text):
        ax.text(i, 0, txt, ha="center", va="center", fontsize=11,
                color="white" if state[0, i] == 0 else "#2d3436",
                fontweight="bold" if state[0, i] == 0 else "normal")
    ax.set_xticks(range(3))
    ax.set_xticklabels(labels, fontsize=10)
    ax.set_yticks([0])
    ax.set_yticklabels(["噬菌體\n9-2-1 Φ8"], fontsize=10)
    ax.tick_params(length=0)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_title("宿主範圍：目前只測過一株\n"
                 "灰色格子是「預測」，不是結果 — 一次 spot assay 就能驗",
                 fontsize=12, pad=14)
    fig.savefig(OUT / "fig3_hostrange_prediction.png", dpi=300, bbox_inches="tight")
    print("wrote fig3_hostrange_prediction.png")


if __name__ == "__main__":
    plt.rcParams["font.sans-serif"] = [
        "Heiti TC", "PingFang TC", "Arial Unicode MS", "DejaVu Sans"]
    plt.rcParams["axes.unicode_minus"] = False
    fig2()
    fig3()
