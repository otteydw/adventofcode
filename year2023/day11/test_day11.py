# test_aoc_template.py

import pathlib

import pytest

from . import day11 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ...


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 374


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example_by_10(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1, expansion=10) == 1030


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example_by_100(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1, expansion=100) == 8410


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...


def test_find_no_galaxies(example1):
    grid = aoc.data_to_grid(example1)
    assert aoc.find_no_galaxies(grid) == ([3, 7], [2, 5, 8])


def test_find_galaxies(example1):
    grid = aoc.data_to_grid(example1)
    assert aoc.find_galaxies(grid) == [
        (0, 3),
        (1, 7),
        (2, 0),
        (4, 6),
        (5, 1),
        (6, 9),
        (8, 7),
        (9, 0),
        (9, 4),
    ]


def test_shortest_distance_between_points():
    assert aoc.shortest_distance_between_points((0, 0), (1, 1)) == 2
    assert aoc.shortest_distance_between_points((6, 9), (9, 4)) == 8
