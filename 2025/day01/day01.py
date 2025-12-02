import argparse
import pathlib


class Safe:
    def __init__(self, initial_value: int):
        self.value = initial_value

    def rotate(self, rotation: str) -> None:
        direction = 1
        if rotation[0] == "L":
            direction = -1

        distance = int(rotation[1:])

        self.value = (self.value + 100 + (direction * distance)) % 100


def parse(puzzle_input: str) -> list[str]:
    return [line for line in puzzle_input.splitlines()]


def part1(data: list[str]) -> int:
    safe = Safe(50)
    zero_counter = 0
    for operation in data:
        # print(f"{operation=}")
        safe.rotate(operation)
        # print(safe.value)
        if safe.value == 0:
            zero_counter += 1
    return zero_counter


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
