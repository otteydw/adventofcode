import itertools
import pathlib
import sys

import numpy as np


def pattern_to_grid(pattern):
    grid = []
    for row in pattern:
        grid.append([character for character in row])

    return np.array(grid)


class Pattern:
    def __init__(self, pattern):
        self.pattern = pattern

    def __repr__(self):
        # output = ""
        # for row in self.pattern:
        #     output += row + "\n"

        # return output.strip()
        return str(self.pattern)

    def find_vertical_reflection(self):
        pattern_transposed = self.pattern.T

        return self.find_horizontal_reflection(pattern_transposed)

    def find_horizontal_reflection(self, pattern=None):
        if pattern is None:
            pattern = self.pattern
        reflection = None
        for i, row in enumerate(pattern):
            if i == 0:
                continue
            if np.array_equal(row, pattern[i - 1]):
                # if row == self.pattern[i-1]:
                above = pattern[:i]
                above_reversed = list(reversed(above))
                below = pattern[i:]
                # print(f"A: {above_reversed}")
                # print(f"B: {below}")

                if len(above) >= len(below):
                    if np.array_equal(below, above_reversed[: len(below)]):
                        # if below == above_reversed[:len(below)]:
                        reflection = i
                else:
                    if np.array_equal(above_reversed, below[: len(above_reversed)]):
                        # if above_reversed == below[:len(above_reversed)]:
                        reflection = i

        return reflection


def split_list(lst, val):
    return [
        list(group) for k, group in itertools.groupby(lst, lambda x: x == val) if not k
    ]


def parse(puzzle_input):
    lines = [line for line in puzzle_input.split("\n")]
    patterns = split_list(lines, "")
    return patterns


def part1(data):
    horizontals = []
    verticals = []
    for pattern in data:
        pattern = pattern_to_grid(pattern)
        this = Pattern(pattern)
        print(this)
        horizontal = this.find_horizontal_reflection()
        vertical = this.find_vertical_reflection()
        print(f"Hor: {horizontal}")
        print(f"Ver: {vertical}")
        # summary = 100 * horizontal + vertical
        # print(f"Sum: {summary}")
        if horizontal:
            horizontals.append(horizontal)
        if vertical:
            verticals.append(vertical)
        print()

    print(horizontals)
    print(verticals)
    summary = 100 * sum(horizontals) + sum(verticals)
    return summary


def part2(data):
    pass


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        for solution_number, solution in enumerate(solutions):
            print(f"Solution {solution_number}: {str(solution)}")
