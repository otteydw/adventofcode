import argparse
import pathlib
from pprint import pprint
from typing import Iterable

import numpy as np


def data_to_array(data: list[str]) -> np.ndarray:
    array = []
    for row in data:
        columns = []
        for character in row:
            columns.append(character)
        array.append(columns)
    array = np.array(array)
    return array


def split_by_seperator(iterable: Iterable[str], seperator: str = "") -> list[list[str]]:
    new_list: list[list[str]] = []

    sub_list: list[str] = []
    for item in iterable:
        if item == seperator:
            new_list.append(sub_list)
            sub_list = []
        else:
            sub_list.append(item)
    new_list.append(sub_list)
    return new_list


class Problem:
    def __init__(self, data: list[str]) -> None:
        # pprint(data)
        # print("done")
        full_data = split_by_seperator(data)
        gift_data = full_data[:-1]
        region_data = full_data[-1]
        # pprint(full_data)
        pprint(gift_data)
        pprint(region_data)
        self._init_gifts(gift_data)
        self._init_regions(region_data)

    def _init_gifts(self, data: list[list[str]]) -> None:
        self.gifts = []

        for line in data:
            gift_data = line[1:]
            gift_array = data_to_array(gift_data)
            self.gifts.append(gift_array)

    def _init_regions(self, data: list[str]) -> None:
        self.regions = []
        for line in data:
            dimensions_string, requirements_string = line.split(": ")
            width_str, length_str = dimensions_string.split("x")
            width = int(width_str)
            length = int(length_str)
            requirements = [int(x) for x in requirements_string.split(" ")]
            region = {"width": width, "length": length, "requirements": requirements}
            self.regions.append(region)

    def __repr__(self) -> str:
        out = "Gifts\n"
        for idx, gift in enumerate(self.gifts):
            out += f"{str(idx)}\n"
            out += str(gift)
            out += "\n"
        out += "\nRegions:\n"
        for region in self.regions:
            out += f"{region['width']}x{region['length']} {region['requirements']}\n"
        return out


def load_input(path: pathlib.Path) -> str:
    return pathlib.Path(path).read_text().strip()


def parse(puzzle_input: str) -> list[str]:
    # pprint(puzzle_input)
    # sys.exit()
    # lines = puzzle_input.splitlines()
    # pprint(lines)
    # sys.exit()
    return [line for line in puzzle_input.splitlines()]


def part1(data: list[str]) -> int:
    problem = Problem(data)
    print(problem)
    return 0


def part2(data: list[str]) -> int:  # type: ignore[empty-body]
    pass


def solve(puzzle_input: str) -> tuple[int | None, int | None]:
    """Solve the puzzle for the given input."""
    # pprint(puzzle_input)
    # sys.exit()
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
        puzzle_input = load_input(path)
        solutions = solve(puzzle_input)
        for solution_number, solution in enumerate(solutions, start=1):
            print(f"Solution {solution_number}: {str(solution)}")
