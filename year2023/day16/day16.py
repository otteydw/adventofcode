import copy
import os
import pathlib
import sys
from time import sleep

import numpy as np


def parse(puzzle_input):
    return [line for line in puzzle_input.split("\n")]


class Beam:
    def __init__(self, position, direction) -> None:
        self.row, self.column = position
        self.direction = direction

    def move(self, direction):
        match direction:
            case "left":
                self.column -= 1
            case "right":
                self.column += 1
            case "up":
                self.row -= 1
            case "down":
                self.row += 1

    def position(self):
        return (self.row, self.column)

    def __repr__(self):
        return f"{self.position()} {self.direction}"

    def __eq__(self, other) -> bool:
        return self.row == other.row and self.column == other.column and self.direction == other.direction


class Grid:
    def __init__(self, grid_array, start_position=(0, -1), start_direction="right"):
        self.grid = grid_array
        self.height = len(self.grid)
        self.width = len(self.grid[0])
        self.energized = set()
        self.beams = []
        self.add_beam(Beam(start_position, start_direction), energize=False)
        self.splits_triggered = set()
        self.mirrors_triggered = set()

    def add_beam(self, beam, energize=True):
        self.beams.append(beam)
        if energize:
            self.energize(beam.position())

    def __repr__(self):
        output = ""
        for row in self.grid:
            for character in row:
                output += character
            output += "\n"
        output += "\n"
        output += str(self.beams)
        output += "\n"
        output += f"Energized: {str(self.energized)}"
        return output

    def out_of_bounds(self, beam):
        return beam.row < 0 or beam.row > self.height - 1 or beam.column < 0 or beam.column > self.width - 1

    def energize(self, coordinate):
        self.energized.add(coordinate)

    def show_energized(self):
        energized_grid = np.full_like(self.grid, ".")

        for row, column in self.energized:
            energized_grid[row][column] = "#"

        output = ""
        for row in energized_grid:
            for character in row:
                output += character if character != "" else " "
            output += "\n"
        print(output)

    def show_state(self):
        state_grid = copy.deepcopy(self.grid)

        for beam in self.beams:
            row, column = beam.position()
            state_grid[row][column] = "#"
        output = ""
        for row in state_grid[:10]:
            for character in row:
                output += character if character != "" else " "
            output += "\n"
        print(output)
        print(f"{len(self.beams)} beams: {str(self.beams)}")
        print(f"{len(self.splits_triggered)} splits: {str(self.splits_triggered)}")
        print(f"{len(self.mirrors_triggered)} mirrors: {str(self.mirrors_triggered)}")

    def interact(self, beam):
        row, column = beam.position()
        current_direction = beam.direction
        grid_content = self.grid[row][column]

        outcome = current_direction
        match grid_content:
            case "\\":
                match current_direction:
                    case "right":
                        outcome = "down"
                    case "left":
                        outcome = "up"
                    case "down":
                        outcome = "right"
                    case "up":
                        outcome = "left"
            case "/":
                match current_direction:
                    case "right":
                        outcome = "up"
                    case "left":
                        outcome = "down"
                    case "down":
                        outcome = "left"
                    case "up":
                        outcome = "right"
            case "|":
                if current_direction in ["left", "right"]:
                    outcome = "split_ud"
            case "-":
                if current_direction in ["up", "down"]:
                    outcome = "split_lr"
        return outcome

    def go(self, show_progress=False):
        while len(self.beams) > 0:
            if show_progress:
                os.system("clear")
            new_beams = []
            old_beams = []
            for beam in self.beams:
                beam.move(beam.direction)
                if self.out_of_bounds(beam):
                    self.beams.remove(beam)
                    continue
                self.energize(beam.position())

                if (beam.position(), beam.direction) in self.mirrors_triggered:
                    old_beams.append(beam)
                else:
                    original_direction = beam.direction
                    beam.direction = self.interact(beam)
                    if beam.direction in ["left", "right", "up", "down"] and beam.direction != original_direction:
                        self.mirrors_triggered.add((beam.position(), original_direction))
                    elif beam.direction == "split_ud":
                        if beam.position() not in self.splits_triggered:
                            beam.direction = "up"
                            new_beam = Beam(beam.position(), "down")
                            new_beams.append(new_beam)
                            self.splits_triggered.add(beam.position())
                        else:
                            old_beams.append(beam)
                    elif beam.direction == "split_lr":
                        if beam.position() not in self.splits_triggered:
                            beam.direction = "left"
                            new_beam = Beam(beam.position(), "right")
                            new_beams.append(new_beam)
                            self.splits_triggered.add(beam.position())
                        else:
                            old_beams.append(beam)

            for beam in new_beams:
                self.add_beam(beam)

            for beam in old_beams:
                self.beams.remove(beam)

            if show_progress:
                self.show_state()
                sleep(0.5)


def potential_starting_positions(grid_array):
    height = len(grid_array)
    width = len(grid_array)
    starting_positions = []

    for row in range(height):
        starting_positions.append((row, -1, "right"))
        starting_positions.append((row, width, "left"))

    for column in range(width):
        starting_positions.append((-1, column, "down"))
        starting_positions.append((height, column, "up"))

    return starting_positions


def data_to_array(data):
    array = []
    for row in data:
        array.append([character for character in row])
    array = np.array(array)
    return array


def part1(data):
    grid_array = data_to_array(data)
    grid = Grid(grid_array)
    print(grid)
    grid.go()
    # grid.go(show_progress=True)
    print()
    grid.show_energized()
    return len(grid.energized)


def part2(data):
    grid_array = data_to_array(data)
    starting_positions = potential_starting_positions(grid_array)
    print(starting_positions)
    max_energized = 0
    for row, column, direction in starting_positions:
        grid = Grid(grid_array, start_position=(row, column), start_direction=direction)
        grid.go()
        max_energized = max(max_energized, len(grid.energized))

    return max_energized


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        for solution_number, solution in enumerate(solutions):
            print(f"Solution {solution_number}: {str(solution)}")
