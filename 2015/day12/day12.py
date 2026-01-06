import argparse
import json
import pathlib
from typing import Any


def load_input(path: pathlib.Path) -> str:
    with open(path, "r") as f:
        return json.load(f)
    # return pathlib.Path(path).read_text().strip()


def parse(puzzle_input: str) -> list[str]:
    return [line for line in puzzle_input.splitlines()]


def walk(data: Any) -> int:
    # print(f"Received {data} of type {type(data)}")
    sum = 0
    if isinstance(data, list):
        for item in data:
            sum += walk(item)
    elif isinstance(data, dict):
        # print(f"Dict data is {data}")
        for key, value in data.items():
            sum += walk(key)
            sum += walk(value)
    elif isinstance(data, int):
        return data
    # elif data.isnumeric(data):
    #     return int(data)
    return sum


def part1(data: Any) -> int:
    return walk(data)


def part2(data: Any) -> int:  # type: ignore[empty-body]
    pass


def solve(data: Any) -> tuple[int | None, int | None]:
    """Solve the puzzle for the given input."""
    # data = parse(puzzle_input)
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
        # print(puzzle_input)
        solutions = solve(puzzle_input)
        for solution_number, solution in enumerate(solutions, start=1):
            print(f"Solution {solution_number}: {str(solution)}")
