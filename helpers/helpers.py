from itertools import combinations
from typing import Any


def combinations_by_size_range(items_list: list[Any], min_items: int, max_items: int) -> list[tuple[Any, ...]]:
    all_combinations = []
    for r in range(min_items, max_items + 1):
        combs = combinations(items_list, r)
        all_combinations.extend(list(combs))
    return all_combinations
