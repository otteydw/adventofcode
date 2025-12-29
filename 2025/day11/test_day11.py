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
    assert aoc.paths_to_target_part2(example2, "ggg", "out") == 0
    assert aoc.paths_to_target_part2(example2, "ggg", "out", seen=["aaa"]) == 0
    assert aoc.paths_to_target_part2(example2, "ggg", "out", seen=["dac"]) == 0
    assert aoc.paths_to_target_part2(example2, "ggg", "out", seen=["fft"]) == 0
    assert aoc.paths_to_target_part2(example2, "ggg", "out", seen=["dac", "fft"]) == 1
    assert aoc.paths_to_target_part2(example2, "ggg", "out", seen=["fft", "dac"]) == 1
    assert aoc.paths_to_target_part2(example2, "ggg", "out", seen=["fft", "aaa", "dac"]) == 1


def test_paths_to_target_part2_one_hop(example2):
    assert aoc.paths_to_target_part2(example2, "fff", "out", seen=["fft", "aaa", "dac"]) == 2


def test_paths_to_target_part2_begin_fft(example2):
    assert aoc.paths_to_target_part2(example2, "fft", "out") == 2


@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ...


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 5


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == ...


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == 2
