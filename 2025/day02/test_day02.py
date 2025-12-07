# test_aoc_template.py

import pathlib

import day02 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


def test_valid_id():
    assert not aoc.valid_id(11)
    assert not aoc.valid_id(22)
    assert not aoc.valid_id(99)
    assert not aoc.valid_id(1010)
    assert not aoc.valid_id(1188511885)
    assert not aoc.valid_id(222222)
    assert not aoc.valid_id(446446)
    assert not aoc.valid_id(38593859)

    assert aoc.valid_id(12)


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ...


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 1227775554


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...
