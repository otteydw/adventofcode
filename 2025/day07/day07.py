import argparse
import pathlib
from functools import lru_cache

import numpy as np


def load_input(path: pathlib.Path) -> str:
    return pathlib.Path(path).read_text().strip()


def parse(puzzle_input: str) -> list[str]:
    return [line for line in puzzle_input.splitlines()]


def data_to_array(data: list[str]) -> np.ndarray:
    array = []
    for row in data:
        columns = []
        for character in row:
            columns.append(character)
        array.append(columns)
    array = np.array(array)
    return array


class Coordinate:
    def __init__(self, value: str) -> None:
        self.start = value == "S"
        self.splitter = value == "^"
        self.beam = self.start

    def __repr__(self) -> str:
        if self.start:
            return "S"
        elif self.splitter:
            return "^"
        elif self.beam:
            return "|"
        else:
            return "."


def part1(data: list[str]) -> int:
    array = data_to_array(data)
    array = np.vectorize(Coordinate, otypes=[object])(array)
    last_row = len(array) - 1
    splits = 0
    for row_num, row in enumerate(array):
        if row_num == last_row:
            break
        for col_num, coord in enumerate(row):
            if coord.beam and not coord.splitter:
                array[row_num + 1][col_num].beam = True
            elif coord.splitter and array[row_num - 1][col_num].beam:
                array[row_num + 1][col_num - 1].beam = True
                array[row_num + 1][col_num + 1].beam = True
                splits += 1
    return splits


class QuantumArray:
    def __init__(self, array: np.ndarray) -> None:
        self.array = array
        self.max_row = len(self.array) - 1

    @lru_cache(maxsize=None)
    def quantum(self, pos: tuple[int, int]) -> int:
        row_num, col_num = pos
        split = None
        for iter_row in range(row_num + 1, self.max_row):
            if self.array[iter_row][col_num] == "^":
                split = (iter_row, col_num)
                break
        if split is None:
            return 1

        left_pos = (split[0] + 1, col_num - 1)
        right_pos = (split[0] + 1, col_num + 1)

        left_splits = self.quantum(left_pos)
        right_splits = self.quantum(right_pos)
        return left_splits + right_splits


def part2(data: list[str]) -> int:
    array = data_to_array(data)
    quantum_array = QuantumArray(array)
    start = tuple(np.argwhere(array == "S")[0])
    return quantum_array.quantum(start)


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
