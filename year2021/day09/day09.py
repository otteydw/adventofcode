import os

import numpy as np


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    with open(input_path, "r") as input_file:
        lines = input_file.readlines()
        lines = [line.rstrip() for line in lines]

    return lines


def load_into_array(filename):

    array = []

    lines = load_from_file(filename)

    for line in lines:
        array.append([int(letter) for letter in line])

    nparray = np.array(array)
    return nparray


def find_lows(npa):
    low_values = []
    for (x, y), value in np.ndenumerate(npa):
        if x > 0 and npa[x - 1, y] <= value:
            continue
        elif x < npa.shape[0] - 1 and npa[x + 1, y] <= value:
            continue
        elif y > 0 and npa[x, y - 1] <= value:
            continue
        elif y < npa.shape[1] - 1 and npa[x, y + 1] <= value:
            continue

        low_values.append(value)

    return low_values


def risk_level(height):
    return 1 + height


def risk_level_sums(npa):
    risk = 0
    for height in find_lows(npa):
        risk += risk_level(height)

    return risk


if __name__ == "__main__":

    array = load_into_array("input.txt")

    print(f"Part 1 - Risk Levels of Low Points: {risk_level_sums(array)}")
