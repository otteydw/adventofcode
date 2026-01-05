import pathlib

import day11 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent


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
