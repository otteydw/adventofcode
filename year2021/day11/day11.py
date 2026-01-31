import os

import numpy as np

from helpers.adjacent_finder import adjacent_finder


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


def flash(npa, coordinate):

    for adjacent in adjacent_finder.adjacent_finder(npa, coordinate):
        npa[adjacent] += 1


def one_step(npa):

    flash_count = 0
    flashed_this_step = set()

    # Add 1 to all
    npa += 1

    # Flash all >9
    coordinates_to_flash_count = float("inf")

    while coordinates_to_flash_count > 0:

        coordinates_greater_than_nine_array = np.where(npa > 9)
        coordinates_greater_than_nine_set = set(
            zip(
                coordinates_greater_than_nine_array[0],
                coordinates_greater_than_nine_array[1],
            )
        )
        coordinates_to_flash = coordinates_greater_than_nine_set - flashed_this_step
        coordinates_to_flash_count = len(coordinates_to_flash)

        for coordinate_to_flash in coordinates_to_flash:
            flash(npa, coordinate_to_flash)
            flashed_this_step.add(coordinate_to_flash)
            flash_count += 1

    # Reset all >9 to 0
    np.place(npa, npa > 9, 0)

    return flash_count


def step(npa, steps):

    flash_count = 0

    for _ in range(steps):
        flash_count += one_step(npa)

    return flash_count


def check_simultaneous_flash(npa):
    # Simultaneous flash is where all values are 0 after flashing
    return np.all(npa == 0)


def get_simultaneous_flash_step(npa):

    step_count = 0

    while not check_simultaneous_flash(npa):
        step_count += 1
        one_step(npa)

    return step_count


if __name__ == "__main__":

    octopus_array = load_into_array("input.txt")
    print(f"Part 1: {step(octopus_array, 100)}")

    octopus_array = load_into_array("input.txt")
    print(f"Part 2: {get_simultaneous_flash_step(octopus_array)}")
