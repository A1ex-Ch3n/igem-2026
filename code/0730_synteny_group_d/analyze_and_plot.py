#!/usr/bin/env python
"""
0730 synteny + similarity — stage 2: tables + figure.

Question (from the PI, 2026-07-29): justify calling 9-2-1 Phi8 a T7-like
podophage "with synteny and similarity", and confirm the structural-module
identity of CDS_20/08/09/13/14.

Inputs (from stage 1 + mmseqs, in WORK; mmseqs was run in a no-space dir because
it breaks on the repo path's space — see memory local_env_gotchas):
  our_phage.tsv T7.tsv phiKMV.tsv KP32.tsv   id,start,end,strand,product (order)
  rbh_T7_phiKMV.m8 rbh_T7_KP32.m8 rbh_phiKMV_KP32.m8   reference orthologs (RBH)
  srch_T7.m8 os_phiKMV.m8 os_KP32.m8                    our-vs-ref sensitive search

Outputs -> code/output/0730_synteny_group_d/
  fig_synteny_4genome.{png,svg}     4-genome map, functional modules + ortholog ribbons
  tables/synteny_similarity.tsv     virion-module CDS: PHROG, position, T7 role, best hit
  tables/ortholog_matrix.tsv        RBH ortholog counts among the 4 genomes

Key finding this encodes: 9-2-1 Phi8 shares ~0 detectable orthologs with T7 /
phiKMV / KP32 (all ~40 kb cultured Autographiviridae), yet keeps the canonical
podovirus virion-module SYNTENY (portal -> capsid -> internal core -> tail ->
fibers). So "T7-like" is organizational, not phylogenetic: a novel, large
(62 kb), likely-temperate podovirus. The tail is group-D-*like* (an anchor fiber
plus a depolymerase tail spike) but LACKS the T4gp10 hallmark that defines
Latka & Briers 2019 group D (see code/0729_t4gp10_check/), so group-D-like, not
group D sensu stricto.
"""
from __future__ import annotations
import os, csv, sys
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrow, Patch, Polygon

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
WORK = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, "code/0730_synteny_group_d/work")
OUT  = os.path.join(REPO, "code/output/0730_synteny_group_d")
os.makedirs(os.path.join(OUT, "tables"), exist_ok=True)

# ── functional classes (ordered keyword rules; first match wins) ──────────────
CLASSES = [
    ("structural",   "#4E79A7", ["portal", "capsid", "head", "tail", "fiber", "spike",
                                  "baseplate", "neck", "collar", "virion", "internal virion",
                                  "structural", "tube", "connector", "scaffold", "decoration"]),
    ("packaging",    "#F28E2B", ["terminase"]),
    ("DNA/replication", "#59A14F", ["polymerase", "primase", "helicase", "ligase", "nuclease",
                                    "kinase", "methyltransferase", "recombinase", "resolvase",
                                    "reca", "rece", "rect", "erf", "recombination", "dnac",
                                    "replication", "ssdna", "dna binding", "annealing",
                                    "ribonucleotide", "thymidylate", "dna metabolism"]),
    ("lysogeny/control", "#B07AA1", ["integrase", "excisionase", "repressor", "antirepressor",
                                     "cro", "ninb", "ref-like"]),
    ("lysis",        "#E15759", ["endolysin", "holin", "spanin", "lysozyme", "lysis", "hol-like"]),
    ("host takeover / accessory", "#76B7B2", ["antirestriction", "darb", "csra", "regulator",
                                              "oxygenase", "acyltransferase", "transferase",
                                              "moron", "nudix", "phosphatase", "inhibitor"]),
]
UNK = ("hypothetical/unknown", "#BAB0AC")


def classify(product: str) -> tuple[str, str]:
    p = product.lower()
    for name, color, kws in CLASSES:
        if any(k in p for k in kws):
            return name, color
    return UNK


def load(name):
    df = pd.read_csv(os.path.join(WORK, name + ".tsv"), sep="\t")
    df["product"] = df["product"].fillna("hypothetical protein")
    df[["class", "color"]] = df["product"].apply(lambda p: pd.Series(classify(p)))
    return df


def read_pairs(fn):
    path = os.path.join(WORK, fn)
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        return []
    out = []
    for line in open(path):
        f = line.rstrip("\n").split("\t")
        if len(f) >= 2:
            out.append((f[0], f[1]))
    return out


# ── load all four genomes ─────────────────────────────────────────────────────
G = {n: load(n) for n in ["our_phage", "T7", "phiKMV", "KP32"]}
POS = {n: {r.id: (int(r.start), int(r.end)) for r in df.itertuples()} for n, df in G.items()}
LEN = {"our_phage": 62416, "T7": 39937, "phiKMV": 42519, "KP32": 41119}
NICE = {"our_phage": "9-2-1 Φ8  (62,416 bp, novel)", "T7": "T7  (NC_001604)",
        "phiKMV": "φKMV  (NC_005045, Pseudomonas)", "KP32": "KP32  (NC_013647)"}

