#!/usr/bin/env python3
"""
Search our bacterial receptor proteins against NCBI Pseudomonas RefSeq to
nominate SURROGATE PHAGE HOSTS: named/characterized bacteria that (a) carry a
receptor highly similar to one of ours and (b) have studied phages we could
borrow. Logic: a phage whose RBP binds the same "lock" (receptor) in a surrogate
host is a candidate to bind ours too.

Why local Pseudomonas RefSeq (not remote BLAST nr): remote NCBI BLASTp can't
batch (qblast multi-query returns empty) -> ~6 min/protein x 106 ~ 8-12 h. The
closest hits are all Pseudomonas (CM25/CM27), so we search the 395 NCBI
*reference* Pseudomonas proteomes (~one per species) locally with mmseqs:
minutes, robust, named species ideal for host nomination.

Pipeline (resumable; each stage skipped if its output exists):
  1. Dedup 264 receptors -> representatives (mmseqs, near-triplicate genomes).
  2. Build/locate the Pseudomonas RefSeq target (NCBI `datasets`) + mmseqs search.
  3. Parse hits -> blast_hits.tsv + receptor_summary.tsv (best hit = novelty).
  4. Bridge: aggregate carrier species, ask NCBI which have known phages ->
     carrier_organisms.tsv + ranked surrogate_hosts.md.

CAVEATS (in the report): identity is a WEAK proxy for phage host range (phages
read variable surface loops); a carrier having the lock != its phage uses the
lock; carriers are dominated by P. putida-group relatives (CM27 etc.); the DB is
395 reference proteomes only (other Pseudomonas strains/genera not searched).

Stdlib + Biopython + mmseqs + NCBI datasets. Run:
    python code/0623_metagenome_rbp/receptor_ncbi_search.py
"""

import os
import re
import sys
import json
import glob
import time
import subprocess

from Bio import Entrez

# ---------------------------------------------------------------- config
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FASTA_DIR = os.path.join(REPO, "code/0623_metagenome_rbp/out_receptor_fasta")
RECEPTORS_TSV = os.path.join(FASTA_DIR, "receptors_all.tsv")
OUT = os.path.join(REPO, "code/0623_metagenome_rbp/out_receptor_ncbi")

# Large regenerable reference DB lives outside the repo (job tmp by default).
PSREF = os.environ.get("PSREF_DIR",
                       os.path.join(os.environ.get("CLAUDE_JOB_DIR", "/tmp"),
                                    "tmp", "psref"))

Entrez.email = "alexchenworking1.618@gmail.com"
if os.environ.get("NCBI_API_KEY"):
    Entrez.api_key = os.environ["NCBI_API_KEY"]

# "carrier shares a near-identical lock" tiers (named-species context: closest
# named Pseudomonas to our unnamed sp. is ~85-99%).
HIGH_ID, HIGH_COV = 90.0, 80.0
MAX_PHAGE_QUERIES = 250


def log(*a):
    print(*a, flush=True)


def sh(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)


# ---------------------------------------------------------------- step 1: dedup
def fasta_iter(path):
    lt, buf = None, []
    with open(path) as fh:
        for line in fh:
            if line.startswith(">"):
                if lt is not None:
                    yield lt, "".join(buf)
                lt = line[1:].split()[0]
                buf = []
            else:
                buf.append(line.strip())
    if lt is not None:
        yield lt, "".join(buf)


def load_receptor_meta():
    meta = {}
    with open(RECEPTORS_TSV) as fh:
        cols = fh.readline().rstrip("\n").split("\t")
        si, li, pi, ci = (cols.index(x) for x in
                          ("strain", "locus_tag", "product", "category"))
        for line in fh:
            f = line.rstrip("\n").split("\t")
            meta[f[li]] = (f[si], f[pi], f[ci])
    return meta


