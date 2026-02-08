import pathlib

import pytest

from . import day20 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


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
