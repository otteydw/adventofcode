import argparse
import pathlib
from dataclasses import dataclass
from itertools import chain, combinations, product
from math import inf
from typing import Any


@dataclass(frozen=True)
class Item:
    name: str
    cost: int
    damage: int
    armor: int


@dataclass
class Player:
    name: str
    hp: int
    damage: int
    armor: int

    def defend(self, opponent: Player) -> None:
        damage_dealt = max(1, opponent.damage - self.armor)
        self.hp -= damage_dealt

    def take_damage(self, damage_taken: int) -> None:
        self.hp -= damage_taken

    def attack(self, oppenent: Player) -> None:
        damage_dealt = max(1, self.damage - oppenent.armor)
        print(
            f"{self.name} with attack {self.damage} attacks {oppenent.name} with armor {oppenent.armor} resulting in {damage_dealt} damage"
        )
        oppenent.take_damage(damage_dealt)
        print(f"Oppent has {oppenent.hp} HP")


WEAPONS = [
    Item("Dagger", 8, 4, 0),
    Item("Shortsword", 10, 5, 0),
    Item("Warhammer", 25, 6, 0),
    Item("Longsword", 40, 7, 0),
    Item("Greataxe", 74, 8, 0),
]

ARMOR = [
    Item("Leather", 13, 0, 1),
    Item("Chainmail", 31, 0, 2),
    Item("Splintmail", 53, 0, 3),
    Item("Bandedmail", 75, 0, 4),
    Item("Platemail", 102, 0, 5),
]

RINGS = [
    Item("Damage +1", 25, 1, 0),
    Item("Damage +2", 50, 2, 0),
    Item("Damage +3", 100, 3, 0),
    Item("Defense +1", 20, 0, 1),
    Item("Defense +2", 40, 0, 2),
    Item("Defense +3", 80, 0, 3),
]

WEAPONS_MIN = 1
WEAPONS_MAX = 1

ARMOR_MIN = 0
ARMOR_MAX = 1

RINGS_MIN = 0
RINGS_MAX = 2


def combinations_of_range_of_items_from_list(
    items_list: list[Any], min_items: int, max_items: int
) -> list[tuple[Any, ...]]:
    all_combinations = []
    for r in range(min_items, max_items + 1):
        combs = combinations(items_list, r)
        all_combinations.extend(list(combs))
    return all_combinations


def load_input(path: pathlib.Path) -> str:
    return pathlib.Path(path).read_text().strip()


def parse(puzzle_input: str) -> tuple[int, int, int]:
    lines = [line for line in puzzle_input.splitlines()]
    hp = int(lines[0].split(": ")[1])
    damage = int(lines[1].split(": ")[1])
    armor = int(lines[2].split(": ")[1])
    return hp, damage, armor


def simulate_round(player: Player, boss: Player) -> str | None:
    # Player attacks boss (boss defends against player)
    player.attack(boss)

    # Check if boss is dead (player won)
    if boss.hp <= 0:
        return "player"

    # Boss attacks player
    boss.attack(player)

    # Check if player is dead (boss won)
    if player.hp <= 0:
        return "boss"

    return None


def simulate_battle(player: Player, boss: Player) -> str:
    result = None
    while result is None:
        result = simulate_round(player, boss)

    return result


WEAPON_COMBOS = combinations_of_range_of_items_from_list(WEAPONS, WEAPONS_MIN, WEAPONS_MAX)
ARMOR_COMBOS = combinations_of_range_of_items_from_list(ARMOR, ARMOR_MIN, ARMOR_MAX)
RING_COMBOS = combinations_of_range_of_items_from_list(RINGS, RINGS_MIN, RINGS_MAX)


def part1(data: tuple[int, int, int]) -> int:
    # weapon_combos = combinations_of_range_of_items_from_list(WEAPONS, WEAPONS_MIN, WEAPONS_MAX)
    # armor_combos = combinations_of_range_of_items_from_list(ARMOR, ARMOR_MIN, ARMOR_MAX)
    # ring_combos = combinations_of_range_of_items_from_list(RINGS, RINGS_MIN, RINGS_MAX)

    # print("Weapon combos")
    # pprint(weapon_combos)
    # print()
    # print("Armor combos")
    # pprint(armor_combos)
    # print()
    # print("Ring combos")
    # pprint(ring_combos)
    cheapest_outfit = inf
    outfit_combos = product(WEAPON_COMBOS, ARMOR_COMBOS, RING_COMBOS)
    # loop=0
    for outfit_combo in outfit_combos:
        # pprint(outfit_combo)
        flattened = list(chain.from_iterable(outfit_combo))
        # pprint(list(flattened))
        # print()
        # loop+=1
        # print(f"{loop=}")
        # if loop==45:
        # for item in outfit_combo:
        #     print(item)
        # import sys
        # sys.exit()
        outfit_cost = sum(item.cost for item in flattened)
        outfit_damage = sum(item.damage for item in flattened)
        outfit_armor = sum(item.armor for item in flattened)
        print(f"{outfit_cost=}, {outfit_damage=}, {outfit_armor=}")

        if outfit_cost < cheapest_outfit:
            player = Player("Player", hp=100, damage=outfit_damage, armor=outfit_armor)
            boss = Player("Boss", *data)

            winner = simulate_battle(player, boss)
            if winner == "player":
                cheapest_outfit = outfit_cost

    assert isinstance(cheapest_outfit, int)
    return cheapest_outfit


def part2(data: tuple[int, int, int]) -> int:
    expensive_outfit = 0
    outfit_combos = product(WEAPON_COMBOS, ARMOR_COMBOS, RING_COMBOS)
    # loop=0
    for outfit_combo in outfit_combos:
        # pprint(outfit_combo)
        flattened = list(chain.from_iterable(outfit_combo))
        # pprint(list(flattened))
        # print()
        # loop+=1
        # print(f"{loop=}")
        # if loop==45:
        # for item in outfit_combo:
        #     print(item)
        # import sys
        # sys.exit()
        outfit_cost = sum(item.cost for item in flattened)
        outfit_damage = sum(item.damage for item in flattened)
        outfit_armor = sum(item.armor for item in flattened)
        print(f"{outfit_cost=}, {outfit_damage=}, {outfit_armor=}")

        if outfit_cost > expensive_outfit:
            player = Player("Player", hp=100, damage=outfit_damage, armor=outfit_armor)
            boss = Player("Boss", *data)

            winner = simulate_battle(player, boss)
            if winner == "boss":
                expensive_outfit = outfit_cost

    # assert isinstance(cheapest_outfit, int)
    return expensive_outfit


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
