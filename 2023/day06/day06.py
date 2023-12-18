import math
import pathlib
import sys
from collections import namedtuple

Race = namedtuple("Race", "time distance")


def parse(puzzle_input):
    return [line for line in puzzle_input.split("\n")]


def parse_data(data):
    times = [int(x) for x in data[0].split(":")[1].split()]
    distances = [int(x) for x in data[1].split(":")[1].split()]
    print(times, distances)
    print()
    races = []
    for time, max_distance in zip(times, distances):
        this_race = Race(time, max_distance)
        races.append(this_race)

    return races


def run_race(max_time, charge_time, distance_to_beat):
    moving_time = max_time - charge_time
    velocity = charge_time
    distance_moved = moving_time * velocity

    return distance_moved > distance_to_beat


def ways_to_win(max_time, distance_to_beat):
    wins = 0
    for charge_time_to_test in range(1, max_time):
        if run_race(max_time, charge_time_to_test, distance_to_beat):
            wins += 1

    return wins


def part1(data):
    my_ways_to_win = []
    race_info = parse_data(data)
    print(race_info)
    for race in race_info:
        my_ways_to_win.append(ways_to_win(race.time, race.distance))

    return math.prod(my_ways_to_win)


def part2(data):
    pass


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        for solution_number, solution in enumerate(solutions):
            print(f"Solution {solution_number}: {str(solution)}")
