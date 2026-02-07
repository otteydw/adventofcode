import pathlib

import pytest

from . import day07 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = aoc.load_input(PUZZLE_DIR / "example1.txt")
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = aoc.load_input(PUZZLE_DIR / "example2.txt")
    return aoc.parse(puzzle_input)


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 21


@pytest.fixture
def quantum_array(example1):
    array = aoc.data_to_array(example1)
    return aoc.QuantumArray(array)


@pytest.mark.parametrize(
    "coord, expected",
    [
        ((14, 1), 1),
        ((13, 1), 2),
        ((12, 2), 1),
        ((11, 2), 4),
    ],
)
def test_quantum_array(quantum_array, coord, expected):
    assert quantum_array.quantum(coord) == expected


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 40
