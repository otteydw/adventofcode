import argparse
import itertools
import pathlib
from math import inf
from typing import Any

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


def to_list(s: str) -> list[int]:
    if isinstance(eval(s), int):
        return [(eval(s))]
    return list(eval(s))


def get_all_combinations(input_list: list[list[int]]) -> Any:
    all_combinations: Any = []
    # Iterate from length 0 to the full length of the list
    for r in range(len(input_list) + 1):
        # Generate combinations of length r
        combs_r = itertools.combinations(input_list, r)
        # Extend the main list with these combinations
        all_combinations.extend(combs_r)

    # Convert tuples to lists for final output if desired
    # return [list(c) for c in all_combinations]
    return all_combinations


class Machine:
    def __init__(self, initiator_lines: str) -> None:

        initiator = initiator_lines.split(" ")

        self.desired_state = [char for char in initiator[0][1:-1]]

        bw_schematics = initiator[1:-1]
        self.bw_schematics = [to_list(thing) for thing in bw_schematics]

        self.joltage_requirements = [int(n) for n in initiator[-1][1:-1].split(",")]
        self.reset()

    def push(self, button: list[int]) -> None:
        for wire in button:
            self.state[wire] = "#" if self.state[wire] == "." else "."

    def push_joltage(self, button: list[int]) -> None:
        for wire in button:
            self.joltage[wire] += 1

    def reset(self) -> None:
        self.state = len(self.desired_state) * ["."]
        self.joltage = len(self.joltage_requirements) * [0]

    def state_matches(self) -> bool:
        return self.state == self.desired_state

    def find_fewest_pressed(self) -> int:
        fewest = inf
        for button_combination in get_all_combinations(self.bw_schematics):
            self.reset()
            presses = 0
            for button in button_combination:
                self.push(button)
                presses += 1
                if presses > fewest:
                    break
            if self.state_matches() and presses < fewest:
                fewest = int(presses)

        return int(fewest)

    def joltage_array(self) -> np.ndarray:
        # A_eq = np.array(
        #     [
        #         [1, 0, 1, 1, 0],  #
        #         [0, 0, 0, 1, 1],  #
        #         [1, 1, 0, 1, 1],  #
        #         [1, 1, 0, 0, 1],  #
        #         [1, 0, 1, 0, 1],  #
        #     ]
        # )
        # b_eq = np.array([7, 5, 12, 7, 2])

        grid = []

        for idx, requirement in enumerate(self.joltage_requirements):
            row = [1 if idx in button else 0 for button in self.bw_schematics]
            grid.append(row)
        return np.array(grid)

    def optimized_buttons_for_joltage(self) -> int:
        # Given:  (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
        # Converted to:
        #    [[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]]
        #    [3, 5, 4, 7]
        #
        # Solve for:
        #   e + f = 3
        #   b + f = 5
        #   c + d + e = 4
        #   a + b + d = 7

        # array_size = len(self.joltage_requirements)
        array_size = len(self.bw_schematics)
        c = np.ones(array_size)

        A_eq = self.joltage_array()
        b_eq = self.joltage_requirements

        constraints = LinearConstraint(A_eq, b_eq, b_eq)

        # Non-negative bounds
        bounds = Bounds(lb=[0] * array_size, ub=[np.inf] * array_size)

        # All variables must be integers
        integrality = np.ones(array_size, dtype=int)
        result = milp(
            c=c,
            constraints=constraints,
            bounds=bounds,
            integrality=integrality,
        )
        return int(result.fun)

    def __repr__(self) -> str:
        desired = "".join(self.desired_state)
        state = "".join(self.state)
        repr = f"Machine\nDES: {desired}\nCUR: {state}\nBUT: {self.bw_schematics}\nJOL_REQ: {self.joltage_requirements}\nJOL_CUR: {self.joltage}\n{self.joltage_array()}"
        return repr


def load_input(path: pathlib.Path) -> str:
    return pathlib.Path(path).read_text().strip()


def parse(puzzle_input: str) -> list[str]:
    return [line for line in puzzle_input.splitlines()]


def part1(data: list[str]) -> int:
    total = 0
    for line in data:
        machine = Machine(line)
        # print(machine)
        total += machine.find_fewest_pressed()
        # print(f"Fewest is {fewest}")
        # total += fewest
    return total


def part2(data: list[str]) -> int:
    total = 0
    for line in data:
        machine = Machine(line)
        # print(machine)
        total += machine.optimized_buttons_for_joltage()
        # print(f"Fewest is {fewest}")
        # total += fewest
    return total


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
