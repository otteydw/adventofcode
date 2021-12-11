import os


class LanternFish:
    def __init__(self, internal_timer):
        self.internal_timer = internal_timer
        self.reset_timer_value = 6

    def reset(self):
        self.internal_timer = self.reset_timer_value

    def decrement_age(self):
        self.internal_timer -= 1
        if self.internal_timer < 0:
            self.reset()
            return True
        return False

    def __repr__(self):
        # return f"Internal timer: {self.internal_timer}"
        return str(self.internal_timer)


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    with open(input_path, "r") as input_file:
        lines = input_file.readlines()
        lines = [line.rstrip() for line in lines]

    return lines


def load_lanternfish_data(filename):
    data_as_string = load_from_file(filename)[0].split(",")
    data_as_ints = [int(x) for x in data_as_string]
    return data_as_ints


def number_of_lanternfish(lanternfish_data, days):

    fishes = []
    for initial_fish_timer in lanternfish_data:
        fish = LanternFish(initial_fish_timer)
        fishes.append(fish)

    for day in range(days):
        print(f"At day {day} there are {len(fishes)} fish.")
        # print(fishes)

        fishes_to_add = []
        for fish in fishes:
            spawn_new_fish = fish.decrement_age()
            if spawn_new_fish:
                new_fish = LanternFish(8)
                fishes_to_add.append(new_fish)
        fishes += fishes_to_add

    return len(fishes)


if __name__ == "__main__":

    lanternfish_data = load_lanternfish_data("input.txt")
    print(number_of_lanternfish(lanternfish_data, 80))
