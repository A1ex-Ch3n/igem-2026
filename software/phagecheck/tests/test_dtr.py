"""The DTR check must separate a linear-with-DTR genome from a circular one."""
import random

import pytest

from phagecheck.dtr import check, coverage_profile, find_dtr

READ_LEN = 120
K = 31


def random_genome(length: int, seed: int) -> str:
    rng = random.Random(seed)
    return "".join(rng.choice("ACGT") for _ in range(length))


def linear_with_dtr(core_len: int = 3000, dtr_len: int = 200, seed: int = 1) -> str:
    """A genome whose first and last dtr_len bases are identical."""
    core = random_genome(core_len, seed)
    return core + core[:dtr_len]


def simulate_reads(genome: str, n: int, seed: int, circular: bool) -> list[str]:
    rng = random.Random(seed)
    reads = []
    for _ in range(n):
        start = rng.randrange(len(genome))
        if circular:
            reads.append((genome + genome)[start:start + READ_LEN])
        else:
            if start + READ_LEN > len(genome):
                continue
            reads.append(genome[start:start + READ_LEN])
    return reads


def write_fastq(tmp_path, reads, name):
    path = tmp_path / name
    path.write_text("".join(f"@r{i}\n{s}\n+\n{'I' * len(s)}\n"
                            for i, s in enumerate(reads)))
    return path


def write_fasta(tmp_path, seq, name):
    path = tmp_path / name
    path.write_text(f">contig\n{seq}\n")
    return path


def test_linear_dtr_is_detected(tmp_path):
    """The assembler collapses the DTR, so reads from both ends pile onto it."""
    genome = linear_with_dtr()
    contig = genome[:-200]                       # the collapsed assembly
    reads = simulate_reads(genome, 4000, seed=2, circular=False)
    fa = write_fasta(tmp_path, contig, "contig.fasta")
    fq = write_fastq(tmp_path, reads, "reads.fastq")

    result = check(fa, [fq], k=K)

    assert result.verdict == "LINEAR + DTR"
    starts = [run[0] for run in result.runs]
    assert min(starts) < 100, f"spike should sit at the contig start, got {result.runs}"


def test_circular_genome_has_no_spike(tmp_path):
    genome = random_genome(3000, seed=3)
    reads = simulate_reads(genome, 4000, seed=4, circular=True)
    fa = write_fasta(tmp_path, genome, "contig.fasta")
    fq = write_fastq(tmp_path, reads, "reads.fastq")

    result = check(fa, [fq], k=K)

    assert result.verdict == "CIRCULAR / no short linear DTR"
    assert result.runs == []


def test_profile_length_and_threshold():
    contig = random_genome(500, seed=5)
    profile = coverage_profile(contig, [], k=K)
    assert len(profile) == len(contig) - K + 1
    assert set(profile) == {0}

    flat = [10] * 100
    result, median = find_dtr(flat)
    assert median == 10 and result.runs == []

    spiked = [10] * 100
    spiked[:20] = [20] * 20
    result, _ = find_dtr(spiked)
    assert result.runs == [(1, 20, 20)]


@pytest.mark.parametrize("kmer,expected", [("AAA", "AAA"), ("TTT", "AAA"), ("ACG", "ACG")])
def test_canonical(kmer, expected):
    from phagecheck.dtr import canonical
    assert canonical(kmer) == expected
