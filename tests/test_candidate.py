"""
tests/test_candidate.py — pytest suite for HEUR-01 candidate generation.
"""
import pytest
from drt.types import MeetingPoint, Request
from drt.candidate import generate_candidates, euclidean


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

def make_request(origin=(0.0, 0.0), destination=(10.0, 10.0)):
    return Request(
        id="r1",
        origin=origin,
        destination=destination,
        earliest=0.0,
        latest=60.0,
        max_ride_time=30.0,
    )


def make_mp(id_, x, y):
    return MeetingPoint(id=id_, coords=(x, y))


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def test_within_radius():
    """3 points, 2 within radius → returns exactly 2."""
    request = make_request(origin=(0.0, 0.0))
    mps = [
        make_mp("A", 1.0, 0.0),   # dist = 1.0  ✓
        make_mp("B", 2.0, 0.0),   # dist = 2.0  ✓
        make_mp("C", 5.0, 0.0),   # dist = 5.0  ✗
    ]
    result = generate_candidates(request, mps, rho=3.0, k_top=10, side="pickup")
    assert len(result) == 2
    assert result[0].id == "A"
    assert result[1].id == "B"


def test_top_k_limit():
    """5 points within radius, k_top=3 → returns 3 closest."""
    request = make_request(origin=(0.0, 0.0))
    mps = [
        make_mp("A", 5.0, 0.0),
        make_mp("B", 1.0, 0.0),
        make_mp("C", 3.0, 0.0),
        make_mp("D", 2.0, 0.0),
        make_mp("E", 4.0, 0.0),
    ]
    result = generate_candidates(request, mps, rho=10.0, k_top=3, side="pickup")
    assert len(result) == 3
    ids = [mp.id for mp in result]
    assert ids == ["B", "D", "C"]  # sorted by distance: 1, 2, 3


def test_empty_result():
    """No points within radius → returns empty list."""
    request = make_request(origin=(0.0, 0.0))
    mps = [
        make_mp("A", 10.0, 0.0),
        make_mp("B", 20.0, 0.0),
    ]
    result = generate_candidates(request, mps, rho=5.0, k_top=10, side="pickup")
    assert result == []


def test_sorted_by_distance():
    """Returned list is sorted ascending by distance."""
    request = make_request(origin=(0.0, 0.0))
    mps = [
        make_mp("far",  4.0, 0.0),
        make_mp("near", 1.0, 0.0),
        make_mp("mid",  2.5, 0.0),
    ]
    result = generate_candidates(request, mps, rho=10.0, k_top=10, side="pickup")
    dists = [euclidean(request.origin, mp.coords) for mp in result]
    assert dists == sorted(dists)


def test_dropoff_side_uses_destination():
    """side='dropoff' filters relative to request.destination, not origin."""
    request = make_request(origin=(0.0, 0.0), destination=(100.0, 0.0))
    mps = [
        make_mp("near_dest", 101.0, 0.0),  # dist from dest = 1.0  ✓
        make_mp("near_orig", 1.0, 0.0),    # dist from dest = 99.0 ✗
    ]
    result = generate_candidates(request, mps, rho=5.0, k_top=10, side="dropoff")
    assert len(result) == 1
    assert result[0].id == "near_dest"


def test_boundary_exactly_at_radius():
    """Point exactly at distance rho is included (≤ rho)."""
    request = make_request(origin=(0.0, 0.0))
    mps = [make_mp("exact", 3.0, 0.0)]  # dist = 3.0
    result = generate_candidates(request, mps, rho=3.0, k_top=10, side="pickup")
    assert len(result) == 1


def test_empty_meeting_points_list():
    """Empty meeting_points input → returns empty list."""
    request = make_request()
    result = generate_candidates(request, [], rho=100.0, k_top=10, side="pickup")
    assert result == []
