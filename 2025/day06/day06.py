import argparse
import math
import pathlib
import sys

import numpy as np


def parse(puzzle_input: str) -> list[str]:
    return [line for line in puzzle_input.splitlines()]


def data_to_array(data: list[str]) -> np.ndarray:
    array = []
    for row in data:
        array.append(row.split())
    array = np.array(array)
    return array


def part1(data: list[str]) -> int:
    grid_array = data_to_array(data)
    # print(grid_array)
    # return
    grid_array_t = grid_array.T
    total = 0
    for row in grid_array_t:
        operator = row[-1]
        operands = [int(x) for x in row[:-1]]
        print(f"{operator=}, {operands=}")
        if operator == "+":
            total += sum(operands)
        elif operator == "*":
            total += math.prod(operands)
        else:
            sys.exit("Unexpected operator!")
    return total


def part2(data: list[str]) -> int:  # type: ignore[empty-body]
    pass


def solve(puzzle_input: str) -> tuple[int | None, int | None]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    print(data)
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
