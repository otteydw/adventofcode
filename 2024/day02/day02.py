import argparse
import itertools
import pathlib


def parse(puzzle_input):
    return parse_to_int_grid(puzzle_input)


def part1(data):
    total_safe = sum([1 for row in data if is_safe(row)])
    return total_safe


def part2(data):
    total_safe = sum([1 for row in data if is_safe_with_dampener(row)])
    return total_safe


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
        return False

    for a, b in itertools.pairwise(lst):
        difference = abs(a - b)
        if difference < 1 or difference > 3:
            return False

    return True


def remove_nth_element(lst, n):
    """Removes the nth element from a list and returns a new list."""

    if n < 0 or n >= len(lst):
        return lst  # Return the original list if n is out of range

    return lst[:n] + lst[n + 1 :]


def is_safe_with_dampener(lst: list) -> bool:
    """The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in
    what would otherwise be a safe report. It's like the bad level never happened!

    Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report
    instead counts as safe."""

    # If the list is safe using original rules, return True
    if is_safe(lst):
        return True

    # Otherwise iterate through permutations of the list where the n'th element is removed and return True if a safe permutation is found.
    for idx in range(len(lst)):
        list_with_item_removed = remove_nth_element(lst, idx)
        if is_safe(list_with_item_removed):
            return True

    # Otherwise the list is still unsafe.
    return False


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
