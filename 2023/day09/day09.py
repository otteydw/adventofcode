import pathlib
import sys


def parse(puzzle_input):
    return [line for line in puzzle_input.split("\n")]


def prediction(history, direction="forward"):
    diffs = []
    for position, value in enumerate(history):
        if position == 0:
            continue
        diffs.append(value - history[position - 1])

    if direction == "forward":
        if set(diffs) == {0}:
            return history[-1]
        else:
            return prediction(diffs) + history[-1]
    elif direction == "backward":
        if set(diffs) == {0}:
            return history[0]
        else:
            return history[0] - prediction(diffs, direction="backward")


def part1(data, direction="forward"):
    predictions = []
    for row in data:
        history = [int(x) for x in row.split()]
        this_prediction = prediction(history, direction=direction)
        predictions.append(this_prediction)
    return sum(predictions)


def part2(data):
    return part1(data, direction="backward")


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
