import os
import numpy


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    data = []

    with open(input_path) as input_file:
        for line in input_file:
            row = []
            for char in line.rstrip():
                row.append(int(char))
            data.append(row)

    return data


class Forest:
    def __init__(self, filename):
        self.trees = load_from_file(filename)
        self.height = len(self.trees)
        self.width = len(self.trees[0])
        # print(f"Width = {self.width} Height = {self.height}")
        self.trees_transposed = numpy.transpose(self.trees)

    def count_visible_trees(self):
        visible_trees = 0
        for row in range(self.height):
            for column in range(self.width):
                # print(f"Checking row={row} colum={column} value={self.trees[row][column]}")
                if self.visible(row, column):
                    visible_trees += 1
        return visible_trees

    def visible(self, row, column):
        if row == 0 or column == 0:
            return True
        elif row == self.height - 1 or column == self.width - 1:
            return True
        elif (
            self.visible_from_left(row, column)
            or self.visible_from_right(row, column)
            or self.visible_from_top(row, column)
            or self.visible_from_bottom(row, column)
        ):
            return True

        return False

    def visible_from_left(self, row, column):
        current_value = self.trees[row][column]
        left_values = self.trees[row][0:column]
        if current_value > max(left_values):
            return True
        return False

    def visible_from_right(self, row, column):
        current_value = self.trees[row][column]
        right_values = self.trees[row][column + 1 :]
        # print(f"Current value {current_value} right_values {right_values}")
        if current_value > max(right_values):
            return True
        return False

    def visible_from_top(self, row, column):
        current_value = self.trees[row][column]
        top_values = self.trees_transposed[column][0:row]
        if current_value > max(top_values):
            return True
        return False

    def visible_from_bottom(self, row, column):
        current_value = self.trees[row][column]
        bottom_values = self.trees_transposed[column][row + 1 :]
        if current_value > max(bottom_values):
            return True
        return False


if __name__ == "__main__":

    # input_filename = "example.txt"
    input_filename = "input.txt"

    forest = Forest(input_filename)
    print(f"Visible trees: {forest.count_visible_trees()}")
