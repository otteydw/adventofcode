import os

# import numpy as np


VALID_OPENING_CHARACTERS = ["(", "[", "{", "<"]
VALID_CLOSING_CHARACTERS = [")", "]", "}", ">"]
EXPECTED_CLOSERS = {"(": ")", "[": "]", "{": "}", "<": ">"}


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    with open(input_path, "r") as input_file:
        lines = input_file.readlines()
        lines = [line.rstrip() for line in lines]

    return lines


def syntax_checker_score(character):

    if character == ")":
        return 3
    elif character == "]":
        return 57
    elif character == "}":
        return 1197
    elif character == ">":
        return 25137
    else:
        return 0


def first_illegal_character(chunk):
    opener_stack = []

    for character in chunk:
        if character in VALID_OPENING_CHARACTERS:
            opener_stack.append(character)
        elif character == EXPECTED_CLOSERS[opener_stack[-1]]:
            opener_stack.pop()
        else:
            return character

    return None


def total_syntax_error_score(filename):
    lines = load_from_file(filename)

    total_score = 0

    for line in lines:
        total_score += syntax_checker_score(first_illegal_character(line))

    return total_score


if __name__ == "__main__":

    print(f"Part 1: {total_syntax_error_score('input.txt')}")
