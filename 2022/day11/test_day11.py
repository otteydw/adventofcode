import unittest

from day11 import Game


class TestSanta(unittest.TestCase):
    def test_monkey_business(self):
        input_filename = "example.txt"
        game = Game(input_filename, rounds=20)
        self.assertEqual(game.monkey_business(), 10605)


if __name__ == "__main__":
    unittest.main()
