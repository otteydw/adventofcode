import os
import sys

class Santa():
    def __init__(self, initial_position=(0,0)):
        self.x = initial_position[0]
        self.y = initial_position[1]

    def move(self, direction):
        if direction == "^":
            self.y += 1
        elif direction == "v":
            self.y -= 1
        elif direction == "<":
            self.x -= 1
        elif direction == ">":
            self.x += 1
        else:
            sys.exit(f"Invalid direction {direction}!")

    def get_position(self):
        return (self.x, self.y)

def deliver_present(presents_tracker, position):
    if not position in presents_tracker.keys():
        presents_tracker[position] = 1
    else:
        presents_tracker[position] += 1

def go_santa(presents, santa, directions):

    deliver_present(presents, santa.get_position())

    for direction in directions:
       santa.move(direction)
       deliver_present(presents, santa.get_position())


if __name__ == "__main__":

    input_path = os.path.join(os.path.dirname(__file__),"input.txt")

    with open(input_path) as input_file:
        DIRECTIONS = input_file.readline()

    presents = {}
    santa = Santa()
    go_santa(presents, santa, DIRECTIONS)

    print(len(presents))