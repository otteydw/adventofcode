import unittest

from . import adjacent_finder


class TestAdjacent(unittest.TestCase):
    def test_adjacent_finder(self):
        npa = adjacent_finder.np.array([[5, 6, 4], [2, 1, 3], [7, 9, 8]])
        self.assertEqual(
            adjacent_finder.adjacent_finder(npa, (1, 1)),
            [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)],
        )
        self.assertEqual(adjacent_finder.adjacent_finder(npa, (2, 2)), [(1, 1), (1, 2), (2, 1)])


if __name__ == "__main__":
    unittest.main()
