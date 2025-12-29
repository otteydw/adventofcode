import pathlib

import day11 as aoc
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


def test_paths_to_target_direct(example1):
    # fff: out
    assert aoc.paths_to_target(example1, "fff", "out") == 1


def test_paths_to_target_one_hop(example1):
    # ddd: ggg
    # ggg: out
    assert aoc.paths_to_target(example1, "ddd", "out") == 1


def test_paths_to_target_triple(example1):
    assert aoc.paths_to_target(example1, "ccc", "out") == 3


def test_paths_to_target_part2_direct(example2):
    map = aoc.Map(example2)
    assert map.paths_to_target_part2("ggg", "out") == 0


def test_paths_to_target_part2_begin_fft(example2):
    map = aoc.Map(example2)
    assert map.paths_to_target_part2("fft", "out") == 2


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 5


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == 2
