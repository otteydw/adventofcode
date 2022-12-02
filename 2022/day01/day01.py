import os


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    data = []

    with open(input_path) as input_file:
        for line in input_file:
            data.append(line.rstrip())

    return data


def elves_calories(list_of_calories):
    elves = []
    current_calorie_total = 0
    for calorie in list_of_calories:
        if calorie != "":
            current_calorie_total += int(calorie)
        else:
            elves.append(current_calorie_total)
            current_calorie_total = 0

    elves.append(current_calorie_total)
    return elves


def most_calorie_elf(list_of_elves):
    return max(list_of_elves)


if __name__ == "__main__":

    input_filename = "input.txt"
    calorie_list = load_from_file(input_filename)
    these_calories = elves_calories(calorie_list)
    print(f"Most calories in a single elf: {most_calorie_elf(these_calories)}")
