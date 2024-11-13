import argparse
import copy
import itertools
import pathlib
from typing import List


def parse(puzzle_input):
    lines = [line for line in puzzle_input.split("\n")]
    program = [int(value) for value in lines[0].split(",")]
    return program


def get_opcode(memory: List, address: int) -> int:
    return memory[address]


def opcode_add(memory: List, instruction_pointer: int) -> None:
    # Opcode 1 adds together numbers read from two positions and stores the result in a third position.
    # The three integers immediately after the opcode tell you these three positions -
    # the first two indicate the positions from which you should read the input values, and the third indicates
    # the position at which the output should be stored.
    position1 = memory[instruction_pointer + 1]
    position2 = memory[instruction_pointer + 2]
    storage_position = memory[instruction_pointer + 3]
    value1 = memory[position1]
    value2 = memory[position2]
    memory[storage_position] = value1 + value2
    return None


def opcode_multiply(memory: List, instruction_pointer: int) -> None:
    # Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three
    # integers after the opcode indicate where the inputs and outputs are, not their values.
    position1 = memory[instruction_pointer + 1]
    position2 = memory[instruction_pointer + 2]
    storage_position = memory[instruction_pointer + 3]
    value1 = memory[position1]
    value2 = memory[position2]
    memory[storage_position] = value1 * value2
    return None


def run_program(program: List):
    program = copy.deepcopy(program)

    current_address = 0
    done = False

    while not done:
        opcode = get_opcode(program, current_address)

        match opcode:
            case 1:
                opcode_add(program, current_address)
                current_address += 4
            case 2:
                opcode_multiply(program, current_address)
                current_address += 4
            case 99:
                done = True
            case _:
                pass

    return program


def part1(data: List):
    data[1] = 12
    data[2] = 2
    program = run_program(data)
    return program[0]


def part2(data: List):
    desired_output = 19690720
    for noun, verb in itertools.product(range(99), range(99)):
        data[1] = noun
        data[2] = verb
        program = run_program(data)
        if program[0] == desired_output:
            break
    return 100 * noun + verb


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
