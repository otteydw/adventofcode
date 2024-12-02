import argparse
import itertools
import pathlib


def parse(puzzle_input):
    return parse_to_int_grid(puzzle_input)


def part1(data):
    total_safe = sum([1 for row in data if is_safe(row)])
    return total_safe


def part2(data):
    pass


def parse_to_int_grid(puzzle_input):
    """Parse a table of ints looking like
    7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9
    into a list of lists of ints
    """
    grid = [[int(val) for val in line.split()] for line in puzzle_input.split("\n")]
    return grid


def is_safe(lst: list) -> bool:
    """Given a list of integers, return True if safe or False is not.

    The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate
    levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the
    following are true:
        The levels are either all increasing or all decreasing.
        Any two adjacent levels differ by at least one and at most three.

    """
    sorted_asc = sorted(lst)
    sorted_desc = sorted(lst, reverse=True)

    if lst != sorted_asc and lst != sorted_desc:
        # print('Not sorted')
        return False
    # print('sorted')
    for a, b in itertools.pairwise(lst):
        difference = abs(a - b)
        # print(f"{difference=}")
        if difference < 1 or difference > 3:
            return False

    return True


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_to_int_grid(puzzle_input)
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
