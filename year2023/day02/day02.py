import pathlib
import sys


def parse(puzzle_input):
    return [line for line in puzzle_input.split("\n")]


def match_parse(match):
    match_summary = {}
    bag_pulls = match.split(", ")
    for bag_pull in bag_pulls:
        quantity, color = bag_pull.split(" ")
        match_summary[color] = int(quantity)

    return match_summary


def game_parse(game):
    game_string, match_string = game.split(": ")

    game_number = int(game_string.split(" ")[1])

    matches_as_strings = match_string.split("; ")

    matches = []
    for match_as_string in matches_as_strings:
        matches.append(match_parse(match_as_string))

    return game_number, matches


def is_possible_game(game_to_check):
    BAG_TO_CHECK_AGAINST = {"red": 12, "green": 13, "blue": 14}

    for match in game_to_check:
        for color, quantity in match.items():
            if quantity > BAG_TO_CHECK_AGAINST[color]:
                return False

    return True


def part1(data):
    sum = 0
    for game in data:
        game_number, game_output = game_parse(game)
        if is_possible_game(game_output):
            sum += game_number

    return sum


def find_minimum_cubes(game):
    minimum_cubes = {"red": 0, "green": 0, "blue": 0}
    for match in game:
        for color, quantity in match.items():
            minimum_cubes[color] = max(quantity, minimum_cubes[color])

    return minimum_cubes


def calculate_cube_set_power(cube_set):
    cube_set_power = 1
    for value in cube_set.values():
        cube_set_power = cube_set_power * value

    return cube_set_power


def part2(data):
    sum = 0
    for game in data:
        _, game_output = game_parse(game)
        minimum_cubes_needed = find_minimum_cubes(game_output)
        cube_set_power = calculate_cube_set_power(minimum_cubes_needed)
        sum += cube_set_power

    return sum


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
            print(f"Solution {solution_number + 1}: {str(solution)}")
