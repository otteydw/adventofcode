# test_aoc_template.py

import copy
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
        (
            [101, 4, 0, 0, 99],
            [105, 4, 0, 0, 99],
        ),  # literal 4 added to 101 from position 0 = 105 stored in position 0
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
    assert aoc.opcode_add([1, 2, 3, 4, 5], 0) == 4


def test_opcode_multiply():
    assert aoc.opcode_multiply([1, 2, 3, 4, 5], 0) == 4


def test_opcode3():
    memory = [1, 2, 3, 4, 5]
    expected_value = 73
    print(f"When prompted, please enter the integer {expected_value}.")
    value = aoc.opcode3(memory, 0)
    assert memory == [1, 2, expected_value, 4, 5]
    assert value == 2


def test_opcode4():
    # Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50.
    assert aoc.opcode4([4, 2, 3, 4, 5], 0) == (
        3,
        2,
    )  # Parameter mode. Output value 3 from position 2
    assert aoc.opcode4([104, 2, 3, 4, 5], 0) == (2, 2)  # Immediate mode. Output value 2 (position 2)


def test_opcode5():
    # Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the
    # second parameter. Otherwise, it does nothing.
    assert (
        aoc.opcode5([5, 1, 4, 7, 5], 0) == 5
    )  # Start pos 0. Value 1 from [Position 1 is non-zero. Set pointer to value 5 from position 4
    assert (
        aoc.opcode5([5, 4, 3, 7, 0], 0) == 3
    )  # Start pos 0. Value 0 from position 4 is zero. Set pointer to current plus 3.
    assert (
        aoc.opcode5([3, 5, 5, 3, 7, 0], 1) == 4
    )  # Start pos 1. Value 0 from position 5 is zero. Set pointer to current plus 3.
    assert (
        aoc.opcode5([3, 1105, 5, 3, 7, 0], 1) == 3
    )  # Immediate mode. Start pos 1. Value 5 from position 2 is non-zero. Set pointer to value 3 from position 3


def test_opcode6():
    # Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the
    # second parameter. Otherwise, it does nothing.
    assert (
        aoc.opcode6([6, 1, 4, 7, 9], 0) == 3
    )  # Start pos 0. Value 1 from position 1 is not zero.  Set pointer to current plus 2.
    assert (
        aoc.opcode6([6, 4, 3, 7, 0], 0) == 7
    )  # Start pos 0. Value 0 from position 4 is zero. Set pointer to value 7 from position 4.
    assert (
        aoc.opcode6([3, 1106, 0, 9, 7, 0], 1) == 9
    )  # Immediate mode. Start pos 1. Value 0 from position 2 is zero. Set pointer to value 9 from position 4.
    assert (
        aoc.opcode6([3, 1106, 1, 9, 7, 0], 1) == 4
    )  # Immediate mode. Start pos 1. Value 1 from position 2 is not zero. Set pointer to current plus 2.


@pytest.mark.parametrize(
    ("memory", "address", "expected_memory", "expected_pointer"),
    (
        (
            [7, 4, 5, 3, 1, 2, 3],
            0,
            [7, 4, 5, 1, 1, 2, 3],
            4,
        ),  # Val 1 from pos 4 is less than Val 2 from pos 5. Store 1 in position 3
        (
            [7, 4, 5, 3, 2, 1, 3],
            0,
            [7, 4, 5, 0, 2, 1, 3],
            4,
        ),  # Val 2 from pos 4 is not less than Val 1 from pos 5. Store 0 in position 3
        (
            [1107, 4, 5, 3, 2, 2, 3],
            0,
            [1107, 4, 5, 1, 2, 2, 3],
            4,
        ),  # Immediate mode. Val 4 from pos 1 is less than Val 5 from pos 2. Store 1 in position 3
        (
            [1107, 5, 4, 3, 1, 2, 3],
            0,
            [1107, 5, 4, 0, 1, 2, 3],
            4,
        ),  # Immediate mode. Val 5 from pos 1 is not less than Val 4 from pos 2. Store 0 in position 3
    ),
)
def test_opcode7(memory, address, expected_memory, expected_pointer):
    # Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given
    # by the third parameter. Otherwise, it stores 0.
    next_pointer = aoc.opcode7(memory, address)
    assert memory == expected_memory
    assert next_pointer == expected_pointer


