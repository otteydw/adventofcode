import unittest

from .day01 import (
    elves_calories,
    load_from_file,
    most_calorie_elf,
    total_calories_of_top_elves,
)


class TestSanta(unittest.TestCase):
    def setUp(self):
        calorie_list = load_from_file("example.txt")
        self.these_calories = elves_calories(calorie_list)

    def test_most_calorie_elf(self):
        self.assertAlmostEqual(most_calorie_elf(self.these_calories), 24000)

    def test_total_calories_of_top_elves(self):
        self.assertAlmostEqual(total_calories_of_top_elves(self.these_calories, 3), 45000)


if __name__ == "__main__":
    unittest.main()
