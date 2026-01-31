import pathlib

import pytest

from . import day06 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = aoc.load_input(PUZZLE_DIR / "example1.txt")
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = aoc.load_input(PUZZLE_DIR / "example2.txt")
    return aoc.parse(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = aoc.load_input(PUZZLE_DIR / "example3.txt")
    return aoc.parse(puzzle_input)


@pytest.fixture
def example4():
    puzzle_input = aoc.load_input(PUZZLE_DIR / "example4.txt")
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ["123 328  51 64 ", " 45 64  387 23 ", "  6 98  215 314", "*   +   *   +  "]


def test_parse_example2(example2):
    """Test that input is parsed properly."""
    assert example2 == ["411", "126", "836", "3  ", "*  "]


def test_parse_example3(example3):
    """Test that input is parsed properly."""
    assert example3 == ["   9", "  79", " 891", "8392", "+   "]


def test_parse_example4(example4):
    """Test that input is parsed properly."""
    assert example4 == ["   9 411", "  79 126", " 891 836", "8392 3  ", "+    *  "]


def test_d2a_example2():
    original_array = ["411", "126", "836", "3  ", "*  "]
    expected_output = [
        ["4", "1", "1"],
        ["1", "2", "6"],
        ["8", "3", "6"],
        ["3", " ", " "],
        ["*", " ", " "],
    ]
    assert (aoc.data_to_array_p2(original_array) == expected_output).all()


def test_d2a_example4():
    original_array = ["   9 411", "  79 126", " 891 836", "8392 3  ", "+    *  "]
    expected_output = [
        [" ", " ", " ", "9", " ", "4", "1", "1"],
        [" ", " ", "7", "9", " ", "1", "2", "6"],
        [" ", "8", "9", "1", " ", "8", "3", "6"],
        ["8", "3", "9", "2", " ", "3", " ", " "],
        ["+", " ", " ", " ", " ", "*", " ", " "],
    ]
    assert (aoc.data_to_array_p2(original_array) == expected_output).all()


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 4277556


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 3263827
