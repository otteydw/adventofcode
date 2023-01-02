import os
from collections import deque, defaultdict

# Part 1 was relatively easy.

# Part 2 was harder. With so many rounds my code was slow. I tried many methods to make it faster, such as incrementing the counter all at once
# and trying to use queues instead of lists. These did not speed it up enough.
# Instead, part 2 required knowing about Chinese Remainder Theorem which I had never heard about.
# Thanks to the following two resources for hints...
# https://www.reddit.com/r/adventofcode/comments/zifqmh/2022_day_11_solutions/
# https://github.com/mahakaal/adventofcode/blob/main/2022/day11/day11.py
monkey_divisor = 1


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    data = []

    with open(input_path) as input_file:
        for line in input_file:
            data.append(line.rstrip())

    return data


class Item:
    def __init__(self, worry_level=0):
        self.worry_level = int(worry_level)

    def relief(self, crt=False):
        global monkey_divisor
        if crt:
            self.worry_level = self.worry_level % monkey_divisor
        else:
            self.worry_level = self.worry_level // 3


class Monkey:
    def __init__(self, crt=False):
        self.items = deque()
        self.operation = None
        self.operand1 = None
        self.operand2 = None
        self.divisible_test = None
        self.true_target = None
        self.false_target = None
        self.items_inspected = 0
        self.crt = crt

    def process_text(self, text):
        global monkey_divisor
        if "Starting" in text:
            item_worry_levels = text.split(": ")[1].split(", ")
            for item_worry_level in item_worry_levels:
                item = Item(item_worry_level)
                self.items.append(item)
        elif "Operation" in text:
            self.operand1, self.operation, self.operand2 = text.split("= ")[1].split(
                " "
            )
            if self.operand1.isdigit():
                self.operand1 = int(self.operand1)
            if self.operand2.isdigit():
                self.operand2 = int(self.operand2)
        elif "Test" in text:
            self.divisible_test = int(text.split("divisible by ")[1])
            monkey_divisor = monkey_divisor * self.divisible_test
        elif "true" in text:
            self.true_target = int(text.split("throw to monkey ")[1])
        elif "false" in text:
            self.false_target = int(text.split("throw to monkey ")[1])

    def inspect_items(self):
        # Since we will inspect every item we currently have, just increment that value up front
        self.items_inspected += len(self.items)

        gifts = defaultdict(list)
        while len(self.items) > 0:
            item = self.items.pop()
            if self.operand1 == "old":
                operand1 = int(item.worry_level)
            else:
                operand1 = self.operand1
            if self.operand2 == "old":
                operand2 = int(item.worry_level)
            else:
                operand2 = self.operand2

            if self.operation == "+":
                item.worry_level = operand1 + operand2
            elif self.operation == "*":
                item.worry_level = operand1 * operand2

            item.relief(crt=self.crt)

            if item.worry_level % self.divisible_test == 0:
                target = self.true_target
            else:
                target = self.false_target
            gifts[target].append(item)
        return gifts

    def get_worry_levels(self):
        worry_levels = []
        for item in self.items:
            worry_levels.append(item.worry_level)
        return worry_levels


class Game:
    def __init__(self, input_filename, rounds=1, crt=False):
        self.load_monkeys(input_filename, crt=crt)
        # report(self.monkeys)

        for round in range(rounds):
            self.play_round()
            # print(f"Completed round {round+1} of {rounds}.")
            # report(self.monkeys)

        self.inspection_count_report()

    def send_gifts(self, gifts):
        for monkey_target, gifts_list in gifts.items():
            self.monkeys[monkey_target].items.extend(gifts_list)

    def play_round(self):
        for monkey in self.monkeys:
            # print(f"Monkey {monkey_number}:")
            # monkey.inspect_items(self.monkeys)
            gifts_to_send = monkey.inspect_items()
            self.send_gifts(gifts_to_send)

    def inspection_count_report(self):
        for monkey_number, monkey in enumerate(self.monkeys):
            print(
                f"Monkey {monkey_number} inspected items {monkey.items_inspected} times."
            )

    def monkey_business(self):
        items_inspected = []
        for monkey in self.monkeys:
            items_inspected.append(monkey.items_inspected)

        highest_items_inspected = sorted(items_inspected, reverse=True)
        return highest_items_inspected[0] * highest_items_inspected[1]

    def load_monkeys(self, filename, crt=False):
        data = load_from_file(filename)
        monkeys = []

        current_monkey = None
        for line in data:
            line_stripped = line.rstrip()
            if line_stripped == "":
                continue
            elif line_stripped.startswith("Monkey"):
                monkey = Monkey(crt=crt)
                monkeys.append(monkey)
                current_monkey = monkey
            else:
                current_monkey.process_text(line_stripped)
        self.monkeys = monkeys


def report(monkeys):
    for monkey_number, monkey in enumerate(monkeys):
        print(f"Monkey {monkey_number}: {monkey.get_worry_levels()}")


if __name__ == "__main__":

    # input_filename = "example.txt"
    input_filename = "input.txt"

    game = Game(input_filename, rounds=20, crt=False)
    print(f"Monkey business Part 1: {game.monkey_business()}")

    game = Game(input_filename, rounds=10000, crt=True)
    print(f"Monkey business Part 2: {game.monkey_business()}")
