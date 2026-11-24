import unittest

from .day02_part2 import RPSGame


class TestSanta(unittest.TestCase):
    def setUp(self):
        self.myRPSGame = RPSGame("example.txt")

    def test_convert_move(self):
        self.assertEqual(self.myRPSGame.convert_move("A"), "R")
        self.assertEqual(self.myRPSGame.convert_move("P"), "P")

    def test_single_game_winner(self):
        self.assertEqual(self.myRPSGame.single_game_winner("R", "P"), 2)
        self.assertEqual(self.myRPSGame.single_game_winner("P", "R"), 1)
        self.assertEqual(self.myRPSGame.single_game_winner("P", "P"), 0)

    def test_single_game_score(self):
        self.assertEqual(self.myRPSGame.single_game_score("win", "P"), 8)
        self.assertEqual(self.myRPSGame.single_game_score("loss", "R"), 1)
        self.assertEqual(self.myRPSGame.single_game_score("draw", "S"), 6)

    def test_run_games(self):
        self.myRPSGame.run_games()
        self.assertEqual(self.myRPSGame.player2_score, 12)

    def test_move_to_achieve_result(self):
        self.assertEqual(self.myRPSGame.move_to_achieve_result("R", "X"), "S")
        self.assertEqual(self.myRPSGame.move_to_achieve_result("S", "Y"), "S")
        self.assertEqual(self.myRPSGame.move_to_achieve_result("P", "Z"), "S")
        self.assertEqual(self.myRPSGame.move_to_achieve_result("P", "X"), "R")


if __name__ == "__main__":
    unittest.main()
