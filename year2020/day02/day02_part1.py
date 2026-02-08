# mypy: ignore-errors
# https://adventofcode.com/2020/day/2


def parse_line(line):
    quantity, letter, password = line.split(" ")

    min_occurence = int(quantity.split("-")[0])
    max_occurence = int(quantity.split("-")[1])
    letter = letter.split(":")[0]
    return min_occurence, max_occurence, letter, password


def validate_password(line):
    min_occurence, max_occurence, letter, password = parse_line(line)
    char_occurences = letter_occurence(letter, password)

    validity = min_occurence <= char_occurences <= max_occurence

    return validity


def letter_occurence(letter, password):
    character_count = 0
    for character in password:
        if character == letter:
            character_count += 1
    return character_count


inputs_path = "input.txt"

with open(inputs_path) as inputs_file:
    lines = inputs_file.readlines()

lines = [x.strip() for x in lines]

valid_password_count = 0
for line in lines:
    if validate_password(line):
        valid_password_count += 1

print(valid_password_count)
