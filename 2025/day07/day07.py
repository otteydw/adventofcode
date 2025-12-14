import argparse
import pathlib

import numpy as np


def load_input(path: pathlib.Path) -> str:
    return pathlib.Path(path).read_text().strip()


def parse(puzzle_input: str) -> list[str]:
    return [line for line in puzzle_input.splitlines()]


def data_to_array(data: list[str]) -> np.ndarray:
    array = []
    for row in data:
        columns = []
        for character in row:
            columns.append(character)
        array.append(columns)
    array = np.array(array)
    return array


class Coordinate:
    def __init__(self, value: str) -> None:
        # self.value = value
        self.start = value == "S"
        self.splitter = value == "^"
        self.beam = self.start

    def __repr__(self) -> str:
        if self.start:
            return "S"
        elif self.splitter:
            return "^"
        elif self.beam:
            return "|"
        else:
            return "."


# def print_array(array) -> None:
# for row_num, row in enumerate(array):
#     for col_num, col in enumerate(row):
#         if col == "S":
#             print(col, end="")
#         elif col == "^":
#             print(col, end="")
#         elif beams[row]
#     print()

# for array_row, beam_row in zip(array, beams):
#     for array_col, beam_col in zip(array_row, beam_row):
#         if array_col == "S":
#             printable=array_col
#         elif beam_col == "|":
#             printable="|"
#         else:
#             printable=array_col
#         print(printable, end="")
#     print()


def part1(data: list[str]) -> int:
    array = data_to_array(data)
    array = np.vectorize(Coordinate, otypes=[object])(array)
    print(array)
    # beams = np.full_like(array, None, dtype=object)
    # beams = array.copy()
    # beams[beams == "S"] = "|"
    # print_array(array, beams)
    last_row = len(array) - 1
    splits = 0
    for row_num, row in enumerate(array):
        if row_num == last_row:
            break
        for col_num, coord in enumerate(row):
            # print(f"Checking coordinate {coord}")
            if coord.beam and not coord.splitter:
                array[row_num + 1][col_num].beam = True
            elif coord.splitter and array[row_num - 1][col_num].beam:
                array[row_num + 1][col_num - 1].beam = True
                array[row_num + 1][col_num + 1].beam = True
                splits += 1
    print()
    print(array)
    # print()
    # print_array(array, beams)

    return splits


def part2(data: list[str]) -> int:  # type: ignore[empty-body]
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
