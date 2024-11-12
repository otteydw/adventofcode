import argparse
import pathlib


def parse(puzzle_input):
    return [line for line in puzzle_input.split("\n")]


def part1(data):
    pass


def part2(data):
    pass


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solve Advent of Code puzzles")
    parser.add_argument("files", nargs="+", help="Input files to process")
    args = parser.parse_args()

    for path in args.files:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        for solution_number, solution in enumerate(solutions):
            print(f"Solution {solution_number}: {str(solution)}")
