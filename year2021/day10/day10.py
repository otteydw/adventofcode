import os
import statistics

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


def is_incomplete(chunk):
    return first_illegal_character(chunk) == None


def autocomplete_score(completion_string):

    total_score = 0

    for character in completion_string:
        if character == ")":
            score = 1
        elif character == "]":
            score = 2
        elif character == "}":
            score = 3
        elif character == ">":
            score = 4
        else:
            score = 0

        total_score = (total_score * 5) + score

    return total_score


def middle_autocomplete_score(filename):
    lines = load_from_file(filename)

    autocomplete_scores = []

    for line in lines:

        if is_incomplete(line):
            autocomplete_scores.append(autocomplete_score(find_completion_string(line)))

    return statistics.median(autocomplete_scores)


def find_completion_string(chunk):
    opener_stack = []
    expected_closer_stack = []

    for character in chunk:
        if character in VALID_OPENING_CHARACTERS:
            opener_stack.append(character)
            expected_closer_stack.append(EXPECTED_CLOSERS[character])
        elif character == expected_closer_stack[-1]:
            opener_stack.pop()
            expected_closer_stack.pop()

    closer_string = ""
    for character in reversed(expected_closer_stack):
        closer_string += character
    return closer_string


if __name__ == "__main__":

    print(f"Part 1: {total_syntax_error_score('input.txt')}")
    print(f"Part 2: {middle_autocomplete_score('input.txt')}")
