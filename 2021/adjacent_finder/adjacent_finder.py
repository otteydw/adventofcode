import numpy as np


def adjacent_finder(npa, position, steps=1):
    """Find adjacent coordinates (including diagonals) in a 2d numpy array

    Args:
        npa (numpy array): An array to search through
        position (tuple): The (X, Y) coordinate to find adjacent neighbors of
        steps (int, optional): Max distance away from position to look. Defaults to 1.

    Returns:
        list: An unsorted list of tuples
    """
    # Modified from https://stackoverflow.com/questions/51657128/how-to-access-the-adjacent-cells-of-each-elements-of-matrix-in-python
    adjacent = []

    for dx in range(-steps, 1 + steps):
        for dy in range(-steps, 1 + steps):
            rangeX = range(0, npa.shape[0])
            rangeY = range(0, npa.shape[1])

            (newX, newY) = (position[0] + dx, position[1] + dy)

            if (newX in rangeX) and (newY in rangeY) and (dx, dy) != (0, 0):
                adjacent.append((newX, newY))

    return adjacent


if __name__ == "__main__":

    pass
