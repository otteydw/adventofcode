import os
from typing import List

def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    data = []

    with open(input_path) as input_file:
        pair = []
        for line in input_file:
            line_stripped = line.rstrip()
            if line_stripped == "":
                data.append(pair)
                pair = []
            else:
                line_as_list = eval(line_stripped)
                pair.append(line_as_list)
        data.append(pair)

    return data

def solve(left, right):
# def solve(pairs):

    print(f"- Compare {left} vs {right}")

    # If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the
    # comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found
    # by instead comparing [0,0,0] and [2].
    if isinstance(left, list) and isinstance(right, int):
        right = [right]
        return solve(left, right)
    elif isinstance(left, int) and isinstance(right, list):
        left = [left]
        return solve(left, right)

    # If both values are lists, compare the first value of each list, then the second value, and so on. If the left list
    # runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs
    # are not in the right order. If the lists are the same length and no comparison makes a decision about the order,
    # continue checking the next part of the input.

    if isinstance(left, list) and isinstance(right, list):
        if len(left) == 0 and len(right) >= 1:
            return True
        elif len(left) >= 1 and len(right) == 0:
            return False
        return solve(left[0], right[0]) and solve(left[1:], right[1:])


    # If both values are integers, the lower integer should come first. If the left integer is lower than the right integer,
    # the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order.
    # Otherwise, the inputs are the same integer; continue checking the next part of the input.
    if (isinstance(left, int) or left.isdigit()) and (isinstance(right, int) or right.isdigit()):
        if int(left) < int(right):
            return True
        elif int(left) > int(right):
            return False
        else:
            return solve(left[0], right[0])



if __name__ == "__main__":

    input_filename = "example.txt"
    # input_filename = "input.txt"
    data = load_from_file(input_filename)
    for pair in data:
        print(pair)
    # solve(data)
    # game = Game(input_filename, rounds=20)
    # print(f"Monkey business: {game.monkey_business()}")
