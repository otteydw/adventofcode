import argparse
import pathlib
import re


def parse(puzzle_input):
    return [line for line in puzzle_input.splitlines()]


def part1(data):
    value = 0
    for row in data:
        muls = find_muls(row)
        for mul in muls:
            value += do_mul(mul)

    return value


def part2(data):
    pass


def do_mul(x: str) -> int:
    """Given string x in the form 'mul(###,###)', return an integer value of the two values multiplied together."""

    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    match = re.search(pattern, x)
    return int(match.group(1)) * int(match.group(2))


def find_muls(x: str) -> list[str]:
    """Given string x, return a list of valid mul values in the form
    ['mul(2,4)', 'mul(23,72)'] etc
    """
    # pattern = r"mul\(d{1,3}\,d{1,3}\)"
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, x)
    return matches


def solve(puzzle_input):
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
        for solution_number, solution in enumerate(solutions):
            print(f"Solution {solution_number}: {str(solution)}")
