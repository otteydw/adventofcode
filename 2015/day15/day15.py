import argparse
import pathlib
from dataclasses import dataclass
from typing import Iterator


@dataclass(frozen=True)
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

    def __str__(self) -> str:
        return self.name


def sums_to_target(length: int, target_sum: int) -> Iterator[tuple[int, ...]]:
    """
    Yield all tuples of `length` non-negative integers whose elements sum to
    `target_sum`.

    Each yielded tuple represents a composition of `target_sum` into exactly
    `length` parts. Values are generated lazily and tuples are produced in
    lexicographic order with respect to their elements.

    Args:
        length: The number of integers in each tuple. Must be >= 1.
        target_sum: The total sum of the integers in each tuple. Must be >= 0.

    Yields:
        Tuples of length `length` containing non-negative integers that sum to
        `target_sum`.

    Raises:
        RecursionError: If `length` is very large due to recursive depth.
    """
    if length == 1:
        yield (target_sum,)
        return

    for value in range(target_sum + 1):
        yield from ((value,) + tail for tail in sums_to_target(length - 1, target_sum - value))


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


def calculate_score(
    ingredient_list: list[Ingredient], quantities: tuple[int, ...], desired_calories: int | None = None
) -> int:
    print(f"{ingredient_list=}, {quantities=}")
    total_capacity = 0
    total_durability = 0
    total_flavor = 0
    total_texture = 0
    total_calories = 0
    for idx, quantity in enumerate(quantities):
        name = ingredient_list[idx].name
        capacity = quantity * ingredient_list[idx].capacity
        durability = quantity * ingredient_list[idx].durability
        flavor = quantity * ingredient_list[idx].flavor
        texture = quantity * ingredient_list[idx].texture
        calories = quantity * ingredient_list[idx].calories
        print(f"{name=}, {capacity=}, {durability=}, {flavor=}, {texture=}")
        total_capacity += capacity
        total_durability += durability
        total_flavor += flavor
        total_texture += texture
        total_calories += calories

    if desired_calories and total_calories != desired_calories:
        return 0

    total_capacity = max(0, total_capacity)
    total_durability = max(0, total_durability)
    total_flavor = max(0, total_flavor)
    total_texture = max(0, total_texture)
    print(f"{total_capacity=}, {total_durability=}, {total_flavor=}, {total_texture=}")
    score = total_capacity * total_durability * total_flavor * total_texture
    print()
    return score


def part1(data: list[Ingredient], desired_calories: int | None = None) -> int:
    number_of_ingredient_types = len(data)
    max_ingredient_count = 100
    permutations = sums_to_target(length=number_of_ingredient_types, target_sum=max_ingredient_count)
    max_score = 0
    for permutation in permutations:
        score = calculate_score(data, permutation, desired_calories)
        # prev_max_score = max_score
        max_score = max(score, max_score)
    #     if max_score != prev_max_score:
    #         max_permutation = permutation
    # print(f"{max_score=} found at {max_permutation=}")
    return max_score


def part2(data: list[Ingredient]) -> int:
    return part1(data, desired_calories=500)


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
