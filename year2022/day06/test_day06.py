import unittest

from .day06 import start_of_message, start_of_packet


class TestSanta(unittest.TestCase):
    def test_start_of_packet(self):
        self.assertEqual(start_of_packet("mjqjpqmgbljsphdztnvjfqwrcgsmlb"), 7)
        self.assertEqual(start_of_packet("bvwbjplbgvbhsrlpgdmjqwftvncz"), 5)
        self.assertEqual(start_of_packet("nppdvjthqldpwncqszvftbrmjlhg"), 6)
        self.assertEqual(start_of_packet("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 10)
        self.assertEqual(start_of_packet("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), 11)

    def test_start_of_message(self):
        self.assertEqual(start_of_message("mjqjpqmgbljsphdztnvjfqwrcgsmlb"), 19)
        self.assertEqual(start_of_message("bvwbjplbgvbhsrlpgdmjqwftvncz"), 23)
        self.assertEqual(start_of_message("nppdvjthqldpwncqszvftbrmjlhg"), 23)
        self.assertEqual(start_of_message("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 29)
        self.assertEqual(start_of_message("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), 26)


if __name__ == "__main__":
    unittest.main()
