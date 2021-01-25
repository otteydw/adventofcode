
# https://adventofcode.com/2020/day/2


def parse_line(line):
    quantity, letter, password = line.split(' ')

    occurenceA=int(quantity.split('-')[0])
    occurenceB=int(quantity.split('-')[1])
    letter=letter.split(':')[0]
    return occurenceA, occurenceB, letter, password

def validate_password(line):
    occurenceA, occurenceB, letter, password = parse_line(line)
    # char_occurences = letter_occurence(letter, password)

    validity = check_validity(occurenceA, occurenceB, letter, password)

    return validity

def char_at_position(position, letter, word):
    return (word[position - 1] == letter)

def check_validity(occurenceA, occurenceB, letter, password):
    counter=0
    for pos in [occurenceA, occurenceB]:
        if char_at_position(pos, letter, password):
            counter += 1

    return (counter == 1)

# def letter_occurence(letter, password):
#     character_count = 0
#     for character in password:
#         if character == letter:
#             character_count+=1
#     return character_count

inputs_path = 'input.txt'

with open(inputs_path) as inputs_file:
    lines = inputs_file.readlines()

lines = [x.strip() for x in lines]

valid_password_count=0
for line in lines:
    if validate_password(line):
        valid_password_count+=1

print(valid_password_count)
