from itertools import combinations
from typing import Any


def combinations_by_size_range(
    items_list: list[Any], min_items: int = 0, max_items: int | None = None
) -> list[tuple[Any, ...]]:
    """Return all combinations of items whose size falls within a range.

    Generates every unique combination of the input items where the number
    of elements in each combination is between ``min_size`` and ``max_size``
    (inclusive).

    Args:
        items: The source list of items to combine.
        min_size: The minimum number of elements in each combination.
        max_size: The maximum number of elements in each combination.

    Returns:
        A list of tuples, where each tuple is a unique combination of items
        whose length is within the specified range.
    """
    if not max_items:
        max_items = len(items_list)

    all_combinations = []
    for r in range(min_items, max_items + 1):
        combs = combinations(items_list, r)
        all_combinations.extend(list(combs))
    return all_combinations
