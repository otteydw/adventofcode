import unittest

from day13 import load_from_file, solve


class TestSanta(unittest.TestCase):
    def setUp(self):
        input_filename = "example.txt"
        self.data = load_from_file(input_filename)

    def test_solve(self):
        self.assertTrue(solve('1', '2'))
        self.assertTrue(solve(['1'], ['2']))
        self.assertTrue(solve(['1'], 2))

        self.assertFalse(solve('2', '1'))
        self.assertFalse(solve(['2'], ['1']))
        self.assertFalse(solve(['2'], 1))

if __name__ == "__main__":
    unittest.main()
