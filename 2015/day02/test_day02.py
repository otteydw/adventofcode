import unittest
from day02 import Present

class TestPresent(unittest.TestCase):
    def test_present_paper(self):
        present = Present("2x3x4")
        self.assertAlmostEqual(present.paper_needed(), 58)
        present = Present("1x1x10")
        self.assertAlmostEqual(present.paper_needed(), 43)

if __name__ == '__main__':
    unittest.main()