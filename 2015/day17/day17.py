import argparse
import pathlib
from collections import defaultdict
from itertools import combinations
from typing import Any, Generator, Iterable


# Hopefully I will remember and use this generator in future AoC!
def non_empty_subsets(iterable: Iterable[Any]) -> Generator[Any]:
    items = list(iterable)
    for r in range(1, len(items) + 1):
        yield from combinations(items, r)


def load_input(path: pathlib.Path) -> str:
    return pathlib.Path(path).read_text().strip()


def parse(puzzle_input: str) -> list[int]:
    return sorted([int(line) for line in puzzle_input.splitlines()])


def part1(data: list[int], eggnog: int = 150) -> int:
    counter = 0
    for number_in_combination in range(1, len(data) + 1):
        for combo in combinations(data, number_in_combination):
            if sum(combo) == eggnog:
                counter += 1
    return counter


def part2(data: list[int], eggnog: int = 150) -> int:
    counter: dict[int, int] = defaultdict(int)
    for combo in non_empty_subsets(data):
        if sum(combo) == eggnog:
            counter[len(combo)] += 1
    minimum_containers = min(counter)
    return counter[minimum_containers]


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
