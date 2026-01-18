import argparse
import pathlib

CORRECT_SUE = {
    "akitas": 0,
    "cars": 2,
    "cats": 7,
    "children": 3,
    "goldfish": 5,
    "perfumes": 1,
    "pomeranians": 3,
    "samoyeds": 2,
    "trees": 3,
    "vizslas": 0,
}


def load_input(path: pathlib.Path) -> str:
    return pathlib.Path(path).read_text().strip()


def parse(puzzle_input: str) -> list[dict[str, str | int]]:
    people = []
    for line in puzzle_input.splitlines():
        # Sue 1: goldfish: 6, trees: 9, akitas: 0
        person_name, items_string = line.split(": ", 1)
        items_list = items_string.split(", ")
        person: dict[str, str | int] = dict()
        person["name"] = person_name
        for item in items_list:
            item_name, item_quantity = item.split(": ")
            person[item_name] = int(item_quantity)
        people.append(person)
    return people


def match_part1(person: dict[str, str | int]) -> bool:
    for key in CORRECT_SUE:
        if key in person and person[key] != CORRECT_SUE[key]:
            return False
    return True


def match_part2(person: dict[str, str | int]) -> bool:
    for key, person_value in person.items():
        if key in CORRECT_SUE:
            correct_value = CORRECT_SUE[key]
            assert isinstance(person_value, int)
            assert isinstance(correct_value, int)
            if key not in ["cats", "trees", "pomeranians", "goldfish"] and person_value != correct_value:
                return False
            elif key in ["cats", "trees"] and not (person_value > correct_value):
                return False
            elif key in ["pomeranians", "goldfish"] and not (person_value < correct_value):
                return False
    return True


def part1(data: list[dict[str, str | int]]) -> int:
    for person in data:
        if match_part1(person):
            person_name = person["name"]
            assert isinstance(person_name, str)
            person_number = int(person_name.split()[1])
            return person_number
    raise AssertionError("Unreachable")


def part2(data: list[dict[str, str | int]]) -> int:
    for person in data:
        if match_part2(person):
            person_name = person["name"]
            assert isinstance(person_name, str)
            person_number = int(person_name.split()[1])
            return person_number
    raise AssertionError("Unreachable")


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
