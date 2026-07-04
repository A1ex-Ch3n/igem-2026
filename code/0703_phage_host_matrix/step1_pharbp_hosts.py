"""
Step 1 of the phage-host receptor matrix: retrieve + clean PharBP's Pseudomonas host
list and resolve each to a downloadable NCBI assembly accession.

PharBP only gives host NAME strings (and messy ones: multi-host, species-only, junk,
mixed strain levels). We pull the hosts of Pseudomonas-named phages, clean the strings,
and resolve each to an NCBI RefSeq assembly via the `datasets` CLI (strain-preferred:
use the named strain's assembly when PharBP gives one, else the species reference).

Does NOT download genomes (that's Step 2) — only resolves accessions.

Outputs (code/output/0703_phage_host_matrix/):
  pharbp_pseudomonas_hosts.tsv   one row per cleaned host + resolved accession
  pharbp_pseudomonas_hosts.md    summary (resolved/unresolved, putida-group vs far)
  unresolved_hosts.txt           hosts with no findable genome

Run: python code/0703_phage_host_matrix/step1_pharbp_hosts.py
"""

import csv
import io
import json
import os
import shutil
import subprocess
import time
from collections import Counter, defaultdict

import requests

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "..", "output", "0703_phage_host_matrix")
EXPORT = "https://pharbp.ugent.be/export/results/"

DATASETS = shutil.which("datasets") or "/opt/anaconda3/bin/datasets"

# named relatives closest to our hosts (P. putida group), for flagging in the summary
PUTIDA_GROUP = ("putida", "capeferrum", "protegens", "fluorescens", "monteilii", "mosselii",
                "plecoglossicida", "entomophila", "asplenii", "taiwanensis", "alloputida",
                "hunanensis", "fortuita", "chlororaphis")

# lowercased host strings to drop entirely (not a resolvable Pseudomonas genome)
JUNK = {"pseudomonas", "pseudomonas sp.", "carbapenem-resistant pseudomonas", ""}


def clean_host_string(raw):
    """Split a messy Host Name(s) field into a list of clean organism names."""
    out = []
    for part in raw.replace(";", ",").split(","):
        p = " ".join(part.split()).strip()
        if p.lower().endswith(" and"):
            p = p[:-4].strip()
        if p.lower() in JUNK:
            continue
        if not (p.lower().startswith("pseudomonas") or p.lower().startswith("stutzerimonas")):
            continue
        out.append(p)
    return out


def parse_name(name):
    """(genus, species, strain). species='sp.' handled; strain = remainder after species."""
    toks = name.split()
    genus = toks[0] if toks else ""
    species = toks[1] if len(toks) > 1 else ""
    strain = " ".join(toks[2:]) if len(toks) > 2 else ""
    return genus, species, strain


def datasets_summary(taxon, extra):
    """Run `datasets summary genome taxon <taxon> <extra...>`; return reports list."""
    cmd = [DATASETS, "summary", "genome", "taxon", taxon] + extra
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if r.returncode != 0 or not r.stdout.strip():
            return []
        return json.loads(r.stdout).get("reports", []) or []
    except (subprocess.SubprocessError, ValueError):
        return []


def pick_best(reports, strain):
    """Choose the best assembly report; strain tokens boost the score."""
    stoks = [t.lower() for t in strain.split()] if strain else []

    def score(r):
        org = r.get("organism", {}).get("organism_name", "").lower()
        info = r.get("assembly_info", {})
        lvl = info.get("assembly_level", "")
        cat = info.get("refseq_category", "")
        has_strain = bool(stoks) and all(t in org for t in stoks)
        return (has_strain, lvl == "Complete Genome",
                cat in ("reference genome", "representative genome"))

    return max(reports, key=score) if reports else None


