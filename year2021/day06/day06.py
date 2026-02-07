import os
from collections import defaultdict


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


def number_of_lanternfish_orig(lanternfish_data, days):
    # Original version I wrote using the LanternFish class

    fishes = []
    for initial_fish_timer in lanternfish_data:
        fish = LanternFish(initial_fish_timer)
        fishes.append(fish)

    for day in range(days):
        print(f"At day {day} there are {len(fishes)} fish.")
        print(fishes)

        fishes_to_add = []
        for fish in fishes:
            spawn_new_fish = fish.decrement_age()
            if spawn_new_fish:
                new_fish = LanternFish(8)
                fishes_to_add.append(new_fish)
        fishes += fishes_to_add

    return len(fishes)


def number_of_lanternfish_unclassed(fish_timers, days):
    """Unclassed version

    The version that used the LanternFish class worked for part 1 but was not efficient for part 2 (256 days).

    I went online for some advice and found this video https://www.youtube.com/watch?v=yJjpXJm7x0o

    It seems the most efficient method for doing this would need to not care about each individual fish, but instead the
    frequency of each fish' starting timer.

    I rewrote my function to remove the LaternFish class, somewhat based on code from
    https://github.com/womogenes/AoC-2021-Solutions/blob/main/day_06/day_06_p1.py

    """

    for day in range(days):
        print(f"At day {day} there are {len(fish_timers)} fish.")

        next_fish_timers = []
        for fish_timer in fish_timers:
            if fish_timer == 0:
                next_fish_timers.append(6)
                next_fish_timers.append(8)
            else:
                next_fish_timers.append(fish_timer - 1)
        fish_timers = next_fish_timers

    return len(fish_timers)


def number_of_lanternfish_counters(fish_timers, days):
    """Frequency Counting version

    After I removed the class (above) it was still inefficient for part 2 (256 days).

    The advice from https://github.com/womogenes/AoC-2021-Solutions/blob/main/day_06/day_06_p2.py would be to use a frequency counter.

    I admit the following code looks almost identical to the above linked code, but I at least learned how to use the defaultdict.

    """

    frequencies = defaultdict(int)
    for fish_timer in fish_timers:
        frequencies[fish_timer] += 1

    for _ in range(days):
        new_frequencies = defaultdict(int)

        for fish_timer in frequencies:
            if fish_timer == 0:
                new_frequencies[6] += frequencies[fish_timer]
                new_frequencies[8] = frequencies[fish_timer]
            else:
                new_frequencies[fish_timer - 1] += frequencies[fish_timer]
        frequencies = new_frequencies

    sum_of_fish = 0
    for frequency in frequencies:
        sum_of_fish += frequencies[frequency]

    return sum_of_fish


if __name__ == "__main__":

    lanternfish_data = load_lanternfish_data("input.txt")
    print(number_of_lanternfish_counters(lanternfish_data, 80))
    print(number_of_lanternfish_counters(lanternfish_data, 256))
