
# https://adventofcode.com/2020/day/6


def isBlank(myString):
    return not (myString and myString.strip())

# def get_fields_from_line(line):
#     fields_in_line = []
#     key_values = line.split(' ')
#     for key_value in key_values:
#         key, value = key_value.strip().split(':')
#         fields_in_line.append([key, value])
#     return fields_in_line

def get_batches_from_file(filename):
    INPUTS_PATH = filename

    with open(INPUTS_PATH) as inputs_file:
        lines = inputs_file.readlines()

    groups = []
    yes_responses = []
    for line in lines:
        if not isBlank(line):
            for letter in line.strip():
                yes_responses.append(letter)
        else:
            groups.append(set(yes_responses))
            yes_responses = []
    groups.append(set(yes_responses)) # Get the last one

    return groups


def main():
    batches = get_batches_from_file('input.txt')
    # batches = get_batches_from_file('input_small.txt')
    # batches = get_batches_from_file('examples.txt')

    # print(batches)
    all_response = []
    for batch in batches:
        for response in batch:
            all_response.append(response)

    print(len(all_response))

main()