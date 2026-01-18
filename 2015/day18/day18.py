import argparse
import itertools
import pathlib
from copy import copy

import numpy as np


def data_to_2d_grid(data: list[str]) -> np.ndarray:
    array = []
    for row in data:
        columns = []
        for character in row:
            columns.append(character)
        array.append(columns)
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


def load_input(path: pathlib.Path) -> str:
    return pathlib.Path(path).read_text().strip()


def parse(puzzle_input: str) -> list[str]:
    return [line for line in puzzle_input.splitlines()]


def process_lights(grid: np.ndarray) -> np.ndarray:
    GRID_HEIGHT = len(grid)
    GRID_WIDTH = len(grid[0])
    MAX_ROW = GRID_HEIGHT - 1
    MAX_COL = GRID_WIDTH - 1

    print(f"Grid size of {GRID_HEIGHT}x{GRID_WIDTH}")

    original_grid = copy(grid)

    for row_idx in range(GRID_HEIGHT):
        for column_idx in range(GRID_WIDTH):
            neighbors = surrounding_coordinates((row_idx, column_idx), False, (0, 0), (MAX_ROW, MAX_COL))
            on_neighbors = sum(1 if original_grid[neighbor[0]][neighbor[1]] == "#" else 0 for neighbor in neighbors)
            if original_grid[row_idx][column_idx] == "#":
                if on_neighbors not in [2, 3]:
                    grid[row_idx][column_idx] = "."
            else:
                if on_neighbors == 3:
                    grid[row_idx][column_idx] = "#"
    return grid


def part1(data: list[str], steps: int = 100) -> int:
    grid_array = data_to_2d_grid(data)
    print(grid_array)

    for _ in range(steps):
        grid_array = process_lights(grid_array)

    print(grid_array)
    return np.sum(grid_array == "#")


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
        puzzle_input = load_input(path)
        solutions = solve(puzzle_input)
        for solution_number, solution in enumerate(solutions, start=1):
            print(f"Solution {solution_number}: {str(solution)}")
