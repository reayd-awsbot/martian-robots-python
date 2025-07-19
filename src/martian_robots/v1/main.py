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


def process_lines(lines: List[str]) -> List[str]:
    """
    Process a sequence of input lines and return the simulation results.

    Args:
        lines: A list of non-empty, stripped strings from the input.
               - The first line defines the upper-right corner of the grid as two ints: "max_x max_y".
               - Each subsequent pair of lines gives:
                   1) The robot's initial x, y coordinates and orientation (N, E, S, W).
                   2) A string of movement instructions: L (turn left), R (turn right), F (forward).

    Returns:
        A list of result strings for each robot in order, e.g.:
            "1 1 E"
            "3 3 N LOST"
            "2 3 S"
    """
    # 1) Clean input: strip whitespace, drop blank lines
    cleaned = [line for line in (l.strip() for l in lines) if line]
    it = iter(cleaned)  # Create an iterator over cleaned lines

    # 2) Parse the grid upper-right coordinates from the first line
    #    The bottom-left of the grid is implicitly (0, 0).
    max_x, max_y = map(int, next(it).split())

    # 3) Track "scents" (positions) where robots have fallen off the grid.
    #    If a robot is about to fall off at a scented point, it ignores that move.
    scents: Set[Tuple[int, int]] = set()

    # 4) Define orientation order and movement deltas
    directions = ["N", "E", "S", "W"]  # Clockwise ordering
    moves = {
        "N": (0, 1),  # north: y + 1
        "E": (1, 0),  # east:  x + 1
        "S": (0, -1),  # south: y - 1
        "W": (-1, 0),  # west:  x - 1
    }

    results: List[str] = []

    # 5) Process each robot: two lines at a time from the iterator
    for pos in it:
        # Parse initial position and orientation
        x_str, y_str, ori = pos.split()
        x, y = int(x_str), int(y_str)
        dir_idx = directions.index(ori)  # Current facing index in `directions`

        # Read instruction string for this robot
        instr = next(it)
        lost = False  # Flag to mark if robot becomes lost

        # 6) Simulate each command in sequence
        for cmd in instr:
            if cmd == "L":
                # Turn left: move index backwards (modulo wrap)
                dir_idx = (dir_idx - 1) % 4
            elif cmd == "R":
                # Turn right: move index forwards (modulo wrap)
                dir_idx = (dir_idx + 1) % 4
            elif cmd == "F":
                # Move forward in current facing direction
                dx, dy = moves[directions[dir_idx]]
                nx, ny = x + dx, y + dy

                # Check if next position is off the grid
                if not (0 <= nx <= max_x and 0 <= ny <= max_y):
                    # If this spot has no scent, robot is lost here
                    if (x, y) not in scents:
                        scents.add((x, y))  # Leave a scent
                        lost = True
                        break  # Stop processing further commands
                    # If there's already a scent, ignore this move
                else:
                    # Valid move: update robot's position
                    x, y = nx, ny
            # Any other character is ignored

        # 7) Format result: include "LOST" if robot fell off
        result = f"{x} {y} {directions[dir_idx]}"
        if lost:
            result += " LOST"
        results.append(result)

    return results


def main():
    """
    Read from standard input, process the lines, and print the results.
    """
    # Read & clean all stdin lines
    lines = [line for line in (l.strip() for l in sys.stdin) if line]
    # Process and output each result line-by-line
    for line in process_lines(lines):
        print(line)


if __name__ == "__main__":
    main()