def run_dedup():
    os.makedirs(OUT, exist_ok=True)
    tmp = os.path.join(PSREF, "dedup")
    os.makedirs(tmp, exist_ok=True)
    allfa = os.path.join(tmp, "all.faa")
    with open(allfa, "w") as out:
        for fa in sorted(glob.glob(os.path.join(FASTA_DIR, "*_receptors.faa"))):
            out.write(open(fa).read())
    pref = os.path.join(tmp, "clust")
    if not os.path.exists(pref + "_rep_seq.fasta"):
        sh(["mmseqs", "easy-cluster", allfa, pref, os.path.join(tmp, "work"),
            "--min-seq-id", "0.99", "-c", "0.9", "--cov-mode", "0", "-v", "1"])

    members = {}
    for line in open(pref + "_cluster.tsv"):
        rep, mem = line.rstrip("\n").split("\t")
        members.setdefault(rep, []).append(mem)
    rep_seqs = dict(fasta_iter(pref + "_rep_seq.fasta"))
    meta = load_receptor_meta()
    reps = sorted(rep_seqs)

    with open(os.path.join(OUT, "receptor_reps.faa"), "w") as out:
        for r in reps:
            out.write(f">{r} category={meta.get(r, ('', '', ''))[2]}\n")
            s = rep_seqs[r]
            for i in range(0, len(s), 60):
                out.write(s[i:i + 60] + "\n")
    with open(os.path.join(OUT, "rep_to_members.tsv"), "w") as out:
        out.write("rep\tcategory\tn_members\tmember_strains\tmember_locus_tags\n")
        for r in reps:
            ms = members.get(r, [r])
            strains = sorted({meta.get(m, ("?",))[0] for m in ms})
            out.write(f"{r}\t{meta.get(r, ('', '', ''))[2]}\t{len(ms)}\t"
                      f"{','.join(strains)}\t{','.join(ms)}\n")
    log(f"dedup: {sum(len(v) for v in members.values())} receptors "
        f"-> {len(reps)} representatives")
    return reps, rep_seqs, meta, members


# ----------------------------------------------- step 2: Pseudomonas DB + search
# Searching all 2.06M reference proteins is dominated by mmseqs rebuilding the
# k-mer index each run (~independent of -s). Since we only want receptor-vs-
# receptor (lock-vs-lock) homology, we FUNCTION-FILTER the target first with the
# SAME receptor ruleset that built our own list -> ~33k proteins (62x smaller),
# after which mmseqs finishes in ~15s at full sensitivity.
TARGET_MINL, TARGET_MAXL = 80, 2000


def _load_classifier():
    import importlib.util
    p = os.path.join(REPO, "code/0623_metagenome_rbp/receptor_fasta.py")
    spec = importlib.util.spec_from_file_location("rf", p)
    rf = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rf)
    return rf


def ensure_target():
    """Download 395 Pseudomonas RefSeq reference proteomes; build a FUNCTION-
    FILTERED, labeled target_receptors.faa (>acc|protein_id, receptor-type only)
    + acc2org.json. Skips if present."""
    os.makedirs(PSREF, exist_ok=True)
    target = os.path.join(PSREF, "target_receptors.faa")
    a2o = os.path.join(PSREF, "acc2org.json")
    if os.path.exists(target) and os.path.exists(a2o):
        return target, a2o
    zf = os.path.join(PSREF, "psref.zip")
    data = os.path.join(PSREF, "ncbi_dataset", "data")
    if not os.path.isdir(data):
        if not os.path.exists(zf):
            log("downloading 395 Pseudomonas RefSeq reference proteomes...")
            sh(["datasets", "download", "genome", "taxon", "Pseudomonas",
                "--reference", "--include", "protein", "--filename", zf])
        sh(["unzip", "-q", "-o", zf, "-d", PSREF])
    org = {}
    for line in open(os.path.join(data, "assembly_data_report.jsonl")):
        d = json.loads(line)
        org[d.get("accession")] = d.get("organism", {}).get("organismName", "?")
    json.dump(org, open(a2o, "w"))

    rf = _load_classifier()
    tot = kept = 0
    with open(target, "w") as out:
        for acc in sorted(org):
            faa = os.path.join(data, acc, "protein.faa")
            if not os.path.exists(faa):
                continue
            pid, desc, buf = None, "", []

            def flush():
                nonlocal kept
                if pid is None:
                    return
                seq = "".join(buf)
                if not (TARGET_MINL <= len(seq) <= TARGET_MAXL):
                    return
                is_rec, _ = rf.classify(desc, set())   # product keyword only
                if is_rec:
                    out.write(f">{acc}|{pid}\n")
                    for i in range(0, len(seq), 60):
                        out.write(seq[i:i + 60] + "\n")
                    kept += 1

            for line in open(faa):
                if line.startswith(">"):
                    flush()
                    h = line[1:].rstrip("\n").split(None, 1)
                    pid, desc, buf = h[0], (h[1] if len(h) > 1 else ""), []
                    tot += 1
                else:
                    buf.append(line.strip())
            flush()
    log(f"target: {len(org)} assemblies, {tot} proteins -> {kept} receptor-type "
        f"({tot/max(kept,1):.0f}x reduction)")
    return target, a2o


def run_search():
    """mmseqs easy-search reps vs filtered target -> hits.m8. Skips if cached."""
    m8 = os.path.join(PSREF, "hits.m8")
    if os.path.exists(m8) and os.path.getsize(m8) > 0:
        log("search: hits.m8 cached, skip")
        return m8
    target, _ = ensure_target()
    reps = os.path.join(OUT, "receptor_reps.faa")
    sh(["mmseqs", "easy-search", reps, target, m8, os.path.join(PSREF, "mmtmp2"),
        "--format-output",
        "query,target,fident,pident,alnlen,qcov,tcov,evalue,bits",
        "-s", "5.7", "--max-seqs", "500", "-v", "1"])
    log(f"search: wrote {m8}")
    return m8


