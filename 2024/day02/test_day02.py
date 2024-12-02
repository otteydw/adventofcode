# test_aoc_template.py

import pathlib

import day02 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_is_safe():
    assert aoc.is_safe([7, 6, 4, 2, 1]) is True
    assert aoc.is_safe([1, 2, 7, 8, 9]) is False
    assert aoc.is_safe([9, 7, 6, 2, 1]) is False
    assert aoc.is_safe([1, 3, 2, 4, 5]) is False
    assert aoc.is_safe([8, 6, 4, 4, 1]) is False
    assert aoc.is_safe([1, 3, 6, 7, 9]) is True


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1[0] == [7, 6, 4, 2, 1]


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 2


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...
