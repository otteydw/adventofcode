import pathlib
import sys
from collections import Counter
from functools import total_ordering

# from pprint import pprint as print


@total_ordering
class Hand:
    def __init__(self, cards_string, bet=0):
        self.cards = self._get_cards(cards_string)
        self.bet = bet
        self.hand_value = self._calc_hand_value()

    def __eq__(self, other):
        return sorted(self.cards) == sorted(other.cards)

    def __lt__(self, other):
        if self.hand_value != other.hand_value:
            return self.hand_value < other.hand_value

        for x, y in zip(self.cards, other.cards):
            if x != y:
                return x < y

    def __repr__(self):
        return f"Cards: {self.cards} | Value: {self.hand_value} | Bet {self.bet}"

    def _get_cards(self, cards_string):
        CARD_MAPPING = {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 11,
            "T": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2,
        }
        cards = [CARD_MAPPING[card] for card in cards_string]
        return cards

    def _calc_hand_value(self):
        # 6 - Five of a kind, where all five cards have the same label: AAAAA
        # 5 - Four of a kind, where four cards have the same label and one card has a different label: AA8AA
        # 4 - Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
        # 3 - Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
        # 2 - Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
        # 1 - One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
        # 0 - High card, where all cards' labels are distinct: 23456

        counts = Counter(self.cards)

        two_most_common = counts.most_common(2)

        if len(two_most_common) == 1:
            return 6

        most, second = two_most_common
        most, second = most[1], second[1]

        if most == 4:
            return 5
        if most == 3:
            if second == 2:
                return 4
            return 3
        if most == 2:
            if second == 2:
                return 2
            return 1
        return 0


def parse(puzzle_input):
    return [line for line in puzzle_input.split("\n")]


def part1(data):
    hands = []
    for row in data:
        hand_string, bet = row.split()
        bet = int(bet)
        hand = Hand(hand_string, bet)
        hands.append(hand)

    # print(hands)
    hands.sort()
    # print(hands)

    total_winnings = 0
    for position, hand in enumerate(hands):
        rank = position + 1
        winnings = rank * hand.bet
        total_winnings += winnings
    return total_winnings


def part2(data):
    pass


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
