import os
from collections import defaultdict


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    with open(input_path, "r") as input_file:
        lines = input_file.readlines()
        lines = [line.rstrip() for line in lines]

    return lines


def load_ints_from_file_line(filename):
    data_as_string = load_from_file(filename)[0].split(",")
    data_as_ints = [int(x) for x in data_as_string]
    return data_as_ints


def fuel_to_converge_on_position(position_data, position_to_converge):

    total_fuel = 0

    for crab_position in position_data:
        total_fuel += abs(crab_position - position_to_converge)

    return total_fuel


def least_fuel_to_converge(position_data):

    least_fuel = float("inf")

    range_min = min(position_data)
    range_max = max(position_data)

    for position in range(range_min, range_max + 1):
        least_fuel = min(
            least_fuel, fuel_to_converge_on_position(position_data, position)
        )

    return least_fuel


if __name__ == "__main__":

    crab_positions = load_ints_from_file_line("input.txt")
    print(f"Part 1: Least fuel to converge: {least_fuel_to_converge(crab_positions)}")
