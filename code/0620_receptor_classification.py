#!/usr/bin/env python3
"""
0620 — Classify Pseudomonas surface/OMP proteins into Moriniere et al. 2026
(EcoliPhage / GenoPHI) receptor classes by receptor-vs-receptor homology.

Pipeline:
  1. Parse the 3 strains' potential_receptors fastas (542 seqs).
  2. Curate a "pure receptors" list with an auditable keyword ruleset
     (keep OMP-receptor folds; flag out-of-scheme surface; exclude non-receptors).
  3. Fetch the 13 canonical E. coli K-12 receptor proteins from UniProt
     (the classes named in the paper); these are the BLAST/MMseqs references.
  4. MMseqs2 easy-search: curated receptors (query) vs 13 refs (target).
  5. Assign class by best hit passing a threshold gate; else Unclassified.
  6. Write classification.tsv, class_summary.tsv, excluded_log.tsv, curated fasta, refs fasta.

Run from anywhere; paths are resolved relative to the repo.
"""
import io
import re
import sys
import time
import subprocess
import urllib.parse
from pathlib import Path

import pandas as pd
import requests

try:                                  # script
    REPO = Path(__file__).resolve().parents[1]
except NameError:                     # notebook (no __file__): walk up to repo root
    _p = Path.cwd()
    REPO = next((q for q in [_p, *_p.parents]
                 if (q / "data" / "processed_genome").exists()), _p)
INDIR = REPO / "data" / "processed_genome"
OUTDIR = REPO / "code" / "output" / "0620_receptor_classification"
OUTDIR.mkdir(parents=True, exist_ok=True)

STRAINS = ["9-2-1", "9-6-2", "10-10-2"]

# ----------------------------------------------------------------------------
# 1. Parse fastas
# ----------------------------------------------------------------------------
def parse_fasta(path):
    recs = []
    name, seq = None, []
    with open(path) as fh:
        for line in fh:
            line = line.rstrip("\n")
            if line.startswith(">"):
                if name is not None:
                    recs.append((name, "".join(seq)))
                name, seq = line[1:], []
            else:
                seq.append(line)
    if name is not None:
        recs.append((name, "".join(seq))
)
    return recs

rows = []
for strain in STRAINS:
    p = INDIR / f"{strain}_potential_receptors.fasta"
    for header, seq in parse_fasta(p):
        locus, _, annot = header.partition(" ")
        rows.append(dict(strain=strain, locus_tag=locus, annotation=annot, sequence=seq))
df = pd.DataFrame(rows)
print(f"[1] parsed {len(df)} sequences across {df.strain.nunique()} strains")
print(df.groupby("strain").size().to_dict())

