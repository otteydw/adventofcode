import argparse
import pathlib
from functools import lru_cache
from pprint import pprint


class Map:
    def __init__(self, data: dict[str, list[str]]) -> None:
        self.data = data

    @lru_cache(maxsize=None)
    def paths_to_target_part2(
        self, current: str, destination: str, seen_fft: bool = False, seen_dac: bool = False
    ) -> int:
        future = self.data[current] if current != "out" else ""
        print(f"{current=}, {destination=}, {seen_fft=}, {seen_dac=}, {future=}")

        if current == destination:
            # return 1

            if seen_fft and seen_dac:
                return 1
            else:
                return 0

        if current == "fft":
            seen_fft = True
        elif current == "dac":
            seen_dac = True

        possible_path_count = 0
        for possible_step in self.data[current]:
            possible_path_count += self.paths_to_target_part2(
                possible_step, destination, seen_fft=seen_fft, seen_dac=seen_dac
            )
        return possible_path_count


def load_input(path: pathlib.Path) -> str:
    return pathlib.Path(path).read_text().strip()


def parse(puzzle_input: str) -> dict[str, list[str]]:
    lines = [line for line in puzzle_input.splitlines()]
    new_dict = {}
    for line in lines:
        key, value_str = line.split(": ")
        value = value_str.split(" ")
        new_dict[key] = sorted(set(value))

    return new_dict


def paths_to_target(data: dict[str, list[str]], source: str, destination: str) -> int:
    if destination in data[source]:
        return 1

    possible_path_count = 0
    for possible_step in data[source]:
        possible_path_count += paths_to_target(data, possible_step, destination)
    return possible_path_count


def part1(data: dict[str, list[str]]) -> int:
    pprint(data)
    return paths_to_target(data, source="you", destination="out")


def part2(data: dict[str, list[str]]) -> int:
    pprint(data)
    map = Map(data)
    return map.paths_to_target_part2(current="svr", destination="out")


def solve(puzzle_input: str) -> tuple[int | None, int | None]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solve1 = True if "you" in data else False
    solve2 = True if "svr" in data else False
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
