import hashlib
import unittest

from day01 import load_ints_from_file, count_depth_increases

class TestSanta(unittest.TestCase):
    def test_count_depth_increases(self):

        depths = load_ints_from_file("example.txt")
        self.assertAlmostEqual(count_depth_increases(depths), 7)

if __name__ == '__main__':
    unittest.main()