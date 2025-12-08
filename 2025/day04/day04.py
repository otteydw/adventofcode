import argparse
import itertools
import pathlib

import numpy as np


def parse(puzzle_input: str) -> list[str]:
    return [line for line in puzzle_input.splitlines()]


def data_to_array(data: list[str]) -> np.ndarray:
    array = []
    for row in data:
        array.append([character for character in row])
    array = np.array(array)
    return array


def surrounding_coordinates(
    coordinate: tuple[int, int],
    inclusive: bool = False,
    min_coordinate: tuple[int, int] | None = None,
    max_coordinate: tuple[int, int] | None = None,
) -> list[tuple[int, int]]:
    x, y = coordinate
    possible_x = [x - 1, x, x + 1]
    possible_y = [y - 1, y, y + 1]
    possible_coordinates = list(itertools.product(possible_x, possible_y))
    if not inclusive:
        possible_coordinates.remove(coordinate)

    if min_coordinate:
        possible_coordinates = [
            coord for coord in possible_coordinates if coord[0] >= min_coordinate[0] and coord[1] >= min_coordinate[1]
        ]
    if max_coordinate:
        possible_coordinates = [
            coord for coord in possible_coordinates if coord[0] <= max_coordinate[0] and coord[1] <= max_coordinate[1]
        ]
    return possible_coordinates


def part1(data: list[str]) -> int:
    grid_array = data_to_array(data)
    shape = grid_array.shape
    max_coord = (shape[0] - 1, shape[1] - 1)
    counter = 0
    for index, value in np.ndenumerate(grid_array):
        if value == "@":
            values = []
            for coord in surrounding_coordinates(index, min_coordinate=(0, 0), max_coordinate=max_coord):
                if grid_array[coord] == "@":
                    values.append(coord)
            if len(values) < 4:
                counter += 1
    return counter


def part2(data: list[str]) -> int:  # type: ignore[empty-body]
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
        for solution_number, solution in enumerate(solutions, start=1):
            print(f"Solution {solution_number}: {str(solution)}")
