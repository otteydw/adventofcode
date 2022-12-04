import os


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    data = []

    with open(input_path) as input_file:
        for line in input_file:
            data.append(line.rstrip())

    return data


class Rucksack:
    def __init__(self, contents):
        self.rucksack_size = len(contents)
        self.compartment1 = contents[: (self.rucksack_size // 2)]
        self.compartment2 = contents[self.rucksack_size // 2 :]

        self.common_item = self.get_common_item()
        self.priority = self.get_priority()

    def get_common_item(self):
        for item in self.compartment1:
            if item in self.compartment2:
                return item

    def get_priority(self):
        if self.common_item == self.common_item.lower():
            difference = 96
        else:
            difference = 38
        priority = ord(self.common_item) - difference
        return priority


def sum_rucksack_priorities(rucksacks):
    priority_sum = 0
    for rucksack in rucksacks:
        this_sack = Rucksack(rucksack)
        priority_sum += this_sack.priority

    return priority_sum


if __name__ == "__main__":

    input_filename = "input.txt"

    all_rucksacks = load_from_file(input_filename)
    rucksack_priority_sum = sum_rucksack_priorities(all_rucksacks)
    print(f"Sum of priority of those items is: {rucksack_priority_sum}")
