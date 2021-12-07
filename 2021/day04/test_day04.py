import unittest

import day04


class TestSanta(unittest.TestCase):
    def test_bingo1(self):

        _, boards = day04.load_bingo('example.txt')

        self.assertEqual(boards[0].value_at_position(2, 3), 16)
        self.assertEqual(boards[0].call(22), True)
        self.assertEqual(boards[0].call(82), False)

        # self.assertAlmostEqual(diag.calculate_gamma_rate(), 22)

    def test_horizontal_bingo(self):

        _, boards = day04.load_bingo('example.txt')

        self.assertEqual(boards[0].check_for_bingo(), False)
        self.assertEqual(boards[0].check_horizontal_bingo(), False)
        boards[0].call(8)
        self.assertEqual(boards[0].check_horizontal_bingo(), False)
        boards[0].call(2)
        self.assertEqual(boards[0].check_horizontal_bingo(), False)
        boards[0].call(23)
        self.assertEqual(boards[0].check_horizontal_bingo(), False)
        boards[0].call(4)
        self.assertEqual(boards[0].check_horizontal_bingo(), False)
        boards[0].call(24)
        self.assertEqual(boards[0].check_horizontal_bingo(), True)
        self.assertEqual(boards[0].check_for_bingo(), True)

    def test_vertical_bingo(self):

        _, boards = day04.load_bingo('example.txt')

        self.assertEqual(boards[0].check_for_bingo(), False)
        self.assertEqual(boards[0].check_vertical_bingo(), False)
        boards[0].call(13)
        self.assertEqual(boards[0].check_vertical_bingo(), False)
        boards[0].call(2)
        self.assertEqual(boards[0].check_vertical_bingo(), False)
        boards[0].call(9)
        self.assertEqual(boards[0].check_vertical_bingo(), False)
        boards[0].call(10)
        self.assertEqual(boards[0].check_vertical_bingo(), False)
        boards[0].call(12)
        self.assertEqual(boards[0].check_vertical_bingo(), True)
        self.assertEqual(boards[0].check_for_bingo(), True)

    def final_test(self):

        drawn_numbers, boards = day04.load_bingo('example.txt')
        for drawn_number in drawn_numbers:
            for board in boards:
                if board.call_and_check(drawn_number):
                    self.assertEqual(board.score(drawn_number), 4512)
                    break
                else:
                    continue
            break

    def first_winning_score(self):

        drawn_numbers, boards = day04.load_bingo('example.txt')
        self.assertEqual(day04.find_first_winning_board(drawn_numbers, boards), 4512)

    def lqast_winning_score(self):

        drawn_numbers, boards = day04.load_bingo('example.txt')
        self.assertEqual(day04.find_first_winning_board(drawn_numbers, boards), 1924)

if __name__ == "__main__":
    unittest.main()
