import pathlib

import day19 as aoc
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


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    conversions, initial_string = example1
    assert conversions == {"H": set(["HO", "OH"]), "O": set(["HH"])}
    assert initial_string == "HOH"


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    conversions, initial_string = example1
    assert aoc.part1(conversions, initial_string) == 4
    assert aoc.part1(conversions, "HOHOHO") == 7


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == ...


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    conversions, medicine_molecule = example2
    assert aoc.part2(conversions, medicine_molecule) == 3
    assert aoc.part2(conversions, "HOHOHO") == 6


def test_part2_backwards_example2(example2):
    """Test part 2 on example input."""
    conversions, medicine_molecule = example2
    assert aoc.part2backwards(conversions, medicine_molecule) == 3
    assert aoc.part2backwards(conversions, "HOHOHO") == 6
