# test_aoc_template.py

import pathlib
from typing import List

import pytest

from . import day02 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (
        ("1,0,0,0,99", [1, 0, 0, 0, 99]),
        ("2,3,0,3,99", [2, 3, 0, 3, 99]),
        ("2,4,4,5,99,0", [2, 4, 4, 5, 99, 0]),
        ("1,1,1,4,99,5,6,0,99", [1, 1, 1, 4, 99, 5, 6, 0, 99]),
    ),
)
def test_parse(input_s: str, expected: List) -> None:
    assert aoc.parse(input_s) == expected


@pytest.mark.parametrize(
    ("input_l", "expected"),
    (
        ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
        ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
        ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
        ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
    ),
)
def test_run_program(input_l: List, expected: List) -> None:
    assert aoc.run_program(input_l) == expected


# @pytest.fixture
# def example1():
#     puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
#     return aoc.parse(puzzle_input)


# @pytest.fixture
# def example2():
#     puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
#     return aoc.parse(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
# def test_parse_example1(example1):
#     """Test that input is parsed properly."""
#     assert example1 == ...


# @pytest.mark.skip(reason="Not implemented")
# def test_part1_example1(example1):
#     """Test part 1 on example input."""
#     assert aoc.part1(example1) == ...


# @pytest.mark.skip(reason="Not implemented")
# def test_part2_example1(example1):
#     """Test part 2 on example input."""
#     assert aoc.part2(example1) == ...


# @pytest.mark.skip(reason="Not implemented")
# def test_part2_example2(example2):
#     """Test part 2 on example input."""
#     assert aoc.part2(example2) == ...
