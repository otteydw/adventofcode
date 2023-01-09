import unittest

from day12 import Grid


class TestSanta(unittest.TestCase):
    def setUp(self):
        input_filename = "example.txt"
        self.grid = Grid(input_filename)

    def test_set_start(self):
        self.assertEqual(self.grid.start, (0, 0))

    def test_set_end(self):
        self.assertEqual(self.grid.end, (2, 5))

    def test_get_height_at_position(self):
        self.assertEqual(self.grid.get_height_at_position(self.grid.start), 0)
        self.assertEqual(self.grid.get_height_at_position(self.grid.end), 25)

    def test_can_go(self):
        self.assertTrue(self.grid.can_go(self.grid.start, 'right'))
        self.assertTrue(self.grid.can_go((0, 1), 'right'))
        self.assertFalse(self.grid.can_go((0, 2), 'right'))

        self.assertFalse(self.grid.can_go(self.grid.start, 'left'))
        self.assertTrue(self.grid.can_go((2, 1), 'left'))

        self.assertFalse(self.grid.can_go(self.grid.start, 'up'))
        self.assertTrue(self.grid.can_go((4, 7), 'up'))

        self.assertTrue(self.grid.can_go(self.grid.start, 'down'))
        self.assertFalse(self.grid.can_go((0, 4), 'down'))

    def test_get_neighbor_position(self):
        self.assertEqual(self.grid.get_neighbor_position((0, 0), 'right'), (0, 1))
        self.assertEqual(self.grid.get_neighbor_position((0, 0), 'left'), None)
        self.assertEqual(self.grid.get_neighbor_position((0, 0), 'up'), None)
        self.assertEqual(self.grid.get_neighbor_position((0, 0), 'down'), (1, 0))

    def test_shortest_distance(self):
        self.assertEqual(self.grid.shortest_distance((0, 0), (0, 0)), 0)
        # self.assertEqual(self.grid.shortest_distance((0, 0), (0, 1)), 1) # one to the right
        # self.assertEqual(self.grid.shortest_distance((0, 0), (1, 1)), 2) # one down and to the right
        # self.assertEqual(self.grid.shortest_distance((0, 0), (2, 2)), 4) # two down and to the right
        # self.assertEqual(self.grid.shortest_distance(self.grid.start, self.grid.end), 31)




if __name__ == "__main__":
    unittest.main()