# ----------------------------------------------------------------------------
# 2. Curation ruleset (order matters; first match wins)
# ----------------------------------------------------------------------------
# EXCLUDE patterns (non-receptor) -> (regex, reason)
EXCLUDE = [
    (r"assembly factor Bam|\bBam[ABCDE]\b|Lol[AB]\b|lipoprotein insertase|lipoprotein chaperone Lol|outer membrane lipid asymmetry|\bMlaD\b",
     "OM biogenesis/assembly (Bam/Lol/Mla)"),
    (r"Energy transducer TonB|Protein TonB|tonB-system energizer|TonB system transport|\bExbB\b|\bExbD\b|TonB C-terminal|Secretin/TonB short",
     "TonB/Exb energizer or fragment"),
    (r"Membrane fusion protein|RND efflux pump membrane fusion|Efflux pump membrane transporter|Multidrug efflux transport system-membrane subunit|Efflux system membrane protein",
     "efflux periplasmic adaptor / inner-membrane RND pump"),
    (r"Inner membrane|\bSecF\b|insertase YidC|\bMurJ\b|murein biosynthesis|transglycosylase|type II secretion|\bGspF\b|type VI secretion|\bTssM\b|ABC transporter|permease|[Bb]inding-protein-dependent|metabolite transport|\bMFS\b|Sodium/calcium|succinate dehydrogenase|Arginine/ornithine transport|Spermidine/putrescine|zinc uptake|\bZnuB\b|Arsenical pump|conjugative element|Paraquat-inducible|\bPqiC\b|membrane transporter protein|Pr6Pr|UPF0|integral membrane|Integrating conjugative",
     "inner-membrane / transporter / not surface receptor"),
    (r"cyclic di-GMP|\bLapD\b|Aerotaxis|response regulator|\bPilG\b|tyrosine kinase|redox modulator|\bAlx\b|Membrane dipeptidase|lipoprotein Blc|\bYfiB\b|regulator of flagellin|Flagellar motor|\bMotB\b|biotin-lipoyl|\bEppA\b|TIGR01666|Membrane lipoprotein|Major outer membrane lipoprotein|OmpH family|biogenesis protein",
     "non-receptor (signaling / lipoprotein / misc)"),
    (r"^Membrane protein$|^Small integral|^Membrane protein YkvI|^Membrane protein PputW619|Membrane-bound redox",
     "generic/uncharacterized membrane protein"),
]
# KEEP patterns (receptor folds) -> (regex, category)
KEEP = [
    (r"\bTolC\b|efflux protein BepC|outer membrane.*efflux|efflux.*outer membrane|RND outer membrane|\bOprN\b|\bOprM\b|\bOprJ\b|\bMepC\b|\bSrpC\b|\bTtgF\b|Toluene efflux pump outer membrane",
     "TolC-family"),
    (r"TonB-dependent|TonB-denpendent|siderophore receptor|Ferrioxamine|Ferrichrome|Ferric[- ]|pseudobactin|enterobactin|heme receptor|copper receptor|\bBfrD\b|\bFoxA\b|receptor,? plug|Outer membrane heme",
     "TBDR (TonB-dependent receptor)"),
    (r"Nucleoside-specific outer membrane|Nucleoside-binding outer membrane|\bTsx\b",
     "Tsx-family (nucleoside channel)"),
    (r"OmpA-like|peptidoglycan-associated|Outer membrane porin F\b|\bOprF\b",
     "OmpA-family"),
    (r"\busher\b|autotransporter|^Flagellin$|\bsecretin\b|Polysaccharide export|\bBcsC\b|cellulose synthase complex outer membrane",
     "surface-other (out-of-scheme)"),
    (r"porin|\bOprD\b|\bOprE\b|\bOprB\b|carbohydrate porin|Porin D|Phenylacetic acid-specific|Histidine-specific outer membrane|Porin-like|Porin domain|Glucose-selective",
     "porin"),
    (r"Outer membrane protein beta-barrel|Outer membrane protein, outer",
     "OMP-other (generic beta-barrel)"),
]

def curate(annot):
    for rgx, reason in EXCLUDE:
        if re.search(rgx, annot, re.IGNORECASE):
            return ("EXCLUDE", reason)
    for rgx, cat in KEEP:
        if re.search(rgx, annot, re.IGNORECASE):
            return ("KEEP", cat)
    return ("EXCLUDE", "no receptor-fold keyword matched")

cur = df.annotation.apply(curate)
df["decision"] = cur.apply(lambda x: x[0])
df["curated_category"] = cur.apply(lambda x: x[1])

curated = df[df.decision == "KEEP"].copy()
excluded = df[df.decision == "EXCLUDE"].copy()
print(f"[2] curated (kept) {len(curated)}  |  excluded {len(excluded)}  |  total {len(df)}")
print("    kept categories:", curated.curated_category.value_counts().to_dict())

# ----------------------------------------------------------------------------
# 3. Fetch the 13 E. coli K-12 receptor references from UniProt (by gene+organism)
# ----------------------------------------------------------------------------
# class label -> E. coli gene name
REF_GENES = {
    "tsx": "tsx", "fadL": "fadL", "ompA": "ompA", "ompF": "ompF",
    "ompW": "ompW", "ompC": "ompC", "fhuA": "fhuA", "btuB": "btuB",
    "lptD": "lptD", "nupG": "nupG", "lamB": "lamB", "tolC": "tolC", "yncD": "yncD",
}
ECOLI_K12_TAXID = 83333

def fetch_ref(gene):
    q = f"gene_exact:{gene} AND organism_id:{ECOLI_K12_TAXID} AND reviewed:true"
    url = ("https://rest.uniprot.org/uniprotkb/search?query="
           + urllib.parse.quote(q) + "&format=fasta&size=1")
    for attempt in range(4):
        r = requests.get(url, timeout=30)
        if r.status_code == 200 and r.text.startswith(">"):
            return r.text
        time.sleep(2)
    raise RuntimeError(f"UniProt fetch failed for {gene}: {r.status_code}")

