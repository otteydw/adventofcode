import unittest
from day03 import Santa, go_santa, go_multi_santa

class TestSanta(unittest.TestCase):
    def test_present_paper(self):

        presents = {}
        santa = Santa()
        go_santa(presents, santa, ">")
        self.assertAlmostEqual(len(presents), 2)

        presents = {}
        santa = Santa()
        go_santa(presents, santa, "^>v<")
        self.assertAlmostEqual(len(presents), 4)

        presents = {}
        santa = Santa()
        go_santa(presents, santa, "^v^v^v^v^v")
        self.assertAlmostEqual(len(presents), 2)

        presents = {}
        santa = Santa()
        robot = Santa()
        go_multi_santa(presents, santa, robot, "^v")
        self.assertAlmostEqual(len(presents), 3)

        presents = {}
        santa = Santa()
        robot = Santa()
        go_multi_santa(presents, santa, robot, "^>v<")
        self.assertAlmostEqual(len(presents), 3)

        presents = {}
        santa = Santa()
        robot = Santa()
        go_multi_santa(presents, santa, robot, "^v^v^v^v^v")
        self.assertAlmostEqual(len(presents), 11)

if __name__ == '__main__':
    unittest.main()