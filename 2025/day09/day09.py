import argparse
import pathlib
from itertools import combinations

# import numpy as np

# def data_to_array(data: list[str]) -> np.ndarray:
#     array = []
#     for row in data:
#         array.append(row.split(','))
#     array = np.array(array)
#     return array


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


def part2(data: list[tuple[int, int]]) -> int:  # type: ignore[empty-body]
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
