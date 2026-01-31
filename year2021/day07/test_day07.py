import unittest

from . import day07


class TestSanta(unittest.TestCase):
    def setUp(self):
        self.crab_positions = day07.load_ints_from_file_line("example.txt")

    def test_fuel_to_converge_on_position(self):

        self.assertEqual(day07.fuel_to_converge_on_position(self.crab_positions, 1), 41)
        self.assertEqual(day07.fuel_to_converge_on_position(self.crab_positions, 2), 37)
        self.assertEqual(day07.fuel_to_converge_on_position(self.crab_positions, 3), 39)
        self.assertEqual(day07.fuel_to_converge_on_position(self.crab_positions, 10), 71)

    def test_least_fuel_to_converge(self):

        self.assertEqual(day07.least_fuel_to_converge(self.crab_positions), 37)

    def test_fuel_to_converge_on_position_not_constant(self):

        self.assertEqual(
            day07.fuel_to_converge_on_position(self.crab_positions, 5, constant_rate=False),
            168,
        )
        self.assertEqual(
            day07.fuel_to_converge_on_position(self.crab_positions, 2, constant_rate=False),
            206,
        )
        self.assertEqual(day07.least_fuel_to_converge(self.crab_positions, constant_rate=False), 168)


if __name__ == "__main__":
    unittest.main()
