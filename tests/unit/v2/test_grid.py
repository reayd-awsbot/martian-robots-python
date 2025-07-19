import pytest
from martian_robots.v2.main import Grid, Robot, Simulator

# ----- Grid Unit Tests -----


def test_is_within_bounds_true():
    grid = Grid(5, 3)
    # corners and interior
    assert grid.is_within_bounds(0, 0)
    assert grid.is_within_bounds(5, 3)
    assert grid.is_within_bounds(2, 1)


def test_is_within_bounds_false():
    grid = Grid(5, 3)
    # outside bounds
    assert not grid.is_within_bounds(-1, 0)
    assert not grid.is_within_bounds(0, 4)
    assert not grid.is_within_bounds(6, 3)


def test_scents_initially_empty():
    grid = Grid(2, 2)
    assert not grid.scents
    assert not grid.has_scent(0, 0)


def test_leave_and_has_scent():
    grid = Grid(2, 2)
    grid.leave_scent(1, 1)
    assert grid.has_scent(1, 1)
    # scent does not affect other positions
    assert not grid.has_scent(0, 0)