# ---------------------------------------------------------------- step 3: parse
def species_of(org):
    toks = org.split()
    return f"{toks[0]} {toks[1]}" if len(toks) >= 2 else org


def parse_m8(m8, a2o):
    org = json.load(open(a2o))
    rows = []  # rep, acc, organism, pid, cov, evalue, bits
    for line in open(m8):
        f = line.rstrip("\n").split("\t")
        rep, target = f[0], f[1]
        fident, qcov, evalue, bits = float(f[2]), float(f[5]), f[7], float(f[8])
        acc = target.split("|")[0]
        rows.append((rep, acc, org.get(acc, "?"), round(fident * 100, 1),
                     round(qcov * 100, 1), evalue, round(bits, 1)))
    return rows


def write_hit_tables(rows, reps, meta, members):
    cat_of = {r: meta.get(r, ("", "", ""))[2] for r in reps}
    # keep top 25 hits per rep by bits for the detail table
    by_rep = {}
    for row in rows:
        by_rep.setdefault(row[0], []).append(row)
    with open(os.path.join(OUT, "blast_hits.tsv"), "w") as out:
        out.write("rep\tcategory\torganism\taccession\tpct_identity\tquery_cov\t"
                  "evalue\tbitscore\n")
        for r in reps:
            hits = sorted(by_rep.get(r, []), key=lambda x: -x[6])[:25]
            for (rep, acc, o, pid, cov, ev, bits) in hits:
                out.write(f"{rep}\t{cat_of.get(rep,'')}\t{o}\t{acc}\t{pid}\t{cov}"
                          f"\t{ev}\t{bits}\n")

    best, high_sp = {}, {}
    for (rep, acc, o, pid, cov, ev, bits) in rows:
        if rep not in best or pid > best[rep][0]:
            best[rep] = (pid, cov, o)
        if pid >= HIGH_ID and cov >= HIGH_COV:
            high_sp.setdefault(rep, set()).add(species_of(o))
    with open(os.path.join(OUT, "receptor_summary.tsv"), "w") as out:
        out.write("rep\tcategory\tn_members\tmember_strains\tbest_pct_id\t"
                  "best_cov\tbest_hit_organism\tn_high_id_carrier_species\n")
        for r in reps:
            ms = members.get(r, [r])
            strains = sorted({meta.get(m, ("?",))[0] for m in ms})
            b = best.get(r, (0.0, 0.0, "none"))
            out.write(f"{r}\t{cat_of.get(r,'')}\t{len(ms)}\t{','.join(strains)}"
                      f"\t{b[0]}\t{b[1]}\t{b[2]}\t{len(high_sp.get(r, set()))}\n")
    return best


# ---------------------------------------------------------------- step 4: bridge
def aggregate_carriers(rows):
    carriers = {}
    for (rep, acc, o, pid, cov, ev, bits) in rows:
        sp = species_of(o)
        low = sp.lower()
        if any(k in low for k in ("uncultured", "metagenome", "unclassified",
                                  "sp.", "bacterium")):
            named = False
        else:
            named = True
        c = carriers.setdefault(sp, {"max_id": 0.0, "reps": set(),
                                     "n_high": 0, "named": named})
        c["max_id"] = max(c["max_id"], pid)
        c["reps"].add(rep)
        if pid >= HIGH_ID and cov >= HIGH_COV:
            c["n_high"] += 1
    return carriers


def has_known_phage(species):
    term = f'"{species}"[Host] AND (Caudoviricetes[Organism] OR phage[Title])'
    try:
        h = Entrez.esearch(db="nuccore", term=term, retmax=5)
        rec = Entrez.read(h)
        h.close()
        return int(rec["Count"]), rec.get("IdList", [])
    except Exception as e:
        log(f"    phage query fail for {species}: {e}")
        return -1, []


