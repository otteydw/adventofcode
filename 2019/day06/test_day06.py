# test_aoc_template.py

import pathlib

import day06 as aoc
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


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {
        "B": "COM",
        "C": "B",
        "D": "C",
        "E": "D",
        "F": "E",
        "G": "B",
        "H": "G",
        "I": "D",
        "J": "E",
        "K": "J",
        "L": "K",
    }


def test_total_orbits_for_object(example1):
    assert aoc.total_orbits_for_object(example1, "D") == 3
    assert aoc.total_orbits_for_object(example1, "L") == 7
    assert aoc.total_orbits_for_object(example1, "COM") == 0


def total_orbits_in_map(example1):
    assert aoc.total_orbits_in_map(example1) == 42


def test_get_object_orbited_by_object(example1, example2):
    assert aoc.get_object_orbited_by_object(example1, "D") == "C"
    assert aoc.get_object_orbited_by_object(example1, "L") == "K"

    assert aoc.get_object_orbited_by_object(example2, "YOU") == "K"
    assert aoc.get_object_orbited_by_object(example2, "SAN") == "I"

    assert aoc.get_object_orbited_by_object(example1, "COM") is None
    assert aoc.get_object_orbited_by_object(example2, "COM") is None


def test_orbit_tree(example2):
    assert aoc.orbit_tree(example2, "YOU") == ["YOU", "K", "J", "E", "D", "C", "B", "COM"]  # 8
    assert aoc.orbit_tree(example2, "SAN") == ["SAN", "I", "D", "C", "B", "COM"]  # 6
    assert aoc.orbit_tree(example2, "D") == ["D", "C", "B", "COM"]  # 4


def test_find_closest_common_ancestor(example2):
    assert aoc.find_closest_common_ancestor(example2, "YOU", "SAN") == "D"


def test_minimum_orbital_transfers_from_you_to_san(example2):
    assert aoc.minimum_orbital_transfers_from_you_to_san(example2) == 4


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
