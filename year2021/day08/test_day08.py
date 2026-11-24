import unittest

from . import day08


class TestSanta(unittest.TestCase):
    def test_what_integer(self):
        self.assertEqual(day08.what_integer("ab"), 1)
        self.assertEqual(day08.what_integer("fa"), 1)
        self.assertEqual(day08.what_integer("abcd"), 4)
        self.assertEqual(day08.what_integer("gbfa"), 4)
        self.assertEqual(day08.what_integer("abc"), 7)
        self.assertEqual(day08.what_integer("fac"), 7)
        self.assertEqual(day08.what_integer("abcdefg"), 8)
        self.assertEqual(day08.what_integer("gcbdfae"), 8)
        self.assertEqual(day08.what_integer("aaaaabbbbbbbbbbb"), 1)

    def test_count_digits(self):

        _, output_values = day08.parse_input("example2.txt")

        self.assertEqual(day08.count_digits(output_values, [1, 4, 7, 8]), 26)


if __name__ == "__main__":
    unittest.main()
