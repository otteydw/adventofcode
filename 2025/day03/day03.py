import argparse
import pathlib


def parse(puzzle_input: str) -> list[str]:
    return [line for line in puzzle_input.splitlines()]


def largest_joltage(bank_int: int) -> int:
    bank = str(bank_int)

    first_digit = sorted(bank[:-1])[-1]
    index_of_first_digit = bank.index(first_digit)

    second_digit = sorted(bank[index_of_first_digit + 1 :])[-1]

    joltage = 10 * int(first_digit) + int(second_digit)
    return joltage


def part1(data: list[str]) -> int:
    total_joltage = 0
    for bank in data:
        total_joltage += largest_joltage(int(bank))

    return total_joltage


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
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        for solution_number, solution in enumerate(solutions, start=1):
            print(f"Solution {solution_number}: {str(solution)}")
