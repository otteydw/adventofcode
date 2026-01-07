import argparse
import pathlib


class Reindeer:
    def __init__(self, name: str, speed: int, speed_time: int, rest_time_required: int) -> None:
        self.name = name
        self.speed = speed
        self.speed_time = speed_time
        self.rest_time_required = rest_time_required

        self.distance_traveled: int
        self.is_resting: bool
        self.timer: int
        self.points: int

        self.reset()

    def tick(self) -> None:
        self.timer += 1
        if self.is_resting:
            self.rest()
        else:
            self.move()

    def move(self) -> None:
        self.distance_traveled += self.speed
        if self.timer == self.speed_time:
            self.is_resting = True
            self.timer = 0

    def rest(self) -> None:
        if self.timer == self.rest_time_required:
            self.is_resting = False
            self.timer = 0

    def reset(self) -> None:
        self.distance_traveled = 0
        self.is_resting = False
        self.timer = 0
        self.points = 0

    def add_point(self) -> None:
        self.points += 1

    def __repr__(self) -> str:
        return f"{self.name} traveled {self.distance_traveled}."


def load_input(path: pathlib.Path) -> str:
    return pathlib.Path(path).read_text().strip()


def parse(puzzle_input: str) -> list[Reindeer]:
    # Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.
    reindeer = []
    for line in puzzle_input.splitlines():
        line_split = line.split()
        name = line_split[0]
        speed = int(line_split[3])
        speed_time = int(line_split[6])
        rest_time_required = int(line_split[-2])
        this_reindeer = Reindeer(name=name, speed=speed, speed_time=speed_time, rest_time_required=rest_time_required)
        reindeer.append(this_reindeer)
    return reindeer


def part1(data: list[Reindeer], seconds: int = 2503) -> int:
    for _ in range(seconds):
        for reindeer in data:
            reindeer.tick()

    winning_distance = max(reindeer.distance_traveled for reindeer in data)
    return winning_distance


def part2(data: list[Reindeer], seconds: int = 2503) -> int:
    for reindeer in data:
        reindeer.reset()

    for _ in range(seconds):
        for reindeer in data:
            reindeer.tick()
        lead_distance = max(reindeer.distance_traveled for reindeer in data)
        for reindeer in data:
            if reindeer.distance_traveled == lead_distance:
                reindeer.add_point()

    winning_points = max(reindeer.points for reindeer in data)
    return winning_points


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
