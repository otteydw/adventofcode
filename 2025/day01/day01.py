import argparse
import pathlib


class Safe:
    def __init__(self, initial_value: int, method: str | None = None) -> None:
        self.value = initial_value
        self.method = method
        self.zero_counter = 0
        print(f"The dial starts by pointing at {self.value}.")

    def rotate(self, rotation: str) -> None:
        direction = 1
        if rotation[0] == "L":
            direction = -1
        distance = int(rotation[1:])

        if not self.method:
            self.value = (self.value + (direction * distance)) % 100
        elif self.method == "0x434C49434B":
            previous_value = self.value
            complete_revolutions, remaining_distance = divmod(distance, 100)
            self.value = (self.value + (direction * remaining_distance)) % 100
            this_zero_counter = complete_revolutions
            if (
                previous_value != 0
                and (direction == -1 and previous_value - remaining_distance <= 0 <= previous_value)
                or (direction == 1 and previous_value <= 100 <= previous_value + remaining_distance)
            ):
                this_zero_counter += 1
            self.zero_counter += this_zero_counter
            print(
                f"The dial is rotated {rotation} to point at {self.value}. During this rotation it points at zero {this_zero_counter} times."
            )


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


def part2(data: list[str]) -> int:
    safe = Safe(50, method="0x434C49434B")
    # zero_counter = 0
    for operation in data:
        # print(f"{operation=}")
        safe.rotate(operation)
        # print(safe.value)
    return safe.zero_counter


def solve(puzzle_input: str) -> tuple[int | None, int | None]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solve1 = False
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