def write_carrier_and_surrogates(carriers):
    ranked = sorted(carriers.items(),
                    key=lambda kv: (kv[1]["n_high"], kv[1]["max_id"]),
                    reverse=True)
    # phage lookups: named species sharing a near-identical lock, capped
    cand = [(sp, d) for sp, d in ranked if d["max_id"] >= HIGH_ID and d["named"]]
    queried = cand[:MAX_PHAGE_QUERIES]
    if len(cand) > MAX_PHAGE_QUERIES:
        log(f"NOTE: {len(cand)} named carriers >= {HIGH_ID}% id; only top "
            f"{MAX_PHAGE_QUERIES} queried for phages.")
    phage = {}
    for i, (sp, d) in enumerate(queried):
        phage[sp] = has_known_phage(sp)
        time.sleep(0.4)
        if (i + 1) % 20 == 0:
            log(f"  phage lookups {i+1}/{len(queried)}")

    with open(os.path.join(OUT, "carrier_organisms.tsv"), "w") as out:
        out.write("organism\tnamed\tmax_pct_id\tn_receptors_shared\t"
                  "n_high_id_hits\tphage_count\texample_phage_accessions\n")
        for sp, d in ranked:
            cnt, accs = phage.get(sp, ("", []))
            out.write(f"{sp}\t{d['named']}\t{d['max_id']}\t{len(d['reps'])}\t"
                      f"{d['n_high']}\t{cnt}\t{','.join(accs)}\n")

    surro = [(sp, d, phage[sp]) for sp, d in queried
             if phage.get(sp, (0,))[0] and phage[sp][0] > 0]
    surro.sort(key=lambda x: (x[1]["n_high"], x[1]["max_id"]), reverse=True)

    lines = [
        "# Surrogate phage-host candidates\n",
        "Named *Pseudomonas* species that BOTH (a) carry a receptor "
        f"near-identical to one of ours (≥{HIGH_ID:.0f}% id, ≥{HIGH_COV:.0f}% "
        "cov) AND (b) have phage records at NCBI. A phage whose RBP binds the "
        "shared receptor in the surrogate host is a candidate to bind ours.\n",
        "**Caveats:** receptor sequence identity is a WEAK proxy for phage host "
        "range (phages read variable surface loops, not whole-protein identity); "
        "NCBI shows the host carries the lock, not that its phage uses that lock. "
        "Leads to test, not answers. DB = 395 NCBI reference proteomes only.\n",
    ]
    if surro:
        lines += ["| surrogate host | receptors shared (≥high-id) | max %id "
                  "| phage records | example phage accessions |",
                  "|---|---|---|---|---|"]
        for sp, d, (cnt, accs) in surro:
            lines.append(f"| {sp} | {d['n_high']} | {d['max_id']} | {cnt} | "
                         f"{','.join(accs)} |")
    else:
        lines.append("_No named carrier cleared both bars. Lower the identity "
                     "threshold (closest named species to our unnamed sp. may be "
                     "<90% id) or widen the DB._")
    lines += ["", "---",
              "*Log: generated by `code/0623_metagenome_rbp/receptor_ncbi_search.py`*"]
    with open(os.path.join(OUT, "surrogate_hosts.md"), "w") as out:
        out.write("\n".join(lines) + "\n")
    return ranked, surro


def write_readme(n_reps, n_rows, n_carriers, n_surro):
    open(os.path.join(OUT, "README.md"), "w").write(f"""# Receptor → NCBI Pseudomonas RefSeq → surrogate phage hosts

Our 264 receptors (deduped to {n_reps} reps, mmseqs 0.99/0.9) searched vs the
395 NCBI *reference* Pseudomonas proteomes. The 2.06M target proteins are first
FUNCTION-FILTERED to receptor-type only (same ruleset as our list -> ~33k, 62x
smaller; lock-vs-lock), then mmseqs easy-search (-s 5.7, ~15s). Carrier species
then checked at NCBI for known phages (Entrez [Host]).

Outputs:
- `receptor_reps.faa`, `rep_to_members.tsv` — dedup
- `blast_hits.tsv` — top hits/rep ({n_rows} total hit rows parsed)
- `receptor_summary.tsv` — per-rep best hit (novelty signal)
- `carrier_organisms.tsv` — {n_carriers} carrier species + phage flags
- `surrogate_hosts.md` — {n_surro} ranked surrogate-host candidates

Caveats: identity is a weak proxy for phage host range; carriers dominated by
P. putida-group relatives; DB limited to 395 reference proteomes. The big DB is
regenerable under $PSREF_DIR (default job tmp), not committed.

---
*Log: generated by `receptor_ncbi_search.py`.*
""")


def main():
    log("=== step 1: dedup ===")
    reps, rep_seqs, meta, members = run_dedup()
    log("=== step 2: Pseudomonas RefSeq target + mmseqs search ===")
    m8 = run_search()
    _, a2o = ensure_target()
    log("=== step 3: parse hits ===")
    rows = parse_m8(m8, a2o)
    write_hit_tables(rows, reps, meta, members)
    log("=== step 4: carrier aggregation + phage bridge ===")
    carriers = aggregate_carriers(rows)
    ranked, surro = write_carrier_and_surrogates(carriers)
    write_readme(len(reps), len(rows), len(ranked), len(surro))
    log(f"DONE. reps={len(reps)} hit_rows={len(rows)} carriers={len(ranked)} "
        f"surrogate_hosts={len(surro)}  -> {OUT}/surrogate_hosts.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
