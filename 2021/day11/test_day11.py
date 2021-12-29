import unittest
import numpy as np

import day11


class TestSanta(unittest.TestCase):
    def test_one_step(self):
        octopus_array = day11.load_into_array("example_small/example.txt")
        print(octopus_array)
        octopus_array_after_one_step = day11.load_into_array("example_small/after_step_01.txt")
        octopus_array_after_two_steps = day11.load_into_array("example_small/after_step_02.txt")
        day11.one_step(octopus_array)
        print(octopus_array)
        self.assertEqual(np.array_equal(octopus_array, octopus_array_after_one_step), True)
        day11.one_step(octopus_array)
        self.assertEqual(np.array_equal(octopus_array, octopus_array_after_two_steps), True)

    def test_one_step_count(self):
        octopus_array = day11.load_into_array("example_small/example.txt")
        self.assertEqual(day11.one_step(octopus_array), 9)
        self.assertEqual(day11.one_step(octopus_array), 0)

    def test_step(self):
        octopus_array = day11.load_into_array("example_small/example.txt")
        octopus_array_after_two_steps = day11.load_into_array("example_small/after_step_02.txt")
        day11.step(octopus_array, 2)
        self.assertEqual(np.array_equal(octopus_array, octopus_array_after_two_steps), True)

    def test_step_count(self):
        octopus_array = day11.load_into_array("example_small/example.txt")
        self.assertEqual(day11.step(octopus_array, 2), 9)

    def test_step_final_little_by_little(self):
        for step_count in range(1, 10):
            octopus_array = day11.load_into_array("example_large/example.txt")
            step_filename = f"example_large/after_step_{str(step_count).zfill(2)}.txt"
            expected_array = day11.load_into_array(step_filename)
            print(f"Testing {step_count}")
            day11.step(octopus_array, step_count)
            self.assertEqual(np.array_equal(octopus_array, expected_array), True)

    def test_step_count_final(self):
        octopus_array = day11.load_into_array("example_large/example.txt")
        self.assertEqual(day11.step(octopus_array, 10), 204)

        octopus_array = day11.load_into_array("example_large/example.txt")
        self.assertEqual(day11.step(octopus_array, 100), 1656)

    def test_check_simultaneous_flash(self):
        octopus_array = day11.load_into_array("example3/example_true.txt")
        self.assertTrue(day11.check_simultaneous_flash(octopus_array))

        octopus_array = day11.load_into_array("example3/example_false1.txt")
        self.assertFalse(day11.check_simultaneous_flash(octopus_array))

        octopus_array = day11.load_into_array("example3/example_false2.txt")
        self.assertFalse(day11.check_simultaneous_flash(octopus_array))

    def test_get_simultaneous_flash_step(self):
        octopus_array = day11.load_into_array("example_large/example.txt")
        self.assertEqual(day11.get_simultaneous_flash_step(octopus_array), 195)
if __name__ == "__main__":
    unittest.main()
