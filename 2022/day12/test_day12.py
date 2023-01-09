import unittest

from day12 import Maze, MazeLocation


class TestSanta(unittest.TestCase):
    def setUp(self):
        input_filename = "example.txt"
        self.maze = Maze(input_filename)

    def test_set_start(self):
        self.assertEqual(self.maze.start, MazeLocation(row=0, column=0))

    def test_set_end(self):
        self.assertEqual(self.maze.goal, MazeLocation(row=2, column=5))

    def test_get_height_at_position(self):
        self.assertEqual(self.maze.get_height_at_position(self.maze.start), 0)
        self.assertEqual(self.maze.get_height_at_position(self.maze.goal), 25)

    def test_goal_test(self):
        self.assertTrue(self.maze.goal_test(self.maze.goal))
        self.assertTrue(self.maze.goal_test(MazeLocation(row=2, column=5)))

    # def test_can_go(self):
    #     self.assertTrue(self.maze.can_go(self.maze.start, 'right'))
    #     self.assertTrue(self.maze.can_go((0, 1), 'right'))
    #     self.assertFalse(self.maze.can_go((0, 2), 'right'))

    #     self.assertFalse(self.maze.can_go(self.maze.start, 'left'))
    #     self.assertTrue(self.maze.can_go((2, 1), 'left'))

    #     self.assertFalse(self.maze.can_go(self.maze.start, 'up'))
    #     self.assertTrue(self.maze.can_go((4, 7), 'up'))

    #     self.assertTrue(self.maze.can_go(self.maze.start, 'down'))
    #     self.assertFalse(self.maze.can_go((0, 4), 'down'))

    # def test_get_neighbor_position(self):
    #     self.assertEqual(self.maze.get_neighbor_position((0, 0), 'right'), (0, 1))
    #     self.assertEqual(self.maze.get_neighbor_position((0, 0), 'left'), None)
    #     self.assertEqual(self.maze.get_neighbor_position((0, 0), 'up'), None)
    #     self.assertEqual(self.maze.get_neighbor_position((0, 0), 'down'), (1, 0))

    # def test_shortest_distance(self):
    #     self.assertEqual(self.maze.shortest_distance((0, 0), (0, 0)), 0)
        # self.assertEqual(self.maze.shortest_distance((0, 0), (0, 1)), 1) # one to the right
        # self.assertEqual(self.maze.shortest_distance((0, 0), (1, 1)), 2) # one down and to the right
        # self.assertEqual(self.maze.shortest_distance((0, 0), (2, 2)), 4) # two down and to the right
        # self.assertEqual(self.maze.shortest_distance(self.maze.start, self.maze.end), 31)

    def test_successors(self):
        self.assertCountEqual(self.maze.successors(MazeLocation(row=0, column=0)), [MazeLocation(row=1, column=0), MazeLocation(row=0, column=1)])
        self.assertCountEqual(self.maze.successors(MazeLocation(row=1, column=1)), [MazeLocation(row=0, column=1), MazeLocation(row=2, column=1), MazeLocation(row=1, column=0), MazeLocation(row=1, column=2)])
        self.assertCountEqual(self.maze.successors(MazeLocation(row=1, column=3)), [MazeLocation(row=0, column=3), MazeLocation(row=2, column=3), MazeLocation(row=1, column=2)])

if __name__ == "__main__":
    unittest.main()
