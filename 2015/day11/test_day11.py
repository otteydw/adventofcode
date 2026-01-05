import pathlib

import day11 as aoc
import pytest

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


def test_is_valid():
    assert not aoc.Password("hijklmmn").is_valid()
    assert not aoc.Password("abc").is_valid()
    assert not aoc.Password("abdc").is_valid()
    assert not aoc.Password("azdc").is_valid()
    assert aoc.Password("abcdffaa").is_valid()


def test_next_password():
    password = aoc.Password("a")
    password.next_password()
    assert password == "b"

    password = aoc.Password("az")
    password.next_password()
    assert password == "ba"


def test_next_valid():
    password = aoc.Password("abcdefgh")
    password.next_valid_password()
    assert password == "abcdffaa"

    password = aoc.Password("ghijklmn")
    password.next_valid_password()
    assert password == "ghjaabcc"
