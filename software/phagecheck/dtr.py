#!/usr/bin/env python3
"""DTR vs circularity for a phage assembly, from read coverage alone.

Distinguishes two cases that an assembler reports identically:

* **linear genome with a Direct Terminal Repeat** (T7-style). The assembler
  collapses the DTR once, so reads from *both* genome ends pile onto it and the
  repeat shows a sharp ~2x k-mer coverage spike.
* **circular or circularly permuted genome**. Coverage is uniform: no spike, and
  no drop-off at the contig's arbitrary ends.

No aligner and no database: the contig's canonical k-mer set is counted against a
read subsample and profiled along the contig. Everything stays on the machine.

This is the check that corrected our own call on phage 9-2-1 Φ8 — reported as
circular by the assembler, actually linear with a 77 bp DTR.
"""
from __future__ import annotations

import argparse
import gzip
import statistics as st
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator, Sequence

COMPLEMENT = str.maketrans("ACGT", "TGCA")


def canonical(kmer: str) -> str:
    """The lexicographically smaller of a k-mer and its reverse complement."""
    rc = kmer.translate(COMPLEMENT)[::-1]
    return kmer if kmer <= rc else rc


def read_contig(path: str | Path) -> str:
    """First (or only) sequence of a FASTA file, uppercased, as one string."""
    seq = []
    for line in Path(path).read_text().splitlines():
        if line.startswith(">"):
            if seq:
                break
            continue
        seq.append(line.strip())
    return "".join(seq).upper()


def stream_reads(path: str | Path, max_reads: int) -> Iterator[str]:
    """Sequence lines of a FASTQ file (plain or gzipped), up to max_reads."""
    path = Path(path)
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt") as fh:
        for n, line in enumerate(fh):
            if n % 4 == 1:
                yield line.strip().upper()
                if (n // 4) + 1 >= max_reads:
                    return


@dataclass
class DTRResult:
    length: int
    median_coverage: float
    max_coverage: int
    first20_mean: float
    last20_mean: float
    runs: list[tuple[int, int, int]] = field(default_factory=list)  # start, end, length (1-based)

    @property
    def verdict(self) -> str:
        return "LINEAR + DTR" if self.runs else "CIRCULAR / no short linear DTR"

    def __str__(self) -> str:
        ratio = self.max_coverage / self.median_coverage if self.median_coverage else float("nan")
        head = (f"contig {self.length} bp | median cov {self.median_coverage:.0f} | "
                f"max {self.max_coverage} (max/median {ratio:.2f}x)\n"
                f"first20 mean: {self.first20_mean:.0f}  last20 mean: {self.last20_mean:.0f}")
        if self.runs:
            return f"{head}\nCandidate DTR: {self.runs} -> {self.verdict}"
        return f"{head}\n{self.verdict}"


def coverage_profile(contig: str, reads: Sequence[str | Path], *,
                     k: int = 31, subsample: int = 150_000) -> list[int]:
    """Per-position canonical k-mer coverage of the contig, from the read subsample."""
    counts: dict[str, int] = {}
    for i in range(len(contig) - k + 1):
        kmer = contig[i:i + k]
        if "N" not in kmer:
            counts[canonical(kmer)] = 0
    for path in reads:
        for seq in stream_reads(path, subsample):
            for i in range(len(seq) - k + 1):
                kmer = seq[i:i + k]
                if "N" in kmer:
                    continue
                ck = canonical(kmer)
                if ck in counts:
                    counts[ck] += 1
    return [counts[canonical(contig[i:i + k])] if "N" not in contig[i:i + k] else 0
            for i in range(len(contig) - k + 1)]


def find_dtr(profile: Sequence[int], *, threshold: float = 1.6,
             min_length: int = 15) -> tuple[DTRResult, float]:
    """Runs of positions covered at >= threshold x the median. Returns the median too."""
    median = st.median(profile)
    cutoff = threshold * median
    runs: list[tuple[int, int, int]] = []
    i = 0
    while i < len(profile):
        if profile[i] >= cutoff:
            j = i
            while j < len(profile) and profile[j] >= cutoff:
                j += 1
            if j - i >= min_length:
                runs.append((i + 1, j, j - i))
            i = j
        else:
            i += 1
    result = DTRResult(
        length=len(profile),
        median_coverage=median,
        max_coverage=max(profile) if profile else 0,
        first20_mean=sum(profile[:20]) / 20 if len(profile) >= 20 else float("nan"),
        last20_mean=sum(profile[-20:]) / 20 if len(profile) >= 20 else float("nan"),
        runs=runs,
    )
    return result, median


def check(contig_fasta: str | Path, reads: Sequence[str | Path], *,
          k: int = 31, subsample: int = 150_000,
          threshold: float = 1.6, min_length: int = 15) -> DTRResult:
    contig = read_contig(contig_fasta)
    profile = coverage_profile(contig, reads, k=k, subsample=subsample)
    result, _ = find_dtr(profile, threshold=threshold, min_length=min_length)
    return result


def main(argv: Sequence[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("contig", help="assembly FASTA (first sequence is used)")
    ap.add_argument("reads", nargs="+", help="FASTQ file(s), plain or .gz")
    ap.add_argument("-k", type=int, default=31, help="k-mer size (default 31)")
    ap.add_argument("--subsample", type=int, default=150_000,
                    help="reads to stream per FASTQ (default 150000)")
    ap.add_argument("--threshold", type=float, default=1.6,
                    help="coverage multiple of the median that counts as a spike (default 1.6)")
    ap.add_argument("--min-length", type=int, default=15,
                    help="shortest spike run to report, in bp (default 15)")
    args = ap.parse_args(argv)
    print(check(args.contig, args.reads, k=args.k, subsample=args.subsample,
                threshold=args.threshold, min_length=args.min_length))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
