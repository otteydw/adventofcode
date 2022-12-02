import unittest

from day01 import load_from_file, elves_calories, most_calorie_elf


class TestSanta(unittest.TestCase):
    def test_most_calorie_elf(self):

        calorie_list = load_from_file("example.txt")
        these_calories = elves_calories(calorie_list)
        self.assertAlmostEqual(most_calorie_elf(these_calories), 24000)


if __name__ == "__main__":
    unittest.main()