def resolve(genus, species, strain, cache):
    """Return (accession, resolution_level, assembly_level, organism_name)."""
    full = " ".join(x for x in (genus, species, strain) if x)
    if full in cache:
        return cache[full]

    result = ("", "unresolved", "", "")
    # 1) strain-preferred (or sp.-strings): query the full name, no --reference
    if strain or species == "sp.":
        reps = datasets_summary(full, ["--assembly-source", "RefSeq", "--limit", "20"])
        time.sleep(0.34)
        best = pick_best(reps, strain)
        if best:
            info = best.get("assembly_info", {})
            result = (best["accession"], "strain-exact", info.get("assembly_level", ""),
                      best.get("organism", {}).get("organism_name", ""))
    # 2) species reference fallback
    if result[1] == "unresolved" and species and species != "sp.":
        sp = f"{genus} {species}"
        reps = datasets_summary(sp, ["--reference", "--limit", "1"])
        time.sleep(0.34)
        if not reps:
            reps = datasets_summary(sp, ["--assembly-source", "RefSeq", "--limit", "5"])
            time.sleep(0.34)
        best = pick_best(reps, "")
        if best:
            info = best.get("assembly_info", {})
            result = (best["accession"], "species-reference", info.get("assembly_level", ""),
                      best.get("organism", {}).get("organism_name", ""))

    cache[full] = result
    return result


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    print("fetching PharBP Pseudomonas-phage records...")
    r = requests.get(EXPORT, params={"phage": "Pseudomonas", "download": "csv"},
                     timeout=180, headers={"User-Agent": "iGEM6317-pharbp-client/1.0"})
    r.raise_for_status()
    rows = list(csv.reader(io.StringIO(r.text)))[1:]

    rbp = Counter()
    phages = defaultdict(set)
    raws = defaultdict(set)
    no_host = 0
    for row in rows:
        if len(row) < 10:
            continue
        phage, host_raw = row[8].strip(), row[9].strip()
        cleaned = clean_host_string(host_raw)
        if not cleaned:
            if not host_raw:
                no_host += 1
            continue
        for h in cleaned:
            rbp[h] += 1
            if phage:
                phages[h].add(phage)
            raws[h].add(host_raw)
    print(f"{len(rows)} records | {len(rbp)} distinct cleaned hosts | {no_host} records had no host")

    cache = {}
    out_rows = []
    for host in sorted(rbp, key=lambda h: -rbp[h]):
        genus, species, strain = parse_name(host)
        acc, level, alevel, orgname = resolve(genus, species, strain, cache)
        note = "reclassified_from_Pseudomonas" if genus == "Stutzerimonas" else ""
        ex_phages = "; ".join(sorted(phages[host])[:5])
        out_rows.append({
            "cleaned_name": host, "genus": genus, "species": species, "strain": strain,
            "ncbi_accession": acc, "resolution_level": level, "assembly_level": alevel,
            "organism_name": orgname, "n_pharbp_rbp": rbp[host], "n_phages": len(phages[host]),
            "example_phages": ex_phages, "raw_host_strings": " | ".join(sorted(raws[host])),
            "note": note,
        })
        print(f"  {host:45} -> {acc or '(unresolved)':18} [{level}]")

    cols = ["cleaned_name", "genus", "species", "strain", "ncbi_accession", "resolution_level",
            "assembly_level", "organism_name", "n_pharbp_rbp", "n_phages", "example_phages",
            "raw_host_strings", "note"]
    tsv = os.path.join(OUT_DIR, "pharbp_pseudomonas_hosts.tsv")
    with open(tsv, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t")
        w.writeheader()
        w.writerows(out_rows)

    unresolved = [r for r in out_rows if r["resolution_level"] == "unresolved"]
    with open(os.path.join(OUT_DIR, "unresolved_hosts.txt"), "w") as fh:
        for r in unresolved:
            fh.write(f"{r['cleaned_name']}\t(rbp={r['n_pharbp_rbp']}, phages={r['n_phages']})\n")

    # ---- markdown summary ----
    resolved = [r for r in out_rows if r["resolution_level"] != "unresolved"]
    putida = [r for r in resolved if any(k in r["cleaned_name"].lower() for k in PUTIDA_GROUP)]
    by_level = Counter(r["resolution_level"] for r in out_rows)
    with open(os.path.join(OUT_DIR, "pharbp_pseudomonas_hosts.md"), "w") as fh:
        fh.write("# PharBP Pseudomonas hosts -> NCBI genomes (Step 1)\n\n")
        fh.write(f"Source: `{EXPORT}?phage=Pseudomonas` ({len(rows)} RBP records; "
                 f"{no_host} had no host).\n\n")
        fh.write(f"- distinct cleaned hosts: **{len(out_rows)}**\n")
        fh.write(f"- resolved to a genome: **{len(resolved)}** "
                 f"({by_level.get('strain-exact',0)} strain-exact, "
                 f"{by_level.get('species-reference',0)} species-reference)\n")
        fh.write(f"- unresolved: **{len(unresolved)}** (see `unresolved_hosts.txt`)\n")
        fh.write(f"- P. putida-group / near-relative hosts (closest to our isolates): "
                 f"**{len(putida)}**\n\n")
        fh.write("## Near-relative hosts (P. putida group) — highest-value for us\n\n")
        fh.write("| host | accession | level | RBPs | phages |\n|---|---|---|---|---|\n")
        for r in sorted(putida, key=lambda x: -x["n_pharbp_rbp"]):
            fh.write(f"| {r['cleaned_name']} | {r['ncbi_accession']} | {r['resolution_level']} "
                     f"| {r['n_pharbp_rbp']} | {r['n_phages']} |\n")
        fh.write("\n## All hosts by PharBP RBP-record count\n\n")
        fh.write("| host | accession | level | RBPs | phages |\n|---|---|---|---|---|\n")
        for r in out_rows:
            fh.write(f"| {r['cleaned_name']} | {r['ncbi_accession'] or '—'} | "
                     f"{r['resolution_level']} | {r['n_pharbp_rbp']} | {r['n_phages']} |\n")

    print(f"\nwrote {tsv}")
    print(f"resolved {len(resolved)}/{len(out_rows)} | unresolved {len(unresolved)} | "
          f"putida-group {len(putida)}")


if __name__ == "__main__":
    main()
