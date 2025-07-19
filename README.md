# Problem:  Martian  Robots 

## The  Problem 
The surface of Mars can be modelled by a rectangular grid around which robots are able to move according to instructions provided from Earth. You are to write a program that determines each sequence of robot positions and reports the final position of the robot.

A robot position consists of a grid coordinate (a pair of integers: x-coordinate followed by
y-coordinate) and an orientation (N, S, E, W for north, south, east, and west).

A robot instruction is a string of the letters “L”, “R”, and “F” which represent, respectively, the
instructions:

* Left : the robot turns left 90 degrees and remains on the current grid point.
* Right : the robot turns right 90 degrees and remains on the current grid point.
* Forward : the robot moves forward one grid point in the direction of the current orientation and maintains the same orientation.

The direction North corresponds to the direction from grid point (x, y) to grid point (x, y+1).

There is also a possibility that additional command types may be required in the future and
provision should be made for this.

Since the grid is rectangular and bounded (…yes Mars is a strange planet), a robot that
moves “off” an edge of the grid is lost forever. However, lost robots leave a robot “scent” that
prohibits future robots from dropping off the world at the same grid point. The scent is left at
the last grid position the robot occupied before disappearing over the edge. An instruction to
move “off” the world from a grid point from which a robot has been previously lost is simply
ignored by the current robot.

## The  Input 
The first line of input is the upper-right coordinates of the rectangular world, the lower-left
coordinates are assumed to be 0, 0.

The remaining input consists of a sequence of robot positions and instructions (two lines per
robot). A position consists of two integers specifying the initial coordinates of the robot and
an orientation (N, S, E, W), all separated by whitespace on one line. A robot instruction is a
string of the letters “L”, “R”, and “F” on one line.

Each robot is processed sequentially, i.e., finishes executing the robot instructions before the
next robot begins execution.

The maximum value for any coordinate is 50.

All instruction strings will be less than 100 characters in length.

## The  Output 
For each robot position/instruction in the input, the output should indicate the final grid
position and orientation of the robot. If a robot falls off the edge of the grid the word “LOST”
should be printed after the position and orientation.

### Sample  Input
```bash
1 1 E
RFRFRFRF

3 2 N
FRRFLLFFRRFLL

0 3 W
LLFFFLFLFL
```
### Sample  Out
```bash
1 1 E
3 3 N LOST
2 3 S
```

## Requirements
- **Python** 3.10.12 (exact)  
- No other runtime dependencies beyond the standard library

For development & testing you’ll also need: `pytest`, `pylint`, `black` (see dev dependencies in `pyproject.toml`).

## Installation

1. **Clone** the repository  
```bash
git clone https://github.com/your-username/martian-robots-python.git
cd martian-robots-python
````

2. **Install** via [Poetry](https://python-poetry.org):

```bash
poetry install
```

*(Alternatively, you can create a virtualenv and `pip install .`.)*



## Testing

Run **unit** and **functional** tests with pytest:

```bash
poetry run pytest
```

* Marker-based tests:

  * `@pytest.mark.unit` for isolated logic
  * `@pytest.mark.functional` for end-to-end scenarios
* Coverage report:

```bash
poetry run pytest --cov
```

Dev linting & formatting:

```bash
poetry run pylint martian_robots
poetry run black --check .
```

## Project Structure

```
    .
    ├── pyproject.toml      # project config & dependencies :contentReference[oaicite:4]{index=4}
    ├── README.md           # this document
    ├── src/
    │   └── martian_robots/ # core package
    │       ├── __main__.py
    │       ├── grid.py
    │       └── robot.py
    └── tests/
        ├── unit/
        └── functional/
```
You can surface all of the handy shortcuts in your README by adding a “Makefile” section. For example, right after your **Usage** section you might insert:


## Makefile

A `Makefile` is provided to simplify common workflows:

- **install**: Install the project’s Poetry environment  
    ```bash
    make install
    ```

* **test**: Run all pytest tests with coverage and clear the cache

    ```bash
    make test
    ```

* **lint**: Run `pylint` across the codebase

    ```bash
    make lint
    ```

* **black**: Auto-format all code with Black

    ```bash
    make black
    ```

* **check-black**: Verify code formatting without making changes

    ```bash
    make check-black
    ```

* **checkin**: Format, test, then commit & push (prompts for a commit message)

    ```bash
    make checkin
    ```

* **run**: Execute the Martian Robots CLI on the sample fixture

    ```bash
    make run
    ```

## GitHub Configuration

This project includes a set of GitHub configuration files and workflows under the `.github/` directory to automate dependency updates, enforce code quality, and streamline collaboration.

### Dependabot

- **`.github/dependabot.yml`**  
  Configures Dependabot to check for updates to your Python dependencies on a regular schedule and open automated pull requests when new versions are available.

### Pull Request Template

- **`.github/pull_request-template.md`**  
  Provides a standardized template for contributors to fill out when opening a pull request, ensuring each PR includes a description of changes, related issues, testing notes, and any other relevant context.

### GitHub Actions Workflows

All workflows live in `.github/workflows/` and run on `push` and `pull_request` events by default.

| Workflow File     | Purpose                                                                               |
|-------------------|---------------------------------------------------------------------------------------|
| `auto-assign.yaml`| Automatically assigns reviewers or teams to new pull requests based on code ownership or labels. |
| `branch.yaml`     | Enforces branch naming conventions and triggers branch-protection checks on new branches or PRs. |
| `linting.yml`     | Runs code linters (`black`, `pylint`) on changed files to ensure style and quality standards are met. |
| `tests.yml`       | Executes the full test suite (`pytest`, coverage) and reports results in the PR status checks. |

These configurations help maintain code quality, keep dependencies up to date, and make collaboration smoother and more consistent across the team.  

## References
* https://github.com/neilkennedy/coding-challenge-martian-robots
* https://joneaves.wordpress.com/2014/07/21/toy-robot-coding-test/
* https://www.jpl.nasa.gov/edu/resources/lesson-plan/mars-sample-return-coding-challenge/
* https://gitlab.doc.ic.ac.uk/ryd23/martian-robots
* https://ece.ncsu.edu/2023/throwbackthursday-ece-alum-cracks-the-mars-rover-code/
* https://amanagrawal.blog/2020/06/28/mars-rover-programming-kata-using-dddtddports-and-adapters/
* https://www.youtube.com/watch?v=QAaDUlhJocQ
* https://code.google.com/archive/p/marsrovertechchallenge/
* https://education.vex.com/stemlabs/123/mars-rover-landing-challenge/unit-overview/background
* https://fr.vittascience.com/public/content/user_data/resources/Martian_robot_booklet_ST.pdf
