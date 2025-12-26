import argparse
import pathlib
from itertools import combinations

import colorama
import numpy as np
from colorama import Fore
from PIL import Image
from skimage.segmentation import flood_fill
from tqdm import tqdm

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
    # EMPTY_CHAR = "."
    # RED_CHAR = "#"
    # GREEN_CHAR = "X"

    # map_chars = ("X", "#", "W")
    # wall_chars = ("#", "W")
    width = max([coordinate[0] for coordinate in coordinates]) + 1 + 2
    height = max([coordinate[1] for coordinate in coordinates]) + 1 + 1
    # array = np.full((height, width), ".")
    # array = np.full((height, width), EMPTY_NUM)
    array = np.full((height, width), EMPTY_NUM, dtype=np.uint8)
    print(f"Created array of type {array.dtype} with shape {array.shape}")
    idx_last_coordinate = len(coordinates) - 1
    for idx, coordinate in enumerate(coordinates):
        col, row = coordinate[0], coordinate[1]
        # array[row][col] = "#"
        array[row][col] = RED_NUM

        if idx == idx_last_coordinate:
            next_coordinate = coordinates[0]
        else:
            next_coordinate = coordinates[idx + 1]

        if coordinate[0] == next_coordinate[0]:
            # columns are same. iterate across rows
            sorted_rows = sorted([coordinate[1], next_coordinate[1]])
            for green_idx in range(sorted_rows[0] + 1, sorted_rows[1]):
                # array[green_idx][col] = "W"
                array[green_idx][col] = GREEN_NUM
        else:
            # rows are same. iterate across columns
            sorted_cols = sorted([coordinate[0], next_coordinate[0]])
            for green_idx in range(sorted_cols[0] + 1, sorted_cols[1]):
                # array[row][green_idx] = "X"
                array[row][green_idx] = GREEN_NUM

    # fig, ax = plt.subplots()
    # print("Running imshow")
    # ax.imshow(array, cmap=plt.cm.gray)
    # ax.axis('scaled')
    # print("Running plt.show")
    # plt.show()
    # sys.exit()

    # print(f"Scaling down array of type {array.dtype} with shape {array.shape}.")
    # # Example: downscale by factor of 4
    # scaled = array[::4, ::4]
    # print(f"Scaled to array of type {scaled.dtype} with shape {scaled.shape}.")

    # save_image(scaled, filename="output_scaled.png")
    # save_image(array, filename="output.png")
    # sys.exit()

    # fill_begin = (
    #     (min([coordinate[0] for coordinate in coordinates]) + 1 + 1),
    #     (min([coordinate[1] for coordinate in coordinates]) + 1 + 1),
    # )
    fill_begin = (25000, 25000)  # CHEAT - HARDCODING THE START VALUE
    print(f"Image fill beginning on array of type {array.dtype} with shape {array.shape} at point {fill_begin}.")
    array = flood_fill(array, fill_begin, GREEN_NUM)
    print("Image fill complete.")

    # CONVERSION = {EMPTY_NUM: EMPTY_CHAR, RED_NUM: RED_CHAR, GREEN_NUM: GREEN_CHAR}

    # print("Converting type of array")
    # array = array.astype(str)
    # print("Converting items in array")
    # for num, char in CONVERSION.items():
    #     # print(f"{num=}, {char=}")
    #     array = np.where(array == str(num), char, array)
    # print("Done converting items in array.")

    return array


def print_array(array: np.ndarray) -> None:
    for row in array:
        for col in row:
            if col == "#" or col == 1:
                col = Fore.RED + str(col)
            elif col == "X" or col == "W" or col == 2:
                col = Fore.GREEN + str(col)
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


