import unittest

from .day04 import find_answer, get_hash, is_mineable


class TestSanta(unittest.TestCase):
    def test_hash(self):
        assert is_mineable(get_hash("abcdef609043"))
        assert not is_mineable(get_hash("abcdef609044"))
        assert is_mineable(get_hash("pqrstuv1048970"))
        assert not is_mineable(get_hash("pqrstuv1048971"))
        assert find_answer("abcdef") == 609043
        assert find_answer("pqrstuv") == 1048970


if __name__ == "__main__":
    unittest.main()
