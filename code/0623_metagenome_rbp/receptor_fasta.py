#!/usr/bin/env python3
"""
Build per-strain receptor-only protein FASTAs, re-derived FRESH from the raw
Bakta genome annotations (NOT from the 0620 curated list).

For each of the 3 sampled isolates (9-6-2, 9-2-1, 10-10-2) we:
  1. Read the raw Bakta `.tsv` (function) + `.faa` (sequence) from the SAME
     annotation run, so locus tags and sequences are internally consistent.
  2. Classify every protein with an independent product-keyword ruleset that
     KEEPS surface receptor folds a phage tail fiber could bind (TonB-dependent
     receptors, OprD/porins, OmpA/W, TolC OM channel, LptD, FadL, Tsx, ushers,
     siderophore receptors) and DROPS unrelated membrane proteins (Bam/Lol/Mla
     biogenesis, TonB/Exb energizers, inner-membrane / periplasmic efflux
     subunits, permeases, aquaporins, OmpR-type transcription factors, IM
     chemotaxis/aerotaxis receptors).
  3. Write one receptor-only FASTA per strain + a combined table.
  4. Cross-check the fresh list against the 0620 curated set (237 proteins) as
     an INDEPENDENT accuracy audit -> reconciliation_vs_0620.md.

Stdlib only. Run from the repo root or anywhere:
    python code/0623_metagenome_rbp/receptor_fasta.py
"""

import os
import re
import sys

# ---------------------------------------------------------------- paths
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

STRAINS = {
    "9-6-2": "data/bacteria_genome/9-6-2/rerun_QB9Y48/annotation/QB9Y48_1_rerun_sample_2_2_1_reference",
    "9-2-1": "data/bacteria_genome/9-2-1/annotation/XH254M_1_sample_1_1_reference",
    "10-10-2": "data/bacteria_genome/10-10-2/annotation/XH254M_3_sample_3_1_reference",
    "8-5-2": "data/bacteria_genome/8-5-2/annotation/B9TF7H_1_Sample_1_8A_1_reference",
    "8-10-2": "data/bacteria_genome/8-10-2/annotation/CZJZZ4_1_rerun_Sample_2_8B_2_1_reference",
}

REF_0620 = "code/output/0620_receptor_classification/receptor_classification.tsv"
OUTDIR = "code/0623_metagenome_rbp/out_receptor_fasta"

# GO terms for outer-membrane localisation (supporting evidence)
GO_OUTER_MEMBRANE = {"GO:0009279", "GO:0019867"}  # cell outer membrane / OM


# ---------------------------------------------------------------- ruleset
# A protein is a receptor candidate iff it is NOT hard-excluded AND it matches
# an include cue. Exclusion is checked first and wins.

def _has(p, *subs):
    return any(s in p for s in subs)


