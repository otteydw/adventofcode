import argparse
import pathlib


def parse(puzzle_input):
    return [line for line in puzzle_input.split("\n")]


def part1(data):

    listA = []
    listB = []
    for line in data:
        a, b = line.split()
        listA.append(int(a))
        listB.append(int(b))

    listA.sort()
    listB.sort()

    distance = 0
    for a, b in zip(listA, listB):
        distance += abs(a - b)

    return distance


def part2(data):
    listA = []
    listB = []
    for line in data:
        a, b = line.split()
        listA.append(int(a))
        listB.append(int(b))

    total_similarity = 0

    for a in listA:
        total_similarity += a * listB.count(a)

    return total_similarity


def solve(puzzle_input):
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
        for solution_number, solution in enumerate(solutions):
            print(f"Solution {solution_number}: {str(solution)}")
