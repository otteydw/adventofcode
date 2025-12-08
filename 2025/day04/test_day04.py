# test_aoc_template.py

import pathlib

import day04 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


def test_surrounding_coordinates():
    assert aoc.surrounding_coordinates((0, 0)) == [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    assert aoc.surrounding_coordinates((10, 10)) == [
        (9, 9),
        (9, 10),
        (9, 11),
        (10, 9),
        (10, 11),
        (11, 9),
        (11, 10),
        (11, 11),
    ]
    assert aoc.surrounding_coordinates((4, 4)) == [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]
    assert aoc.surrounding_coordinates((4, 4), inclusive=True) == [
        (3, 3),
        (3, 4),
        (3, 5),
        (4, 3),
        (4, 4),
        (4, 5),
        (5, 3),
        (5, 4),
        (5, 5),
    ]
    assert aoc.surrounding_coordinates((0, 0), min_coordinate=(0, 0)) == [(0, 1), (1, 0), (1, 1)]
    assert aoc.surrounding_coordinates((10, 10), max_coordinate=(10, 10)) == [
        (9, 9),
        (9, 10),
        (10, 9),
    ]


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
    assert aoc.part1(example1) == 13


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 43
