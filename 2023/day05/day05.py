import pathlib
import sys
from typing import List
from more_itertools import split_at, grouper
from functools import lru_cache
from itertools import repeat


# from pprint import pprint as print

def parse(puzzle_input):
    return [line for line in puzzle_input.split("\n")]

class Map():
    def __init__(self, mapping_data):
        self.name = mapping_data[0].split()[0]
        self.source, self.destination = self.name.split('-to-')
        self.maps = self.parse_map_data(mapping_data[1:])

    def parse_map_data(self, mapping_data):
        maps = []

        for mapping_data_row in mapping_data:
            destination, source, range = [int(value) for value in mapping_data_row.split()]
            this_map = {
                'destination': destination,
                'source': source,
                'range': range
            }
            maps.append(this_map)

        return maps

    @lru_cache(maxsize=None)
    def process(self, input_value):
        for map in self.maps:
            if map['source'] <= input_value <= map['source'] + map['range']:
                difference = input_value - map['source']
                return map['destination'] + difference

        return input_value


    def __repr__(self):

        return f"{self.source} to {self.destination} | {self.maps}"

def extract_maps(data: List[str]):
    # seeds = [int(seed_number) for seed_number in data.pop(0).split(': ')[1].split()]
    # print(data)
    map_chunks = list(split_at(data[1:], lambda x: x.strip() == ''))

    maps = {}
    for map_chunk in map_chunks:
        this_map = Map(map_chunk)
        maps[this_map.source] = this_map

    # print(seeds)
    # print(maps)

    return maps

# @lru_cache(maxsize=None)
def process_seed(map, seed):

    soil = map['seed'].process(seed)
    fertilizer = map['soil'].process(soil)
    water = map['fertilizer'].process(fertilizer)
    light = map['water'].process(water)
    temperature = map['light'].process(light)
    humidity = map['temperature'].process(temperature)
    location = map['humidity'].process(humidity)

    return location

def part1(data: List[str]):
    seeds = [int(seed_number) for seed_number in data.pop(0).split(': ')[1].split()]
    maps = extract_maps(data)

    lowest_location = min([process_seed(maps, seed) for seed in seeds])
    return lowest_location

def part2(data: List[str]):
    seed_data = [int(seed_number) for seed_number in data.pop(0).split(': ')[1].split()]
    print(seed_data)

    seed_data_pairs = grouper(seed_data, 2)

    maps = extract_maps(data)

    # print(list(seed_data_pairs))

    lowest_locations = []
    # print(len(list(seed_data_pairs)))
    for seed_data_pair in seed_data_pairs:
        print(seed_data_pair)
        seed_start, seed_range = seed_data_pair
        # seeds += [seed for seed in ]
        # lowest_location = min([process_seed(maps, seed) for seed in range(seed_start, seed_start + seed_range)])
        lowest_location = min(map(process_seed, repeat(maps), range(seed_start, seed_start + seed_range)))
        lowest_locations.append(lowest_location)

    lowest_location = min(lowest_locations)

    return lowest_location


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    data = parse(puzzle_input)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        for solution_number, solution in enumerate(solutions):
            print(f"Solution {solution_number}: {str(solution)}")
