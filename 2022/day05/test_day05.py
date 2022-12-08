import unittest

from day05 import Supplies


class TestSanta(unittest.TestCase):
    def setUp(self):
        input_filename = "example.txt"
        self.my_supplies = Supplies(input_filename)

    def test_top_crates(self):
        self.my_supplies.process_moves()
        self.assertEqual(self.my_supplies.see_top_crates(), "CMZ")

    def test_top_crates_9001(self):
        self.my_supplies.process_moves(crane=9001)
        self.assertEqual(self.my_supplies.see_top_crates(), "MCD")


if __name__ == "__main__":
    unittest.main()
