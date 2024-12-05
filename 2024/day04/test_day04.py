# test_aoc_template.py

import pathlib

import day04 as aoc
import numpy as np
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


@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == ...


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 4


@pytest.mark.skip(reason="Not implemented")
def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc.part1(example2) == 18


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...


def test_search_in_row():
    assert aoc.search_in_row(["X" "M" "A" "S" "." "S"], "XMAS") == 1


def test_search_in_row_with_reverse():
    assert aoc.search_in_row(["X" "M" "A" "S" "." "S", "A", "M", "X"], "XMAS") == 2


def test_search_diagonals(example1):
    assert aoc.search_diagnals(example1, "XMAS") == 1


def test_part1_across():
    assert (
        aoc.part1(
            np.array(
                [
                    ["A", "B", "C"],
                    [".", ".", "."],
                    [".", ".", "."],
                ],
                dtype="<U1",
            ),
            search_string="ABC",
        )
        == 1
    )


def test_part1_across_reverse():
    assert (
        aoc.part1(
            np.array(
                [
                    ["C", "B", "A"],
                    [".", ".", "."],
                    [".", ".", "."],
                ],
                dtype="<U1",
            ),
            search_string="ABC",
        )
        == 1
    )


def test_part1_diagonal1():
    assert (
        aoc.part1(
            np.array(
                [
                    ["A", ".", "."],
                    [".", "B", "."],
                    [".", ".", "C"],
                ],
                dtype="<U1",
            ),
            search_string="ABC",
        )
        == 1
    )


def test_part1_diagonal2():
    assert (
        aoc.part1(
            np.array(
                [
                    [".", ".", "C"],
                    [".", "B", "."],
                    ["A", ".", "."],
                ],
                dtype="<U1",
            ),
            search_string="ABC",
        )
        == 1
    )


def test_part1_diagonal3():
    assert (
        aoc.part1(
            np.array(
                [
                    ["C", ".", "."],
                    [".", "B", "."],
                    [".", ".", "A"],
                ],
                dtype="<U1",
            ),
            search_string="ABC",
        )
        == 1
    )


def test_part1_down():
    assert (
        aoc.part1(
            np.array(
                [
                    ["C", ".", "."],
                    ["B", ".", "."],
                    ["A", ".", "."],
                ],
                dtype="<U1",
            ),
            search_string="ABC",
        )
        == 1
    )
    assert (
        aoc.part1(
            np.array(
                [
                    [".", ".", "."],
                    ["A", ".", "."],
                    [".", "B", "."],
                ],
                dtype="<U1",
            ),
            search_string="AB",
        )
        == 1
    )
