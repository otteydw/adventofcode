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
        self.trees_transposed = numpy.transpose(self.trees)

    def count_visible_trees(self):
        visible_trees = 0
        for row in range(self.height):
            for column in range(self.width):
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

    def viewing_distance_left(self, row, column):
        viewing_distance = 0
        current_value = self.trees[row][column]
        left_values = self.trees[row][0:column]

        for check_value in reversed(left_values):
            viewing_distance += 1
            if check_value >= current_value:
                break

        return viewing_distance

    def viewing_distance_right(self, row, column):
        viewing_distance = 0
        current_value = self.trees[row][column]
        right_values = self.trees[row][column + 1 :]

        for check_value in right_values:
            viewing_distance += 1
            if check_value >= current_value:
                break

        return viewing_distance

    def viewing_distance_up(self, row, column):
        viewing_distance = 0
        current_value = self.trees[row][column]
        up_values = self.trees_transposed[column][0:row]

        for check_value in reversed(up_values):
            viewing_distance += 1
            if check_value >= current_value:
                break

        return viewing_distance

    def viewing_distance_down(self, row, column):
        viewing_distance = 0
        current_value = self.trees[row][column]
        down_values = self.trees_transposed[column][row + 1 :]

        for check_value in down_values:
            viewing_distance += 1
            if check_value >= current_value:
                break

        return viewing_distance

    def scenic_score(self, row, column):
        return (
            self.viewing_distance_left(row, column)
            * self.viewing_distance_right(row, column)
            * self.viewing_distance_up(row, column)
            * self.viewing_distance_down(row, column)
        )

    def highest_scenic_score(self):
        highest_scenic_score = 0
        for row in range(self.height):
            for column in range(self.width):
                scenic_score = self.scenic_score(row, column)
                if scenic_score > highest_scenic_score:
                    highest_scenic_score = scenic_score
        return highest_scenic_score


if __name__ == "__main__":

    # input_filename = "example.txt"
    input_filename = "input.txt"

    forest = Forest(input_filename)
    print(f"Visible trees: {forest.count_visible_trees()}")
    print(f"Highest scenic score: {forest.highest_scenic_score()}")
