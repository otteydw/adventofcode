#!/usr/bin/python3

import sys


def get_opcode(program, position):
    return program[position]


def intcode(program, position=0):

    opcode = get_opcode(program, position)

    if opcode == 1:
        opcode_add(program, position)

    elif opcode == 2:
        opcode_multiply(program, position)

    elif opcode == 99:
        return program

    else:
        print("Invalid opcode!")
        sys.exit(1)

    position += 4
    return intcode(program, position)


def opcode_add(program, position):
    storage_position = program[position + 3]
    a_pos = program[position + 1]
    b_pos = program[position + 2]
    a_val = program[a_pos]
    b_val = program[b_pos]
    program[storage_position] = a_val + b_val
    return program


def opcode_multiply(program, position):
    storage_position = program[position + 3]
    a_pos = program[position + 1]
    b_pos = program[position + 2]
    a_val = program[a_pos]
    b_val = program[b_pos]
    program[storage_position] = a_val * b_val
    return program


# input_program = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]

# input_program
# result = intcode(input_program, 0)

# print(result)

inputs_path = "input.txt"

with open(inputs_path) as input_file:
    input_program = [int(x) for x in input_file.readline().rstrip().split(",")]

input_program[1] = 12
input_program[2] = 2
result = intcode(input_program)
print(result[0])
