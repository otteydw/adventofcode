import argparse
import pathlib
import re
from collections import defaultdict

# 'Al': {'ThF',
#     'ThRnFAr'},
# 'B': {'BCa',
#     'TiB',
#     'TiRnFAr'},
# 'Ca': {'CaCa',
#     'PB',
#     'PRnFAr',
#     'SiRnFYFAr',
#     'SiRnMgAr',
#     'SiTh'},
# 'F': {'CaF',
#     'PMg',
#     'SiAl'},
# 'H': {'CRnAlAr',
#     'CRnFYFYFAr',
#     'CRnFYMgAr',
#     'CRnMgYFAr',
#     'HCa',
#     'NRnFYFAr',
#     'NRnMgAr',
#     'NTh',
#     'OB',
#     'ORnFAr'},
# 'Mg': {'BF',
#     'TiMg'},
# 'N': {'CRnFAr',
#     'HSi'},
# 'O': {'CRnFYFAr',
#     'CRnMgAr',
#     'HP',
#     'NRnFAr',
#     'OTi'},
# 'P': {'CaP',
#     'PTi',
#     'SiRnFAr'},
# 'Si': {'CaSi'},
# 'Th': {'ThCa'},
# 'Ti': {'BP',
#     'TiTi'},
# 'e': {'HF',
#     'NAl',
#     'OMg'}


def load_input(path: pathlib.Path) -> str:
    return pathlib.Path(path).read_text().strip()


def parse(puzzle_input: str) -> tuple[dict[str, set[str]], str]:
    lines = puzzle_input.splitlines()
    initial_string = lines[-1]
    conversions = defaultdict(set)

    for line in lines[:-2]:
        from_string, to_string = line.split(" => ")
        conversions[from_string].add(to_string)
    return (conversions, initial_string)


# def convert(conversion: dict[str, set[str]], initial_string: str) -> set[str]:


def part1(conversions: dict[str, set[str]], initial_string: str) -> int:
    # pprint(conversions, width=1)
    new_words = set()
    # pprint(conversions)
    for key, values in conversions.items():
        for value in values:
            matches = re.finditer(key, initial_string)
            for match in matches:
                idx_start, idx_end = match.span()
                new_word = initial_string[:idx_start] + value + initial_string[idx_end:]
                # print(f"{initial_string}, {key} => {value} at {match.span()} ... Adding {new_word=}")
                new_words.add(new_word)
    # pprint(f"{new_words=}")
    return len(new_words)


def part2(conversion: dict[str, set[str]], initial_string: str) -> int:  # type: ignore[empty-body]
    pass


def solve(puzzle_input: str) -> tuple[int | None, int | None]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solve1 = True
    solve2 = True
    conversions, inititial_string = data
    solution1 = part1(conversions, inititial_string) if solve1 else None
    solution2 = part2(conversions, inititial_string) if solve2 else None

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
