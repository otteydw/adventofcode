import unittest

from day09 import Rope


class TestSanta(unittest.TestCase):
    def setUp(self):
        input_filename = "example.txt"
        self.rope = Rope(input_filename)

    def test_check_head_tail_touching(self):
        self.rope.head_position = (0, 0)
        self.rope.tail_position = (0, 0)
        self.assertTrue(self.rope.check_head_tail_touching())
        self.rope.head_position = (0, 0)
        self.rope.tail_position = (1, 1)
        self.assertTrue(self.rope.check_head_tail_touching())
        self.rope.head_position = (0, 0)
        self.rope.tail_position = (1, 2)
        self.assertFalse(self.rope.check_head_tail_touching())
        self.rope.head_position = (0, 0)
        self.rope.tail_position = (2, 1)
        self.assertFalse(self.rope.check_head_tail_touching())

    def test_count_tail_visited_positions(self):
        self.assertEqual(self.rope.count_tail_visited_positions(), 13)


if __name__ == "__main__":
    unittest.main()
