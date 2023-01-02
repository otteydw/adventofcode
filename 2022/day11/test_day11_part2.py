import unittest

from day11_part2 import Game


class TestSanta(unittest.TestCase):
    def test_monkey_business(self):
        input_filename = "example.txt"
        game = Game(input_filename, rounds=20)
        self.assertEqual(game.monkey_business(), 10605)

        game = Game(input_filename, rounds=10000, crt=True)
        self.assertEqual(game.monkey_business(), 2713310158)

        # game = Game(input_filename, rounds=1000, relief_enabled=False)
        # self.assertEqual(game.monkey_business(), 27019168)

        # game = Game(input_filename, rounds=10000, relief_enabled=False)
        # self.assertEqual(game.monkey_business(), 2713310158)

if __name__ == "__main__":
    unittest.main()
