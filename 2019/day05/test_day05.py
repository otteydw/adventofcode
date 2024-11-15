# test_aoc_template.py

import pathlib
from typing import List

import day05 as aoc
import pytest

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
        ([101, 4, 0, 0, 99], [105, 4, 0, 0, 99]),  # literal 4 added to 101 from position 0 = 105 stored in position 0
        (
            [102, 4, 0, 0, 99],
            [408, 4, 0, 0, 99],
        ),  # literal 4 multiplied by 102 from position 0 = 408 stored in position 0
        ([1101, 100, -1, 4, 0], [1101, 100, -1, 4, 99]),
    ),
)
def test_run_program(input_l: List, expected: List) -> None:
    memory = input_l
    aoc.run_program(memory)
    assert memory == expected


# @pytest.mark.parametrize(
#     ("program", "address", "expected"),
#     (
#         ([1, 0, 0, 0, 99], 0, 1),
#         ([2, 3, 0, 3, 99], 0, 2),
#         ([1002, 3, 0, 3, 99], 0, 2),
#     ),
# )
# def test_get_opcode(program, address, expected):
#     assert aoc.get_opcode(program, address) == expected


@pytest.mark.parametrize(
    ("instruction", "expected"),
    (
        (1, 1),
        (2, 2),
        (1002, 2),
    ),
)
def test_get_opcode(instruction, expected):
    assert aoc.get_opcode(instruction) == expected


def test_get_modes():
    assert aoc.get_modes(1002) == {1: 0, 2: 1, 3: 0}
    assert aoc.get_modes(11002) == {1: 0, 2: 1, 3: 1}
    assert aoc.get_modes(1101) == {1: 1, 2: 1, 3: 0}


@pytest.mark.parametrize(
    ("memory", "address", "mode_value", "expected"),
    (
        ([1, 0, 0, 0, 99], 0, 0, 0),
        ([1, 0, 0, 0, 99], 0, 1, 1),
        ([1002, 3, 0, 3, 99], 2, 0, 1002),
        ([1002, 3, 0, 3, 99], 2, 1, 0),
    ),
)
def test_get_value_via_mode(memory: List, address: int, mode_value: int, expected: int):
    assert aoc.get_value_via_mode(memory, address, mode_value) == expected


def test_opcode_add():
    assert aoc.opcode_add([1, 2, 3, 4, 5], 0, {1: 0, 2: 0, 3: 0}) == 4


def test_opcode_multiply():
    assert aoc.opcode_add([1, 2, 3, 4, 5], 0, {1: 0, 2: 0, 3: 0}) == 4


# def test_opcode3():
#     memory = [1, 2, 3, 4, 5]
#     expected_value = 73
#     print(f"When prompted, please enter the integer {expected_value}.")
#     value = aoc.opcode3(memory, 0)
#     assert memory == [1, 2, expected_value, 4, 5]
#     assert value == 2


def test_opcode4():
    assert aoc.opcode4([1, 2, 3, 4, 5], 0) == (3, 2)


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
