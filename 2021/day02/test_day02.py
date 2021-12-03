import unittest

import day02

class TestSanta(unittest.TestCase):
    def test_sub(self):

        sub = day02.Submarine()
        instructions = day02.load_from_file("example.txt")

        for instruction in instructions:
            sub.move(instruction)

        self.assertAlmostEqual(sub.depth, 10)
        self.assertAlmostEqual(sub.horizontal_position, 15)

    def test_sub2(self):

        sub = day02.Submarine2()
        instructions = day02.load_from_file("example.txt")

        for instruction in instructions:
            sub.move(instruction)

        self.assertAlmostEqual(sub.depth, 60)
        self.assertAlmostEqual(sub.horizontal_position, 15)

if __name__ == '__main__':
    unittest.main()