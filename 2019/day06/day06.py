import argparse
import pathlib
from collections import defaultdict


def parse(puzzle_input):
    lines = [line for line in puzzle_input.split("\n")]
    print(lines)
    orbits = defaultdict(lambda: None)
    for line in lines:
        objectA, objectB = line.split(")")
        orbits[objectB] = objectA
    print(orbits)
    return orbits


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

    inner_object = orbit_dict[obj]
    orbits = 1 + total_orbits_for_object(orbit_dict, inner_object)

    return orbits


def slice_list_up_to_element(lst: list, element):
    """Given a list, return the slice of the list from beginning up to the first matching element"""
    index_of_element = lst.index(element)
    slice = lst[:index_of_element]
    return slice


def minimum_orbital_transfers(orbit_dict: dict, from_object: str, to_object: str):
    """Given orbit_dict, return the minimum number of orbital transfers required to move from from_object to to_object"""
    closest_ancestor = find_closest_common_ancestor(orbit_dict, from_object, to_object)

    from_orbit_tree = orbit_tree(orbit_dict, from_object)
    to_orbit_tree = orbit_tree(orbit_dict, to_object)

    from_orbit_to_common_slice = slice_list_up_to_element(from_orbit_tree, closest_ancestor)
    to_orbit_to_common_slice = slice_list_up_to_element(to_orbit_tree, closest_ancestor)

    transfers = len(from_orbit_to_common_slice) + len(to_orbit_to_common_slice)

    return transfers


def get_object_orbited_by_object(orbit_dict: dict, obj: str) -> str:
    """Given orbit_dict and the name of an object, return the object this object orbits."""
    return orbit_dict[obj]


def minimum_orbital_transfers_from_you_to_san(orbit_dict: dict):
    """Given orbit_dict, return the minimum number of orbital transfers required to move from the object YOU are orbiting to the object SAN is orbiting"""
    object_orbited_by_you = get_object_orbited_by_object(orbit_dict, "YOU")
    object_orbited_by_san = get_object_orbited_by_object(orbit_dict, "SAN")

    return minimum_orbital_transfers(orbit_dict, object_orbited_by_you, object_orbited_by_san)


def orbit_tree(orbit_dict: dict, obj: str):
    """Given orbit_dict and the name of an object, return the tree of orbits"""

    this_obj_orbits = get_object_orbited_by_object(orbit_dict, obj)
    if not this_obj_orbits:
        return [obj]

    return [obj] + orbit_tree(orbit_dict, this_obj_orbits)


def find_closest_common_ancestor(orbit_dict: dict, objectA: str, objectB: str):
    """Given orbit_dict and the name of two objects, find the closest common ancestor that they both orbit"""
    treeA = orbit_tree(orbit_dict, objectA)
    treeB = orbit_tree(orbit_dict, objectB)

    return next((ancestor for ancestor in treeA if ancestor in treeB), None)


def part1(data):
    return total_orbits_in_map(data)


def part2(data):
    return minimum_orbital_transfers_from_you_to_san(data)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solve1 = True
    solve2 = True
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
