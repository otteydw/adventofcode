import unittest

from day08 import Forest


class TestSanta(unittest.TestCase):
    def setUp(self):
        input_filename = "example.txt"
        self.forest = Forest(input_filename)

    def test_visible_from_left(self):
        self.assertEqual(self.forest.visible_from_left(1, 1), True)  # Top left 5
        self.assertEqual(self.forest.visible_from_left(1, 2), False)
        self.assertEqual(self.forest.visible_from_left(1, 2), False)  # Top middle 5
        self.assertEqual(
            self.forest.visible_from_left(2, 2), False
        )  # center 3 (not visible from anywhere)

    def test_visible_from_right(self):
        self.assertEqual(self.forest.visible_from_right(1, 2), True)  # Top middle 5
        self.assertEqual(self.forest.visible_from_right(1, 1), False)  # Top left 5
        self.assertEqual(
            self.forest.visible_from_right(2, 2), False
        )  # center 3 (not visible from anywhere)

    def test_visible_from_top(self):
        self.assertEqual(self.forest.visible_from_top(1, 1), True)  # Top left 5
        self.assertEqual(
            self.forest.visible_from_top(2, 2), False
        )  # center 3 (not visible from anywhere)

    def test_visible_from_bottom(self):
        self.assertEqual(self.forest.visible_from_bottom(3, 2), True)  # Bottom middle 5
        self.assertEqual(self.forest.visible_from_bottom(3, 3), False)  # bottom 4
        self.assertEqual(
            self.forest.visible_from_bottom(2, 2), False
        )  # center 3 (not visible from anywhere)

    def test_count_visible_trees(self):
        self.assertEqual(self.forest.count_visible_trees(), 21)


if __name__ == "__main__":
    unittest.main()
