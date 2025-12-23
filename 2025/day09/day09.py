import argparse
import pathlib
from itertools import combinations
from sys import exit

import colorama
import numpy as np
from colorama import Fore
from skimage.segmentation import flood_fill

colorama.init(autoreset=True)

# def red_coordinates_to_array(coordinates: list[tuple[int,int]]) -> np.ndarray:
#     width = max(coordinate[0] for coordinate in coordinates) + 1 + 2
#     height = max(coordinate[1] for coordinate in coordinates) + 1 + 1
#     array = np.full((height, width), '.')
#     for coordinate in coordinates:
#         col,row = coordinate[0], coordinate[1]
#         array[row][col] = "#"
#     return array


def create_array(coordinates: list[tuple[int, int]]) -> np.ndarray:
    EMPTY_NUM = 0
    RED_NUM = 1
    GREEN_NUM = 2
    EMPTY_CHAR = "."
    RED_CHAR = "#"
    GREEN_CHAR = "X"

    # map_chars = ("X", "#", "W")
    # wall_chars = ("#", "W")
    width = max([coordinate[0] for coordinate in coordinates]) + 1 + 2
    height = max([coordinate[1] for coordinate in coordinates]) + 1 + 1
    # array = np.full((height, width), ".")
    array = np.full((height, width), EMPTY_NUM)
    idx_last_coordinate = len(coordinates) - 1
    for idx, coordinate in enumerate(coordinates):
        # print(f"Beginning {coordinate=}, {idx=}")
        col, row = coordinate[0], coordinate[1]
        # array[row][col] = "#"
        array[row][col] = RED_NUM

        if idx == idx_last_coordinate:
            next_coordinate = coordinates[0]
        else:
            next_coordinate = coordinates[idx + 1]

        if coordinate[0] == next_coordinate[0]:
            # columns are same. iterate across rows
            # print("cols same")
            sorted_rows = sorted([coordinate[1], next_coordinate[1]])
            for green_idx in range(sorted_rows[0] + 1, sorted_rows[1]):
                # array[green_idx][col] = "W"
                array[green_idx][col] = GREEN_NUM
        else:
            # rows are same. iterate across columns
            # print("rows same")
            sorted_cols = sorted([coordinate[0], next_coordinate[0]])
            for green_idx in range(sorted_cols[0] + 1, sorted_cols[1]):
                # array[row][green_idx] = "X"
                array[row][green_idx] = GREEN_NUM
    corner = (
        (min([coordinate[0] for coordinate in coordinates]) + 1 + 1),
        (min([coordinate[1] for coordinate in coordinates]) + 1 + 1),
    )
    # print(f"{corner=}")
    array = flood_fill(array, corner, GREEN_NUM)

    CONVERSION = {EMPTY_NUM: EMPTY_CHAR, RED_NUM: RED_CHAR, GREEN_NUM: GREEN_CHAR}

    array = array.astype(str)
    for num, char in CONVERSION.items():
        # print(f"{num=}, {char=}")
        array = np.where(array == str(num), char, array)
    # for row_idx, row in enumerate(array):
    #     # print(f"{row_idx=}")
    #     color_green=False
    # for char_idx, char in enumerate(row):
    #     if char == "W":
    #         color_green = not color_green
    #     elif char == "#" and (array[row_idx][char_idx - 1] in ('.',"X") or array[row_idx][char_idx + 1] in ('.',"X")):
    #         color_green = not color_green
    #     elif char != "X" and color_green:
    #         array[row_idx][char_idx] = "x"
    # flip=False
    # # if (
    # #     char == "W"
    # #     or (char == "#" and array[row_idx][char_idx + 1] == "." and "W" in array[row_idx][char_idx:])
    # #     or (char == "#" and array[row_idx][char_idx + 1] == "X")
    # # ):
    # #     color_green = not color_green
    # # elif color_green and char not in map_chars and (char_idx, row_idx) not in coordinates:
    # #     array[row_idx][char_idx] = 'x'
    # if not color_green:
    #     if char == "W" or char == "#" and array[row_idx][char_idx + 1] in (".", "X"):
    #         flip=True
    # else:
    #     if char == "W" or char == "#" and array[row_idx][char_idx - 1] in ('.', "X"):
    #         flip=True
    # if flip:
    #     color_green = not color_green
    # elif color_green:
    #     array[row_idx][char_idx] = "x"

    # if color_green:
    #     array[row_idx][char_idx] = "x"
    #     from collections import Counter

    #     if char == '.':
    #         left_counter = Counter(array[row_idx][:char_idx])
    #         right_counter = Counter(array[row_idx][char_idx+1:])
    #         left_count = sum(left_counter[letter] for letter in wall_chars)
    #         right_count = sum(right_counter[letter] for letter in wall_chars)
    #         left_even = left_count % 2
    #         right_even = right_count % 2
    #         # print(f"{left_counter=}, {right_counter=}")
    #         # print(f"{left_count=}, {right_count=}")
    #         if left_even != right_even:
    #             array[row_idx][char_idx] = "x"
    # if row_idx==4:
    #     break
    return array


def print_array(array: np.ndarray) -> None:
    for row in array:
        for col in row:
            if col == "#":
                col = Fore.RED + col
            elif col == "X" or col == "W":
                col = Fore.GREEN + col
            print(col, end="")
        print()


def load_input(path: pathlib.Path) -> str:
    return pathlib.Path(path).read_text().strip()


def parse(puzzle_input: str) -> list[tuple[int, int]]:
    data = []
    for line in puzzle_input.splitlines():
        members = line.split(",")
        x, y = [int(member) for member in members]
        data.append((x, y))
    return data


def area(coordinate1: tuple[int, int], coordinate2: tuple[int, int]) -> int:
    dimension1 = abs(coordinate1[0] - coordinate2[0]) + 1
    dimension2 = abs(coordinate1[1] - coordinate2[1]) + 1
    return dimension1 * dimension2


def part1(data: list[tuple[int, int]]) -> int:
    print(data)
    pairs = combinations(data, 2)
    max_area = 0
    for pair in pairs:
        max_area = max(area(*pair), max_area)
    return max_area


def part2(data: list[tuple[int, int]]) -> int:
    # array = red_coordinates_to_array(data)
    array = create_array(data)
    print_array(array)

    pairs = combinations(data, 2)
    # print(list(pairs)[0])

    max_area = 0
    for pair in pairs:
        current_area = area(*pair)
        print(f"Area of pair {pair} is {current_area}.")
        if current_area > max_area:
            col0, row0 = pair[0]
            col1, row1 = pair[1]
            row0, row1 = sorted([row0, row1])
            col0, col1 = sorted([col0, col1])
            subset = array[row0:row1, col0:col1]
            print(subset)
            valid_subset = np.all((subset == "#") | (subset == "X"))
            if valid_subset:
                max_pair = pair
                max_area = current_area
                if max_area == 50:
                    # print(subset)
                    exit()
    print(f"{max_pair=}")
    return max_area


def solve(puzzle_input: str) -> tuple[int | None, int | None]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solve1 = False
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
        puzzle_input = load_input(path)
        solutions = solve(puzzle_input)
        for solution_number, solution in enumerate(solutions, start=1):
            print(f"Solution {solution_number}: {str(solution)}")