refs_fasta = OUTDIR / "ecoli_receptor_refs.fasta"
ref_meta = []
ref_blocks = []
for cls, gene in REF_GENES.items():
    fa = fetch_ref(gene)
    hdr = fa.splitlines()[0]
    acc = hdr.split("|")[1] if "|" in hdr else "?"
    seq = "".join(fa.splitlines()[1:])
    ref_blocks.append(f">{cls} {acc} gene={gene}\n{seq}\n")
    ref_meta.append(dict(receptor_class=cls, gene=gene, accession=acc, length=len(seq)))
    print(f"    ref {cls:6s} {acc:10s} len={len(seq)}")
refs_fasta.write_text("".join(ref_blocks))
pd.DataFrame(ref_meta).to_csv(OUTDIR / "ecoli_receptor_refs_meta.tsv", sep="\t", index=False)
print(f"[3] wrote {refs_fasta.name} ({len(ref_meta)} refs)")

# ----------------------------------------------------------------------------
# 4. Write fastas and run mmseqs easy-search on ALL 542
# ----------------------------------------------------------------------------
# Curation is annotation-based; to honour "homology > annotation" we search ALL
# 542 (not just the curated set), so a real receptor hiding under a wrong
# annotation can still be rescued by homology (see step 6).
df["qid"] = df.strain + "::" + df.locus_tag
curated_fasta = OUTDIR / "pseudomonas_receptors_curated.fasta"   # the annotation-curated list (deliverable)
with open(curated_fasta, "w") as fh:
    for r in curated.itertuples():
        fh.write(f">{r.strain}::{r.locus_tag} {r.annotation}\n{r.sequence}\n")
search_fasta = OUTDIR / "_all_proteins.fasta"
with open(search_fasta, "w") as fh:
    for r in df.itertuples():
        fh.write(f">{r.qid}\n{r.sequence}\n")
print(f"[4] curated list = {len(curated)}; searching all {len(df)} proteins vs {len(ref_meta)} refs")

tmp = OUTDIR / "_mmseqs_tmp"
m8 = OUTDIR / "_search.m8"
fmt = "query,target,pident,qcov,tcov,alnlen,mismatch,gapopen,evalue,bits"
cmd = ["mmseqs", "easy-search", str(search_fasta), str(refs_fasta), str(m8), str(tmp),
       "-s", "7.5", "-e", "1000", "--max-seqs", "50",
       "--format-output", fmt, "--threads", "4"]
subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

cols = fmt.split(",")
hits = pd.read_csv(m8, sep="\t", names=cols)
# normalise pident (mmseqs gives fraction 0-1) and coverage (0-1)
if hits.pident.max() <= 1.0:
    hits["pident"] = hits["pident"] * 100.0
print(f"[4] {len(hits)} raw hits; pident range {hits.pident.min():.1f}-{hits.pident.max():.1f}")

# ----------------------------------------------------------------------------
# 5. Best hit per query + threshold gate
# ----------------------------------------------------------------------------
# Cross-genus OMP homology: e-value + coverage are reliable; raw %identity is not
# (genuine homologs sit at ~20-35% id). So the gate is e-value + coverage; %identity
# only sets the confidence tier. Coverage>=0.5 also removes spurious short best-hits.
COV_MIN, EVAL_MAX = 0.50, 1e-5
FOLD_FAMILY = {
    "fhuA": "TBDR (TonB-dependent receptor)", "btuB": "TBDR (TonB-dependent receptor)",
    "yncD": "TBDR (TonB-dependent receptor)",
    "ompC": "porin", "ompF": "porin", "ompW": "porin", "lamB": "porin",
    "tsx": "porin/channel", "fadL": "porin/channel",
    "ompA": "OmpA-family", "tolC": "TolC-family", "lptD": "LptD-family", "nupG": "NupG/MFS",
}

hits = hits.sort_values(["query", "bits"], ascending=[True, False])
raw_best = hits.groupby("query", as_index=False).first()[
    ["query", "target", "pident", "qcov", "evalue", "bits"]]
gated = hits[(hits.qcov >= COV_MIN) & (hits.evalue <= EVAL_MAX)]
gated_best = gated.groupby("query", as_index=False).first()[
    ["query", "target", "pident", "qcov", "evalue", "bits"]]

res = df.merge(gated_best, left_on="qid", right_on="query", how="left",
               suffixes=("", "_g"))
res = res.merge(raw_best, left_on="qid", right_on="query", how="left",
                suffixes=("", "_raw"))

