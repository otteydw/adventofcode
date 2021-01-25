
# https://adventofcode.com/2020/day/2


def parse_line(my_line):
    quantity, letter, password = my_line.split(' ')

    occurenceA = int(quantity.split('-')[0])
    occurenceB = int(quantity.split('-')[1])
    letter = letter.split(':')[0]
    return occurenceA, occurenceB, letter, password

def validate_password(my_line):
    occurenceA, occurenceB, letter, password = parse_line(my_line)
    return check_validity(occurenceA, occurenceB, letter, password)

def char_at_position(position, letter, word):
    return word[position - 1] == letter

def check_validity(occurenceA, occurenceB, letter, password):
    counter = 0
    for pos in [occurenceA, occurenceB]:
        if char_at_position(pos, letter, password):
            counter += 1

    return counter == 1

INPUTS_PATH = 'input.txt'

with open(INPUTS_PATH) as inputs_file:
    lines = inputs_file.readlines()

lines = [x.strip() for x in lines]

valid_password_count = 0
for line in lines:
    if validate_password(line):
        valid_password_count += 1

print(valid_password_count)
