import itertools
import pathlib
import sys

import numpy as np

# from pprint import pprint as print


def parse(puzzle_input):
    return [line for line in puzzle_input.split("\n")]


def data_to_grid(data):
    grid = []
    for row in data:
        grid.append([character for character in row])

    return np.array(grid)


def find_no_galaxies(grid):
    grid = grid
    grid_transposed = grid.T

    no_galaxy_rows = []
    no_galaxy_columns = []
    for row_number, row in enumerate(grid):
        if "#" not in row:
            no_galaxy_rows.append(row_number)

    for column_number, column in enumerate(grid_transposed):
        if "#" not in column:
            no_galaxy_columns.append(column_number)

    return no_galaxy_rows, no_galaxy_columns


def expand_galaxies(grid, rows_to_expand, columns_to_expand):
    for insertion_number, row_to_insert in enumerate(rows_to_expand):
        grid = np.insert(grid, row_to_insert + insertion_number, ".", axis=0)

    for insertion_number, column_to_insert in enumerate(columns_to_expand):
        grid = np.insert(grid, column_to_insert + insertion_number, ".", axis=1)

    return grid


def find_galaxies(grid):
    arrays = np.where(grid == "#")
    return [(x, y) for x, y in zip(*arrays)]


def shortest_distance_between_points(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def shortest_distance_between_points2(a, b, expansion, expanded_rows, expanded_columns):
    low_row = min(a[0], b[0])
    high_row = max(a[0], b[0])

    low_column = min(a[1], b[1])
    high_column = max(a[1], b[1])

    rows_between = len([row for row in expanded_rows if low_row < row < high_row])
    columns_between = len([column for column in expanded_columns if low_column < column < high_column])

    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + ((expansion - 1) * (rows_between + columns_between))


def part1(data):
    grid = data_to_grid(data)
    no_galaxy_rows, no_galaxy_columns = find_no_galaxies(grid)

    grid = expand_galaxies(grid, no_galaxy_rows, no_galaxy_columns)

    galaxies = find_galaxies(grid)

    return sum([shortest_distance_between_points(x, y) for x, y in itertools.combinations(galaxies, 2)])


def part2(data, expansion=2):
    grid = data_to_grid(data)
    no_galaxy_rows, no_galaxy_columns = find_no_galaxies(grid)

    galaxies = find_galaxies(grid)

    return sum(
        [
            shortest_distance_between_points2(x, y, expansion, no_galaxy_rows, no_galaxy_columns)
            for x, y in itertools.combinations(galaxies, 2)
        ]
    )


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data, expansion=1000000)
    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        for solution_number, solution in enumerate(solutions):
            print(f"Solution {solution_number}: {str(solution)}")

    data = parse(puzzle_input)
    grid = data_to_grid(data)
