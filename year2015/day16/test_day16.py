import pathlib

from . import day16 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


def test_match2():
    sue = {}
    assert aoc.match_part2(sue)

    # "cars": 2,
    sue = {"cars": 2}
    assert aoc.match_part2(sue)

    sue = {"cars": 3}
    assert not aoc.match_part2(sue)

    sue = {"cars": 1}
    assert not aoc.match_part2(sue)

    # cats and trees readings indicates that there are greater than that many
    # "cats": 7,
    sue = {"cats": 8}
    assert aoc.match_part2(sue)

    sue = {"cats": 7}
    assert not aoc.match_part2(sue)

    sue = {"cats": 6}
    assert not aoc.match_part2(sue)

    # pomeranians and goldfish readings indicate that there are fewer than that many
    # "goldfish": 5,
    sue = {"goldfish": 6}
    assert not aoc.match_part2(sue)

    sue = {"goldfish": 5}
    assert not aoc.match_part2(sue)

    sue = {"goldfish": 4}
    assert aoc.match_part2(sue)

    # combos
    sue = {"cars": 2, "cats": 8}
    assert aoc.match_part2(sue)

    sue = {"cars": 3, "cats": 8}  # cars is wrong
    assert not aoc.match_part2(sue)

    sue = {"cars": 2, "cats": 7}  # cats is wrong
    assert not aoc.match_part2(sue)
