# test_aoc_template.py

import pathlib

import pytest

import day05 as aoc

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
    assert aoc.part1(example1) == 35


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 46


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...

def test_map_processing(example1):
    maps = aoc.extract_maps(example1[1:])
    # print(maps)
    assert maps['seed'].process(0) == 0
    assert maps['seed'].process(49) == 49
    assert maps['seed'].process(50) == 52
    assert maps['seed'].process(50) == 52
    assert maps['seed'].process(79) == 81
    assert maps['seed'].process(14) == 14
    assert maps['seed'].process(55) == 57
    assert maps['seed'].process(13) == 13

def test_process_seed(example1):
    maps = aoc.extract_maps(example1[1:])

    assert aoc.process_seed(maps, 79) == 82
    assert aoc.process_seed(maps, 14) == 43
    assert aoc.process_seed(maps, 55) == 86
    assert aoc.process_seed(maps, 13) == 35