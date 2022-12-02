import os


def load_from_file(filename):
    input_path = os.path.join(os.path.dirname(__file__), filename)

    data = []

    with open(input_path) as input_file:
        for line in input_file:
            data.append(line.rstrip())

    return data


class RPSGame:
    def __init__(self, input_filename):
        rounds_as_text = load_from_file(input_filename)
        # self.player1_moves = []
        # self.player2_moves = []
        # self.rounds = []
        self.player1_score = 0
        self.player2_score = 0

        self.rounds = self.process_moves(rounds_as_text)

        # self.run_games()

    def process_moves(self, rounds_as_text):
        rounds = []
        for round_as_text in rounds_as_text:
            player1_move, player2_move = round_as_text.split(" ")
            # self.player1_moves.append(player1_move)
            # self.player2_moves.append(player2_move)
            rounds.append((player1_move, player2_move))

        return rounds

    def convert_move(self, move):
        if move in ["A", "X", "R"]:
            return "R"
        if move in ["B", "Y", "P"]:
            return "P"
        if move in ["C", "Z", "S"]:
            return "S"

    def single_game_winner(self, player1_move, player2_move):
        """Returns the player number of the winner (1 or 2) or 0 if it is a draw"""
        player1_move = self.convert_move(player1_move)
        player2_move = self.convert_move(player2_move)

        if player1_move == player2_move:
            return 0
        if (
            (player1_move == "R" and player2_move == "S")
            or (player1_move == "P" and player2_move == "R")
            or (player1_move == "S" and player2_move == "P")
        ):
            return 1
        return 2

    def single_game_score(self, game_result, move_made):
        score = 0

        if move_made == "R":
            score += 1
        elif move_made == "P":
            score += 2
        elif move_made == "S":
            score += 3

        if game_result == "win":
            score += 6
        elif game_result == "draw":
            score += 3

        return score

    def run_games(self):
        for round in self.rounds:
            player1_move = self.convert_move(round[0])
            player2_move = self.convert_move(round[1])

            winner = self.single_game_winner(player1_move, player2_move)

            if winner == 0:
                player1_result = "draw"
                player2_result = "draw"
            elif winner == 1:
                player1_result = "win"
                player2_result = "loss"
            else:
                player1_result = "loss"
                player2_result = "win"

            self.player1_score += self.single_game_score(player1_result, player1_move)
            self.player2_score += self.single_game_score(player2_result, player2_move)


if __name__ == "__main__":

    input_filename = "input.txt"
    myRPSGame = RPSGame(input_filename)
    myRPSGame.run_games()

    print(f"Player2 total score: {myRPSGame.player2_score}")
