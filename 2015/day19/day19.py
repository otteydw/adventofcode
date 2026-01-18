import argparse
import pathlib
from collections import defaultdict


def load_input(path: pathlib.Path) -> str:
    return pathlib.Path(path).read_text().strip()


def parse(puzzle_input: str) -> tuple[dict[str, set[str]], str]:
    lines = puzzle_input.splitlines()
    initial_string = lines[-1]
    conversions = defaultdict(set)

    for line in lines[:-2]:
        from_string, to_string = line.split(" => ")
        conversions[from_string].add(to_string)

    return (conversions, initial_string)


def part1(data: tuple[dict[str, set[str]], str]) -> int:  # type: ignore[empty-body]
    pass


def part2(data: tuple[dict[str, set[str]], str]) -> int:  # type: ignore[empty-body]
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
