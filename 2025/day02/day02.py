import argparse
import pathlib
from itertools import batched


def parse(puzzle_input: str) -> list[str]:
    return [line for line in puzzle_input.splitlines()]


def valid_id(numeric_id: int) -> bool:
    id: str = str(numeric_id)
    if len(id) == 1:
        return True

    if len(id) % 2 != 0:
        return True

    mid = len(id) // 2

    first_half = id[:mid]
    second_half = id[mid:]

    return not (first_half == second_half)


def invalid_ids_from_range(id_range: str, part: int = 1) -> list[int]:
    range_min_str, range_max_str = id_range.split("-")
    range_min = int(range_min_str)
    range_max = int(range_max_str) + 1

    if part == 1:
        return [id for id in range(range_min, range_max) if not valid_id(id)]
    else:
        # Part 2
        return [id for id in range(range_min, range_max) if not p2_valid_id(id)]


def part1(data: list[str]) -> int:
    part_sum = 0
    line = data[0]
    id_ranges = line.split(",")
    for id_range in id_ranges:
        part_sum += sum(invalid_ids_from_range(id_range))

    return part_sum


def p2_valid_id(numeric_id: int) -> bool:
    id: str = str(numeric_id)
    mid = len(id) // 2
    batch_size_range = range(1, mid + 1)
    for batch_size in batch_size_range:
        batch = batched(id, batch_size)
        if len(set(batch)) == 1:
            return False
    return True


def part2(data: list[str]) -> int:
    part_sum = 0
    line = data[0]
    id_ranges = line.split(",")
    for id_range in id_ranges:
        part_sum += sum(invalid_ids_from_range(id_range, part=2))

    return part_sum


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
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        for solution_number, solution in enumerate(solutions, start=1):
            print(f"Solution {solution_number}: {str(solution)}")
