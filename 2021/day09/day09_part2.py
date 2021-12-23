import os
import numpy as np


class LavaTube:
    def __init__(self, npa):
        self.array = npa
        self.array_basin = np.full_like(self.array, False)
        self.lows = self.find_lows()

    def find_lows(self):
        low_values = []
        for (x, y), value in np.ndenumerate(self.array):
            if x > 0 and self.array[x - 1, y] <= value:
                continue
            elif x < self.array.shape[0] - 1 and self.array[x + 1, y] <= value:
                continue
            elif y > 0 and self.array[x, y - 1] <= value:
                continue
            elif y < self.array.shape[1] - 1 and self.array[x, y + 1] <= value:
                continue

            low_values.append(value)
            self.array_basin[x][y] = True

        return low_values

    def risk_level(self, height):
        return 1 + height

    def risk_level_sums(self):
        risk = 0
        for height in self.lows:
            risk += self.risk_level(height)

        return risk


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


if __name__ == "__main__":

    array = load_into_array("input.txt")
    tube = LavaTube(array)

    print(f"Part 1 - Risk Levels of Low Points: {tube.risk_level_sums()}")
