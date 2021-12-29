import numpy as np
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from adjacent_finder import adjacent_finder


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
    # print(f"Flashing around coordinate {coordinate}")

    for adjacent in adjacent_finder.adjacent_finder(npa, coordinate):
        npa[adjacent] += 1


# def one_stepb(npa):

#     npa += 1
#     npa = np.where(npa >= 9, npa+1, npa)
#     return npa

# def one_stepc(npa):
#     # Add 1 to all
#     npa += 1

#     flashed_this_step = np.where(npa >= 0, False, True)
#     print(flashed_this_step)
#     # Flash all >=9
#     coordinates_greater_than_nine = np.where(npa >= 9, True, False)
#     print(coordinates_greater_than_nine)
#     # new_npa = np.where(coordinates_greater_than_nine == True and flashed_this_step == False, npa+1, npa)
#     new_npa = np.all(coordinates_greater_than_nine == True and flashed_this_step == False, npa+1, npa)
#     print(new_npa)

#     # print(type(new_npa))


def one_step(npa):

    flash_count = 0
    flashed_this_step = set()

    # Add 1 to all
    npa += 1

    # Flash all >9
    coordinates_greater_than_nine_array = np.where(npa > 9)
    coordinates_greater_than_nine_set = set(zip(coordinates_greater_than_nine_array[0], coordinates_greater_than_nine_array[1]))

    # for coordinate_greater_than_nine in coordinates_greater_than_nine_set:
    #     if coordinate_greater_than_nine not in flashed_this_step:
    #             flashed_this_step.add(coordinate_greater_than_nine)
    #             flash(npa, coordinate_greater_than_nine)

    # coordinates_to_flash = coordinates_greater_than_nine_set - flashed_this_step
    # # print(f"Flashing coordinates: {coordinates_to_flash}")
    # for coordinate_to_flash in coordinates_to_flash:
    #     flash(npa, coordinate_to_flash)
    #     flashed_this_step.add(coordinate_to_flash)
    #     flash_count += 1

    coordinates_to_flash = coordinates_greater_than_nine_set - flashed_this_step

    while len(coordinates_to_flash) > 0:
        for coordinate_to_flash in coordinates_to_flash:
            flash(npa, coordinate_to_flash)
            flashed_this_step.add(coordinate_to_flash)
            flash_count += 1
        coordinates_greater_than_nine_array = np.where(npa > 9)
        coordinates_greater_than_nine_set = set(zip(coordinates_greater_than_nine_array[0], coordinates_greater_than_nine_array[1]))
        coordinates_to_flash = coordinates_greater_than_nine_set - flashed_this_step

    # Reset to 0
    np.place(npa, npa>9, 0)

    return flash_count

def step(npa, steps):

    flash_count = 0

    for step in range(steps):
        flash_count += one_step(npa)
        print(f"After step {step+1}")
        print(npa)

    return flash_count

# def one_step(npa):

#     # Add 1
#     npa += 1

#     flashed_this_step = set()

#     # Flash all >=9
#     coordinates_greater_than_nine = np.where(npa >= 9)
#     print(coordinates_greater_than_nine)

#     while len(coordinates_greater_than_nine) > 0:
#         for coordinate_greater_than_nine in coordinates_greater_than_nine:
#             if coordinate_greater_than_nine not in flashed_this_step:
#                 flashed_this_step.add(coordinate_greater_than_nine)
#                 flash(npa, coordinate_greater_than_nine)
#         coordinates_greater_than_nine = np.where(npa >= 9)



#     print(npa)
#     count_of_nines = np.sum(npa == 9)
#     print(f"Count of nines: {count_of_nines}")
#     while count_of_nines > 0:
#         print("Flashing onces")
#         # Find all the coordinates of 9s
#         coordinates_of_nines = np.where(npa == 9)
#         # print("coordinates of nines")
#         # print(coordinates_of_nines)
#         # Find the coordinates of all neighbors of nines
#         coordinates_to_flash = set(coordinates_of_nines)
#         for coordinate in coordinates_of_nines:
#             coordinates_to_flash += adjacent_finder(npa, coordinate)

#         # Do the flash around every 9
#         for coordinate_to_flash in coordinates_to_flash:
#             flash(npa, coordinate_to_flash)

#         # Recount how many nines there are now
#         count_of_nines = np.sum(npa == 9)

#     # Reset to 0
#     np.place(npa, npa>=9, 0)
#     # print(np.sum(npa == 9))

if __name__ == "__main__":

    octopus_array = load_into_array("input.txt")
    print(f"Part 1: {step(octopus_array, 100)}")