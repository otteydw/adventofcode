import pathlib

import day08 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = aoc.load_input(PUZZLE_DIR / "example1.txt")
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = aoc.load_input(PUZZLE_DIR / "example2.txt")
    return aoc.parse(puzzle_input)


def test_straight_line_distance():
    coordinate1 = (162, 817, 812)
    coordinate2 = (425, 690, 689)
    distance1 = aoc.straight_line_distance(coordinate1, coordinate2)

    coordinate3 = (162, 817, 812)
    coordinate4 = (431, 825, 988)
    distance2 = aoc.straight_line_distance(coordinate3, coordinate4)

    assert distance1 < distance2


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1[0] == (162, 817, 812)
    assert example1[19] == (425, 690, 689)


# def test_sort_coordinates(example1):
#     sorted_coordinates = aoc.sort_coordinates(example1)
#     assert sorted_coordinates[0] == (162, 817, 812)


def test_sort_coordinate_pairs(example1):
    sorted_pairs = aoc.sort_coordinate_pairs(example1)
    assert sorted_pairs[0] == ((162, 817, 812), (425, 690, 689))


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1, max_pairs=1) == 2
    assert aoc.part1(example1, max_pairs=2) == 3
    assert aoc.part1(example1, max_pairs=3) == 6
    assert aoc.part1(example1, max_pairs=4) == 6
    assert aoc.part1(example1, max_pairs=10) == 40


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...
