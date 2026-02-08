import pathlib

import pytest

from . import day21 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


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


def test_simulate_round():
    player = aoc.Player("Player", 8, 5, 5)
    boss = aoc.Player("Boss", 12, 7, 2)
    aoc.simulate_round(player, boss)
    assert boss.hp == 9
    assert player.hp == 6


def test_simulate_round_end():
    player = aoc.Player("Player", 8, 5, 5)
    boss = aoc.Player("Boss", 12, 7, 2)
    for _ in range(3):
        result = aoc.simulate_round(player, boss)
        assert result is None

    result = aoc.simulate_round(player, boss)
    assert result == "player"


def test_simulate_battle():
    player = aoc.Player("Player", 8, 5, 5)
    boss = aoc.Player("Boss", 12, 7, 2)

    assert aoc.simulate_battle(player, boss) == "player"


@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...
