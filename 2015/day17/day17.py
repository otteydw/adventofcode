import argparse
import pathlib
from itertools import combinations


def load_input(path: pathlib.Path) -> str:
    return pathlib.Path(path).read_text().strip()


def parse(puzzle_input: str) -> list[int]:
    return sorted([int(line) for line in puzzle_input.splitlines()])


def part1(data: list[int], eggnog: int = 150) -> int:
    # print(data)

    counter = 0
    for number_in_combination in range(1, len(data) + 1):
        for combo in combinations(data, number_in_combination):
            # print(f"{combo=}, {sum(combo)=}")
            if sum(combo) == eggnog:
                # print("Increasing counter")
                counter += 1
    return counter


def part2(data: list[int]) -> int:  # type: ignore[empty-body]
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
