
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

def trees_in_slope(slope_right, slope_down, map):
    ROWS_IN_MAP = len(map)

    current_row = 0
    current_column = 0
    tree_count = 0

    while current_row < ROWS_IN_MAP-1:
        current_row, current_column = move(current_row, current_column, slope_down, slope_right, map)
        # print(current_row, current_column)
        if is_tree(current_row, current_column, map):
            tree_count += 1

    return tree_count

def main():
    INPUTS_PATH = 'input.txt'

    with open(INPUTS_PATH) as inputs_file:
        lines = inputs_file.readlines()

    lines = [x.strip() for x in lines]
    map = []

    for line in lines:
        map.append(line)

    tree_mult = 1

    for right, down in [(1, 1), (3, 1), (5,1), (7,1),(1,2)]:
        tree_mult = tree_mult * trees_in_slope(right, down, map)

    print(tree_mult)

main()