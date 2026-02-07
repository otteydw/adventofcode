import unittest

from . import day09


class TestSanta(unittest.TestCase):
    def setUp(self):
        self.array = day09.load_into_array("example.txt")
        self.array0 = day09.load_into_array("example0.txt")
        self.array9 = day09.load_into_array("example9.txt")

    def test_find_lows(self):
        self.assertEqual(day09.find_lows(self.array), [1, 0, 5, 5])
        self.assertEqual(day09.find_lows(self.array0), [])
        self.assertEqual(day09.find_lows(self.array9), [])

    def test_risk_level(self):
        self.assertEqual(day09.risk_level(1), 2)
        self.assertEqual(day09.risk_level(0), 1)
        self.assertEqual(day09.risk_level(5), 6)

    def test_risk_level_sums(self):
        self.assertEqual(day09.risk_level_sums(self.array), 15)
        self.assertEqual(day09.risk_level_sums(self.array0), 0)
        self.assertEqual(day09.risk_level_sums(self.array9), 0)


if __name__ == "__main__":
    unittest.main()
