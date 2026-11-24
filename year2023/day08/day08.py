# mypy: ignore-errors
import math
import pathlib
import sys
from collections import namedtuple
from itertools import cycle

Node = namedtuple("Node", "left right")


def parse(puzzle_input):
    return [line for line in puzzle_input.split("\n")]


def node_parse(data):
    node_name, left_right_string = data.split(" = ")

    left, right = left_right_string.replace("(", "").replace(")", "").split(", ")

    return node_name, left, right


def parse_data(data):
    sequence = data[0]

    network = {}
    for row in data[2:]:
        node_name, left_node, right_node = node_parse(row)
        node = Node(left_node, right_node)
        network[node_name] = node

    return sequence, network


def part1(data):
    sequence, network = parse_data(data)

    start_node = "AAA"

    if start_node not in network:
        return None

    current_node = start_node
    steps = 0
    for direction in cycle(sequence):
        if direction == "L":
            current_node = network[current_node].left
        else:
            current_node = network[current_node].right
        steps += 1
        if current_node == "ZZZ":
            return steps


def part2(data):
    sequence, network = parse_data(data)

    starting_nodes = [x for x in network.keys() if x.endswith("A")]

    all_steps = []
    for node in starting_nodes:
        steps = 0
        current_node = node
        for direction in cycle(sequence):
            if direction == "L":
                current_node = network[current_node].left
            else:
                current_node = network[current_node].right
            steps += 1
            if current_node.endswith("Z"):
                break
        all_steps.append(steps)

    return math.lcm(*all_steps)


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
