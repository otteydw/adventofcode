import hashlib
import unittest

from day04 import is_mineable, get_hash, find_answer

class TestSanta(unittest.TestCase):
    def test_hash(self):

        self.assertAlmostEqual(is_mineable(get_hash("abcdef609043")), True)
        self.assertAlmostEqual(is_mineable(get_hash("abcdef609044")), False)
        self.assertAlmostEqual(is_mineable(get_hash("pqrstuv1048970")), True)
        self.assertAlmostEqual(is_mineable(get_hash("pqrstuv1048971")), False)
        self.assertAlmostEqual(find_answer("abcdef"), 609043)
        self.assertAlmostEqual(find_answer("pqrstuv"), 1048970)

if __name__ == '__main__':
    unittest.main()