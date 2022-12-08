import unittest

from day05 import (
    Supplies
)


class TestSanta(unittest.TestCase):
    def test_top_crates(self):
        input_filename = "example.txt"
        my_supplies = Supplies(input_filename)
        self.assertEqual(my_supplies.see_top_crates(), "CMZ")


if __name__ == "__main__":
    unittest.main()
