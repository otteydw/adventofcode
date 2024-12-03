# test_aoc_template.py

import pathlib

import day03 as aoc
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


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 161


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == 48


def test_find_muls(example1):
    assert aoc.find_muls(example1) == ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]
    assert aoc.find_muls("mul(1234,1)") == []


def test_do_mul():
    assert aoc.do_mul("mul(23,111)") == 2553


def test_add_do_and_dont(example2):
    assert (
        aoc.add_do_and_dont(example2)
        == "do()xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))don't()"
    )


def test_find_do_sections():
    assert aoc.find_do_sections(
        "do()xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))don't()"
    ) == ["xmul(2,4)&mul[3,7]!^", "?mul(8,5))"]
