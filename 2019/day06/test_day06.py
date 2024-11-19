# test_aoc_template.py

import pathlib

import day06 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


# @pytest.fixture
# def example2():
#     puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
#     return aoc.parse(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly."""
    # assert example1 == {
    #     "COM": ["B"],
    #     "B": ["C", "G"],
    #     "C": ["D"],
    #     "D": ["E", "I"],
    #     "E": ["F", "J"],
    #     "G": ["H"],
    #     "J": ["K"],
    #     "K": ["L"],
    # }
    assert example1 == {
        "B": ["COM"],
        "C": ["B"],
        "D": ["C"],
        "E": ["D"],
        "F": ["E"],
        "G": ["B"],
        "H": ["G"],
        "I": ["D"],
        "J": ["E"],
        "K": ["J"],
        "L": ["K"],
    }


# def test_orbits_directly(example1):
#     assert aoc.orbits_directly(example1, "D", "C") is True
#     assert aoc.orbits_directly(example1, "L", "K") is True
#     assert aoc.orbits_directly(example1, "C", "D") is False

# def test_orbits_indirectly(example1):
#     assert aoc.orbits_indirectly(example1, "D", "C") is True
#     assert aoc.orbits_indirectly(example1, "C", "D") is False


def test_total_orbits_for_object(example1):
    assert aoc.total_orbits_for_object(example1, "D") == 3
    assert aoc.total_orbits_for_object(example1, "L") == 7
    assert aoc.total_orbits_for_object(example1, "COM") == 0


def total_orbits_in_map(example1):
    assert aoc.total_orbits_in_map(example1) == 42


# @pytest.mark.skip(reason="Not implemented")
# def test_part1_example1(example1):
#     """Test part 1 on example input."""
#     assert aoc.part1(example1) == ...


# @pytest.mark.skip(reason="Not implemented")
# def test_part2_example1(example1):
#     """Test part 2 on example input."""
#     assert aoc.part2(example1) == ...


# @pytest.mark.skip(reason="Not implemented")
# def test_part2_example2(example2):
#     """Test part 2 on example input."""
#     assert aoc.part2(example2) == ...
