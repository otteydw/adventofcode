import os

from collections import deque
from queue import SimpleQueue

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

    def relief(self):
        self.worry_level = self.worry_level // 3
        # print(
        #     f"    Monkey gets bored with item. Worry level is divided by 3 to {self.worry_level}."
        # )


class Monkey:
    def __init__(self, relief_enabled=True):
        # self.items = deque()
        self.items = SimpleQueue()
        self.operation = None
        self.operand1 = None
        self.operand2 = None
        self.divisible_test = None
        self.true_target = None
        self.false_target = None
        self.items_inspected = 0
        self.relief_enabled = relief_enabled

    def process_text(self, text):
        if "Starting" in text:
            item_worry_levels = text.split(": ")[1].split(", ")
            for item_worry_level in item_worry_levels:
                item = Item(item_worry_level)
                # self.items.append(item)
                self.items.put_nowait(item)
        elif "Operation" in text:
            self.operand1, self.operation, self.operand2 = text.split("= ")[1].split(
                " "
            )
        elif "Test" in text:
            self.divisible_test = int(text.split("divisible by ")[1])
        elif "true" in text:
            self.true_target = int(text.split("throw to monkey ")[1])
        elif "false" in text:
            self.false_target = int(text.split("throw to monkey ")[1])

    def inspect_items(self, monkeys):
        # for item in list(self.items):  # iterate over a copy of the list so we can manipulate the list
        # while len(self.items) > 0:
        while not self.items.empty():
            # item = self.items.popleft()
            item = self.items.get()
            self.items_inspected += 1
            # print(f"  Monkey inspects an item with worry_level {item.worry_level}.")
            operand1 = self.operand1
            if operand1 == "old":
                operand1 = int(item.worry_level)
            else:
                operand1 = int(operand1)
            operand2 = self.operand2
            if operand2 == "old":
                operand2 = int(item.worry_level)
            else:
                operand2 = int(operand2)
            if self.operation == "+":
                item.worry_level = operand1 + operand2
            if self.operation == "*":
                item.worry_level = operand1 * operand2
                # print(
                #     f"    Worry level is multiplied by {operand2} to {item.worry_level}."
                # )

            if self.relief_enabled:
                item.relief()

            if item.worry_level % self.divisible_test == 0:
                target = self.true_target
                # print(f"    Current worry level is divisible by {self.divisible_test}.")
            else:
                target = self.false_target
                # print(
                #     f"    Current worry level is not divisible by {self.divisible_test}."
                # )

            # print(
            #     f"    Item with worry level {item.worry_level} is thrown to monkey {target}."
            # )
            # self.items.remove(item)
            # monkeys[target].items.append(item)
            monkeys[target].items.put_nowait(item)

    def get_worry_levels(self):
        worry_levels = []
        for item in self.items:
            worry_levels.append(item.worry_level)
        return worry_levels


class Game:
    def __init__(self, input_filename, rounds=1, relief_enabled=True):
        self.load_monkeys(input_filename, relief_enabled=relief_enabled)
        # report(self.monkeys)

        for round in range(rounds):
            self.play_round()
            # print()
            # print(
            #     f"After round {round+1}, the monkeys are holding items with these worry levels:"
            # )
            print(f"Complete round {round+1} of {rounds}.")
            # report(self.monkeys)

        self.inspection_count_report()

    def play_round(self):
        for monkey_number, monkey in enumerate(self.monkeys):
            # print(f"Monkey {monkey_number}:")
            monkey.inspect_items(self.monkeys)

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


    def load_monkeys(self, filename, relief_enabled=True):
        data = load_from_file(filename)
        monkeys = []

        current_monkey = None
        for line in data:
            line_stripped = line.rstrip()
            if line_stripped == "":
                continue
            elif line_stripped.startswith("Monkey"):
                monkey = Monkey(relief_enabled=relief_enabled)
                monkeys.append(monkey)
                current_monkey = monkey
            else:
                current_monkey.process_text(line_stripped)
        self.monkeys = monkeys


def report(monkeys):
    for monkey_number, monkey in enumerate(monkeys):
        print(f"Monkey {monkey_number}: {monkey.get_worry_levels()}")


if __name__ == "__main__":

    input_filename = "example.txt"
    # input_filename = "input.txt"
    game = Game(input_filename, rounds=20)
    print(f"Monkey business: {game.monkey_business()}")
