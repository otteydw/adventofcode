from functools import lru_cache

from sympy import divisors

# House 1 got 10 presents.
# House 2 got 30 presents.
# House 3 got 40 presents.
# House 4 got 70 presents.
# House 5 got 60 presents.
# House 6 got 120 presents.
# House 7 got 80 presents.
# House 8 got 150 presents.
# House 9 got 130 presents.
#
# While I initially tried to "brute force" the solution, it was very slow.
# I used ChatGPT to at least determine that this numberical pattern is
# "a well-known number theory function called the divisor sum function"


# This function ended up not being used after realizing it was some math function to solve the puzzle.
# Keeping it here since I had some tests written for it.
@lru_cache(maxsize=None)
def gifts_delivered_by_elf(elf_number: int, house_number: int) -> int:
    if not house_number % elf_number == 0:
        return 0

    gifts_delivered_per_house = 10 * elf_number
    return gifts_delivered_per_house


def gifts_delivered_to_house(house_number: int, multiplier: int = 10, limit: None | int = None) -> int:
    if not limit:
        return multiplier * sum(divisors(house_number))
    else:
        return multiplier * sum(d for d in divisors(house_number) if house_number // d <= limit)


def part1(puzzle_input: int) -> int:
    house = 1
    while True:
        delivered = gifts_delivered_to_house(house)
        print(f"House {house} received {delivered} gifts.")
        if delivered >= puzzle_input:
            return house
        house += 1


def part2(puzzle_input: int) -> int:
    house = 1
    while True:
        delivered = gifts_delivered_to_house(house, multiplier=11, limit=50)
        print(f"House {house} received {delivered} gifts.")
        if delivered >= puzzle_input:
            return house
        house += 1


def solve(puzzle_input: int) -> tuple[int | None, int | None]:
    """Solve the puzzle for the given input."""
    solve1 = True
    solve2 = True
    solution1 = part1(puzzle_input) if solve1 else None
    solution2 = part2(puzzle_input) if solve2 else None

    return solution1, solution2


if __name__ == "__main__":

    puzzle_input = 29000000
    solutions = solve(puzzle_input)
    for solution_number, solution in enumerate(solutions, start=1):
        print(f"Solution {solution_number}: {str(solution)}")
