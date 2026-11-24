# mypy: ignore-errors
import pathlib
import sys
from dataclasses import dataclass


def parse(puzzle_input):
    return [line for line in puzzle_input.split("\n")]


@dataclass(repr=False, frozen=True)
class Part:
    row: int
    start_column: int
    end_column: int
    number: int

    def __repr__(self):
        return str(self.number)


def create_schematic(data):
    schematic = []
    current_part_number = ""

    for row_position, row in enumerate(data):
        schematic_row = []
        for character_position, character in enumerate(row):
            if character == ".":
                character = ""

            schematic_row.append(character)

            if character.isdigit():
                current_part_number += character

                if character_position == len(row) - 1 or not row[character_position + 1].isdigit():
                    print(current_part_number)
                    this_part = Part(
                        row=row_position,
                        start_column=character_position - len(current_part_number) + 1,
                        end_column=character_position,
                        number=int(current_part_number),
                    )
                    for part_number_position in range(len(current_part_number)):
                        schematic_row[character_position - part_number_position] = this_part

                    current_part_number = ""

        schematic.append(schematic_row)

    return schematic


def get_surrounding_positions(row, column, grid):
    MAX_ROW = len(grid)
    MAX_COLUMN = len(grid[0])

    surrounding_positions = set()

    # Left
    if column - 1 >= 0:
        surrounding_positions.add((row, column - 1))

    # Right
    if column + 1 <= MAX_COLUMN:
        surrounding_positions.add((row, column + 1))

    # Above
    if row - 1 >= 0:
        surrounding_positions.add((row - 1, column))

        # Above, Left
        if column - 1 >= 0:
            surrounding_positions.add((row - 1, column - 1))

        # Above, Right
        if column + 1 <= MAX_COLUMN:
            surrounding_positions.add((row - 1, column + 1))

    # Below
    if row + 1 <= MAX_ROW:
        surrounding_positions.add((row + 1, column))

        # Below, Left
        if column - 1 >= 0:
            surrounding_positions.add((row + 1, column - 1))

        # Below, Right
        if column + 1 <= MAX_COLUMN:
            surrounding_positions.add((row + 1, column + 1))

    return surrounding_positions


def get_part_numbers(schematic):
    parts = set()

    for row_number, row in enumerate(schematic):
        for column_number, column_content in enumerate(row):
            if not (column_content == "" or isinstance(column_content, Part)):
                surrounding_positions = get_surrounding_positions(row_number, column_number, schematic)
                # print(surrounding_positions)
                for surrounding_position in surrounding_positions:
                    if isinstance(
                        schematic[surrounding_position[0]][surrounding_position[1]],
                        Part,
                    ):
                        parts.add(schematic[surrounding_position[0]][surrounding_position[1]])

    part_numbers = [part.number for part in parts]

    return part_numbers


def get_gear_ratios(schematic):
    gear_ratios = []

    for row_number, row in enumerate(schematic):
        for column_number, column_content in enumerate(row):
            if not (column_content == "" or isinstance(column_content, Part)):
                adjacent_parts = set()
                surrounding_positions = get_surrounding_positions(row_number, column_number, schematic)
                # print(surrounding_positions)
                for surrounding_position in surrounding_positions:
                    if isinstance(
                        schematic[surrounding_position[0]][surrounding_position[1]],
                        Part,
                    ):
                        adjacent_parts.add(schematic[surrounding_position[0]][surrounding_position[1]])

                if len(adjacent_parts) == 2:
                    adjacent_parts = list(adjacent_parts)
                    gear_ratios.append(adjacent_parts[0].number * adjacent_parts[1].number)

    return gear_ratios


def part1(data):
    schematic = create_schematic(data)
    # print(pandas.DataFrame(schematic))

    part_numbers = get_part_numbers(schematic)

    return sum(part_numbers)


def part2(data):
    schematic = create_schematic(data)

    gear_ratios = get_gear_ratios(schematic)

    return sum(gear_ratios)


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
