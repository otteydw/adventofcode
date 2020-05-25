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
        print('Invalid opcode!')
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


inputs_path = 'input.txt'

with open(inputs_path) as input_file:
    input_program = [int(x) for x in input_file.readline().rstrip().split(',')]


DESIRED_OUTPUT = 19690720
for noun in range(0, 99):
    for verb in range(0, 99):
        this_program = input_program.copy()
        this_program[1] = noun
        this_program[2] = verb

        if intcode(this_program)[0] == DESIRED_OUTPUT:
            print('Noun = ' + str(noun))
            print('Verb = ' + str(verb))
            print('Answer = ' + str(100 * noun + verb))
            break