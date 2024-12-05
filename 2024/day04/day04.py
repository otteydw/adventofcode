import argparse
import pathlib

import numpy as np


def parse(puzzle_input: str) -> np.array:
    list_of_lists = [[char for char in line] for line in puzzle_input.splitlines()]
    my_array = np.array(list_of_lists)
    return my_array


def search_in_row(row: list[str], search_string: str, reverse: bool = True) -> int:
    row_as_string = "".join(row)
    count = row_as_string.count(search_string)

    if reverse:
        reversed_search_string = search_string[::-1]
        count += row_as_string.count(reversed_search_string)

    return count


def search_diagnals(my_array: np.array, search_string: str, reverse: bool = True) -> int:
    """To search all diagonals of an array, we get all diagonals including the ones that do not begin
    on the top row. I needed a tip from ChatGPT for that tidbit!"""
    found = 0
    # flipped_array = np.fliplr(my_array)
    # reversed_search_string = search_string[::-1]

    # Received a tip from ChatGPT on this.
    rows, cols = my_array.shape
    for offset in range(-rows + 1, cols):
        diagonal = my_array.diagonal(offset)
        found += search_in_row(diagonal, search_string, reverse=reverse)

        # if reverse:
        #     found+=search_in_row(diagonal, reversed_search_string)

        # flipped_diagonal = flipped_array.diagonal(i)
        # found +=search_in_row(flipped_diagonal, search_string)

    return found


# def part1(data: np.array, search_string: str = 'XMAS') -> int:
#     """Rotate the array to get all permutations and search each row of each rotation for the string."""
#     my_array = data
#     found=0
#     for _ in range(4):

#         # Search each row ow this array
#         for row in my_array:
#             found+=search_in_row(row, search_string)

#         found += search_diagnals(my_array, search_string)
#         # Rotate the array for the next iteration
#         my_array = np.rot90(my_array)

#     return found


def part1(data: np.array, search_string: str = "XMAS") -> int:
    """Rotate the array to get all permutations and search each row of each rotation for the string."""
    my_array = data
    found = 0

    rotated_array = np.rot90(my_array)
    # flipped_array = np.flipud(my_array)
    # arrays_to_check = [my_array, rotated_array]

    for array_to_check in my_array, rotated_array:
        for row in array_to_check:
            found += search_in_row(row, search_string)
        found += search_diagnals(array_to_check, search_string)

    # found += search_diagnals(my_array, search_string)
    # found += search_diagnals(flipped_array, search_string)

    return found


def is_coordinate_in_grid(coordinate: tuple[int, int], grid: np.array) -> bool:
    """Given a coordinate in form of (row, column) return true if it is within the bounds of the array's shape"""
    rows, cols = grid.shape
    row, col = coordinate

    return (row >= 0) and (row <= rows - 1) and (col >= 0) and (col <= cols - 1)


def found_x(my_array: np.array, coordinate: tuple[int, int]) -> bool:
    # rows, cols = my_array.shape
    row, column = coordinate

    upper_left = (row - 1, column - 1)
    upper_right = (row - 1, column + 1)
    lower_left = (row + 1, column - 1)
    lower_right = (row + 1, column + 1)

    # Make sure all possible coordinates are inside the grid
    possible_coordinates = [upper_left, upper_right, lower_left, lower_right]
    if not all((is_coordinate_in_grid(possible_coordinate, my_array) for possible_coordinate in possible_coordinates)):
        return False

    upper_left_value = my_array[upper_left[0]][upper_left[1]]
    upper_right_value = my_array[upper_right[0]][upper_right[1]]
    lower_left_value = my_array[lower_left[0]][lower_left[1]]
    lower_right_value = my_array[lower_right[0]][lower_right[1]]

    leg1 = set([upper_left_value, lower_right_value])
    leg2 = set([lower_left_value, upper_right_value])

    return leg1 == leg2 == set(["M", "S"])


def coordinates_of_element_in_array(my_array: np.array, value: str) -> list[tuple[int, int]]:
    rows, cols = np.where(my_array == value)

    # Convert coordinates to a list of (row, col) tuples with standard Python integers
    coordinates = [(int(row), int(col)) for row, col in zip(rows, cols)]
    return coordinates


def part2(data: np.array) -> int:
    """Find the X-MAS in the array.  An X-MAS looks like this

    M.S
    .A.
    M.S

    """
    my_array = data
    found = 0

    # Loop through each of the four rotations
    # for _ in range(4):
    # Begin by finding all the "A" coordinates
    a_coordinates = coordinates_of_element_in_array(my_array, "A")
    print(f"{a_coordinates=}")
    # Iterate over the A values and look for X-MAS
    for a_coordinate in a_coordinates:
        print(f"{a_coordinate=}")
        if found_x(my_array, a_coordinate):
            found += 1
        # Then rotate the array
        # np.rot90(my_array)

    return found


def solve(puzzle_input: str) -> tuple[int | None, int | None]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solve1 = True
    solve2 = True
    solution1 = part1(data) if solve1 else None
    solution2 = part2(data) if solve2 else None

    return solution1, solution2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solve Advent of Code puzzles")
    parser.add_argument("files", nargs="+", help="Input files to process")
    args = parser.parse_args()

    for path in args.files:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        for solution_number, solution in enumerate(solutions):
            print(f"Solution {solution_number}: {str(solution)}")
