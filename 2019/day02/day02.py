import argparse
import pathlib
from typing import List


def parse(puzzle_input):
    lines = [line for line in puzzle_input.split("\n")]
    program = [int(value) for value in lines[0].split(",")]
    return program


def get_opcode(program: List, position: int) -> int:
    return program[position]


def opcode_add(program: List, current_position: int) -> None:
    # Opcode 1 adds together numbers read from two positions and stores the result in a third position.
    # The three integers immediately after the opcode tell you these three positions -
    # the first two indicate the positions from which you should read the input values, and the third indicates
    # the position at which the output should be stored.
    position1 = program[current_position + 1]
    position2 = program[current_position + 2]
    storage_position = program[current_position + 3]
    value1 = program[position1]
    value2 = program[position2]
    program[storage_position] = value1 + value2
    return None


def opcode_multiply(program: List, current_position: int) -> None:
    # Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three
    # integers after the opcode indicate where the inputs and outputs are, not their values.
    position1 = program[current_position + 1]
    position2 = program[current_position + 2]
    storage_position = program[current_position + 3]
    value1 = program[position1]
    value2 = program[position2]
    program[storage_position] = value1 * value2


def run_program(program: List):
    current_position = 0
    done = False

    while not done:
        opcode = get_opcode(program, current_position)

        match opcode:
            case 1:
                opcode_add(program, current_position)
            case 2:
                opcode_multiply(program, current_position)
            case 99:
                done = True
            case _:
                pass

        current_position += 4
    return program


def part1(data: List):
    data[1] = 12
    data[2] = 2
    program = run_program(data)
    return program[0]


def part2(data):
    pass


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solve Advent of Code puzzles")
    parser.add_argument("files", nargs="+", help="Input files to process")
    args = parser.parse_args()

    for path in args.files:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        for solution_number, solution in enumerate(solutions):
            print(f"Solution {solution_number}: {str(solution)}")
