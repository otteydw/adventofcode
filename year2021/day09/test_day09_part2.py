import unittest

from . import day09_part2


class TestSanta(unittest.TestCase):
    def setUp(self):
        self.tube = day09_part2.LavaTube(day09_part2.load_into_array("example.txt"))
        self.tube0 = day09_part2.LavaTube(day09_part2.load_into_array("example0.txt"))
        self.tube9 = day09_part2.LavaTube(day09_part2.load_into_array("example0.txt"))

    def test_find_lows(self):
        self.assertEqual(self.tube.find_lows(), [1, 0, 5, 5])
        self.assertEqual(self.tube0.find_lows(), [])
        self.assertEqual(self.tube9.find_lows(), [])

    def test_risk_level(self):
        self.assertEqual(self.tube.risk_level(1), 2)
        self.assertEqual(self.tube.risk_level(0), 1)
        self.assertEqual(self.tube.risk_level(5), 6)

    def test_risk_level_sums(self):
        self.assertEqual(self.tube.risk_level_sums(), 15)
        self.assertEqual(self.tube0.risk_level_sums(), 0)
        self.assertEqual(self.tube9.risk_level_sums(), 0)

    def test_find_size_of_basins(self):
        self.assertEqual(self.tube.find_size_of_basins(), [3, 9, 14, 9])

    def test_product_largest_basins_largest_basins(self):
        self.assertEqual(self.tube.product_largest_basins(3), 1134)
        self.assertEqual(self.tube.product_largest_basins(), 3402)


if __name__ == "__main__":
    unittest.main()
