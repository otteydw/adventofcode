import os
import numpy as np
import parse


class VentField:
    def __init__(self, data_from_file, draw_diagonals=True):
        self.draw_diagonals = draw_diagonals
        self.parse_data(data_from_file)
        # print(self.array)

    def parse_data(self, data):

        vent_lines = []

        for line in data:
            pattern = "{x1:d},{y1:d} -> {x2:d},{y2:d}"
            match = parse.search(pattern, line)
            vent_lines.append(match)

        max_x1 = max(vent_lines, key=lambda x: x["x1"])["x1"]
        max_x2 = max(vent_lines, key=lambda x: x["x2"])["x2"]
        max_x = max(max_x1, max_x2)
        max_y1 = max(vent_lines, key=lambda x: x["y1"])["y1"]
        max_y2 = max(vent_lines, key=lambda x: x["y2"])["y2"]
        max_y = max(max_y1, max_y2)

        array_x_size = max_x + 1
        array_y_size = max_y + 1
        print(f"Creating an array with y={array_y_size}, x={array_x_size}.")
        self.array = np.zeros((array_y_size, array_x_size))

        for vent_line in vent_lines:
            # print(self.__repr__())
            self.draw_line(vent_line)

    def draw_line(self, line):
        x1, x2 = line["x1"], line["x2"]
        y1, y2 = line["y1"], line["y2"]

        # line_start = (x1, y1)
        # line_end = (x2, y2)
        # print(f"Draw a line from {line_start} to {line_end}.")

        if x1 == x2:
            self.draw_vertical_line(x=x1, y1=y1, y2=y2)
        elif y1 == y2:
            self.draw_horizontal_line(y=y1, x1=x1, x2=x2)
        elif self.draw_diagonals:
            self.draw_diagonal_line(x1=x1, x2=x2, y1=y1, y2=y2)

    def draw_vertical_line(self, x, y1, y2):
        start_y = min(y1, y2)
        end_y = max(y1, y2)
        for y in range(start_y, end_y + 1):
            # print(f"Drawing point at x={x}, y={y}")
            self.add_point(x, y)

    def draw_horizontal_line(self, y, x1, x2):
        start_x = min(x1, x2)
        end_x = max(x1, x2)
        for x in range(start_x, end_x + 1):
            # print(f"Drawing point at x={x}, y={y}")
            self.add_point(x, y)

    def draw_diagonal_line(self, x1, x2, y1, y2):
        if not self.is_line_45_degrees(x1, x2, y1, y2):
            pass

        x_direction = 1 if x1 < x2 else -1
        y_direction = 1 if y1 < y2 else -1

        x_positions = range(x1, x2 + x_direction, x_direction)
        y_positions = range(y1, y2 + y_direction, y_direction)

        diagonal_positions = zip(x_positions, y_positions)

        for x, y in diagonal_positions:
            self.add_point(x, y)

    def is_line_45_degrees(self, x1, x2, y1, y2):
        # Checking that the line's slope is 45 degrees
        return abs(x1 - x2) == abs(y1 - y2)

    def add_point(self, x, y):
        self.array[y][x] += 1

    def number_of_lines_covering_point(self, point):
        x, y = point
        return self.array[y][x]

    def number_of_points_with_overlap(self, overlapping_points=2):
        return (self.array >= 2).sum()

    def __repr__(self):
        # print(self.array)
        printout = "  "

        for column_index in range(len(self.array[0])):
            printout += str(column_index)
        printout += "\n"
        for row_index, row in enumerate(self.array):
            printout += f"{row_index} "
            for column in row:
                if column == 0:
                    printout += "."
                else:
                    printout += str(int(column))
            printout += "\n"

        return printout


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    with open(input_path, "r") as input_file:
        lines = input_file.readlines()
        lines = [line.rstrip() for line in lines]

    return lines


if __name__ == "__main__":

    data = load_from_file("input.txt")
    vent_without_diagonals = VentField(data, draw_diagonals=False)
    print(
        f"Number of points with overlap (without diagonals): {vent_without_diagonals.number_of_points_with_overlap()}"
    )
    vent_with_diagonals = VentField(data, draw_diagonals=True)
    print(
        f"Number of points with overlap (with diagonals): {vent_with_diagonals.number_of_points_with_overlap()}"
    )
    # vent.printme()
    # print(vent.array)