# ── ortholog matrix (RBH counts) ──────────────────────────────────────────────
rbh = {
    ("T7", "phiKMV"): read_pairs("rbh_T7_phiKMV.m8"),
    ("T7", "KP32"):   read_pairs("rbh_T7_KP32.m8"),
    ("phiKMV", "KP32"): read_pairs("rbh_phiKMV_KP32.m8"),
}
# our-vs-ref: RBH was 0; use sensitive-search best hits for the count (still ~0)
our_hits = {ref: set() for ref in ["T7", "phiKMV", "KP32"]}
for ref in ["T7", "phiKMV", "KP32"]:
    # run_mmseqs.sh writes srch_<ref>.m8; the first manual run also left os_<ref>.m8
    for fn in (f"srch_{ref}.m8", f"os_{ref}.m8"):
        for q, t in read_pairs(fn):
            our_hits[ref].add(q)

names = ["our_phage", "T7", "phiKMV", "KP32"]
mat = pd.DataFrame(0, index=names, columns=names, dtype=int)
for n in names:
    mat.loc[n, n] = len(G[n])
for (a, b), pairs in rbh.items():
    mat.loc[a, b] = mat.loc[b, a] = len(pairs)
for ref, qs in our_hits.items():
    mat.loc["our_phage", ref] = mat.loc[ref, "our_phage"] = len(qs)
mat.to_csv(os.path.join(OUT, "tables/ortholog_matrix.tsv"), sep="\t")
print("ortholog RBH matrix (diagonal = CDS count):")
print(mat.to_string())

# ── C3/C4 virion-module table ─────────────────────────────────────────────────
# canonical T7 podovirus roles for the module CDS the PI named (+ head genes)
T7_ROLE = {
    "UUAIURNK_CDS_0020": "portal / head-tail connector (T7 gp8)",
    "UUAIURNK_CDS_0017": "major capsid protein (T7 gp10)",
    "UUAIURNK_CDS_0016": "head/adaptor structural protein",
    "UUAIURNK_CDS_0014": "tail/adaptor structural protein",
    "UUAIURNK_CDS_0013": "tail/adaptor structural protein",
    "UUAIURNK_CDS_0011": "tail spike RBP — β-helix depolymerase",
    "UUAIURNK_CDS_0010": "tail protein (anchor-fiber position; unknown, group-D-like anchor)",
    "UUAIURNK_CDS_0009": "tail fiber",
    "UUAIURNK_CDS_0008": "internal virion / ejection protein (T7 gp14–16)",
}
ordf = G["our_phage"].set_index("id")
rows = []
for cid in ["UUAIURNK_CDS_0020", "UUAIURNK_CDS_0017", "UUAIURNK_CDS_0016",
            "UUAIURNK_CDS_0014", "UUAIURNK_CDS_0013", "UUAIURNK_CDS_0012",
            "UUAIURNK_CDS_0011", "UUAIURNK_CDS_0010", "UUAIURNK_CDS_0009",
            "UUAIURNK_CDS_0008"]:
    if cid not in ordf.index:
        continue
    r = ordf.loc[cid]
    aa = (int(r.end) - int(r.start) + 1) // 3 - 1
    besthit = "none"
    for ref in ["T7", "phiKMV", "KP32"]:
        if cid in our_hits[ref]:
            besthit = f"weak hit in {ref}"
            break
    role = T7_ROLE.get(cid, "—")
    if cid == "UUAIURNK_CDS_0012":
        role = "GH5 depolymerase (our AF3 call; PHROG: hypothetical)"
    rows.append([cid.replace("UUAIURNK_", ""), r["product"], f"{int(r.start)}–{int(r.end)}",
                 r["strand"], aa, role, besthit])
tbl = pd.DataFrame(rows, columns=["CDS", "PHROG_product", "position_bp", "strand",
                                  "length_aa", "T7_canonical_role", "best_ref_hit"])
tbl.to_csv(os.path.join(OUT, "tables/synteny_similarity.tsv"), sep="\t", index=False)
print("\nvirion-module table:")
print(tbl.to_string(index=False))


# ── figure: 4-genome synteny with ortholog ribbons ────────────────────────────
def arrow(ax, y, s, e, strand, color, h=0.30):
    L = e - s
    head = min(abs(L) * 0.5, 900)
    if strand == "-":
        x, dx = e, -(L)
    else:
        x, dx = s, L
    ax.add_patch(FancyArrow(x, y, dx, 0, width=h, head_width=h, head_length=head,
                            length_includes_head=True, fc=color, ec="black",
                            lw=0.25, alpha=0.95))


