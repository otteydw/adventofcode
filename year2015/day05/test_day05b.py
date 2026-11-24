import unittest

from .day05b import is_nice, rule1, rule2


class TestSanta(unittest.TestCase):
    def test_hash(self):

        self.assertAlmostEqual(rule1("xyxy"), True)
        self.assertAlmostEqual(rule1("aabcdefgaa"), True)
        self.assertAlmostEqual(rule1("uurcxstgmygtbstg"), True)
        self.assertAlmostEqual(rule1("aaa"), False)
        self.assertAlmostEqual(rule1("ieodomkazucvgmuy"), False)

        self.assertAlmostEqual(rule2("xyx"), True)
        self.assertAlmostEqual(rule2("abcdefeghi"), True)
        self.assertAlmostEqual(rule2("aaa"), True)
        self.assertAlmostEqual(rule2("ieodomkazucvgmuy"), True)
        self.assertAlmostEqual(rule2("uurcxstgmygtbstg"), False)

        self.assertAlmostEqual(is_nice("qjhvhtzxzqqjkmpb"), True)
        self.assertAlmostEqual(is_nice("xxyxx"), True)
        self.assertAlmostEqual(is_nice("uurcxstgmygtbstg"), False)
        self.assertAlmostEqual(is_nice("ieodomkazucvgmuy"), False)


if __name__ == "__main__":
    unittest.main()
