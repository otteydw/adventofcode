import unittest
from day03 import Santa, go_santa

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

if __name__ == '__main__':
    unittest.main()