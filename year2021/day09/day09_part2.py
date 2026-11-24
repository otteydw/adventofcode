# mypy: ignore-errors
import os

import numpy as np
from scipy import ndimage


class LavaTube:
    def __init__(self, npa):
        self.array = npa

    def find_lows(self):
        """Find low points - the locations that are lower than any of its adjacent locations

        Returns:
            List: A list of heights at low points
        """
        low_values = []
        for (row, column), value in np.ndenumerate(self.array):
            row_above, row_below = row - 1, row + 1
            column_left, column_right = column - 1, column + 1

            # Compare to row above
            if row > 0 and self.array[row_above, column] <= value:
                continue
            # Compare to row below
            elif row < self.array.shape[0] - 1 and self.array[row_below, column] <= value:
                continue
            # Compare to column left
            elif column > 0 and self.array[row, column_left] <= value:
                continue
            # Compare to column right
            elif column < self.array.shape[1] - 1 and self.array[row, column_right] <= value:
                continue

            low_values.append(value)

        return low_values

    def product_largest_basins(self, number_of_basins=None):
        """The product of the largest basins

        Args:
            number_of_basins (int, optional): The number of largest basins to include. Defaults to None which includes all basins.

        Returns:
            int: The product of the "number_of_basins" largest basins
        """
        basin_sizes = self.find_size_of_basins()

        if number_of_basins is not None:
            basin_sizes = sorted(basin_sizes, reverse=True)[0:number_of_basins]

        return np.prod(basin_sizes)

    def find_size_of_basins(self):
        """Find the size of basins, where a basin consists of a group of tube heights that are less than 9

        Returns:
            List: A list of basin sizes
        """
        label, _ = ndimage.label(self.array < 9)
        basin_sizes = np.bincount(label.ravel())
        return list(basin_sizes)[1:]

    def risk_level(self, height):
        """Compute the risk level (1 plus the height)

        Args:
            height (int): The height of the lava tube

        Returns:
            int: The risk level
        """
        return 1 + height

    def risk_level_sums(self):
        """Computer the sum of all risk levels

        Returns:
            int: The sum of all risk levels
        """
        risk = 0
        for height in self.find_lows():
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
        array.append([int(character) for character in line])

    nparray = np.array(array)
    return nparray


if __name__ == "__main__":

    array = load_into_array("input.txt")
    tube = LavaTube(array)

    print(f"Part 1 - Risk Levels of Low Points: {tube.risk_level_sums()}")
    print(f"Part 2: Product of largest 3 basins: {tube.product_largest_basins(3)}")
