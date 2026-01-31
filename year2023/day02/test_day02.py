import pathlib

import pytest

from . import day02 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 8


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 2286


def test_match_parse():
    assert aoc.match_parse("3 blue, 4 red") == {"blue": 3, "red": 4}
    assert aoc.match_parse("1 green, 3 red, 6 blue") == {
        "blue": 6,
        "red": 3,
        "green": 1,
    }


def test_game_pasrse():
    assert aoc.game_parse("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == (
        1,
        [{"blue": 3, "red": 4}, {"green": 2, "red": 1, "blue": 6}, {"green": 2}],
    )
    assert aoc.game_parse("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red") == (
        4,
        [
            {"green": 1, "red": 3, "blue": 6},
            {"green": 3, "red": 6},
            {"green": 3, "blue": 15, "red": 14},
        ],
    )


def test_is_possible_game():
    assert aoc.is_possible_game(aoc.game_parse("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")[1])
    assert not aoc.is_possible_game(
        aoc.game_parse("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")[1]
    )


def test_find_minimum_cubes():
    assert aoc.find_minimum_cubes(aoc.game_parse("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")[1]) == {
        "red": 4,
        "green": 2,
        "blue": 6,
    }


def test_calculate_cube_set_power():
    assert aoc.calculate_cube_set_power({"red": 4, "green": 2, "blue": 6}) == 48
