import json
import pathlib

import pytest

from . import day12 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


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
