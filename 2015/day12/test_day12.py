import json
import pathlib

import day12 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


# @pytest.fixture
# def example1():
#     puzzle_input = aoc.load_input(PUZZLE_DIR / "example1.txt")
#     return aoc.parse(puzzle_input)


# @pytest.fixture
# def example2():
#     puzzle_input = aoc.load_input(PUZZLE_DIR / "example2.txt")
#     return aoc.parse(puzzle_input)


# @pytest.mark.skip(reason="Not implemented")
# def test_parse_example1(example1):
#     """Test that input is parsed properly."""
#     assert example1 == ...


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


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (
        ("[1,2,3]", 6),
        ('{"a":2,"b":4}', 6),
        ("[[[3]]]", 3),
        ('{"a":{"b":4},"c":-1}', 3),
        ('{"a":[-1,1]}', 0),
        ('[-1,{"a":1}]', 0),
        ("[]", 0),
        ("{}", 0),
        ('[1,{"c":"red","b":2},3]', 6),
    ),
)
def test_walk(input_s: str, expected: int) -> None:
    data = json.loads(input_s)
    assert aoc.walk(data) == expected


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (
        ("[1,2,3]", 6),
        ('[1,{"c":"red","b":2},3]', 4),
        ('{"d":"red","e":[1,2,3,4],"f":5}', 0),
        ('[1,"red",5]', 6),
    ),
)
def test_walk_ignore_red(input_s: str, expected: int) -> None:
    data = json.loads(input_s)
    assert aoc.walk(data, ignore_red=True) == expected
