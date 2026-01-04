import argparse
from itertools import groupby

# def load_input(path: pathlib.Path) -> str:
#     return pathlib.Path(path).read_text().strip()


# def parse(puzzle_input: str) -> list[str]:
#     return [line for line in puzzle_input.splitlines()]


def look_and_say(sequence: str) -> str:
    s = ""
    for char, group in groupby(sequence):
        count = len(list(group))
        # print(f"{char}: {count}")
        s += str(count) + str(char)
    return s


def part1(sequence: str) -> int:
    for _ in range(40):
        sequence = look_and_say(sequence)
    return len(sequence)


def part2(sequence: str) -> int:  # type: ignore[empty-body]
    pass


def solve(sequence: str) -> tuple[int | None, int | None]:
    """Solve the puzzle for the given input."""
    # data = parse(puzzle_input)
    solve1 = True
    solve2 = True
    solution1 = part1(sequence) if solve1 else None
    solution2 = part2(sequence) if solve2 else None

    return solution1, solution2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solve Advent of Code puzzles")
    parser.add_argument("sequence", nargs="+", help="Input sequence to process")
    args = parser.parse_args()

    # for path in args.files:
    sequence = args.sequence[0]
    print(f"{sequence}:")
    # puzzle_input = load_input(path)
    solutions = solve(sequence)
    for solution_number, solution in enumerate(solutions, start=1):
        print(f"Solution {solution_number}: {str(solution)}")
