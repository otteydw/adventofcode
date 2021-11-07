import hashlib
import unittest

from day05 import has_double, is_nice, three_vowels

class TestSanta(unittest.TestCase):
    def test_hash(self):

        self.assertAlmostEqual(three_vowels("aei"), True)
        self.assertAlmostEqual(three_vowels("xazegov"), True)
        self.assertAlmostEqual(three_vowels("aeiouaeiouaeiou"), True)

        self.assertAlmostEqual(has_double("xx"), True)
        self.assertAlmostEqual(has_double("abcdde"), True)
        self.assertAlmostEqual(has_double("aabbccdd"), True)

        self.assertAlmostEqual(is_nice("ugknbfddgicrmopn"), True)
        self.assertAlmostEqual(is_nice("aaa"), True)
        self.assertAlmostEqual(is_nice("jchzalrnumimnmhp"), False)
        self.assertAlmostEqual(is_nice("haegwjzuvuyypxyu"), False)
        self.assertAlmostEqual(is_nice("dvszwmarrgswjxmb"), False)

if __name__ == '__main__':
    unittest.main()