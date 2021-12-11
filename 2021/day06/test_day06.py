import unittest

import day06


class TestSanta(unittest.TestCase):
    def test_lanternfish1(self):

        lanternfish_data = day06.load_lanternfish_data("example.txt")
        self.assertEqual(day06.number_of_lanternfish(lanternfish_data, 18), 26)
        self.assertEqual(day06.number_of_lanternfish(lanternfish_data, 80), 5934)


if __name__ == "__main__":
    unittest.main()
