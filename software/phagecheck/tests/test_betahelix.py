"""Unit tests for the β-helix signature, plus a regression test on a real fold."""
from pathlib import Path

import numpy as np
import pytest

from phagecheck.betahelix import (classify, elongation, hbond_offset_histogram,
                                  periodic_core)

# the tail spike whose β-helix call this tool was written to make
REPO = Path(__file__).resolve().parents[3]
TAILSPIKE = (REPO / "code/output/0712_phage_rbp_detect/structure/pdb"
             / "9-2-1_phi8__CDS_0016__trimer_unrelaxed_rank_001"
               "_alphafold2_multimer_v3_model_1_seed_000.pdb")


def test_elongation_separates_a_rod_from_a_ball():
    rng = np.random.default_rng(0)
    ball = rng.normal(size=(300, 3))
    rod = ball.copy()
    rod[:, 0] *= 20
    assert elongation(ball) < 1.5
    assert elongation(rod) > 5


def _paired_strands(n: int, offset: int, spacing: float = 2.9):
    """Two rows of atoms spaced so that N(i) pairs with O(i+offset)."""
    N = np.array([[i * 3.3, 0.0, 0.0] for i in range(n)])
    O = np.array([[(i - offset) * 3.3, spacing, 0.0] for i in range(n)])
    return N, O


def test_hbond_histogram_finds_the_register():
    N, O = _paired_strands(60, offset=18)
    hist = hbond_offset_histogram(N, O)
    assert int(np.argmax(hist[6:]) + 6) == 18
    assert hist[18] > 20


def test_periodic_core_spans_the_paired_region():
    N, O = _paired_strands(60, offset=18)
    start, end, count = periodic_core(N, O, period=18)
    assert start == 0 and end == 59
    assert count >= 40


def test_periodic_core_empty_when_nothing_is_in_register():
    N, O = _paired_strands(60, offset=18)
    assert periodic_core(N, O, period=4) == (0, 0, 0)


@pytest.mark.skipif(not TAILSPIKE.exists(), reason="ColabFold output not present")
def test_known_tailspike_is_called_a_beta_helix():
    call = classify(TAILSPIKE)
    assert call is not None
    assert call.verdict == "beta-helix"
    assert 16 <= call.period <= 26
    assert call.elongation >= 2.0