def is_excluded(prod):
    """Membrane proteins that are NOT phage receptors. Returns reason or ''."""
    p = prod.lower()

    # OM biogenesis / assembly machinery (Bam, Lol, Mla, Skp/OmpH, surface assembly)
    if _has(p, "assembly factor", "bama", "bamb", "bamc", "bamd", "bame"):
        return "OM biogenesis (Bam)"
    if _has(p, "lol", "lipoprotein insertase", "lipoprotein-releasing",
            "lipoprotein chaperone"):
        return "lipoprotein localization (Lol)"
    if _has(p, "mla", "lipid asymmetry", "phospholipid transport",
            "intermembrane phospholipid", "mce/mlad"):
        return "phospholipid/asymmetry (Mla/Mce)"
    if _has(p, "omph family", "skp ", "periplasmic chaperone", "chaperone sura"):
        return "periplasmic chaperone (Skp/OmpH)"

    # TonB / Exb / Tol energizers (NOT the TonB-dependent receptors)
    if "tonb" in p and "dependent" not in p and "denpendent" not in p:
        return "TonB/Exb energizer or fragment"
    if _has(p, "exbb", "exbd", "biopolymer transport", "proton channel",
            "mota/tolq", "tolq", "tolr"):
        return "TonB/Tol energizer"

    # signaling / regulators that carry 'receptor' or 'Omp' but are cytoplasmic/IM
    if _has(p, "transcriptional regulat", "response regulator", "ompr"):
        return "transcription factor / two-component regulator"
    if _has(p, "aerotaxis", "chemotaxis", "methyl-accepting",
            "cyclic di-gmp", "di-gmp receptor"):
        return "inner-membrane signaling receptor"

    # water/glycerol channels (MIP family, inner membrane) -- match 'porin'
    if _has(p, "aquaporin", "aquaglyceroporin"):
        return "aquaporin (inner membrane water channel)"

    # inner-membrane / periplasmic transport components
    if _has(p, "permease", "abc transporter", "atp-binding", "atp binding",
            "ftsx", "feob", "ncs1", "mfs transporter", "mate transporter",
            "smr transporter", "pace transporter", "symporter", "antiporter"):
        return "inner-membrane transporter component"
    # efflux components: keep ONLY the OM channel subunit; drop IM/periplasmic parts
    if "efflux" in p and "outer membrane" not in p:
        return "efflux pump inner-membrane/periplasmic subunit"
    if _has(p, "periplasmic adaptor", "membrane fusion protein",
            "adaptor subunit"):
        return "efflux periplasmic adaptor (membrane fusion)"

    # OM-anchored enzymes / structural appendage / biogenesis lipoproteins
    if _has(p, "transglycosylase", "murein", "lytic"):
        return "peptidoglycan enzyme"
    if "flagellar" in p:                       # rings/hook/basal body (flagellin kept below)
        return "flagellar structural component"
    if _has(p, "lpte", "lpta", "lptc", "lps-assembly lipoprotein"):
        return "LPS-assembly accessory (not LptD)"
    if _has(p, "alginate biosynthesis", "osmotically"):
        return "biosynthesis/stress lipoprotein"

    # small structural OM lipoproteins (not receptors)
    if _has(p, "major outer membrane lipoprotein", "lipoprotein blc"):
        return "structural OM lipoprotein"
    if p.startswith("peptidoglycan-associated"):  # Pal (keep full OmpA/Pal barrels)
        return "structural OM lipoprotein (Pal)"

    return ""


def include_category(prod, dbxrefs):
    """Return a coarse receptor category if this is a receptor, else ''.
    Order encodes priority for the category label."""
    p = prod.lower()
    om = "outer membrane" in p

    # flagellin filament (flagellotropic phage receptor); 'flagellar' parts excluded upstream
    if "flagellin" in p and not _has(p, "regulator", "synthesis", "export",
                                     "chaperone", "methyltransferase"):
        return "flagellin"

    # type IV major pilin (PilA) -- dominant Pseudomonas phage receptor; exclude
    # the assembly/secretion/regulatory machinery (pseudopilins, prepilin, PilQ, etc.)
    if "pilin" in p and not _has(p, "assembly", "prepilin", "pseudopilin",
                                 "peptidase", "leader", "methyltransferase",
                                 "regulator", "biogenesis", "modification",
                                 "stability", "minor", "atpase", "secretin"):
        return "pilin"

    # TonB-dependent / siderophore / iron receptors
    if _has(p, "tonb-dependent", "tonb-denpendent", "siderophore receptor"):
        return "TBDR"
    if _has(p, "ferrichrome", "ferrioxamine", "pseudobactin", "enterobactin",
            "ferric") and _has(p, "receptor", "outer membrane", "transporter/phage"):
        return "TBDR"

    if "lptd" in p:
        return "LptD"
    if _has(p, "fadl", "long-chain fatty acid transport"):
        return "FadL"
    if "usher" in p:
        return "usher"
    if _has(p, "tsx") or ("nucleoside" in p and (om or "channel" in p)):
        return "Tsx"
    if _has(p, "tolc") or ("efflux" in p and om):
        return "TolC/efflux-OM"
    if _has(p, "ompa"):
        return "OmpA"
    if _has(p, "ompw", "ompc", "ompf", "ompk"):
        return "Omp-porin"
    if "porin" in p:        # aquaporins already excluded upstream
        return "porin"
    if om:                  # remaining genuine OM beta-barrels / surface proteins
        return "other-OM"
    return ""


