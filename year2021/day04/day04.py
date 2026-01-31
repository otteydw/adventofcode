import itertools
import os

# import pandas as pd
# import numpy as np

# class BingoBoard:
#     def __init__(self, board_grid_data):
#         self.board_grid = self._initialize_board(board_grid_data)
#         self.board_selections = np.zeros((5,5), dtype=bool)

#     def _initialize_board(self, board_grid_data):

#         board = []
#         for row in board_grid_data:
#             columns = row.split()
#             board.append([int(i) for i in columns])

#         # print(board)
#         np_board = np.array(board, dtype=int)
#         return np_board

#     def print_board(self):
#         print(self.board_grid)
#         print(self.board_selections)

#     def call(self, value):

#         found = np.where(self.board_grid == value)
#         if len(found) > 0 and len(found[0]):
#             print(f"Found value {value} at {found}")
#             self.board_selections[found] = True
#             return True
#         else:
#             return False


class BingoBoard:
    def __init__(self, board_grid_data):
        self.board_grid = self._initialize_board(board_grid_data)
        self.board_selections = [[False] * 5 for i in range(5)]

    def _initialize_board(self, board_grid_data):

        board = []
        for row in board_grid_data:
            columns = row.split()
            board.append([int(i) for i in columns])

        return board

    def print_board(self):
        print(self.board_selections)
        for row in self.board_grid:
            print(row)
        print()
        for row in self.board_selections:
            print(row)

    def value_at_position(self, x, y):
        return self.board_grid[x][y]

    def set_called(self, x, y):
        self.board_selections[x][y] = True

    def was_called(self, x, y):
        return self.board_selections[x][y]

    def call(self, value):

        for x in range(5):
            for y in range(5):
                if self.value_at_position(x, y) == value:
                    self.set_called(x, y)
                    return True

        return False

    def check_horizontal_bingo(self):

        for x in range(5):
            if (
                self.was_called(x, 0)
                and self.was_called(x, 1)
                and self.was_called(x, 2)
                and self.was_called(x, 3)
                and self.was_called(x, 4)
            ):
                return True

        return False

    def check_vertical_bingo(self):

        for y in range(5):
            if (
                self.was_called(0, y)
                and self.was_called(1, y)
                and self.was_called(2, y)
                and self.was_called(3, y)
                and self.was_called(4, y)
            ):
                return True

        return False

    def check_for_bingo(self):

        return self.check_horizontal_bingo() or self.check_vertical_bingo()

    def call_and_check(self, value):

        self.call(value)
        return self.check_for_bingo()

    def score(self, value_just_called):

        sum_of_uncalled = 0

        for x in range(5):
            for y in range(5):
                if not self.was_called(x, y):
                    sum_of_uncalled += self.value_at_position(x, y)

        return sum_of_uncalled * value_just_called


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    with open(input_path, "r") as input_file:
        lines = input_file.readlines()
        lines = [line.rstrip() for line in lines]

    return lines


# https://stackoverflow.com/questions/434287/what-is-the-most-pythonic-way-to-iterate-over-a-list-in-chunks
def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


def load_bingo(filename):
    data = load_from_file(filename)

    drawn_numbers = [int(i) for i in data[0].split(",")]
    all_board_data = data[2:]

    boards = []

    for board_data in grouper(all_board_data, 6):

        board = BingoBoard(board_data[0:5])
        boards.append(board)

    return drawn_numbers, boards


def find_first_winning_board(drawn_numbers, boards):

    for drawn_number in drawn_numbers:
        for board in boards:
            if board.call_and_check(drawn_number):
                return board.score(drawn_number)


def find_last_winning_board(drawn_numbers, boards):

    most_recent_score = -1

    for drawn_number in drawn_numbers:
        for board in boards:
            if not board.check_for_bingo() and board.call_and_check(drawn_number):
                most_recent_score = board.score(drawn_number)

    return most_recent_score


if __name__ == "__main__":

    drawn_numbers, boards = load_bingo("input.txt")
    print(f"Score of first winning board: {find_first_winning_board(drawn_numbers, boards)}")

    drawn_numbers, boards = load_bingo("input.txt")
    print(f"Score of last winning board: {find_last_winning_board(drawn_numbers, boards)}")
