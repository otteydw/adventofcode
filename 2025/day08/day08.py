import argparse
import pathlib
from itertools import combinations
from math import pow, prod, sqrt


def load_input(path: pathlib.Path) -> str:
    return pathlib.Path(path).read_text().strip()


def parse(puzzle_input: str) -> list[tuple[int, int, int]]:
    # lines = [line for line in puzzle_input.splitlines()]
    lst = []
    for line in puzzle_input.splitlines():
        x, y, z = line.split(",")
        lst.append((int(x), int(y), int(z)))
    return lst


def straight_line_distance(coordinate1: tuple[int, int, int], coordinate2: tuple[int, int, int]) -> float:
    x1, y1, z1 = coordinate1
    x2, y2, z2 = coordinate2
    x_diff = pow((x1 - x2), 2)
    y_diff = pow((y1 - y2), 2)
    z_diff = pow((z1 - z2), 2)
    return sqrt(sum([x_diff, y_diff, z_diff]))


def sort_coordinate_pairs(
    coordinates: list[tuple[int, int, int]],
) -> list[tuple[tuple[int, int, int], tuple[int, int, int]]]:
    pairs = combinations(coordinates, 2)
    # print(list(pairs))
    # sys.exit()
    pairs_sorted = sorted(pairs, key=lambda pair: straight_line_distance(pair[0], pair[1]))
    return pairs_sorted


def print_circuits(circuits: list[list[tuple[int, int, int]]]) -> None:
    for circuit in circuits:
        print(f"{len(circuit)=}")
        print("   " + str(circuit))


def part1(data: list[tuple[int, int, int]], max_pairs: int = 1000) -> int:
    circuits = [[coordinate] for coordinate in data]
    sorted_pairs = sort_coordinate_pairs(data)
    print(f"{len(sorted_pairs)=}")
    print("Truncating")
    # print(f"{max_pairs=}, {len(sorted_pairs)=}")
    # max_pairs = min(max_pairs, len(sorted_pairs))
    # print(f"{max_pairs=}")
    sorted_pairs = sorted_pairs[:max_pairs]
    print(f"{len(sorted_pairs)=}")
    print(f"{len(circuits)=}")

    for pair in sorted_pairs:
        for idx, circuit in enumerate(circuits):
            if pair[0] in circuit:
                idx1 = idx
            if pair[1] in circuit:
                idx2 = idx
        if idx1 == idx2:
            continue
        # print()
        # pprint(circuits)
        # print_circuits(circuits)
        # print(f"{idx1=}, {idx2=}")
        # print(f"Planning to pop at {idx2} with {len(circuits)=}")
        idx1, idx2 = sorted([idx1, idx2], reverse=True)
        circuit1 = circuits.pop(idx1)
        circuit2 = circuits.pop(idx2)
        circuits.append(circuit1 + circuit2)
    print_circuits(circuits)
    # sys.exit()

    circuit_sizes = sorted([len(circuit) for circuit in circuits], reverse=True)
    print(f"{circuit_sizes=}")
    return prod(circuit_sizes[:3])


def part2(data: list[tuple[int, int, int]]) -> int:  # type: ignore[empty-body]
    pass


def solve(puzzle_input: str) -> tuple[int | None, int | None]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    # print(data)
    # sys.exit()
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
