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
        self.contents = contents
        self.rucksack_size = len(self.contents)
        self.compartment1 = self.contents[: (self.rucksack_size // 2)]
        self.compartment2 = self.contents[self.rucksack_size // 2 :]
        self.common_item = self.get_common_item()
        self.priority = get_priority(self.common_item)

    def get_common_item(self):
        for item in self.compartment1:
            if item in self.compartment2:
                return item


class ElfGroup:
    def __init__(self, group_of_rucksacks):
        self.group_of_rucksacks = group_of_rucksacks
        self.common_item = self.get_common_item()
        self.priority = get_priority(self.common_item)

    def get_common_item(self):
        for item in self.group_of_rucksacks[0].contents:
            if (
                item in self.group_of_rucksacks[1].contents
                and item in self.group_of_rucksacks[2].contents
            ):
                return item


def get_priority(item):
    if item == item.lower():
        difference = 96
    else:
        difference = 38
    priority = ord(item) - difference
    return priority


# https://stackoverflow.com/questions/434287/how-to-iterate-over-a-list-in-chunks
def chunker(seq, size):
    return (seq[pos : pos + size] for pos in range(0, len(seq), size))


def sum_rucksack_priorities(rucksacks):
    priority_sum = 0
    for rucksack in rucksacks:
        this_sack = Rucksack(rucksack)
        priority_sum += this_sack.priority

    return priority_sum


def sum_group_priorities(rucksacks):
    priority_sum = 0
    for chunk in chunker(rucksacks, 3):
        group = []
        for rucksack in chunk:
            this_sack = Rucksack(rucksack)
            group.append(this_sack)
        this_group = ElfGroup(group)
        priority_sum += this_group.priority

    return priority_sum


if __name__ == "__main__":

    input_filename = "input.txt"

    all_rucksacks = load_from_file(input_filename)

    rucksack_priority_sum = sum_rucksack_priorities(all_rucksacks)
    print(f"Sum of priority of those items is: {rucksack_priority_sum}")

    group_priority_sum = sum_group_priorities(all_rucksacks)
    print(f"Sum of priority of the group items is: {group_priority_sum}")
