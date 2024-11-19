import argparse
import pathlib
from collections import defaultdict


def parse(puzzle_input):
    lines = [line for line in puzzle_input.split("\n")]
    print(lines)
    orbits = defaultdict(list)
    for line in lines:
        # print(line)
        objectA, objectB = line.split(")")
        # orbits[objectA].append(objectB)
        orbits[objectB].append(objectA)
    print(orbits)
    return orbits


# def orbits_directly(orbit_dict: dict, objectA: str, objectB: str):
#     """ Based on orbit_dict, return True if objectA orbits directly around objectB"""
#     # return objectA in orbit_dict[objectB]
#     return objectB in orbit_dict[objectA]


def total_orbits_in_map(orbit_dict: dict) -> int:
    """Based on orbit_dict, return the total number of direct plus indirect orbits in this map."""
    orbits = 0
    for obj in orbit_dict:
        orbits += total_orbits_for_object(orbit_dict, obj)

    return orbits


def total_orbits_for_object(orbit_dict: dict, obj: str) -> int:
    """Given orbit_dict and name of object, return total number of orbits."""
    print(f"Checking for orbits in {obj=}")
    if obj not in orbit_dict:
        return 0

    orbits = 1
    for inner_object in orbit_dict[obj]:
        orbits += total_orbits_for_object(orbit_dict, inner_object)

    return orbits


def part1(data):
    return total_orbits_in_map(data)


def part2(data):
    pass


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solve1 = True
    solve2 = False
    solution1 = part1(data) if solve1 else None
    solution2 = part2(data) if solve2 else None

    return solution1, solution2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solve Advent of Code puzzles")
    parser.add_argument("files", nargs="+", help="Input files to process")
    args = parser.parse_args()

    for path in args.files:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        for solution_number, solution in enumerate(solutions):
            print(f"Solution {solution_number}: {str(solution)}")
