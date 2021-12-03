import unittest

import day03


class TestSanta(unittest.TestCase):
    def test_diagnostic_report(self):

        reported_values = day03.load_from_file("example.txt")
        diag = day03.DiagnosticReport(reported_values)

        self.assertAlmostEqual(diag._find_common_bit_at_position(0), "1")
        self.assertAlmostEqual(diag._find_common_bit_at_position(1), "0")

        self.assertAlmostEqual(diag.calculate_gamma_rate(), 22)

        self.assertAlmostEqual(diag._find_least_common_bit_at_position(0), "0")
        self.assertAlmostEqual(diag._find_least_common_bit_at_position(1), "1")

        self.assertAlmostEqual(diag.calculate_epsilon_rate(), 9)

        self.assertAlmostEqual(diag.calculate_power_consumption(), 198)


if __name__ == "__main__":
    unittest.main()
