# test_aoc_template.py

import pathlib

import pytest

import day16 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 46


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 51
