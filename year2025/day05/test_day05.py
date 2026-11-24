# test_aoc_template.py

import pathlib

import pytest

from . import day05 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


def test_is_fresh():
    my_ranges = [(3, 5), (10, 14), (16, 20), (12, 18)]

    assert not aoc.is_fresh(my_ranges, 1)
    assert not aoc.is_fresh(my_ranges, 8)
    assert not aoc.is_fresh(my_ranges, 32)
    assert aoc.is_fresh(my_ranges, 5)
    assert aoc.is_fresh(my_ranges, 11)
    assert aoc.is_fresh(my_ranges, 17)


def test_combine_ranges():
    assert aoc.merge_intervals([(1, 10), (4, 9)]) == [(1, 10)]
    assert aoc.merge_intervals([(4, 9), (1, 10)]) == [(1, 10)]
    assert aoc.merge_intervals([(1, 5), (3, 7), (10, 12), (9, 11)]) == [(1, 7), (9, 12)]


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 3


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 14
