import argparse
from itertools import groupby


class Password:
    def __init__(self, s: str) -> None:
        self.value = [char for char in s]

    def is_valid(self) -> bool:
        def _invalid_chars(s: str | list[str]) -> bool:
            INVALID_CHARS = ["i", "o", "l"]
            for invalid_char in INVALID_CHARS:
                if invalid_char in self.value:
                    return True
            return False

        def _increasing_straight(s: str | list[str]) -> bool:
            REQUIRED_STRAIGHT_LENGTH = 3
            for idx in range(len(s) - REQUIRED_STRAIGHT_LENGTH + 1):
                # print(f"Checking char {s[idx]} at {idx=}")
                ord1 = ord(s[idx])
                ord2 = ord(s[idx + 1])
                ord3 = ord(s[idx + 2])
                if ord1 + 1 == ord2 and ord2 + 1 == ord3:
                    return True
            return False

        def _has_non_overlapping_pairs(s: str | list[str]) -> bool:
            MINIMUM_PAIRS_REQUIRED = 2
            pair_counter = sum(1 if len(list(v)) >= 2 else 0 for k, v in groupby(s))
            return pair_counter >= MINIMUM_PAIRS_REQUIRED

        if _invalid_chars(self.value):
            return False

        if not _increasing_straight(self.value):
            return False

        if not _has_non_overlapping_pairs(self.value):
            return False

        return True

    def next_password(self) -> None:
        # print(f"Current password is {self.value}")
        INVALID_CHARS = ["i", "o", "l"]

        for idx in range(len(self.value) - 1, -1, -1):
            wrapped = False
            found_valid_next_char = False

            while not found_valid_next_char:
                ord_at_idx = ord(self.value[idx])
                next_char = chr(ord_at_idx + 1)
                if next_char == "{":
                    wrapped = True
                    next_char = "a"
                self.value[idx] = next_char
                found_valid_next_char = self.value[idx] not in INVALID_CHARS
            if not wrapped:
                return None
        print(f"Oops! Password is {self.value} and {wrapped=}")
        raise

    def next_valid_password(self) -> None:
        found_valid = False
        while not found_valid:
            self.next_password()
            found_valid = self.is_valid()

    def __repr__(self) -> str:
        return "".join(self.value)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, str):
            return NotImplemented
        return "".join(self.value) == other


def part1(data: str) -> str:
    password = Password(data)
    password.next_valid_password()
    return str(password)


def part2(password: str) -> str:
    return ""


def solve(password: str) -> tuple[str | None, str | None]:
    """Solve the puzzle for the given input."""
    solve1 = True
    solve2 = True
    solution1 = part1(password) if solve1 else None
    solution2 = part2(password) if solve2 else None

    return solution1, solution2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Solve Advent of Code puzzles")
    parser.add_argument("password", help="Input password to process")
    args = parser.parse_args()

    password = args.password
    print(f"{password}:")
    solutions = solve(password)
    for solution_number, solution in enumerate(solutions, start=1):
        print(f"Solution {solution_number}: {str(solution)}")
