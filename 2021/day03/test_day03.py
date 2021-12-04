import unittest

import day03


class TestSanta(unittest.TestCase):
    def test_diagnostic_report_part1(self):

        reported_values = day03.load_from_file("example.txt")
        diag = day03.DiagnosticReport(reported_values)

        self.assertEqual(diag._find_common_bit_at_position(0), "1")
        self.assertEqual(diag._find_common_bit_at_position(1), "0")

        self.assertAlmostEqual(diag.calculate_gamma_rate(), 22)

        self.assertEqual(diag._find_least_common_bit_at_position(0), "0")
        self.assertEqual(diag._find_least_common_bit_at_position(1), "1")

        self.assertAlmostEqual(diag.calculate_epsilon_rate(), 9)

        self.assertAlmostEqual(diag.calculate_power_consumption(), 198)

    def test_diagnostic_report_part2(self):

        reported_values = day03.load_from_file("example.txt")
        diag = day03.DiagnosticReport(reported_values)

        self.assertAlmostEqual(diag.calculate_oxygen_generator_rating(), 23)
        self.assertAlmostEqual(diag.calculate_CO2_scrubber_rating(), 10)

        self.assertAlmostEqual(diag.calculate_life_support_rating(), 230)


if __name__ == "__main__":
    unittest.main()
