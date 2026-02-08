# mypy: ignore-errors
import pathlib
import sys
from functools import lru_cache


class ScratcherGame:
    def __init__(self, game_data):
        self.game_info = {}
        for card in game_data:
            card_number, matching_numbers = self.card_winning_info(card)
            self.game_info[card_number] = matching_numbers

    def card_winning_info(self, card):
        card_string, match_string = card.split(": ")

        card_number = int(card_string.split()[1])

        winning_numbers_string, my_numbers_string = match_string.split(" | ")
        winning_numbers = {int(x) for x in winning_numbers_string.split()}
        my_numbers = {int(x) for x in my_numbers_string.split()}

        common_numbers = winning_numbers & my_numbers

        return card_number, len(common_numbers)

    @lru_cache(maxsize=None)
    def scratchers_won_from_card(self, card_number):
        scratchers_won_this_card = self.game_info[card_number]
        if scratchers_won_this_card == 0:
            return 1

        total_scratchers_won = 1
        for x in range(card_number + 1, card_number + 1 + scratchers_won_this_card):
            total_scratchers_won += self.scratchers_won_from_card(x)

        return total_scratchers_won

    def total_scratchers(self):
        total_scratchers = 0
        for card_number in self.game_info.keys():
            scratchers_this_card = self.scratchers_won_from_card(card_number)
            total_scratchers += scratchers_this_card

        return total_scratchers


def parse(puzzle_input):
    return [line for line in puzzle_input.split("\n")]


def card_score(card):
    match_string = card.split(": ")[1]

    winning_numbers_string, my_numbers_string = match_string.split(" | ")
    winning_numbers = {int(x) for x in winning_numbers_string.split()}
    my_numbers = {int(x) for x in my_numbers_string.split()}

    common_numbers = winning_numbers & my_numbers

    if len(common_numbers) < 2:
        score = len(common_numbers)
    else:
        score = 2 ** (len(common_numbers) - 1)

    return score


def part1(data):
    total_score = 0
    for card in data:
        total_score += card_score(card)
    return total_score


def part2(data):
    scratcher = ScratcherGame(data)
    return scratcher.total_scratchers()


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
