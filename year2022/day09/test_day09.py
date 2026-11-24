import unittest

from .day09 import Rope


class TestSanta(unittest.TestCase):

    def test_count_tail_visited_positions(self):
        input_filename = "example.txt"

        self.rope = Rope(input_filename, knots=2)
        self.assertEqual(self.rope.count_tail_visited_positions(), 13)

        self.rope = Rope(input_filename, knots=10)
        self.assertEqual(self.rope.count_tail_visited_positions(), 1)

        input_filename = "example2.txt"
        self.rope = Rope(input_filename, knots=10)
        self.assertEqual(self.rope.count_tail_visited_positions(), 36)


if __name__ == "__main__":
    unittest.main()
