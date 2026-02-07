import os
from collections import defaultdict

import matplotlib.pyplot as plt


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


def graph_fuel_to_converge_on_positions(position_data):
    fuel_requirements = defaultdict(int)

    range_min = min(position_data)
    range_max = max(position_data)

    for position in range(range_min, range_max + 1):
        fuel_requirements[position] = fuel_to_converge_on_position(position_data, position)

    fig, ax = plt.subplots()
    ax.plot(fuel_requirements.keys(), fuel_requirements.values())
    ax.set(
        xlabel="Converge Position",
        ylabel="Fuel Required",
        title="Fuel Required to Converge on Position",
    )
    ax.grid()

    # fig.savefig("graph.png")
    plt.show()


if __name__ == "__main__":

    crab_positions = load_ints_from_file_line("input.txt")
    graph_fuel_to_converge_on_positions(crab_positions)
