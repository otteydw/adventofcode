import unittest

import day06


class TestSanta(unittest.TestCase):
    def test_lanternfish_orig(self):

        lanternfish_data = day06.load_lanternfish_data("example.txt")
        self.assertEqual(day06.number_of_lanternfish_orig(lanternfish_data, 18), 26)
        self.assertEqual(day06.number_of_lanternfish_orig(lanternfish_data, 80), 5934)
        self.assertEqual(day06.number_of_lanternfish_orig(lanternfish_data, 1), 5)

    def test_lanternfish_unclassed(self):

        lanternfish_data = day06.load_lanternfish_data("example.txt")
        self.assertEqual(day06.number_of_lanternfish_unclassed(lanternfish_data, 18), 26)
        self.assertEqual(day06.number_of_lanternfish_unclassed(lanternfish_data, 80), 5934)
        # self.assertEqual(day06.number_of_lanternfish_unclassed(lanternfish_data, 256), 26984457539)

if __name__ == "__main__":
    unittest.main()
