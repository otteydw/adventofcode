import unittest

from .day07 import (
    get_space_to_free,
    get_unused_space,
    load_from_file,
    parse_terminal_output,
    size_of_dir_to_delete,
)


class TestSanta(unittest.TestCase):
    def setUp(self):
        input_filename = "example.txt"
        data = load_from_file(input_filename)
        self.filesystem = parse_terminal_output(data)
        # self.filesystem.print_tree()

    def test_sum(self):
        self.assertEqual(self.filesystem.sum_dirs_under_size(100000), 95437)

    def test_get_unused_space(self):
        self.assertEqual(get_unused_space(self.filesystem), 21618835)

    def test_get_space_to_free(self):
        self.assertEqual(get_space_to_free(self.filesystem), 8381165)

    def test_delete(self):
        self.filesystem.print_tree()
        self.assertEqual(size_of_dir_to_delete(self.filesystem), 24933642)


if __name__ == "__main__":
    unittest.main()
