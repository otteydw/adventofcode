import argparse
import math
import pathlib
import sys

import numpy as np


def parse(puzzle_input: str) -> list[str]:
    return [line for line in puzzle_input.splitlines()]


def data_to_array(data: list[str]) -> np.ndarray:
    array = []
    for row in data:
        array.append(row.split())
    array = np.array(array)
    return array


def data_to_array_p2(data: list[str]) -> np.ndarray:
    array = []
    for row in data:
        columns = []
        for character in row:
            # print(f"Char is {character}")
            columns.append(character)
        array.append(columns)
    # from pprint import pprint
    # pprint(array)
    print(array)
    # sys.exit()
    # for row in array:
    #     print(f"{len(row)=}")

    # max_length = max(len(row) for row in array)
    # print(f"{max_length=}")
    # array = [np.pad(row, (0, max_length - len(row)), 'constant', constant_values=' ') for row in array]
    # print()
    # for row in array:
    #     print(f"{len(row)=}")
    array = np.array(array)
    # print(array)
    # sys.exit()
    return array


def part1(data: list[str]) -> int:
    grid_array = data_to_array(data)
    # print(grid_array)
    # return
    grid_array_t = grid_array.T
    total = 0
    for row in grid_array_t:
        operator = row[-1]
        operands = [int(x) for x in row[:-1]]
        print(f"{operator=}, {operands=}")
        if operator == "+":
            total += sum(operands)
        elif operator == "*":
            total += math.prod(operands)
        else:
            sys.exit("Unexpected operator!")
    return total


def part2(data: list[str]) -> int:
    grid_array = data_to_array_p2(data)
    # print(grid_array)
    # sys.exit()
    operators = np.flip(grid_array[-1])
    operands = np.flipud(grid_array[:-1].T)

    # operators = [operator for operator in operators if operator is not None]
    operators = [operator for operator in operators if operator != " "]

    print()
    print("Operators")
    print(operators)
    print("Operands")
    print(operands)
    print()
    # sys.exit()
    total = 0
    numbers = []
    compute = False
    for row_num, row in enumerate(operands):
        print(row)
        if (row == " ").all():
            compute = True
        else:
            number = int("".join([x for x in row if x != " "]))
            numbers.append(number)
        if row_num == len(operands) - 1:
            compute = True
        # print(number)
        # print()
        if compute:
            operator = operators.pop(0)
            print(f"I will {operator} on {numbers} = ", end="")
            if operator == "+":
                this_compute = sum(numbers)
            elif operator == "*":
                this_compute = math.prod(numbers)
            else:
                sys.exit(f"Unexpected operator! {operator}")
            print(this_compute)
            total += this_compute
            numbers = []
            compute = False
    return total


def solve(puzzle_input: str) -> tuple[int | None, int | None]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    # print(data)
    # sys.exit()
    # data=puzzle_input
    solve1 = False
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
        # puzzle_input = pathlib.Path(path).read_text().strip()
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        for solution_number, solution in enumerate(solutions, start=1):
            print(f"Solution {solution_number}: {str(solution)}")
