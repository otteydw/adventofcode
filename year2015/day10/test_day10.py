import pathlib

from . import day10 as aoc

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


def test_look_and_say():
    assert aoc.look_and_say("1") == "11"
    assert aoc.look_and_say("11") == "21"
    assert aoc.look_and_say("21") == "1211"
    assert aoc.look_and_say("1211") == "111221"
    assert aoc.look_and_say("111221") == "312211"
