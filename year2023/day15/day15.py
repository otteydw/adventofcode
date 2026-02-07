import pathlib
import sys


def parse(puzzle_input):
    return [line for line in puzzle_input.split("\n")][0].split(",")


def part1(data):
    return sum([hash(input_string) for input_string in data])


class Lens:
    def __init__(self, label, focal_length):
        self.label = label
        self.focal_length = focal_length

    def __repr__(self) -> str:
        return f"[{self.label} {self.focal_length}]"

    def __eq__(self, other) -> bool:
        # Two lenses are considered equivalent if their labels match regardless of their focal lengths.
        return self.label == other.label


class Box:
    def __init__(self):
        self.contents = []

    def __repr__(self) -> str:
        output = ""
        if len(self.contents) > 0:
            for lens in self.contents:
                output += f"{str(lens)} "
        return output

    def is_empty(self):
        return len(self.contents) == 0

    def append(self, item):
        self.contents.append(item)

    def contains_lens(self, lens):
        return lens in self.contents

    def remove(self, lens):
        self.contents.remove(lens)

    def replace(self, lens):
        for lens_number, existing_lens in enumerate(self.contents):
            if lens == existing_lens:
                self.contents[lens_number] = lens
                break

    def focusing_power(self):
        focusing_power = 0
        for lens in self.contents:
            lens_focusing_power = (self.contents.index(lens) + 1) * lens.focal_length
            focusing_power += lens_focusing_power

        return focusing_power


def print_boxes(boxes):
    for box_number, box in enumerate(boxes):
        if not box.is_empty():
            print(f"Box {box_number}: {str(box)}")


def boxes_focusing_power(boxes):
    focusing_power = 0
    for box_number, box in enumerate(boxes):
        focusing_power += (1 + box_number) * box.focusing_power()
    return focusing_power


def hashmap(data):
    NUMBER_OF_BOXES = 256
    boxes = [Box() for _ in range(NUMBER_OF_BOXES)]

    for step in data:
        if "-" in step:
            label = step.split("-")[0]
            box_number = hash(label)
            try:
                boxes[box_number].remove(Lens(label, None))
            except ValueError:
                pass
        elif "=" in step:
            label, focal_length = step.split("=")
            focal_length = int(focal_length)
            box_number = hash(label)

            this_lens = Lens(label, focal_length)
            if boxes[box_number].contains_lens(this_lens):
                boxes[box_number].replace(this_lens)
            else:
                boxes[box_number].append(this_lens)
        else:
            print("Couldn't find the operation character.")
            sys.exit(1)

        print(f"After {step}")
        print_boxes(boxes)

        print()

    return boxes


def part2(data):
    boxes = hashmap(data)
    return boxes_focusing_power(boxes)


def hash(input_string):
    # start with a current value of 0.
    current_value = 0

    # Then, for each character in the string starting from the beginning:
    for character in input_string:
        # Determine the ASCII code for the current character of the string.
        character_ascii_value = ord(character)

        # Increase the current value by the ASCII code you just determined.
        current_value += character_ascii_value

        # Set the current value to itself multiplied by 17.
        current_value *= 17

        # Set the current value to the remainder of dividing itself by 256.
        current_value %= 256

    # print(f"Returning {current_value}")
    return current_value


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)

    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        for solution_number, solution in enumerate(solutions):
            print(f"Solution {solution_number}: {str(solution)}")
