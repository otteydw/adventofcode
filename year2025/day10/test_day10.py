import pathlib

import pytest

from . import day10 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


def test_to_list():
    assert aoc.to_list("(3)") == [3]
    assert aoc.to_list("(4,5)") == [4, 5]


@pytest.fixture
def example1():
    puzzle_input = aoc.load_input(PUZZLE_DIR / "example1.txt")
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = aoc.load_input(PUZZLE_DIR / "example2.txt")
    return aoc.parse(puzzle_input)


@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ...


# @pytest.mark.skip(reason="Not implemented")
def test_push():
    machine = aoc.Machine("[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}")
    machine.push((0, 1))
    machine.push((0, 2))
    assert machine.state_matches


def test_push_joltage():
    machine = aoc.Machine("[....] (3) (1,3) (2) (2,3) (0,2) (0,1) {0,1,2,3}")
    # print(machine)
    machine.joltage = [0, 1, 2, 3]
    machine.push_joltage((1, 3))
    # print(machine)
    assert machine.joltage == [0, 2, 2, 4]


def test_optimize_joltage():
    machine = aoc.Machine("[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}")
    assert machine.optimized_buttons_for_joltage() == 10


def test_fewest():
    machine = aoc.Machine("[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}")
    machine.find_fewest_pressed() == 2


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 7


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 33


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...
