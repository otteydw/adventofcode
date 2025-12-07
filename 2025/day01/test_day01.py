# test_aoc_template.py

import pathlib

import day01 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_rotation():
    safe = aoc.Safe(5)
    safe.rotate("L10")
    assert safe.value == 95

    safe = aoc.Safe(5)
    safe.rotate("L210")
    assert safe.value == 95


def test_rotation_alt_method():
    safe = aoc.Safe(5, method="0x434C49434B")
    safe.rotate("L10")
    assert safe.value == 95
    assert safe.zero_counter == 1

    safe = aoc.Safe(50, method="0x434C49434B")
    safe.rotate("R1000")
    assert safe.value == 50
    assert safe.zero_counter == 10

    safe = aoc.Safe(50, method="0x434C49434B")
    safe.rotate("L1000")
    assert safe.value == 50
    assert safe.zero_counter == 10

    safe = aoc.Safe(74, method="0x434C49434B")
    safe.rotate("R28")
    assert safe.value == 2
    assert safe.zero_counter == 1

    safe = aoc.Safe(0, method="0x434C49434B")
    safe.rotate("L5")
    assert safe.value == 95
    assert safe.zero_counter == 0

    safe = aoc.Safe(0, method="0x434C49434B")
    safe.rotate("R14")
    assert safe.value == 14
    assert safe.zero_counter == 0

    safe = aoc.Safe(55, method="0x434C49434B")
    safe.rotate("L55")
    assert safe.value == 0
    assert safe.zero_counter == 1


@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ...


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 3


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 6


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...
