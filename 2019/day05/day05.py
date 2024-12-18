import argparse
import copy
import logging
import pathlib
from typing import List
from unittest.mock import patch

logger = logging.getLogger("intcode")
logger.setLevel(logging.DEBUG)


def parse(puzzle_input):
    lines = [line for line in puzzle_input.split("\n")]
    program = [int(value) for value in lines[0].split(",")]
    return program


def log_program(program):
    logger.info("Program:")
    spacing = 4

    # Print index positions
    index_positions = " ".join(f"{i:{spacing}}" for i in range(len(program)))
    logger.info(index_positions)

    # Print the list items in the same way
    item_positions = " ".join(f"{item:{spacing}}" for item in program)
    logger.info(f"{item_positions}")


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


# def opcode_add(memory: List, instruction_pointer: int, modes: dict) -> int:
def opcode_add(memory: List, instruction_pointer: int) -> int:
    # Opcode 1 adds together numbers read from two positions and stores the result in a third position.
    # The three integers immediately after the opcode tell you these three positions -
    # the first two indicate the positions from which you should read the input values, and the third indicates
    # the position at which the output should be stored.

    pointer_increment = 4
    instruction = memory[instruction_pointer]
    modes = get_modes(instruction)

    value1 = get_value_via_mode(memory, instruction_pointer + 1, modes[1])
    value2 = get_value_via_mode(memory, instruction_pointer + 2, modes[2])
    storage_position = get_position_via_mode(memory, instruction_pointer + 3, modes[3])
    logger.debug(f"I will add {value1} and {value2} and store the result in position {storage_position}")

    memory[storage_position] = value1 + value2

    next_pointer = instruction_pointer + pointer_increment
    return next_pointer


# def opcode_multiply(memory: List, instruction_pointer: int, modes: dict) -> int:
def opcode_multiply(memory: List, instruction_pointer: int) -> int:
    # Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding them. Again, the three
    # integers after the opcode indicate where the inputs and outputs are, not their values.

    pointer_increment = 4

    instruction = memory[instruction_pointer]
    modes = get_modes(instruction)

    value1 = get_value_via_mode(memory, instruction_pointer + 1, modes[1])
    value2 = get_value_via_mode(memory, instruction_pointer + 2, modes[2])
    storage_position = get_position_via_mode(memory, instruction_pointer + 3, modes[3])
    logger.debug(f"I will multiply {value1} and {value2} and store the result in position {storage_position}")

    memory[storage_position] = value1 * value2

    next_pointer = instruction_pointer + pointer_increment
    return next_pointer


def opcode3(memory: List, instruction_pointer: int) -> int:
    # Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example,
    # the instruction 3,50 would take an input value and store it at address 50.

    pointer_increment = 2

    value_to_store = int(input("Input a single integer: "))
    storage_position = memory[instruction_pointer + 1]
    logger.debug(f"Storing value {value_to_store} at position {storage_position}")
    memory[storage_position] = value_to_store

    next_pointer = instruction_pointer + pointer_increment
    return next_pointer


def opcode4(memory: List, instruction_pointer: int) -> tuple[int, int]:
    # Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50.

    pointer_increment = 2

    instruction = memory[instruction_pointer]
    modes = get_modes(instruction)

    value = get_value_via_mode(memory, instruction_pointer + 1, modes[1])

    logger.debug(f"Returning value {value}.")
    next_pointer = instruction_pointer + pointer_increment
    return value, next_pointer


def opcode5(memory: List, instruction_pointer: int) -> int:
    # Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the
    # second parameter. Otherwise, it does nothing.

    instruction = memory[instruction_pointer]
    modes = get_modes(instruction)

    parameter1 = get_value_via_mode(memory, instruction_pointer + 1, modes[1])
    parameter2 = get_value_via_mode(memory, instruction_pointer + 2, modes[2])

    logger.debug(
        f"Checking if {parameter1=} is not zero. If true, jump to {parameter2=} else jump to {instruction_pointer+3}."
    )

    if parameter1 != 0:
        next_pointer = parameter2
    else:
        next_pointer = instruction_pointer + 3

    return next_pointer


