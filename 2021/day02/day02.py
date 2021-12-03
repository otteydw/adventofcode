
import os

class Submarine():
    def __init__(self):
        self.depth = 0
        self.horizontal_position = 0

    def move(self, instruction):
        direction, distance = instruction.split(' ')
        distance = int(distance)

        if direction == "forward":
            self.horizontal_position += distance
        elif direction == "down":
            self.depth += distance
        elif direction == "up":
            self.depth -= distance
        else:
            raise Exception(f'Invalid direction {direction}!')

def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__),filename)

    with open(input_path, 'r') as input_file:
        lines = input_file.readlines()
        lines = [line.rstrip() for line in lines]

    return lines

if __name__ == "__main__":

    sub = Submarine()
    instructions = load_from_file("input.txt")
    for instruction in instructions:
        sub.move(instruction)

    print(f'Part 1 answer is: {sub.depth * sub.horizontal_position}')