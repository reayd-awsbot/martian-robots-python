import pytest
from martian_robots.v2.main import Grid, Robot

pytestmark = pytest.mark.unit


@pytest.fixture
def small_grid():
    return Grid(1, 1)


def test_turns_cycle():
    r = Robot(0, 0, "N")
    assert r.orientation == "N"
    r.turn_right()
    assert r.orientation == "E"
    r.turn_right()
    assert r.orientation == "S"
    r.turn_left()
    assert r.orientation == "E"
    # full circle
    for _ in range(4):
        r.turn_left()
    assert r.orientation == "E"


def test_move_within_bounds(small_grid):
    r = Robot(0, 0, "N")
    r.move_forward(small_grid)
    assert (r.x, r.y) == (0, 1)
    assert not r.is_lost


def test_move_off_grid_leaves_scent_and_lost(small_grid):
    r1 = Robot(0, 1, "N")
    r1.move_forward(small_grid)
    assert r1.is_lost
    # grid should now have a scent at (0,1)
    assert small_grid.has_scent(0, 1)


def test_scent_prevents_second_loss(small_grid):
    # First robot falls off at (0,1)
    r1 = Robot(0, 1, "N")
    r1.move_forward(small_grid)
    assert r1.is_lost

    # Second robot at same spot tries to fall off again
    r2 = Robot(0, 1, "N")
    r2.move_forward(small_grid)
    assert not r2.is_lost
    # position unchanged
    assert (r2.x, r2.y) == (0, 1)
