#!/usr/bin/env python3
import sys
from typing import List, Tuple, Set

# -----------------------------------------------------------------------------
# Mars Robot Simulator
# -----------------------------------------------------------------------------
# This script reads a rectangular grid size and a series of robot starting
# positions with movement instructions from input lines, simulates each
# robot's path on the grid, and reports their final positions. Robots that
# move off the grid are considered "lost" and leave a scent that prevents
# subsequent robots from falling off at the same point.
# -----------------------------------------------------------------------------


class Grid:
    """
    Represents the rectangular grid on which robots move.
    Manages the bounds and "scents" where robots were lost.
    """

    def __init__(self, max_x: int, max_y: int):
        self.max_x, self.max_y = max_x, max_y
        # Positions (x,y) where robots have been lost
        self.scents: Set[Tuple[int, int]] = set()

    def is_within_bounds(self, x: int, y: int) -> bool:
        """Return True if (x,y) lies inside the grid (including edges)."""
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y

    def has_scent(self, x: int, y: int) -> bool:
        """Return True if a scent is present at (x,y)."""
        return (x, y) in self.scents

    def leave_scent(self, x: int, y: int):
        """Mark the position (x,y) with a scent (robot was lost here)."""
        self.scents.add((x, y))


class Robot:
    """
    Represents a robot on the grid with position, orientation, and lost flag.
    """

    DIRECTIONS = ["N", "E", "S", "W"]  # Clockwise order for turns
    MOVES = {
        "N": (0, 1),  # north: y+1
        "E": (1, 0),  # east:  x+1
        "S": (0, -1),  # south: y-1
        "W": (-1, 0),  # west:  x-1
    }

    def __init__(self, x: int, y: int, orientation: str):
        self.x = x
        self.y = y
        # index in DIRECTIONS
        self.dir_idx = Robot.DIRECTIONS.index(orientation)
        # becomes True if the robot moves off the grid
        self.is_lost = False

    @property
    def orientation(self) -> str:
        """Current cardinal orientation as a letter 'N', 'E', 'S', or 'W'."""
        return Robot.DIRECTIONS[self.dir_idx]

    def turn_left(self):
        """Rotate orientation 90° left (counter-clockwise)."""
        self.dir_idx = (self.dir_idx - 1) % 4

    def turn_right(self):
        """Rotate orientation 90° right (clockwise)."""
        self.dir_idx = (self.dir_idx + 1) % 4

    def move_forward(self, grid: Grid):
        """
        Attempt to move forward one step in the current orientation.
        If this step would leave the grid and no scent exists, the robot
        is marked lost and leaves a scent. If a scent exists, the command
        is ignored. Otherwise, update (x,y).
        """
        dx, dy = Robot.MOVES[self.orientation]
        nx, ny = self.x + dx, self.y + dy

        # Check grid bounds
        if not grid.is_within_bounds(nx, ny):
            # No previous scent here? Robot is lost, leave scent
            if not grid.has_scent(self.x, self.y):
                grid.leave_scent(self.x, self.y)
                self.is_lost = True
            # If there is a scent, ignore this forward command
        else:
            # Valid move: update position
            self.x, self.y = nx, ny


class Simulator:
    """
    Runs instruction sequences on robots within a given grid.
    Commands map to Robot methods or grid interactions.
    """

    COMMANDS = {
        "L": lambda robot, grid: robot.turn_left(),
        "R": lambda robot, grid: robot.turn_right(),
        "F": lambda robot, grid: robot.move_forward(grid),
    }

    def __init__(self, grid: Grid):
        self.grid = grid

    def run(self, robot: Robot, instructions: str) -> Robot:
        """
        Execute each command character on the robot until it finishes
        or gets lost. Returns the final robot object.
        """
        for cmd in instructions:
            # Only process valid commands and if robot is not already lost
            if not robot.is_lost and cmd in Simulator.COMMANDS:
                Simulator.COMMANDS[cmd](robot, self.grid)
        return robot


def process_lines(lines: List[str]) -> List[str]:
    """
    Parse and execute the full simulation from a list of text lines.

    1) First line: two ints defining grid's max x and y.
    2) Then for each robot:
       - A line "x y O" for initial state.
       - A line of instructions (e.g. "RFRFF").

    Returns a list of output lines:
      "x y O" or "x y O LOST" for each robot.
    """
    # Clean input: strip whitespace, drop empty lines
    cleaned = [line for line in (l.strip() for l in lines) if line]
    it = iter(cleaned)

    # 1) Grid setup
    max_x, max_y = map(int, next(it).split())
    grid = Grid(max_x, max_y)
    simulator = Simulator(grid)

    results: List[str] = []

    # 2) Process each robot (two lines at a time)
    while True:
        try:
            pos = next(it)
        except StopIteration:
            break
        x_str, y_str, ori = pos.split()
        instr = next(it)

        # Create a fresh robot and execute instructions
        robot = Robot(int(x_str), int(y_str), ori)
        final_robot = simulator.run(robot, instr)

        # Format result
        out = f"{final_robot.x} {final_robot.y} {final_robot.orientation}"
        if final_robot.is_lost:
            out += " LOST"
        results.append(out)

    return results


def main():
    """
    Read from stdin, process, and print results.
    """
    lines = [line for line in (l.strip() for l in sys.stdin) if line]
    for output_line in process_lines(lines):
        print(output_line)


if __name__ == "__main__":
    main()