def classify(prod, dbxrefs):
    """-> (is_receptor: bool, category_or_excludereason: str)"""
    reason = is_excluded(prod)
    if reason:
        return False, reason
    cat = include_category(prod, dbxrefs)
    if cat:
        return True, cat
    return False, "not a receptor fold"


# ---------------------------------------------------------------- parsing
def parse_tsv(path):
    """Return list of dicts for CDS rows: locus_tag, gene, product, dbxrefs(set)."""
    rows = []
    with open(path) as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            f = line.rstrip("\n").split("\t")
            if len(f) < 8 or f[1] != "cds":
                continue
            dbx = set()
            if len(f) >= 9:
                dbx = {x.strip() for x in f[8].split(",") if x.strip()}
            rows.append({
                "locus_tag": f[5].strip(),
                "gene": f[6].strip(),
                "product": f[7].strip(),
                "dbxrefs": dbx,
            })
    return rows


def parse_faa(path):
    """Return {locus_tag: sequence}."""
    seqs, lt, buf = {}, None, []
    with open(path) as fh:
        for line in fh:
            if line.startswith(">"):
                if lt is not None:
                    seqs[lt] = "".join(buf)
                lt = line[1:].split()[0].strip()
                buf = []
            else:
                buf.append(line.strip())
    if lt is not None:
        seqs[lt] = "".join(buf)
    return seqs


def load_0620(path):
    """Return {(strain, locus_tag): annotation} for the curated reference set."""
    ref = {}
    with open(path) as fh:
        header = fh.readline().rstrip("\n").split("\t")
        si, li, ai = header.index("strain"), header.index("locus_tag"), header.index("annotation")
        for line in fh:
            f = line.rstrip("\n").split("\t")
            if len(f) <= max(si, li, ai):
                continue
            ref[(f[si].strip(), f[li].strip())] = f[ai].strip()
    return ref


# ---------------------------------------------------------------- main
def wrap(seq, width=60):
    return "\n".join(seq[i:i + width] for i in range(0, len(seq), width))


