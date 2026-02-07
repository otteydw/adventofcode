# test_aoc_template.py

import pathlib

import pytest

from . import day03 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


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


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 4361


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 467835


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...


def test_create_schematic(example1):
    schematic = aoc.create_schematic(example1)
    assert isinstance(schematic[0][0], aoc.Part)
    assert schematic[0][0].row == 0
    assert schematic[0][0].start_column == 0
    assert schematic[0][0].end_column == 2
    assert schematic[0][0].number == 467

    assert isinstance(schematic[9][5], aoc.Part)
    assert schematic[9][5].row == 9
    assert schematic[9][5].start_column == 5
    assert schematic[9][5].end_column == 7
    assert schematic[9][5].number == 598

    assert not isinstance(schematic[8][5], aoc.Part)
    assert not isinstance(schematic[0][3], aoc.Part)


def test_get_surrounding_positions(example1):
    schematic = aoc.create_schematic(example1)
    assert aoc.get_surrounding_positions(0, 0, schematic) == set([(1, 0), (0, 1), (1, 1)])


def test_get_part_numbers(example1):
    schematic = aoc.create_schematic(example1)
    assert sorted(aoc.get_part_numbers(schematic)) == sorted([467, 35, 633, 617, 592, 755, 664, 598])
