import argparse
from itertools import groupby


def look_and_say(sequence: str) -> str:
    s = ""
    for char, group in groupby(sequence):
        count = len(list(group))
        s += str(count) + str(char)
    return s


def part1(sequence: str) -> int:
    for _ in range(40):
        sequence = look_and_say(sequence)
    return len(sequence)


def part2(sequence: str) -> int:
    for _ in range(50):
        sequence = look_and_say(sequence)
    return len(sequence)


def solve(sequence: str) -> tuple[int | None, int | None]:
    """Solve the puzzle for the given input."""
    solve1 = True
    solve2 = True
    solution1 = part1(sequence) if solve1 else None
    solution2 = part2(sequence) if solve2 else None

    return solution1, solution2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solve Advent of Code puzzles")
    parser.add_argument("sequence", help="Input sequence to process")
    args = parser.parse_args()

    sequence = args.sequence
    print(f"{sequence}:")
    solutions = solve(sequence)
    for solution_number, solution in enumerate(solutions, start=1):
        print(f"Solution {solution_number}: {str(solution)}")
