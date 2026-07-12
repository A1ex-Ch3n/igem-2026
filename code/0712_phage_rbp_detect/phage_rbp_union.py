"""
Cross-check PhageRBPdetect (RBP Detect, ML) calls against the Pharokka
annotation for the 9-2-1 Phi8 phage, then emit the UNION RBP set.

Two independent RBP evidence sources for the 80 phage CDS:
  - RBP Detect : preds==1 (score>=0.5) from run_rbp_inference.py on phanotate.faa
  - Pharokka   : the curated tail-module CDS already extracted to
                 code/0708_rbp_analysis/seqs/rbps_all.faa (CDS 0014-0020),
                 with the raw pharokka function label shown per CDS.

Outputs (to --out-dir):
  rbp_detect_vs_pharokka.tsv   one row per CDS that is an RBP by EITHER source,
                               columns: gene, pharokka_annot, pharokka_category,
                               rbp_detect_pred, rbp_detect_score, in_pharokka_curated,
                               evidence (both/detect_only/pharokka_only), in_union
  9-2-1_phi8_RBPs_union.faa    FASTA of the union set, pulled from phanotate.faa,
                               headers annotated with CDS + evidence.

Join key across all files: the CDS locus tag prefix, e.g. FHABPWTM_CDS_0015.
"""

import argparse
import csv
import os
import re

from Bio import SeqIO

CDS_RE = re.compile(r"(FHABPWTM_CDS_\d+)")


def cds_tag(s):
    """Extract the FHABPWTM_CDS_#### locus tag from any id/header string."""
    m = CDS_RE.search(s)
    return m.group(1) if m else s


def read_predictions(pred_csv):
    """gene -> (pred int, score float) from the RBP Detect output CSV."""
    out = {}
    with open(pred_csv, newline="") as fh:
        for row in csv.DictReader(fh):
            out[cds_tag(row["protein_name"])] = (int(row["preds"]), float(row["score"]))
    return out


def read_pharokka_annot(tsv):
    """gene -> (annot, category) from pharokka_cds_final_merged_output.tsv."""
    out = {}
    with open(tsv, newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            out[cds_tag(row["gene"])] = (row.get("annot", ""), row.get("category", ""))
    return out


def read_pharokka_curated(faa):
    """Set of CDS tags in the curated 0708 RBP FASTA (Pharokka tail module)."""
    return {cds_tag(rec.id) for rec in SeqIO.parse(faa, "fasta")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pred-csv", required=True)
    ap.add_argument("--pharokka-tsv", required=True)
    ap.add_argument("--pharokka-curated-faa", required=True,
                    help="code/0708_rbp_analysis/seqs/rbps_all.faa (defines the Pharokka RBP set)")
    ap.add_argument("--phanotate-faa", required=True,
                    help="source protein FASTA to pull union sequences from")
    ap.add_argument("--out-dir", required=True)
    args = ap.parse_args()

    os.makedirs(args.out_dir, exist_ok=True)

    preds = read_predictions(args.pred_csv)
    annot = read_pharokka_annot(args.pharokka_tsv)
    curated = read_pharokka_curated(args.pharokka_curated_faa)

    detect_pos = {g for g, (p, _) in preds.items() if p == 1}
    union = sorted(detect_pos | curated, key=cds_tag)

    # comparison table
    tsv_path = os.path.join(args.out_dir, "rbp_detect_vs_pharokka.tsv")
    with open(tsv_path, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["gene", "pharokka_annot", "pharokka_category",
                    "rbp_detect_pred", "rbp_detect_score",
                    "in_pharokka_curated", "evidence", "in_union"])
        for g in union:
            pred, score = preds.get(g, (0, float("nan")))
            in_cur = g in curated
            in_det = g in detect_pos
            evidence = ("both" if (in_det and in_cur)
                        else "detect_only" if in_det else "pharokka_only")
            a, c = annot.get(g, ("", ""))
            w.writerow([g, a, c, pred,
                        f"{score:.6f}" if score == score else "NA",
                        "yes" if in_cur else "no", evidence, "yes"])

    # union FASTA
    seqs = {cds_tag(rec.id): rec for rec in SeqIO.parse(args.phanotate_faa, "fasta")}
    faa_path = os.path.join(args.out_dir, "9-2-1_phi8_RBPs_union.faa")
    n_written = 0
    with open(faa_path, "w") as fh:
        for g in union:
            rec = seqs.get(g)
            if rec is None:
                print(f"  WARNING: {g} not found in {args.phanotate_faa}")
                continue
            pred, score = preds.get(g, (0, float("nan")))
            in_cur = g in curated
            in_det = g in detect_pos
            evidence = ("both" if (in_det and in_cur)
                        else "detect_only" if in_det else "pharokka_only")
            a = annot.get(g, ("", ""))[0]
            rec.description = (f"pharokka=\"{a}\" rbpdetect_pred={pred} "
                               f"score={score:.3f} evidence={evidence}")
            SeqIO.write(rec, fh, "fasta")
            n_written += 1

    # console summary
    print(f"RBP Detect positives : {len(detect_pos)}  {sorted(detect_pos, key=cds_tag)}")
    print(f"Pharokka curated set : {len(curated)}  {sorted(curated, key=cds_tag)}")
    print(f"Union                : {len(union)}")
    print(f"  both        : {sorted((detect_pos & curated), key=cds_tag)}")
    print(f"  detect_only : {sorted((detect_pos - curated), key=cds_tag)}")
    print(f"  pharokka_only: {sorted((curated - detect_pos), key=cds_tag)}")
    print(f"Wrote {tsv_path}")
    print(f"Wrote {faa_path} ({n_written} sequences)")


if __name__ == "__main__":
    main()
