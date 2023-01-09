import os
import pprint
# import sys
import numpy as np
from enum import Enum
from typing import List, NamedTuple, Callable, Optional
from generic_search import dfs, node_to_path, Node, bfs
# np.set_printoptions(threshold=sys.maxsize)

# OPPOSITE_DIRECTIONS = {"left": 'right', 'right':'left','up':'down','down':'up'}

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

class MazeLocation(NamedTuple):
    row: int
    column: int

class Maze:
    def __init__(self, filename):
        # self.start = None
        # self.end = None
        self._grid, self.start, self.goal = self.process_input(load_from_file(filename))
        self._rows = len(self._grid)-1
        self._columns = len(self._grid[0])-1
        # print(self.start)
        # print(self.goal)
        # self.report()


    def __str__(self) -> str:
        # for row in self.grid:
        #     print(row)
        # pprint.pprint(self.grid)
        # print(np.matrix(self.grid))
        output =  str(np.matrix(self._grid))
        # output: str = ""
        # for row in self._grid:
        #     # output += "".join([c.value for c in row]) + "\n"
        #     output += "".join([str(c) for c in row]) + "\n"
        return output

    # def report(self):
    #     # print(self.grid)
    #     self.print_grid()
    #     print(f"Start: {self.start}")
    #     print(f"End: {self.end}")

    def goal_test(self, m1: MazeLocation) -> bool:
        # print(f"{m1} | {self.goal}")
        return m1 == self.goal

    def successors(self, m1: MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []

        current_height = self.get_height_at_position(m1)
        if m1.row + 1 < self._rows and self.get_height_at_position(MazeLocation(m1.row + 1, m1.column)) - current_height <= 1:
            locations.append(MazeLocation(m1.row + 1, m1.column))
        if m1.row - 1 >= 0 and self.get_height_at_position(MazeLocation(m1.row - 1, m1.column)) - current_height <= 1:
            locations.append(MazeLocation(m1.row - 1, m1.column))
        if m1.column + 1 < self._columns and self.get_height_at_position(MazeLocation(m1.row, m1.column + 1)) - current_height <= 1:
            locations.append(MazeLocation(m1.row, m1.column + 1))
        if m1.column - 1 >= 0 and self.get_height_at_position(MazeLocation(m1.row, m1.column - 1)) - current_height <= 1:
            locations.append(MazeLocation(m1.row, m1.column - 1))
        # print(f" Successors: {locations}")
        return locations


    def get_height_at_position(self, position):
        # print(position)
        # return self._grid[position[0]][position[1]]
        # print(position)
        return self._grid[position.row][position.column]

    def process_input(self, input_grid):
        output_grid = []
        for row_number, row in enumerate(input_grid):
            output_row = []
            for column_number, column in enumerate(row):
                if column == "S":
                    start = MazeLocation(row=row_number, column=column_number)
                    column = "a"
                elif column == "E":
                    end = MazeLocation(row=row_number, column=column_number)
                    column = "z"
                column_value = ord(column) - 97
                output_row.append(column_value)
            output_grid.append(output_row)
        return output_grid, start, end

    # def can_go(self, position, direction):
    #     row = position[0]
    #     column = position[1]
    #     current_height = self.get_height_at_position(position)

    #     if direction == "right":
    #         new_row = row
    #         new_column = column + 1
    #     elif direction == "left":
    #         new_row = row
    #         new_column = column - 1
    #     elif direction == "up":
    #         new_row = row - 1
    #         new_column = column
    #     elif direction == "down":
    #         new_row = row + 1
    #         new_column = column

    #     if new_row < 0:
    #         return False
    #     elif new_row > len(self.grid)-1:
    #         return False
    #     elif new_column < 0:
    #         return False
    #     elif new_column > len(self.grid[0])-1:
    #         return False

    #     new_height = self.get_height_at_position((new_row, new_column))

    #     if new_height - current_height > 1:
    #         # print(f"New height of {new_height} is too higher than {current_height}!")
    #         return False

    #     return True

    # def get_neighbor_position(self, position, direction):
    #     if not self.can_go(position, direction):
    #         return None

    #     row = position[0]
    #     column = position[1]
    #     if direction == "right":
    #         new_row = row
    #         new_column = column + 1
    #     elif direction == "left":
    #         new_row = row
    #         new_column = column - 1
    #     elif direction == "up":
    #         new_row = row - 1
    #         new_column = column
    #     elif direction == "down":
    #         new_row = row + 1
    #         new_column = column
    #     return (new_row, new_column)





if __name__ == "__main__":

    input_filename = "example.txt"
    # input_filename = "input.txt"

    maze = Maze(input_filename)
    print(maze)
    # print(maze.successors(MazeLocation(0,0)))
    # interesting_signals = [20, 60, 100, 140, 180, 220]
    # print(f"Sum of signals: {tube.sum_of_signal_strengths(interesting_signals)}")
    # print()
    # tube.draw()

    solution1: Optional[Node[MazeLocation]] = bfs(maze.start, maze.goal_test, maze.successors)

    if solution1 is None:
        print("No solution found using depth-first search!")
    else:
        path1: List[MazeLocation] = node_to_path(solution1)
