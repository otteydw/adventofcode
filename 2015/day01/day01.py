import os

def find_floor(directions):
    floor = 0

    for direction in directions:
        if direction == "(":
            floor += 1
        elif direction == ")":
            floor -=1

    return floor

def find_basement_position(directions):
    floor = 0

    for index, direction in enumerate(directions):
        if direction == "(":
            floor += 1
        elif direction == ")":
            floor -=1

        if floor == -1:
            return index + 1


if __name__ == "__main__":

    input_path = os.path.join(os.path.dirname(__file__),"input.txt")

    with open(input_path) as input_file:
        INPUT = input_file.readline()

    # print(find_floor(INPUT))
    print(find_basement_position(INPUT))
