# https://adventofcode.com/2020/day/6

# Some code copied from https://www.youtube.com/watch?v=_pPgnryUEDw


def get_data_from_file(filename):
    INPUTS_PATH = filename

    with open(INPUTS_PATH) as inputs_file:

        data = inputs_file.readlines()
        data = [line.strip() for line in data]

        return data


def get_unique_answer_all(responses):
    questions = []

    for char in responses[0]:
        inAllLines = True
        for line in responses:
            if char not in line:
                inAllLines = False

        if inAllLines and char not in questions:
            questions.append(char)
    # print(questions)
    return len(questions)


def main():

    data = get_data_from_file("input.txt")
    # print(data)

    sum = 0
    currentResponse = []
    for line in data:
        if line != "":
            currentResponse.append(line)
        else:
            sum += get_unique_answer_all(currentResponse)
            currentResponse = []

    sum += get_unique_answer_all(currentResponse)

    print(sum)


main()
