import os
from collections import defaultdict
import itertools


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    with open(input_path, "r") as input_file:
        lines = input_file.readlines()
        lines = [line.rstrip() for line in lines]

    return lines


def parse_input(filename):

    input_strings = load_from_file(filename)

    unique_signal_patterns = []
    output_values = []

    for line in input_strings:
        unique_signal_pattern_string, output_value_string = line.split(" | ")
        unique_signal_pattern = unique_signal_pattern_string.split()
        output_value = output_value_string.split()

        unique_signal_patterns.append(unique_signal_pattern)
        output_values.append(output_value)

    return unique_signal_patterns, output_values


def what_integer(value):

    count_of_letters = defaultdict(int)
    for letter in value:
        count_of_letters[letter] += 1
    unique_number_of_segments = len(count_of_letters)

    if unique_number_of_segments == 2:
        return 1
    elif unique_number_of_segments == 4:
        return 4
    elif unique_number_of_segments == 3:
        return 7
    elif unique_number_of_segments == 7:
        return 8
    else:
        return -1


def count_digits(values_to_search, integers_to_match):

    matching_count = 0

    for value_to_search in itertools.chain.from_iterable(values_to_search):
        this_integer = what_integer(value_to_search)
        if this_integer in integers_to_match:
            matching_count += 1

    return matching_count


if __name__ == "__main__":

    _, output_values = parse_input("input.txt")

    print(f"Part 1: {count_digits(output_values, [1,4,7,8])}")
