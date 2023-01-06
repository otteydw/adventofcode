import os
import pprint
# import sys
import numpy as np
# np.set_printoptions(threshold=sys.maxsize)

OPPOSITE_DIRECTIONS = {"left": 'right', 'right':'left','up':'down','down':'up'}

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
            # print(f"New height of {new_height} is too higher than {current_height}!")
            return False

        return True

    def get_neighbor_position(self, position, direction):
        if not self.can_go(position, direction):
            return None

        row = position[0]
        column = position[1]
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
        return (new_row, new_column)

    # def shortest_distance(self, position1, position2, arrived_with_direction=None):
    #     print(f"Current pos: {position1} | Dest pos: {position2} | arrived_with_direction: {arrived_with_direction}")

    #     if position1 == position2:
    #         return 0

    #     shortest_distance_found = 99999999999
    #     if arrived_with_direction == None:
    #         directions_to_test=['right', 'left', 'up', 'down']
    #     else:
    #         directions_to_test = [direction for direction in ['right', 'left', 'up', 'down'] if direction != OPPOSITE_DIRECTIONS[arrived_with_direction]]
    #     print(f"Checking {directions_to_test}")
    #     # directions_to_test.remove(arrived_with_direction)
    #     for direction in directions_to_test:
    #         if self.can_go(position1, direction):
    #             shortest_distance_found = min(shortest_distance_found, self.shortest_distance(self.get_neighbor_position(position1, direction), position2, arrived_with_direction=direction) + 1)

    #     return shortest_distance_found

    def shortest_distance(self, position1, position2, previous_locations=None):
        if previous_locations == None:
            previous_locations = set()
        # print(f"Current pos: {position1} | Dest pos: {position2} | previous_locations: {previous_locations}")
        # indent = len(previous_locations)*' '
        # print(f"{indent}Current pos: {position1} | Current height: {self.get_height_at_position(position1)} | Dest pos: {position2}")

        if position1 == position2:
            return 0

        shortest_distance_found = 99999999999
        directions_to_test=['right', 'left', 'up', 'down']
        previous_locations.add(position1)
        for direction in directions_to_test:
            # print(f"{indent}Checking {direction}")
            if self.can_go(position1, direction):
                position_to_check = self.get_neighbor_position(position1, direction)
                if position_to_check not in previous_locations:

                    shortest_distance_found = min(shortest_distance_found, self.shortest_distance(position_to_check, position2, previous_locations=previous_locations) + 1)

        return shortest_distance_found

    # def find_path(self, position1, position2, all_previous_locations=None):
    #     if all_previous_locations == None:
    #         all_previous_locations = set()
    #         # shortest_path = [None]*10000

    #     if position1 == position2:
    #         return position1

    #     # shortest_distance_found = 99999999999

    #     directions_to_test=['right', 'left', 'up', 'down']
    #     all_previous_locations.add(position1)
    #     for direction in directions_to_test:
    #         # found_path = []
    #         found_path = [None]*10000
    #         if self.can_go(position1, direction):
    #             position_to_check = self.get_neighbor_position(position1, direction)
    #             if position_to_check not in all_previous_locations:

    #                 # shortest_distance_found = min(shortest_distance_found, self.shortest_distance(position_to_check, position2, all_previous_locations=all_previous_locations) + 1)

    #                 future_path = self.find_path(position_to_check, position2, all_previous_locations=all_previous_locations)
    #                 if future_path != None:
    #                     if len(future_path) < len(shortest_path):
    #                         # shortest_path = found_path
    #                         shortest_path = future_path
    #     shortest_path.extend(position2)
    #     return shortest_path

    # def shortest_distance(self, position1, position2):
    #     return len(self.find_path(position1, position2))

if __name__ == "__main__":

    input_filename = "example.txt"
    # input_filename = "input.txt"

    grid = Grid(input_filename)

    # interesting_signals = [20, 60, 100, 140, 180, 220]
    # print(f"Sum of signals: {tube.sum_of_signal_strengths(interesting_signals)}")
    # print()
    # tube.draw()
