# mypy: ignore-errors
# https://adventofcode.com/2020/day/3


# def print_map(map):
#     for line in map:
#         print(line)


def char_at_map_pos(row, column, map):
    return map[row][column]


def is_tree(row, column, map):
    return char_at_map_pos(row, column, map) == "#"


def move(start_row, start_column, row_move, column_move, map):
    map_width = len(map[0])

    new_row = start_row + row_move
    new_column = start_column + column_move

    if new_column >= map_width:
        new_column = new_column - map_width

    return new_row, new_column


INPUTS_PATH = "input.txt"

with open(INPUTS_PATH) as inputs_file:
    lines = inputs_file.readlines()

lines = [x.strip() for x in lines]
map = []

for line in lines:
    map.append(line)

ROWS_IN_MAP = len(map)

current_row = 0
current_column = 0
tree_count = 0

while current_row < ROWS_IN_MAP - 1:
    current_row, current_column = move(current_row, current_column, 1, 3, map)
    # print(current_row, current_column)
    if is_tree(current_row, current_column, map):
        tree_count += 1

print(tree_count)
