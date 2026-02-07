# test_aoc_template.py

import pathlib

import pytest

from . import day13 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


# @pytest.fixture
# def example1_1():
#     puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
#     pattern = aoc.parse(puzzle_input)[0]
#     return aoc.Pattern(pattern)

# @pytest.fixture
# def example2():
#     puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
#     return aoc.parse(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
# def test_parse_example1(example1):
#     """Test that input is parsed properly."""
#     assert example1 == ...


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 405


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 400


# @pytest.mark.skip(reason="Not implemented")
# def test_part2_example2(example2):
#     """Test part 2 on example input."""
#     assert aoc.part2(example2) == ...
def test_horizontal_example1(example1):
    pattern0 = aoc.pattern_to_grid(example1[0])
    this0 = aoc.Pattern(pattern0)
    assert this0.find_horizontal_reflection() is None

    pattern1 = aoc.pattern_to_grid(example1[1])
    this1 = aoc.Pattern(pattern1)
    assert this1.find_horizontal_reflection() == 4


def test_vertical_example1(example1):
    pattern0 = aoc.pattern_to_grid(example1[0])
    this0 = aoc.Pattern(pattern0)
    assert this0.find_vertical_reflection() == 5

    pattern1 = aoc.pattern_to_grid(example1[1])
    this1 = aoc.Pattern(pattern1)
    assert this1.find_vertical_reflection() is None


def test_smudge_example1(example1):
    pattern0 = aoc.pattern_to_grid(example1[0])
    this0 = aoc.Pattern(pattern0)
    this0.smudge(0, 0)
    print(this0)
    assert this0.find_horizontal_reflection2() == 3
    assert this0.find_vertical_reflection2() == 5


@pytest.mark.skip(reason="Not implemented")
def test_iterate_smudges_example1(example1):
    pattern0 = aoc.pattern_to_grid(example1[0])
    this0 = aoc.Pattern(pattern0)
    horizontal, vertical = aoc.iterate_smudges(this0)
    assert horizontal == 3
    assert vertical is None

    pattern1 = aoc.pattern_to_grid(example1[1])
    this1 = aoc.Pattern(pattern1)
    horizontal, vertical = aoc.iterate_smudges(this1)
    assert horizontal == 1
    assert vertical is None