def opcode6(memory: List, instruction_pointer: int) -> int:
    # Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the
    # second parameter. Otherwise, it does nothing.

    instruction = memory[instruction_pointer]
    modes = get_modes(instruction)

    parameter1 = get_value_via_mode(memory, instruction_pointer + 1, modes[1])
    parameter2 = get_value_via_mode(memory, instruction_pointer + 2, modes[2])

    logger.debug(
        f"Checking if {parameter1=} is zero. If true, jump to {parameter2=} else jump to {instruction_pointer+3}."
    )

    if parameter1 == 0:
        next_pointer = parameter2
    else:
        next_pointer = instruction_pointer + 3

    return next_pointer


def opcode7(memory: List, instruction_pointer: int) -> int:
    # def opcode7(memory: List, instruction_pointer: int, modes) -> int:
    # Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given
    # by the third parameter. Otherwise, it stores 0.

    pointer_increment = 4

    instruction = memory[instruction_pointer]
    modes = get_modes(instruction)

    parameter1 = get_value_via_mode(memory, instruction_pointer + 1, modes[1])
    parameter2 = get_value_via_mode(memory, instruction_pointer + 2, modes[2])

    parameter3_pointer = instruction_pointer + 3
    parameter3_position = memory[parameter3_pointer]

    logger.debug(f"Checking if {parameter1=} is less than {parameter2=}. Store 1 if true, 0 if false.")

    if parameter1 < parameter2:
        value_to_store = 1
    else:
        value_to_store = 0
    logger.debug(f"Storing {value_to_store} in position {parameter3_position}.")
    memory[parameter3_position] = value_to_store

    next_pointer = instruction_pointer + pointer_increment
    return next_pointer


def opcode8(memory: List, instruction_pointer: int) -> int:
    # Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by
    # the third parameter. Otherwise, it stores 0.

    pointer_increment = 4

    instruction = memory[instruction_pointer]
    modes = get_modes(instruction)

    parameter1 = get_value_via_mode(memory, instruction_pointer + 1, modes[1])
    parameter2 = get_value_via_mode(memory, instruction_pointer + 2, modes[2])

    parameter3_pointer = instruction_pointer + 3

    parameter3_position = memory[parameter3_pointer]

    logger.debug(f"Checking if {parameter1=} is equal to {parameter2=}. Store 1 if true, 0 if false.")

    if parameter1 == parameter2:
        value_to_store = 1
    else:
        value_to_store = 0
    logger.debug(f"Storing {value_to_store} in position {parameter3_position}.")
    memory[parameter3_position] = value_to_store

    next_pointer = instruction_pointer + pointer_increment
    return next_pointer


def run_program(program: List) -> int:

    current_address = 0
    done = False

    while not done:
        instruction = program[current_address]
        log_program(program)
        logger.info(f"Instruction {instruction} from address {current_address}")
        opcode = get_opcode(instruction)

        match opcode:
            case 1:
                next_address = opcode_add(program, current_address)
            case 2:
                next_address = opcode_multiply(program, current_address)
            case 3:
                next_address = opcode3(program, current_address)
            case 4:
                diagnostic_value, next_address = opcode4(program, current_address)
            case 5:
                next_address = opcode5(program, current_address)
            case 6:
                next_address = opcode6(program, current_address)
            case 7:
                next_address = opcode7(program, current_address)
            case 8:
                next_address = opcode8(program, current_address)
            case 99:
                done = True
            case _:
                raise ValueError(f"Unhandled opcode {opcode} at address {current_address}")
        current_address = next_address

    try:
        return diagnostic_value
    except:
        return None


def part1(data: List):
    program = copy.deepcopy(data)
    input_value = 1
    with patch("builtins.input", return_value=input_value):
        response = run_program(program)
    return response


def part2(data: List):
    program = copy.deepcopy(data)
    input_value = 5
    with patch("builtins.input", return_value=input_value):
        response = run_program(program)
    return response


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solve1 = True
    solve2 = True
    solution1 = part1(data) if solve1 else None
    solution2 = part2(data) if solve2 else None

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
