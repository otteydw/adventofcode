import unittest
from day02 import Present

class TestPresent(unittest.TestCase):
    def test_present_paper(self):
        present = Present("2x3x4")
        self.assertAlmostEqual(present.paper_needed(), 58)
        self.assertAlmostEqual(present.ribbon_needed(), 34)
        present = Present("1x1x10")
        self.assertAlmostEqual(present.paper_needed(), 43)
        self.assertAlmostEqual(present.ribbon_needed(), 14)

if __name__ == '__main__':
    unittest.main()