@pytest.mark.parametrize(
    ("memory", "address", "expected_memory", "expected_pointer"),
    (
        (
            [8, 4, 5, 3, 1, 1, 3],
            0,
            [8, 4, 5, 1, 1, 1, 3],
            4,
        ),  # Val 1 from pos 4 is equal to Val 1 from pos 5. Store 1 in position 3
        (
            [8, 4, 5, 3, 2, 1, 3],
            0,
            [8, 4, 5, 0, 2, 1, 3],
            4,
        ),  # Val 2 from pos 4 is not equal to than Val 1 from pos 5. Store 0 in position 3
        (
            [1108, 4, 4, 3, 1, 2, 3],
            0,
            [1108, 4, 4, 1, 1, 2, 3],
            4,
        ),  # Immediate mode. Val 4 from pos 1 is equal to Val 4 from pos 2. Store 1 in position 3
        (
            [1108, 5, 4, 3, 2, 2, 3],
            0,
            [1108, 5, 4, 0, 2, 2, 3],
            4,
        ),  # Immediate mode. Val 5 from pos 1 is not euqual to Val 4 from pos 2. Store 0 in position 3
    ),
)
def test_opcode8(memory, address, expected_memory, expected_pointer):
    # Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by
    # the third parameter. Otherwise, it stores 0.
    next_pointer = aoc.opcode8(memory, address)
    assert memory == expected_memory
    assert next_pointer == expected_pointer


def test_day5b_1():
    # Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
    program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    print("When prompted, enter 7")
    diagnositc_code = aoc.run_program(program)
    assert diagnositc_code == 0

    program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    print("When prompted, enter 8")
    diagnositc_code = aoc.run_program(program)
    assert diagnositc_code == 1

    program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
    print("When prompted, enter 9")
    diagnositc_code = aoc.run_program(program)
    assert diagnositc_code == 0


def test_day5b_2():
    # Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
    program = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    print("When prompted, enter 7")
    diagnositc_code = aoc.run_program(program)
    assert diagnositc_code == 1

    program = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    print("When prompted, enter 8")
    diagnositc_code = aoc.run_program(program)
    assert diagnositc_code == 0

    program = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
    print("When prompted, enter 9")
    diagnositc_code = aoc.run_program(program)
    assert diagnositc_code == 0


def test_day5b_3():
    # Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
    program = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    print("When prompted, enter 7")
    diagnositc_code = aoc.run_program(program)
    assert diagnositc_code == 0

    program = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    print("When prompted, enter 8")
    diagnositc_code = aoc.run_program(program)
    assert diagnositc_code == 1

    program = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
    print("When prompted, enter 9")
    diagnositc_code = aoc.run_program(program)
    assert diagnositc_code == 0


def test_day5b_4():
    # Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
    program = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    print("When prompted, enter 7")
    diagnositc_code = aoc.run_program(program)
    assert diagnositc_code == 1

    program = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    print("When prompted, enter 8")
    diagnositc_code = aoc.run_program(program)
    assert diagnositc_code == 0

    program = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
    print("When prompted, enter 9")
    diagnositc_code = aoc.run_program(program)
    assert diagnositc_code == 0


def test_day5b_jump():
    # Here are some jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero:

    # position mode
    program = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    print("When prompted, enter 0")
    diagnositc_code = aoc.run_program(program)
    assert diagnositc_code == 0

    program = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
    print("When prompted, enter 1")
    diagnositc_code = aoc.run_program(program)
    assert diagnositc_code == 1

    # immediate mode
    program = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    print("When prompted, enter 0")
    diagnositc_code = aoc.run_program(program)
    assert diagnositc_code == 0

    program = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
    print("When prompted, enter 1")
    diagnositc_code = aoc.run_program(program)
    assert diagnositc_code == 1


def test_day5_part2():
    # The example program uses an input instruction to ask for a single number.
    # The program will then
    #   output 999 if the input value is below 8,
    #   output 1000 if the input value is equal to 8,
    #   or output 1001 if the input value is greater than 8.
    program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
               1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
               999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]  # fmt: skip

    program1 = copy.deepcopy(program)
    print("When prompted, enter 7")
    diagnositc_code = aoc.run_program(program1)
    assert diagnositc_code == 999

    program2 = copy.deepcopy(program)
    print("When prompted, enter 8")
    diagnositc_code = aoc.run_program(program2)
    assert diagnositc_code == 1000

    program3 = copy.deepcopy(program)
    print("When prompted, enter 9")
    diagnositc_code = aoc.run_program(program3)
    assert diagnositc_code == 1001


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
