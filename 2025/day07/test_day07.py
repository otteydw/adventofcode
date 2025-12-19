import pathlib

import day07 as aoc
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


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 21


def test_quantum_array(example1):
    array = aoc.data_to_array(example1)
    quantum_array = aoc.QuantumArray(array)
    assert quantum_array.quantum((14, 1)) == 1
    assert quantum_array.quantum((13, 1)) == 2
    assert quantum_array.quantum((12, 2)) == 1
    assert quantum_array.quantum((11, 2)) == 4


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 40
