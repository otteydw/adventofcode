import itertools
import pathlib
import sys
import copy

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

    def find_vertical_reflection2(self):
        pattern_transposed = self.pattern.T

        return self.find_horizontal_reflection2(pattern_transposed)

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

    def find_horizontal_reflection2(self, pattern=None):
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
                if abs(len(above) - len(below)) <= 1:
                    print(f"Length above = {len(above)} | Length below = {len(below)}")
                    if len(above) >= len(below):
                    # if len(above) - len(below) <= 1
                        if np.array_equal(below, above_reversed[: len(below)]):
                            # if below == above_reversed[:len(below)]:
                            reflection = i
                    else:
                        if np.array_equal(above_reversed, below[: len(above_reversed)]):
                            # if above_reversed == below[:len(above_reversed)]:
                            reflection = i

        return reflection

    def get_height(self):
        return len(self.pattern)

    def get_width(self):
        return len(self.pattern[0])

    def get_dimensions(self):
        return (self.get_height(), self.get_width())

    def smudge(self, row, column):
        self.pattern[row][column] = '#' if self.pattern[row][column] == '.' else '.'

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
        print(this.get_dimensions())
        horizontal = this.find_horizontal_reflection2()
        vertical = this.find_vertical_reflection2()
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

def iterate_smudges(pattern):
    # print("Original")
    # print(pattern)
    rows, columns = pattern.get_dimensions()

    original_horizontal = pattern.find_horizontal_reflection()
    original_vertical = pattern.find_vertical_reflection()

    for row in range(rows):
        for column in range(columns):
            print('--------------------------------------------------------------------')
            print(f"Smudged {row+1}, {column+1}")
            pattern_copy = copy.deepcopy(pattern)
            pattern_copy.smudge(row, column)
            print(pattern_copy)
            print('Horizontal')
            horizontal = pattern_copy.find_horizontal_reflection2()
            # horizontal = pattern_copy.find_horizontal_reflection()
            print('Vertical')
            vertical = pattern_copy.find_vertical_reflection2()
            # vertical = pattern_copy.find_vertical_reflection()
            # horizontal = None
            # vertical = None
            print(f"Original: Horizontal: {original_horizontal} | Vertical: {original_vertical}")
            print(f"Current: Horizontal: {horizontal} | Vertical: {vertical}")
            if horizontal == original_horizontal:
                horizontal = None
            if vertical == original_vertical:
                vertical = None
            if horizontal is not None or vertical is not None:
                print(f"Returning {horizontal}, {vertical}")
                return(horizontal, vertical)

    print("I think we smudged everything and didn't find a valid one!")
    sys.exit(1)

def part2(data):
    horizontals = []
    verticals = []
    for pattern in data:
        pattern = pattern_to_grid(pattern)
        this = Pattern(pattern)
        print('Original pattern:')
        print(this)
        horizontal, vertical = iterate_smudges(this)
        print(f"Hor: {horizontal}")
        print(f"Ver: {vertical}")
        if horizontal:
            horizontals.append(horizontal)
        if vertical:
            verticals.append(vertical)
        print()

    # print(horizontals)
    # print(verticals)
    summary = 100 * sum(horizontals) + sum(verticals)
    return summary


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = None
    # solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        for solution_number, solution in enumerate(solutions):
            print(f"Solution {solution_number}: {str(solution)}")
