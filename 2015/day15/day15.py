import argparse
import pathlib
from pprint import pprint
from typing import Generator


class Ingredient:
    def __init__(self, name: str, capacity: int, durability: int, flavor: int, texture: int, calories: int) -> None:
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    # def score(self, qunatity: int) -> int:
    #     return qunatity * (self.)
    def __repr__(self) -> str:
        return self.name


# def find_permutations_sum_to_target(target_sum: int, number_of_values: int):
#     # Generate all possible tuples of 4 integers where each integer is in range(101) (0 to 100)
#     # itertools.product is equivalent to nested for-loops
#     all_possible_values = product(range(target_sum + 1), repeat=number_of_values)

#     # Filter the results to include only those where the sum is 100
#     # permutations_list = [p for p in all_possible_values if sum(p) == target_sum]
#     permutations_comp = (p for p in all_possible_values if sum(p) == target_sum)

#     # return permutations_list
#     return permutations_comp


def sums_to_target(
    length: int, target_sum: int, current_tuple: tuple[int, ...] = ()
) -> Generator[tuple[int, ...], None, None]:
    """
    Generates all permutations of 'length' non-negative integers that sum to 'target_sum'.
    """
    if length == 1:
        yield current_tuple + (target_sum,)
    else:
        # Iterate from 0 up to the remaining sum for the current number
        for value in range(target_sum + 1):
            # Recursively call the function for the remaining length and remaining sum
            yield from sums_to_target(length - 1, target_sum - value, current_tuple + (value,))


def load_input(path: pathlib.Path) -> str:
    return pathlib.Path(path).read_text().strip()


def parse(puzzle_input: str) -> list[Ingredient]:
    # Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
    ingredients = []
    for line in puzzle_input.splitlines():
        line = line.replace(",", "").replace(":", "")
        line_split = line.split()
        name = line_split[0]
        capacity = int(line_split[2])
        durability = int(line_split[4])
        flavor = int(line_split[6])
        texture = int(line_split[8])
        calories = int(line_split[10])
        ingredient = Ingredient(
            name=name,
            capacity=capacity,
            durability=durability,
            flavor=flavor,
            texture=texture,
            calories=calories,
        )
        ingredients.append(ingredient)
    return ingredients


def calculate_score(ingredient_list: list[Ingredient], quantities: tuple[int, ...]) -> int:
    # print()
    print(f"{ingredient_list=}, {quantities=}")
    total_capacity = 0
    total_durability = 0
    total_flavor = 0
    total_texture = 0
    for idx, quantity in enumerate(quantities):
        name = ingredient_list[idx].name
        capacity = quantity * ingredient_list[idx].capacity
        durability = quantity * ingredient_list[idx].durability
        flavor = quantity * ingredient_list[idx].flavor
        texture = quantity * ingredient_list[idx].texture
        print(f"{name=}, {capacity=}, {durability=}, {flavor=}, {texture=}")
        total_capacity += capacity
        total_durability += durability
        total_flavor += flavor
        total_texture += texture
    total_capacity = max(0, total_capacity)
    total_durability = max(0, total_durability)
    total_flavor = max(0, total_flavor)
    total_texture = max(0, total_texture)
    print(f"{total_capacity=}, {total_durability=}, {total_flavor=}, {total_texture=}")
    score = total_capacity * total_durability * total_flavor * total_texture
    print()
    return score


def part1(data: list[Ingredient]) -> int:
    pprint(data)
    number_of_ingredient_types = len(data)
    max_ingredient_count = 100
    print(f"Permutations for {number_of_ingredient_types} ingredient types:")
    # permutations = find_permutations_sum_to_target(number_of_ingredient_types, max_ingredient_count)
    permutations = sums_to_target(length=number_of_ingredient_types, target_sum=max_ingredient_count)
    max_score = 0
    # permutations=[(50,50),(44,56)]
    for permutation in permutations:
        print(f"Calculating score for {permutation=}")
        score = calculate_score(data, permutation)
        prev_max_score = max_score
        max_score = max(score, max_score)
        if max_score != prev_max_score:
            max_permutation = permutation
    print(f"{max_score=} found at {max_permutation=}")
    return max_score


def part2(data: list[Ingredient]) -> int:  # type: ignore[empty-body]
    pass


def solve(puzzle_input: str) -> tuple[int | None, int | None]:
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
        puzzle_input = load_input(path)
        solutions = solve(puzzle_input)
        for solution_number, solution in enumerate(solutions, start=1):
            print(f"Solution {solution_number}: {str(solution)}")
