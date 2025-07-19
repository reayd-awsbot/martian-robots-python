# tests/test_process_lines.py
import pytest
from martian_robots.v1.main import process_lines

pytestmark = pytest.mark.functional


def test_sample_output(sample_input_lines):
    expected = [
        "1 1 E",
        "3 3 N LOST",
        "2 3 S",
    ]
    assert process_lines(sample_input_lines) == expected
