import pathlib

import day17 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = aoc.load_input(PUZZLE_DIR / "example1.txt")
    return aoc.parse(puzzle_input)


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1, eggnog=25) == 4


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1, eggnog=25) == 3