def assign(row):
    if pd.notna(row.target):                       # passed the gate
        g = row.target
        fam = FOLD_FAMILY.get(g, "")
        conf = "high" if (row.pident >= 40 and row.qcov >= 0.70) else "family-level"
        note = f"best homolog E. coli {g} (id={row.pident:.1f}%, cov={row.qcov:.2f}, e={row.evalue:.1g})"
        if conf == "family-level":
            note += "; member-level ambiguous across genus — trust at fold-family level"
        return pd.Series([g, fam, conf, note,
                          g, row.pident, row.qcov, row.evalue, row.bits])
    # did not pass the gate -> Unclassified, but report the closest ref for transparency
    if pd.notna(row.target_raw):
        note = (f"no homolog passes gate (cov>={COV_MIN}, e<={EVAL_MAX:g}); "
                f"closest E. coli ref {row.target_raw} only id={row.pident_raw:.1f}%, "
                f"cov={row.qcov_raw:.2f}, e={row.evalue_raw:.1g}")
    else:
        note = "no homology hit to any E. coli reference"
    if row.curated_category == "porin" or "OprD" in row.annotation:
        note += " — Pseudomonas OprD-family/specific porin, no E. coli 13-class ortholog"
    return pd.Series(["Unclassified", "", "none", note,
                      row.target_raw, row.pident_raw, row.qcov_raw, row.evalue_raw, row.bits_raw])

res[["assigned_class", "fold_family", "confidence", "basis_note",
     "best_ref_gene", "pct_identity", "query_cov", "evalue", "bitscore"]] = res.apply(assign, axis=1)

# ----------------------------------------------------------------------------
# 6. Homology overrides annotation; write outputs
# ----------------------------------------------------------------------------
# A protein belongs in the receptor table if it was curated-kept OR it passes the
# homology gate (rescued from a wrong annotation-based exclusion).
res["passed"] = res.assigned_class != "Unclassified"
res["curation"] = "kept"
res.loc[(res.decision == "EXCLUDE") & res.passed, "curation"] = "rescued-by-homology"
recep = res[(res.decision == "KEEP") | res.passed].copy()
resc = recep.curation == "rescued-by-homology"
recep.loc[resc, "basis_note"] = (
    "RESCUED (annotation-excluded as '" + recep.loc[resc, "curated_category"]
    + "', homology overrides): " + recep.loc[resc, "basis_note"])
print(f"[6] receptor table {len(recep)} (curated-kept {len(curated)} + "
      f"rescued {int(resc.sum())}); annotation excludes that passed homology: {int(resc.sum())}")

out_cols = ["strain", "locus_tag", "annotation", "curated_category", "curation",
            "assigned_class", "fold_family", "best_ref_gene", "pct_identity",
            "query_cov", "evalue", "bitscore", "confidence", "basis_note"]
recep_out = recep[out_cols].sort_values(["strain", "assigned_class", "locus_tag"])
recep_out.to_csv(OUTDIR / "receptor_classification.tsv", sep="\t", index=False,
                 float_format="%.4g")

excluded_final = res[(res.decision == "EXCLUDE") & ~res.passed]
excluded_final[["strain", "locus_tag", "annotation", "curated_category"]].rename(
    columns={"curated_category": "exclusion_reason"}).to_csv(
    OUTDIR / "excluded_log.tsv", sep="\t", index=False)

summary = (recep_out.groupby(["assigned_class", "strain"]).size()
           .unstack(fill_value=0))
summary["total"] = summary.sum(axis=1)
summary = summary.sort_values("total", ascending=False)
summary.to_csv(OUTDIR / "class_summary.tsv", sep="\t")

# keep the raw search for audit; drop scratch
import shutil
m8.replace(OUTDIR / "blast_raw_hits.m8")
shutil.rmtree(tmp, ignore_errors=True)
search_fasta.unlink(missing_ok=True)

print("\n[6] ==== class_summary ====")
print(summary)
print(f"\nreceptor_table + excluded = {len(recep)}+{len(excluded_final)} = "
      f"{len(recep)+len(excluded_final)} (expect 542)")
print("confidence:", recep_out.confidence.value_counts().to_dict())
print("classified:", int((recep_out.assigned_class != 'Unclassified').sum()),
      "| Unclassified-but-kept:", int((recep_out.assigned_class == 'Unclassified').sum()))
print("wrote outputs to", OUTDIR)