def ribbon(ax, y_top, y_bot, xa, xb, color="#888888", alpha=0.18):
    (a0, a1), (b0, b1) = xa, xb
    ax.add_patch(Polygon([(a0, y_top), (a1, y_top), (b1, y_bot), (b0, y_bot)],
                         closed=True, fc=color, ec="none", alpha=alpha))


order = ["our_phage", "phiKMV", "T7", "KP32"]           # ours isolated at top
ymap = {n: len(order) - i for i, n in enumerate(order)}   # top = highest y
fig, ax = plt.subplots(figsize=(15, 6.2))

# ribbons between adjacent tracks
adj = [("phiKMV", "T7", rbh[("T7", "phiKMV")]),          # 6 orthologs
       ("T7", "KP32", rbh[("T7", "KP32")])]              # 40 orthologs (conserved core)
# note: (our_phage, phiKMV) has 0 orthologs -> no ribbon, which is the finding
for top, bot, pairs in adj:
    for a, b in pairs:
        # RBH files are query=first-genome, target=second; map to each track's ids
        ca = a if a in POS[top] else b
        cb = b if b in POS[bot] else a
        if ca in POS[top] and cb in POS[bot]:
            ribbon(ax, ymap[top] - 0.30, ymap[bot] + 0.30, POS[top][ca], POS[bot][cb])

# gene arrows
seen_classes = set()
for n in order:
    y = ymap[n]
    for r in G[n].itertuples():
        arrow(ax, y, int(r.start), int(r.end), r.strand, r.color)
    for cls, col in zip(G[n]["class"], G[n]["color"]):
        seen_classes.add((cls, col))
    ax.text(-1200, y, NICE[n], ha="right", va="center", fontsize=11, weight="bold")
    ax.plot([0, LEN[n]], [y, y], color="black", lw=0.4, zorder=0)

# label key genes on our phage
LAB = {"UUAIURNK_CDS_0020": "portal", "UUAIURNK_CDS_0017": "major capsid",
       "UUAIURNK_CDS_0011": "tail spike\n(depolymerase)", "UUAIURNK_CDS_0010": "tail (unknown)",
       "UUAIURNK_CDS_0009": "tail fiber", "UUAIURNK_CDS_0008": "internal virion",
       "UUAIURNK_CDS_0012": "GH5 depol.", "UUAIURNK_CDS_0080": "DarB antirestriction",
       "UUAIURNK_CDS_0001": "DarB antirestriction", "UUAIURNK_CDS_0061": "RecE recombination",
       "UUAIURNK_CDS_0070": "excisionase"}
yo = ymap["our_phage"]
for cid, lab in LAB.items():
    if cid in POS["our_phage"]:
        s, e = POS["our_phage"][cid]
        ax.annotate(lab, xy=((s + e) / 2, yo + 0.33), xytext=((s + e) / 2, yo + 0.95),
                    ha="center", va="bottom", fontsize=7.3, rotation=35,
                    arrowprops=dict(arrowstyle="-", lw=0.4, color="#555"))

# bracket the podovirus virion-synteny block on our phage
vb_s, vb_e = POS["our_phage"]["UUAIURNK_CDS_0003"][0], POS["our_phage"]["UUAIURNK_CDS_0020"][1]
ax.plot([vb_s, vb_e], [yo - 0.55, yo - 0.55], color="#c0392b", lw=1.6)
ax.text((vb_s + vb_e) / 2, yo - 0.75, "podovirus virion module (portal→capsid→tail→fibers)",
        ha="center", va="top", fontsize=8, color="#c0392b", weight="bold")

ax.set_xlim(-9000, 63500)
ax.set_ylim(0.1, len(order) + 1.4)
ax.set_yticks([])
ax.set_xlabel("genome position (bp)", fontsize=10)
for sp in ("top", "right", "left"):
    ax.spines[sp].set_visible(False)

handles = [Patch(fc=c, ec="black", lw=0.3, label=n) for n, c in sorted(seen_classes)]
ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.09),
          ncol=4, fontsize=8.5, frameon=False, title="functional class")
ax.set_title("Synteny & similarity of 9-2-1 Φ8 vs cultured T7-like podophages\n"
             "ribbons = reciprocal-best-hit orthologs — T7/φKMV/KP32 share a conserved core; "
             "9-2-1 Φ8 shares none, yet keeps the podovirus module order (novel, ~62 kb, "
             "with a lysogeny/recombination module)",
             fontsize=11.5, pad=14)
fig.tight_layout()
for ext in ("png", "svg"):
    fig.savefig(os.path.join(OUT, f"fig_synteny_4genome.{ext}"), dpi=300, bbox_inches="tight")
print("\nwrote fig_synteny_4genome.png|svg")
