# test_aoc_template.py

import pathlib

import pytest

import day14 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example1_tilted():
    puzzle_input = (PUZZLE_DIR / "example1_tilted.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example1_cycle1():
    puzzle_input = (PUZZLE_DIR / "example1_cycle1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example1_cycle2():
    puzzle_input = (PUZZLE_DIR / "example1_cycle2.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example1_cycle3():
    puzzle_input = (PUZZLE_DIR / "example1_cycle3.txt").read_text().strip()
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
    assert aoc.part1(example1) == 136


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 64


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...

def test_tilting(example1, example1_tilted):
    dish1 = aoc.Dish(example1)
    dish1_tilted = aoc.Dish(example1_tilted)
    # print(dish1)
    dish1.tilt()
    # print(dish1)
    # print()
    # print(dish1_tilted)

    # assert True
    assert dish1 == dish1_tilted

def test_cycle(example1, example1_cycle1, example1_cycle2, example1_cycle3):
    dish1 = aoc.Dish(example1)
    dish1_cycle1 = aoc.Dish(example1_cycle1)
    dish1_cycle2 = aoc.Dish(example1_cycle2)
    dish1_cycle3 = aoc.Dish(example1_cycle3)
    dish1.cycle()
    assert dish1 == dish1_cycle1
    dish1.cycle()
    assert dish1 == dish1_cycle2
    dish1.cycle()
    assert dish1 == dish1_cycle3