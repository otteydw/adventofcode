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


@lru_cache(maxsize=None)
def gifts_delivered_by_elf(elf_number: int, house_number: int) -> int:
    if not house_number % elf_number == 0:
        return 0

    gifts_delivered_per_house = 10 * elf_number
    return gifts_delivered_per_house


# @lru_cache(maxsize=None)
# def gifts_delivered_to_house(house_number: int) -> int:
#     gifts_delivered = 0
#     for elf in range(1, house_number+1):
#         gifts_delivered += gifts_delivered_by_elf(elf, house_number)
#     return gifts_delivered


def gifts_delivered_to_house(house_number: int) -> int:
    return 10 * sum(divisors(house_number))


def part1(puzzle_input: int) -> int:
    house = 1
    while True:
        delivered = gifts_delivered_to_house(house)
        print(f"House {house} received {delivered} gifts.")
        if delivered >= puzzle_input:
            return house
        house += 1


def part2(data: int) -> int:  # type: ignore[empty-body]
    pass


def solve(puzzle_input: int) -> tuple[int | None, int | None]:
    """Solve the puzzle for the given input."""
    # data = parse(puzzle_input)
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