def main():
    outdir = os.path.join(REPO, OUTDIR)
    os.makedirs(outdir, exist_ok=True)

    ref0620 = load_0620(os.path.join(REPO, REF_0620))
    ref0620_by_strain = {}
    for (s, lt) in ref0620:
        ref0620_by_strain.setdefault(s, set()).add(lt)

    all_rows = []          # kept receptors across strains
    per_strain_kept = {}
    fresh_by_strain = {}   # strain -> set(locus_tag) kept

    for strain, base in STRAINS.items():
        tsv = os.path.join(REPO, base + ".tsv")
        faa = os.path.join(REPO, base + ".faa")
        rows = parse_tsv(tsv)
        seqs = parse_faa(faa)

        kept = []
        for r in rows:
            lt = r["locus_tag"]
            seq = seqs.get(lt)
            if not seq:
                continue
            is_rec, label = classify(r["product"], r["dbxrefs"])
            if is_rec:
                kept.append((r, seq, label))

        # write per-strain receptor FASTA
        fa_path = os.path.join(outdir, f"{strain}_receptors.faa")
        with open(fa_path, "w") as out:
            for r, seq, cat in kept:
                hdr = (f">{r['locus_tag']} strain={strain} category={cat} "
                       f"product={r['product']}")
                out.write(hdr + "\n" + wrap(seq) + "\n")

        per_strain_kept[strain] = len(kept)
        fresh_by_strain[strain] = {r["locus_tag"] for r, _, _ in kept}
        for r, seq, cat in kept:
            go_om = bool(GO_OUTER_MEMBRANE & r["dbxrefs"])
            in0620 = (strain, r["locus_tag"]) in ref0620
            all_rows.append({
                "strain": strain, "locus_tag": r["locus_tag"], "gene": r["gene"],
                "product": r["product"], "category": cat,
                "go_outer_membrane": "yes" if go_om else "",
                "in_0620": "yes" if in0620 else "no",
            })
        print(f"{strain}: {len(rows)} CDS -> {len(kept)} receptors")

    total = sum(per_strain_kept.values())
    print(f"TOTAL receptors: {total}")

    # combined table
    cols = ["strain", "locus_tag", "gene", "product", "category",
            "go_outer_membrane", "in_0620"]
    tbl_path = os.path.join(outdir, "receptors_all.tsv")
    with open(tbl_path, "w") as out:
        out.write("\t".join(cols) + "\n")
        for row in all_rows:
            out.write("\t".join(row[c] for c in cols) + "\n")

    # ---------------- reconciliation vs 0620 (accuracy audit) ----------------
    lines = []
    lines.append("# Receptor list accuracy check: fresh (0623, from raw data) vs 0620 curated\n")
    lines.append("Fresh list re-derived independently from the raw Bakta annotations "
                 "by product-keyword ruleset. The 0620 curated list (237) is used "
                 "here only as an independent reference to gauge accuracy.\n")
    lines.append("| strain | fresh | 0620 | shared | fresh-only | 0620-only |")
    lines.append("|---|---|---|---|---|---|")
    g_fresh = g_ref = g_shared = 0
    new_only_all, ref_only_all = [], []
    for strain in STRAINS:
        fresh = fresh_by_strain[strain]
        ref = ref0620_by_strain.get(strain, set())
        shared = fresh & ref
        new_only = sorted(fresh - ref)
        ref_only = sorted(ref - fresh)
        g_fresh += len(fresh); g_ref += len(ref); g_shared += len(shared)
        new_only_all += [(strain, lt) for lt in new_only]
        ref_only_all += [(strain, lt) for lt in ref_only]
        lines.append(f"| {strain} | {len(fresh)} | {len(ref)} | {len(shared)} "
                     f"| {len(new_only)} | {len(ref_only)} |")
    pct = (100.0 * g_shared / g_ref) if g_ref else 0.0
    lines.append(f"| **total** | **{g_fresh}** | **{g_ref}** | **{g_shared}** "
                 f"| **{g_fresh - g_shared}** | **{g_ref - g_shared}** |")
    lines.append(f"\n**Overlap: {g_shared}/{g_ref} of the 0620 set recovered "
                 f"({pct:.1f}%).**\n")

    # product lookups for the diff entries
    prod_lookup = {}
    for strain, base in STRAINS.items():
        for r in parse_tsv(os.path.join(REPO, base + ".tsv")):
            prod_lookup[(strain, r["locus_tag"])] = r["product"]

    lines.append("## Fresh-only (found now, absent from 0620) — receptors 0620 missed\n")
    if new_only_all:
        lines.append("| strain | locus_tag | product |")
        lines.append("|---|---|---|")
        for s, lt in new_only_all:
            lines.append(f"| {s} | {lt} | {prod_lookup.get((s, lt), '?')} |")
    else:
        lines.append("_none_")
    lines.append("")

    lines.append("## 0620-only (in 0620, dropped now) — review for false drops\n")
    if ref_only_all:
        lines.append("| strain | locus_tag | 0620 annotation | dropped because |")
        lines.append("|---|---|---|---|")
        for s, lt in ref_only_all:
            prod = prod_lookup.get((s, lt), ref0620.get((s, lt), "?"))
            reason = is_excluded(prod) or "no receptor cue matched"
            lines.append(f"| {s} | {lt} | {ref0620.get((s, lt), '?')} | {reason} |")
    else:
        lines.append("_none_")
    lines.append("")
    lines.append("---")
    lines.append("*Log: generated by `code/0623_metagenome_rbp/receptor_fasta.py`.*")

    rec_path = os.path.join(outdir, "reconciliation_vs_0620.md")
    with open(rec_path, "w") as out:
        out.write("\n".join(lines) + "\n")

    print(f"Wrote: {tbl_path}")
    print(f"Wrote: {rec_path}")
    print(f"Overlap with 0620: {g_shared}/{g_ref} ({pct:.1f}%)")


if __name__ == "__main__":
    sys.exit(main())
