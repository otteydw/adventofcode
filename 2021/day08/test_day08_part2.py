import unittest

import day08_part2


class TestSanta(unittest.TestCase):
    # def setUp(self):
    #     self.input_values1, self.output_values1 = day08_part2.parse_input("example1.txt")
    #     self.input_values2, self.output_values2 = day08_part2.parse_input("example2.txt")

    def test_decode_string(self):
        input_values, output_values = day08_part2.parse_input("example1.txt")
        for input_value, _ in zip(input_values, output_values):
            mycode = day08_part2.ClockDecoder(input_value)
            self.assertEqual(mycode.decode_string("acedgfb"), 8)
            self.assertEqual(mycode.decode_string("cdfbe"), 5)
            self.assertEqual(mycode.decode_string("gcdfa"), 2)
            self.assertEqual(mycode.decode_string("fbcad"), 3)
            self.assertEqual(mycode.decode_string("dab"), 7)
            self.assertEqual(mycode.decode_string("cefabd"), 9)
            self.assertEqual(mycode.decode_string("cdfgeb"), 6)
            self.assertEqual(mycode.decode_string("eafb"), 4)
            self.assertEqual(mycode.decode_string("cagedb"), 0)
            self.assertEqual(mycode.decode_string("ab"), 1)

    def test_decode_list_example1(self):
        input_values, output_values = day08_part2.parse_input("example1.txt")
        for input_value, output_value in zip(input_values, output_values):
            mycode = day08_part2.ClockDecoder(input_value)
            self.assertEqual(mycode.decode_list(output_value), "5353")

    def test_decode_list_example2(self):
        input_values, output_values = day08_part2.parse_input("example2.txt")
        expected_outputs = ["8394", "9781", "1197", "9361", "4873", "8418", "4548", "1625", "8717", "4315"]
        for input_value, output_value, expected_output in zip(input_values, output_values, expected_outputs):
            mycode = day08_part2.ClockDecoder(input_value)
            self.assertEqual(mycode.decode_list(output_value), expected_output)

    def test_sum_decoded_values_from_input(self):
        self.assertEqual(day08_part2.sum_decoded_values_from_input('example2.txt'), 61229)

if __name__ == "__main__":
    unittest.main()
