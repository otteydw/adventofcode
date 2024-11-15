import argparse
import copy
import itertools
import pathlib
from typing import List


def parse(puzzle_input):
    lines = [line for line in puzzle_input.split("\n")]
    program = [int(value) for value in lines[0].split(",")]
    return program


# def get_opcode(memory: List, address: int) -> int:
#     """Returns the opcode of a program at a given address

#     Args:
#         memory (List): The program memory
#         address (int): The address of the instruction

#     Returns:
#         int: the opcode
#     """
#     return memory[address] % 100


def get_opcode(instruction: int) -> int:
    return instruction % 100


def get_modes(instruction: int) -> dict:
    """Given an instruction, return the modes of the 3 parameters.

    Args:
        instruction (int): An instruction value

    Returns:
        dict: The modes of the 3 parameters
    """

    # ABCDE
    #  1002

    # DE - two-digit opcode,      02 == opcode 2
    #  C - mode of 1st parameter,  0 == position mode
    #  B - mode of 2nd parameter,  1 == immediate mode
    #  A - mode of 3rd parameter,  0 == position mode,
    #                                   omitted due to being a leading zero
    parameter_modes = {
        1: int(instruction % 1000 / 100),
        2: int(instruction % 10000 / 1000),
        3: int(instruction % 100000 / 10000),
    }
    return parameter_modes


# def get_modes(memory: List, address: int) -> dict:
#     """Given an instruction, return the modes of the 3 parameters.

#     Args:
#         instruction (int): An instruction value

#     Returns:
#         dict: The modes of the 3 parameters
#     """

#     # ABCDE
#     #  1002

#     # DE - two-digit opcode,      02 == opcode 2
#     #  C - mode of 1st parameter,  0 == position mode
#     #  B - mode of 2nd parameter,  1 == immediate mode
#     #  A - mode of 3rd parameter,  0 == position mode,
#     #                                   omitted due to being a leading zero

#     instruction = memory[address]
#     parameter_modes = {
#         1: int(instruction % 1000 / 100),
#         2: int(instruction % 10000 / 1000),
#         3: int(instruction % 100000 / 10000),
#     }
#     return parameter_modes


def get_value_via_mode(memory: List, address: int, mode: int):
    match mode:
        case 0:
            position = memory[address]
            value = memory[position]
        case 1:
            value = memory[address]
        case _:
            raise ValueError(f"Unexpected mode {mode}")

    return value


def get_position_via_mode(memory: List, address: int, mode: int):
    match mode:
        case 0:
            value = memory[address]
        case 1:
            position = memory[address]
            value = memory[position]
        case _:
            raise ValueError(f"Unexpected mode {mode}")

    return value


def opcode_add(memory: List, instruction_pointer: int, modes: dict) -> None:
    # Opcode 1 adds together numbers read from two positions and stores the result in a third position.
    # The three integers immediately after the opcode tell you these three positions -
    # the first two indicate the positions from which you should read the input values, and the third indicates
    # the position at which the output should be stored.

    # print()
    # print(f"Memory: {memory}")
    # print(f"instruction_pointer: {instruction_pointer}")
    # print(f"My modes: {modes}")

    value1 = get_value_via_mode(memory, instruction_pointer + 1, modes[1])
    value2 = get_value_via_mode(memory, instruction_pointer + 2, modes[2])
    storage_position = get_position_via_mode(memory, instruction_pointer + 3, modes[3])
    # print(f"I will add {value1} and {value2} and store the result in position {storage_position}")

    memory[storage_position] = value1 + value2

    return None


def opcode_multiply(memory: List, instruction_pointer: int, modes: dict) -> None:
    # Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three
    # integers after the opcode indicate where the inputs and outputs are, not their values.

    # print()
    # print(f"Memory: {memory}")
    # print(f"instruction_pointer: {instruction_pointer}")
    # print(f"My modes: {modes}")

    value1 = get_value_via_mode(memory, instruction_pointer + 1, modes[1])
    value2 = get_value_via_mode(memory, instruction_pointer + 2, modes[2])
    storage_position = get_position_via_mode(memory, instruction_pointer + 3, modes[3])
    # print(f"I will multiply {value1} and {value2} and store the result in position {storage_position}")

    memory[storage_position] = value1 * value2


# def opcode3(memory: List, instruction_pointer: int) -> None:
#     # Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example,
#     # the instruction 3,50 would take an input value and store it at address 50.
#     storage_position = memory[instruction_pointer + 3]


def run_program(program: List):
    program = copy.deepcopy(program)

    current_address = 0
    done = False

    while not done:
        instruction = program[current_address]
        opcode = get_opcode(instruction)
        modes = get_modes(instruction)

        match opcode:
            case 1:
                opcode_add(program, current_address, modes)
                current_address += 4
            case 2:
                opcode_multiply(program, current_address, modes)
                current_address += 4
            case 3:
                pass
            case 4:
                pass
            case 99:
                done = True
            case _:
                raise ValueError(f"Unhandled opcode {opcode}")

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
