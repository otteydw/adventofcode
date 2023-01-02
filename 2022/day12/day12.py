import os
import pprint
# import sys
import numpy as np
# np.set_printoptions(threshold=sys.maxsize)

def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    data = []

    with open(input_path) as input_file:
        for line in input_file:
            row = []
            for char in line.rstrip():
                row.append(char)
            data.append(row)

    return data


class Grid:
    def __init__(self, filename):
        self.start = None
        self.end = None
        self.grid = self.process_input(load_from_file(filename))
        # self.report()

    def print_grid(self):
        # for row in self.grid:
        #     print(row)
        # pprint.pprint(self.grid)
        print(np.matrix(self.grid))

    def report(self):
        # print(self.grid)
        self.print_grid()
        print(f"Start: {self.start}")
        print(f"End: {self.end}")

    def get_height_at_position(self, position):
        # print(position)
        return self.grid[position[0]][position[1]]

    def process_input(self, input_grid):
        output_grid = []
        for row_number, row in enumerate(input_grid):
            output_row = []
            for column_number, column in enumerate(row):
                if column == "S":
                    self.start = (row_number, column_number)
                    column = "a"
                elif column == "E":
                    self.end = (row_number, column_number)
                    column = "z"
                column_value = ord(column) - 97
                output_row.append(column_value)
            output_grid.append(output_row)
        return output_grid

    def can_go(self, position, direction):
        row = position[0]
        column = position[1]
        current_height = self.get_height_at_position(position)

        if direction == "right":
            new_row = row
            new_column = column + 1
        elif direction == "left":
            new_row = row
            new_column = column - 1
        elif direction == "up":
            new_row = row - 1
            new_column = column
        elif direction == "down":
            new_row = row + 1
            new_column = column

        if new_row < 0:
            return False
        elif new_row > len(self.grid)-1:
            return False
        elif new_column < 0:
            return False
        elif new_column > len(self.grid[0])-1:
            return False

        new_height = self.get_height_at_position((new_row, new_column))

        if new_height - current_height > 1:
            return False

        return True

if __name__ == "__main__":

    input_filename = "example.txt"
    # input_filename = "input.txt"

    grid = Grid(input_filename)

    # interesting_signals = [20, 60, 100, 140, 180, 220]
    # print(f"Sum of signals: {tube.sum_of_signal_strengths(interesting_signals)}")
    # print()
    # tube.draw()
