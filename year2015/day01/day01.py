import os


def find_floor(directions: str) -> int:
    floor = 0

    for direction in directions:
        if direction == "(":
            floor += 1
        elif direction == ")":
            floor -= 1

    return floor


def find_basement_position(directions: str) -> int | None:
    floor = 0

    for index, direction in enumerate(directions):
        if direction == "(":
            floor += 1
        elif direction == ")":
            floor -= 1

        if floor == -1:
            return index + 1
    return None


if __name__ == "__main__":

    input_path = os.path.join(os.path.dirname(__file__), "input.txt")

    with open(input_path) as input_file:
        INPUT = input_file.readline()

    print(f"Part 1: {find_floor(INPUT)}")
    print(f"Part 2: {find_basement_position(INPUT)}")
