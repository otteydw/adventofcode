import argparse
import pathlib


def parse(puzzle_input: str) -> list[str]:
    return [line for line in puzzle_input.splitlines()]


def split_list_on_empty_string(some_list: list[str], split_on: str = "") -> tuple[list[str], list[str]]:
    split_index = some_list.index(split_on)
    a = some_list[:split_index]
    b = some_list[split_index + 1 :]
    return (a, b)


def is_fresh(fresh_ranges: list[tuple[int, int]], id_to_check: int) -> bool:
    for fresh_range in fresh_ranges:
        range_min, range_max = fresh_range
        range_max += 1
        if id_to_check in range(range_min, range_max):
            return True
    return False


# Google AI Snippet
# I knew I needed to merge the intervals, but needed the function to do it.  (shrug)
def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current_start, current_end in intervals[1:]:
        last_merged_start, last_merged_end = merged[-1]

        if current_start <= last_merged_end:  # Overlap
            merged[-1] = (last_merged_start, max(last_merged_end, current_end))
        else:
            merged.append((current_start, current_end))
    return merged


def part1(data: list[str]) -> int:
    fresh_ingredient_range_strings, ingredient_id_strings = split_list_on_empty_string(data)
    fresh_ingredient_ranges = []
    for id_range in fresh_ingredient_range_strings:
        range_min_str, range_max_str = id_range.split("-")
        range_min = int(range_min_str)
        range_max = int(range_max_str)
        fresh_ingredient_ranges.append((range_min, range_max))

    ingredient_ids = [int(id) for id in ingredient_id_strings]

    return sum(1 for id in ingredient_ids if is_fresh(fresh_ingredient_ranges, id))


def part2(data: list[str]) -> int:
    fresh_ingredient_range_strings, _ = split_list_on_empty_string(data)
    fresh_ingredient_ranges = []

    for id_range in fresh_ingredient_range_strings:
        range_min_str, range_max_str = id_range.split("-")
        range_min = int(range_min_str)
        range_max = int(range_max_str) + 1
        fresh_ingredient_ranges.append((range_min, range_max))
    print(f"{len(fresh_ingredient_ranges)=}")
    all_fresh_id_intervals = merge_intervals(fresh_ingredient_ranges)
    print(f"{len(all_fresh_id_intervals)=}")
    fresh_id_count = 0
    for rng_min, rng_max in all_fresh_id_intervals:
        fresh_id_count += rng_max - rng_min
    return fresh_id_count


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
