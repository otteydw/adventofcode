import pathlib
import sys
import itertools

import numpy as np

def split_list(lst, val):
    return [
        list(group) for k, group in itertools.groupby(lst, lambda x: x == val) if not k
    ]

def parse(puzzle_input):
    # return [line for line in puzzle_input.split("\n")]
    lines = [line for line in puzzle_input.split("\n")]
    return lines
    # return split_list(lines, "")

class Dish:
    def __init__(self, grid):
        # print(grid)

        self.grid = []
        for row in grid:
            self.grid.append([character for character in row])
        self.grid = np.array(self.grid)

    def __repr__(self):
        # return str(self.grid)
        output=''
        for row in self.grid:
            for character in row:
                output += character
            output+='\n'
        return output

    def __eq__(self, other):
        return np.array_equiv(self.grid, other.grid)
        # return (self.grid == other.grid).all()

    def tilt_column(self, column_number):
        # print(f'Tilt column {column_number}')
        column_height = len(self.grid)

        number_of_moves = 0
        for row in range(1, column_height):
            # print(f'Tilting row {row} column {column_number}')
            if self.grid[row - 1][column_number] == '.' and self.grid[row][column_number] == 'O':
                self.grid[row - 1][column_number] = 'O'
                self.grid[row][column_number] = '.'
                number_of_moves += 1

        if number_of_moves != 0:
            self.tilt_column(column_number)

    def tilt(self):
        for column_number in range(len(self.grid[0])):
            self.tilt_column(column_number)

    def calculate_load(self):
        print(self.grid)
        print()
        flipped = np.flipud(self.grid)
        print(flipped)
        load = 0
        for row_number, row in enumerate(flipped):
            print(list(row))
            row_power = (row_number+1) * sum(1 for i in row if i == 'O')
            print(row_power)
            load += row_power
        return load

def part1(data):
    # for dish in data:
    dish = data
        # print(dish)
        # print()
    this_dish = Dish(dish)
    # print(this_dish)
    this_dish.tilt()
    # print(this_dish)
    # this_dish.calculate_load()
    return this_dish.calculate_load()
    pass


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
