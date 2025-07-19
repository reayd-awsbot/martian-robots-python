import pytest
from martian_robots.v2.main import Grid, Robot, Simulator

# ----- Simulator Unit Tests -----


@pytest.fixture
def simple_grid():
    return Grid(5, 3)


@pytest.fixture
def simulator(simple_grid):
    return Simulator(simple_grid)


def test_simulator_turn_and_move(simple_grid, simulator):
    # Start at (1,1) facing East, instruct: R -> now South, F moves to (1,0)
    robot = Robot(1, 1, "E")
    final = simulator.run(robot, "RF")
    assert (final.x, final.y) == (1, 0)
    assert final.orientation == "S"
    assert not final.is_lost


def test_simulator_forward_inside_bounds(simple_grid, simulator):
    robot = Robot(0, 0, "N")
    final = simulator.run(robot, "FFF")
    # Moves north three steps but grid max_y=3
    assert (final.x, final.y) == (0, 3)
    assert not final.is_lost


def test_simulator_robot_lost_and_scent_prevents_second(simple_grid, simulator):
    # Robot1 runs off north edge at (0,3)
    r1 = Robot(0, 3, "N")
    final1 = simulator.run(r1, "F")
    assert final1.is_lost
    # Grid now has scent at (0,3)
    assert simple_grid.has_scent(0, 3)

    # Robot2 at same start; forward should be ignored and not lost
    r2 = Robot(0, 3, "N")
    final2 = simulator.run(r2, "F")
    assert not final2.is_lost
    assert (final2.x, final2.y) == (0, 3)


def test_simulator_invalid_commands_ignored(simple_grid, simulator):
    # Commands other than L,R,F are no-ops
    robot = Robot(2, 2, "S")
    final = simulator.run(robot, "FXAFL")
    # F moves south to (2,1), X and A ignored, F moves to (2,0), L turns to E
    assert (final.x, final.y) == (2, 0)
    assert final.orientation == "E"
    assert not final.is_lost
