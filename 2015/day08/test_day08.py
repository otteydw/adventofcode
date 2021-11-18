import unittest
import os

from day08 import SantaList

class TestSanta(unittest.TestCase):

    def get_string_from_example(self, filename):

        input_path = os.path.join(os.path.dirname(__file__), filename)
        with open(input_path) as input_file:
            string = input_file.readline().rstrip()

        return string

    def test_empty_string(self):

        santa_list = SantaList()
        string = self.get_string_from_example('example1.txt')
        self.assertAlmostEqual(santa_list._count_memory_chars(string), 2)
        self.assertAlmostEqual(santa_list._count_string_literal_chars(string), 0)
        self.assertAlmostEqual(santa_list._count_memory_escaped(string), 6)

    def test_escape_none(self):

        santa_list = SantaList()
        string = self.get_string_from_example('example2.txt')
        self.assertAlmostEqual(santa_list._count_memory_chars(string), 5)
        self.assertAlmostEqual(santa_list._count_string_literal_chars(string), 3)
        self.assertAlmostEqual(santa_list._count_memory_escaped(string), 9)

    def test_slash(self):

        santa_list = SantaList()
        string = self.get_string_from_example('example3.txt')
        self.assertAlmostEqual(santa_list._count_memory_chars(string), 10)
        self.assertAlmostEqual(santa_list._count_string_literal_chars(string), 7)
        self.assertAlmostEqual(santa_list._count_memory_escaped(string), 16)

    def test_hex(self):

        santa_list = SantaList()
        string = self.get_string_from_example('example4.txt')
        self.assertAlmostEqual(santa_list._count_memory_chars(string), 6)
        self.assertAlmostEqual(santa_list._count_string_literal_chars(string), 1)
        self.assertAlmostEqual(santa_list._count_memory_escaped(string), 11)

    def test_add(self):

        santa_list = SantaList()
        for example in ['example1.txt', 'example2.txt', 'example3.txt', 'example4.txt']:
            string = self.get_string_from_example(example)
            santa_list.add(string)
        self.assertAlmostEqual(santa_list.get_memory_chars(), 23)
        self.assertAlmostEqual(santa_list.get_string_literal_chars(), 11)
        self.assertAlmostEqual(santa_list.get_memory_escaped(), 42)



if __name__ == '__main__':
    unittest.main()