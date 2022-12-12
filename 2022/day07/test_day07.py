import unittest

from day07 import load_from_file, parse_terminal_output


class TestSanta(unittest.TestCase):
    def setUp(self):
        input_filename = "example.txt"
        data = load_from_file(input_filename)
        self.filesystem = parse_terminal_output(data)

    def test_sum(self):
        self.assertEqual(self.filesystem.sum_dirs_under_size(100000), 95437)


if __name__ == "__main__":
    unittest.main()
