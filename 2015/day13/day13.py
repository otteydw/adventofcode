import argparse
import pathlib
from collections import defaultdict
from itertools import permutations
from pprint import pprint


def load_input(path: pathlib.Path) -> str:
    return pathlib.Path(path).read_text().strip()


def parse(puzzle_input: str) -> dict[str, dict[str, int]]:
    # Alice would gain 54 happiness units by sitting next to Bob.
    happiness: defaultdict[str, dict[str, int]] = defaultdict(dict)
    for line in puzzle_input.splitlines():
        line_split = line.split()
        person1 = line_split[0]
        person2 = line_split[-1].removesuffix(".")
        direction = 1 if line_split[2] == "gain" else -1
        value = direction * int(line_split[3])
        happiness[person1][person2] = value
    return happiness


def part1(happiness: dict[str, dict[str, int]]) -> int:
    # pprint(happiness)
    people = happiness.keys()
    pprint(people)
    max_happiness = 0
    people_count = len(people)
    for order in permutations(people):
        # full_cycle = list(order) + [order[0]]
        # print(full_cycle, end='')
        # print(order, end="")
        total_happiness = 0
        for idx in range(people_count):
            before = order[-1] if idx == 0 else order[idx - 1]
            current = order[idx]
            after = order[0] if idx == people_count - 1 else order[idx + 1]
            total_happiness += happiness[current][before]
            total_happiness += happiness[current][after]
        # print(f" {total_happiness=}")
        max_happiness = max(total_happiness, max_happiness)
    return max_happiness


def part2(happiness: dict[str, dict[str, int]]) -> int:
    # pprint(happiness)
    people = list(happiness.keys())
    # print(people)
    for person in people:
        happiness[person]["Me"] = 0
        happiness["Me"][person] = 0
    # pprint(happiness)
    return part1(happiness)


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
