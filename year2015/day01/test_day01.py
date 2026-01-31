import unittest

from .day01 import find_basement_position, find_floor


class TestFloorFinder(unittest.TestCase):
    def test_find_floor(self):
        self.assertAlmostEqual(find_floor("(())"), 0)
        self.assertAlmostEqual(find_floor("()()"), 0)
        self.assertAlmostEqual(find_floor("((("), 3)
        self.assertAlmostEqual(find_floor("(()(()("), 3)
        self.assertAlmostEqual(find_floor("))((((("), 3)
        self.assertAlmostEqual(find_floor("())"), -1)
        self.assertAlmostEqual(find_floor("))("), -1)
        self.assertAlmostEqual(find_floor(")))"), -3)
        self.assertAlmostEqual(find_floor(")())())"), -3)

    def test_find_basement_position(self):
        self.assertAlmostEqual(find_basement_position(")"), 1)
        self.assertAlmostEqual(find_basement_position("()())"), 5)
