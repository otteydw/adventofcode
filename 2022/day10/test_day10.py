import unittest

from day10 import Tube


class TestSanta(unittest.TestCase):

    def test_signal_strength(self):
        input_filename = "small_program.txt"
        self.tube = Tube(input_filename)
        self.assertEqual(self.tube.signal_strength(5), -5)

        input_filename = "larger_program.txt"
        self.tube = Tube(input_filename)
        self.assertEqual(self.tube.signal_strength(20), 420)
        self.assertEqual(self.tube.signal_strength(60), 1140)
        self.assertEqual(self.tube.signal_strength(100), 1800)
        self.assertEqual(self.tube.signal_strength(140), 2940)
        self.assertEqual(self.tube.signal_strength(180), 2880)
        self.assertEqual(self.tube.signal_strength(220), 3960)

    def test_sum_of_signal_strengths(self):
        input_filename = "larger_program.txt"
        self.tube = Tube(input_filename)
        interesting_signals=[20, 60, 100, 140, 180, 220]
        self.assertEqual(self.tube.sum_of_signal_strengths(interesting_signals), 13140)

if __name__ == "__main__":
    unittest.main()
