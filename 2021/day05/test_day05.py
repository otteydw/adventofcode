import unittest

import day05


class TestSanta(unittest.TestCase):
    def test_test1(self):

        data = day05.load_from_file("example.txt")
        vent = day05.VentField(data)
        print(vent)
        self.assertEqual(vent.number_of_lines_covering_point((2, 9)), 2)
        self.assertEqual(vent.number_of_lines_covering_point((2, 1)), 1)
        self.assertEqual(vent.number_of_lines_covering_point((2, 2)), 1)
        self.assertEqual(vent.number_of_lines_covering_point((2, 3)), 0)
        self.assertEqual(vent.number_of_points_with_overlap(), 5)


if __name__ == "__main__":
    unittest.main()
