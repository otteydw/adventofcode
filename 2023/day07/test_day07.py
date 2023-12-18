# test_aoc_template.py

import pathlib

import pytest

import day07 as aoc

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
    assert aoc.part1(example1) == 6440


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...


def test_get_cards():
    hand = aoc.Hand("32T3K")
    assert hand.cards == [3, 2, 10, 3, 13]


def test_cards_equal():
    hand1 = aoc.Hand("32T3K")
    hand2 = aoc.Hand("32T3K")
    hand3 = aoc.Hand("3293K")
    assert (hand1 == hand2) is True
    assert (hand2 == hand1) is True
    assert (hand1 == hand3) is False


def test_hand_value():
    hand1 = aoc.Hand("32T3K")
    hand2 = aoc.Hand("KK677")
    hand3 = aoc.Hand("KTJJT")
    hand4 = aoc.Hand("QQQJA")
    hand5 = aoc.Hand("QQQJQ")
    hand6 = aoc.Hand("QQQQQ")
    assert hand1.hand_value == 1
    assert hand2.hand_value == 2
    assert hand3.hand_value == 2
    assert hand4.hand_value == 3
    assert hand5.hand_value == 5
    assert hand6.hand_value == 6


def test_hand_value_jokers():
    hand1 = aoc.Hand("32T3K", jokers=True)
    hand2 = aoc.Hand("T55J5", jokers=True)
    hand3 = aoc.Hand("KK677", jokers=True)
    hand4 = aoc.Hand("KTJJT", jokers=True)
    hand5 = aoc.Hand("QQQJA", jokers=True)
    hand6 = aoc.Hand("QQQQQ", jokers=True)
    assert hand1.hand_value == 1  # one pair
    assert hand2.hand_value == 5  # four of a kind
    assert hand3.hand_value == 2  # two pair
    assert hand4.hand_value == 5  # four of a kind
    assert hand5.hand_value == 5  # four of a kind
    assert hand6.hand_value == 6  # five of a kind


def test_cards_lt():
    hand1 = aoc.Hand("32T3K")
    hand2 = aoc.Hand("KK677")
    hand3 = aoc.Hand("KTJJT")
    assert (hand1 < hand2) is True
    assert (hand2 < hand1) is False
    assert (hand2 < hand3) is False
    assert (hand3 < hand2) is True


def test_cards_gt():
    hand1 = aoc.Hand("32T3K")
    hand2 = aoc.Hand("KK677")
    hand3 = aoc.Hand("KTJJT")
    assert (hand1 > hand2) is False
    assert (hand2 > hand1) is True
    assert (hand2 > hand3) is True
    assert (hand3 > hand2) is False


def test_cards_gte():
    hand1 = aoc.Hand("32T3K")
    hand2 = aoc.Hand("32T3K")
    hand3 = aoc.Hand("KK677")
    assert (hand1 >= hand2) is True
    assert (hand2 >= hand1) is True
    assert (hand1 >= hand3) is False
    assert (hand3 >= hand1) is True


def test_cards_lt_jokers():
    assert (aoc.Hand("T55J5", jokers=True) < aoc.Hand("QQQJA", jokers=True)) is True
    assert (aoc.Hand("T55J5", jokers=True) < aoc.Hand("KTJJT", jokers=True)) is True
    assert (aoc.Hand("QQQJA", jokers=True) < aoc.Hand("KTJJT", jokers=True)) is True
    assert (aoc.Hand("32T3K", jokers=True) < aoc.Hand("KTJJT", jokers=True)) is True
    assert (aoc.Hand("32T3K", jokers=True) < aoc.Hand("KK677", jokers=True)) is True
