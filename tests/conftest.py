# tests/conftest.py
import pytest
from pathlib import Path


@pytest.fixture
def sample_input_lines():
    fixtures_dir = Path(__file__).parent / "fixtures"
    input_path = fixtures_dir / "input.txt"
    # Read all non-blank, stripped lines
    return [
        line.strip() for line in input_path.read_text().splitlines() if line.strip()
    ]


@pytest.fixture
def expected_output_lines():
    fixtures_dir = Path(__file__).parent / "fixtures"
    output_path = fixtures_dir / "output.txt"
    # Read all non-blank, stripped lines
    return [
        line.strip() for line in output_path.read_text().splitlines() if line.strip()
    ]