def save_image(array: np.ndarray, filename: str = "output.png") -> None:
    print(f"Saving image to {filename}")
    # # Define colors for 0, 1, 2
    # # 0 -> black (or white, your choice)
    # # 1 -> red
    # # 2 -> green
    # cmap = ListedColormap(["white", "red", "green"])
    # # plt.figure(figsize=(8, 8))
    # plt.imshow(array, cmap=cmap, interpolation="nearest")
    # plt.axis("off")
    # # plt.show()
    # plt.imsave(filename, array, cmap=cmap)

    # Create palette image
    img = Image.fromarray(array, mode="P")

    # Palette: 256 entries (RGB triplets)
    # palette = [
    #     0,
    #     0,
    #     0,  # 0 -> black
    #     255,
    #     0,
    #     0,  # 1 -> red
    #     0,
    #     255,
    #     0,  # 2 -> green
    # ] + [0, 0, 0] * (256 - 3)

    # Palette: 256 entries (RGB triplets)
    palette = [
        255,
        255,
        255,  # 0 -> white
        255,
        0,
        0,  # 1 -> red
        0,
        255,
        0,  # 2 -> green
    ] + [
        0,
        0,
        0,
    ] * (256 - 3)

    img.putpalette(palette)

    # new_size = (2000, 2000)  # (width, height)
    # resized = img.resize(new_size, resample=Image.NEAREST)
    # resized.save(filename, optimize=True)

    # Save
    img.save(filename, optimize=True)


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
    # save_image(array)
    # sys.exit()
    # # fig, ax = plt.subplots(ncols=1, figsize=(10, 5))
    # plt.imshow(array, cmap=plt.cm.gray)
    # plt.show()
    # sys.exit()

    if array.shape[0] < 100:
        print_array(array)

    pairs = combinations(data, 2)
    # print(list(pairs)[0])

    # max_area = 0

    # size = len(list(pairs))
    pairs = combinations(data, 2)
    best_areas = {}
    # for idx, pair in enumerate(pairs, start=1):
    for pair in tqdm(pairs):
        current_area = area(*pair)
        # print(f"Area of pair #{idx}/{size} {pair} is {current_area}.")
        best_areas[current_area] = pair
    # sys.exit()
    # for current_area, pair in tqdm(sorted(best_areas.items(), reverse=True)):

    items = sorted(best_areas.items(), reverse=True)
    with tqdm(items, desc="Processing areas") as pbar:
        for current_area, pair in pbar:
            pbar.set_postfix(
                area=current_area,
                pair=pair,
            )
            # print(f"Checking for validity of {pair} with area {current_area}")
            col0, row0 = pair[0]
            col1, row1 = pair[1]
            row0, row1 = sorted([row0, row1])
            col0, col1 = sorted([col0, col1])
            subset = array[row0:row1, col0:col1]
            # print(f"Subset type is {subset.dtype}")
            # valid_subset = np.all(subset != 0)
            # valid = not np.any(subset == 0)
            # valid_subset = subset.min() != 0
            # valid_subset=False

            # Check all edges for any "white"
            top = subset[0, :]
            bottom = subset[-1, :]
            left = subset[:, 0]
            right = subset[:, -1]
            valid = not (np.any(top == 0) or np.any(bottom == 0) or np.any(left == 0) or np.any(right == 0))
            if valid:
                print(f"max_pair is {pair}")
                return current_area
    return -1
    # print(f"{max_pair=}")
    # return max_area


# def part2_2(data: list[tuple[int, int]]) -> int:
#     array = create_array(data)

#     if array.shape[0] < 100:
#         print_array(array)

#     pairs = combinations(data, 2)
#     pairs = combinations(data, 2)
#     best_areas = {}

#     for pair in tqdm(pairs):
#         current_area = area(*pair)
#         best_areas[current_area] = pair

#     items = sorted(best_areas.items(), reverse=True)
#     with tqdm(items, desc="Processing areas") as pbar:
#         for current_area, pair in pbar:
#             pbar.set_postfix(
#                 area=current_area,
#                 pair=pair,
#             )

#             col0, row0 = pair[0]
#             col1, row1 = pair[1]
#             row0, row1 = sorted([row0, row1])
#             col0, col1 = sorted([col0, col1])


#             valid=None
#             if valid:
#                 print(f"max_pair is {pair}")
#                 return current_area


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
