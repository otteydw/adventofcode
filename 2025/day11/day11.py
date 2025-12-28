import argparse
import pathlib
from pprint import pprint


def load_input(path: pathlib.Path) -> str:
    return pathlib.Path(path).read_text().strip()


def parse(puzzle_input: str) -> dict[str, list[str]]:
    lines = [line for line in puzzle_input.splitlines()]
    new_dict = {}
    for line in lines:
        key, value_str = line.split(": ")
        value = value_str.split(" ")
        new_dict[key] = value

    return new_dict


# def paths_to_target(data, source, destination, seen=None) -> int:
def paths_to_target(data: dict[str, list[str]], source: str, destination: str) -> int:
    # if seen is None:
    #     seen = []

    if destination in data[source]:
        return 1

    possible_path_count = 0
    # seen.append(source)
    for possible_step in data[source]:
        # possible_path_count += paths_to_target(data, possible_step, destination, seen)
        possible_path_count += paths_to_target(data, possible_step, destination)
    return possible_path_count


def part1(data: dict[str, list[str]]) -> int:
    pprint(data)
    return paths_to_target(data, source="you", destination="out")


def part2(data: dict[str, list[str]]) -> int:  # type: ignore[empty-body]
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
