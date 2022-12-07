import unittest

from day04 import (
    check_overlap,
    convert_assignment,
    load_from_file,
    parse_section_assignments,
    count_overlaps,
)


class TestSanta(unittest.TestCase):
    def test_convert_assignment(self):
        self.assertEqual(convert_assignment("2-4"), (2, 4))
        self.assertEqual(convert_assignment("6-6"), (6, 6))

    def test_check_overlap(self):
        self.assertEqual(check_overlap((2, 8), (3, 7)), True)
        self.assertEqual(check_overlap((3, 7), (2, 8)), True)
        self.assertEqual(check_overlap((6, 6), (4, 6)), True)
        self.assertEqual(check_overlap((4, 6), (6, 6)), True)
        self.assertEqual(check_overlap((2, 3), (5, 7)), False)
        self.assertEqual(check_overlap((5, 7), (2, 3)), False)

    def test_count_overlaps(self):
        input_filename = "example.txt"
        data = load_from_file(input_filename)
        assignments = parse_section_assignments(data)
        self.assertEqual(count_overlaps(assignments), 2)


if __name__ == "__main__":
    unittest.main()
