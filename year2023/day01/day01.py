# mypy: ignore-errors
import pathlib
import sys
from string import digits


def convert_to_numbers(s: str):
    words_to_numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    if len(s) == 1:
        return s

    for key in words_to_numbers.keys():
        if s.startswith(key):
            s = words_to_numbers[key] + s[1:]
            continue
    return s[0] + convert_to_numbers(s[1:])


def extract_digits(s: str):
    return "".join(c for c in s if c in digits)


def parse(puzzle_input):
    return [line for line in puzzle_input.split("\n")]


def part1(data):
    sum = 0
    for line in data:
        digits_only = extract_digits(line)
        if len(digits_only) == 0:
            continue
        sum += int(digits_only[0] + digits_only[-1])
    return sum


def part2(data):
    sum = 0
    for line in data:
        line = convert_to_numbers(line)
        digits_only = extract_digits(line)
        sum += int(digits_only[0] + digits_only[-1])
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
            print(f"Solution {solution_number+1}: {str(solution)}")
