import argparse
import pathlib
import re
from collections import defaultdict
from pprint import pprint

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


def sub(conversions: dict[str, set[str]], initial_string: str) -> set[str]:
    new_words = set()
    for key, values in conversions.items():
        for value in values:
            matches = re.finditer(key, initial_string)
            for match in matches:
                idx_start, idx_end = match.span()
                new_word = initial_string[:idx_start] + value + initial_string[idx_end:]
                if new_word.startswith(tuple(conversions.keys())) and new_word.endswith(tuple(conversions.keys())):
                    new_words.add(new_word)
    return new_words


def part1(conversions: dict[str, set[str]], initial_string: str) -> int:
    new_words = set()
    for key, values in conversions.items():
        for value in values:
            matches = re.finditer(key, initial_string)
            for match in matches:
                idx_start, idx_end = match.span()
                new_word = initial_string[:idx_start] + value + initial_string[idx_end:]
                new_words.add(new_word)
    # new_words = sub(conversions, initial_string)
    return len(new_words)


def part2(
    conversions: dict[str, set[str]], medicine_molecule: str, initial_string: str = "e", start_letter: str = "e"
) -> int:
    # Word = namedtuple("Word", "word next_letter")

    # word = Word(start_letter, start_letter)
    # all_words: set[Word] = set([word])
    all_words: set[str] = set([initial_string])
    # for value in conversions[start_letter]:
    #     word = Word(initial_string, value)
    #     all_words.add(word)
    print(all_words)

    len_medicine_molecule = len(medicine_molecule)
    print(f"{len_medicine_molecule=}")
    counter = 0
    while True:
        counter += 1
        new_words: set[str] = set()
        # for word in all_words:
        #     # print(f"Processing {word=}")
        #     key = word.next_letter
        #     values = conversions[key]
        #     for value in values:
        #         matches = re.finditer(key, word.word)
        #         # if not matches:
        #         #     new_words.add(word.word)
        #         for match in matches:
        #             idx_start, idx_end = match.span()
        #             new_word = Word(word.word[:idx_start] + value + word.word[idx_end:], value)
        #             new_words.add(new_word)
        # # if medicine_molecule in new_words:
        # #     return counter
        # all_words = new_words
        # print(all_words)
        # if counter == 3:
        #     return None

        for word in all_words:
            new_words = new_words.union(sub(conversions, word))
        if medicine_molecule in new_words:
            return counter
        all_words = new_words
        print(f"{len(all_words)}")
        pprint(all_words)
        print(f"{counter=}")
        # if counter == 3:
        #     return None


def reverse_sub(conversions: dict[str, set[str]], initial_string: str) -> set[str]:
    new_words = set()
    for key, values in conversions.items():
        for value in values:
            matches = re.finditer(value, initial_string)
            for match in matches:
                idx_start, idx_end = match.span()
                new_word = initial_string[:idx_start] + key + initial_string[idx_end:]
                new_words.add(new_word)
    return new_words


def part2backwards(conversions: dict[str, set[str]], medicine_molecule: str, target_letter: str = "e") -> int:
    all_words: set[str] = set([medicine_molecule])
    print(all_words)
    counter = 0
    while True:
        counter += 1
        new_words: set[str] = set()
        for word in all_words:
            new_words = new_words.union(reverse_sub(conversions, word))
        if target_letter in new_words:
            return counter
        all_words = new_words


def part2dingo(conversions: dict[str, set[str]], medicine_molecule: str, target_letter: str = "e") -> int:
    something = medicine_molecule.replace("Rn", "(").replace("Y", ",").replace("Ar", ")")
    print(something)
    return 0


def solve(puzzle_input: str) -> tuple[int | None, int | None]:
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solve1 = True
    solve2 = True
    conversions, inititial_string = data
    solution1 = part1(conversions, inititial_string) if solve1 else None
    # solution2 = part2(conversions, inititial_string) if solve2 else None
    # solution2 = part2backwards(conversions, inititial_string) if solve2 else None
    solution2 = part2dingo(conversions, inititial_string) if solve2 else None

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
