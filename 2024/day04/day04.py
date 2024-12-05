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


def part2(data: np.array) -> int:  # type: ignore[empty-body]
    pass


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
