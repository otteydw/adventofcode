import pathlib

import pytest

from . import day20 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


# @pytest.fixture
# def example1():
#     puzzle_input = aoc.load_input(PUZZLE_DIR / "example1.txt")
#     return aoc.parse(puzzle_input)


# @pytest.fixture
# def example2():
#     puzzle_input = aoc.load_input(PUZZLE_DIR / "example2.txt")
#     return aoc.parse(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
# def test_parse_example1(example1):
#     """Test that input is parsed properly."""
#     assert example1 == ...


# @pytest.mark.skip(reason="Not implemented")
# def test_gifts():
#     """Test part 1"""
#     assert aoc.gifts(1) == 10
#     assert aoc.gifts(2) == 30
#     assert aoc.gifts(3) == 40
#     # assert aoc.gifts(4) == 70


@pytest.mark.parametrize(
    "elf, house, expected",
    [
        [1, 1, 10],
        [2, 1, 0],
        [2, 2, 20],
        [3, 1, 0],
        [3, 2, 0],
        [3, 3, 30],
        [3, 4, 0],
        [3, 6, 30],
    ],
)
def test_gifts_delivered_by_elf(elf, house, expected):
    assert aoc.gifts_delivered_by_elf(elf, house) == expected


@pytest.mark.parametrize(
    "house, expected",
    [
        [1, 10],
        [2, 30],
        [3, 40],
        [4, 70],
        [5, 60],
        [6, 120],
        [7, 80],
        [8, 150],
        [9, 130],
    ],
)
def test_gifts_delivered_to_house(house, expected):
    assert aoc.gifts_delivered_to_house(house) == expected


def test_part1():
    assert aoc.part1(30) == 2
    assert aoc.part1(130) == 8


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...
