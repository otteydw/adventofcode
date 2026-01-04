import argparse
import pathlib
from collections import defaultdict
from itertools import permutations
from math import inf


def load_input(path: pathlib.Path) -> str:
    return pathlib.Path(path).read_text().strip()


def parse(puzzle_input: str) -> dict[str, dict[str, int]]:
    distances: defaultdict[str, dict[str, int]] = defaultdict(dict)
    for line in puzzle_input.splitlines():
        cities_str, distance_str = line.split(" = ")
        cities = cities_str.split(" to ")
        source = cities[0]
        destination = cities[1]
        distance = int(distance_str)

        distances[source][destination] = distance
        distances[destination][source] = distance
    return distances


def part1(data: dict[str, dict[str, int]]) -> int:
    all_cities = set(data.keys())
    # print(all_cities)

    all_path_permutations = permutations(all_cities)
    # print(list(all_path_permutations))

    min_distance = inf
    for path in all_path_permutations:
        this_distance = 0
        for idx in range(len(path) - 1):
            source_city = path[idx]
            destination_city = path[idx + 1]
            this_distance += data[source_city][destination_city]
        min_distance = min(this_distance, min_distance)
    return int(min_distance)


def part2(data: dict[str, dict[str, int]]) -> int:  # type: ignore[empty-body]
    pass


def solve(puzzle_input: str) -> tuple[int | None, int | None]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    print(data)
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
