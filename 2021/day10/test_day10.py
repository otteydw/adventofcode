import unittest

import day10


class TestSanta(unittest.TestCase):
    def test_syntax_checker_score(self):
        self.assertEqual(day10.syntax_checker_score("}"), 1197)
        self.assertEqual(day10.syntax_checker_score(")"), 3)
        self.assertEqual(day10.syntax_checker_score(">"), 25137)
        self.assertEqual(day10.syntax_checker_score("]"), 57)

    def test_first_illegal_character(self):
        self.assertEqual(day10.first_illegal_character("{([(<{}[<>[]}>{[]{[(<()"), "}")
        self.assertEqual(day10.first_illegal_character("[[<[([]))<([[{}[[()]]]"), ")")
        self.assertEqual(day10.first_illegal_character("[{[{({}]{}}([{[{{{}}([]"), "]")
        self.assertEqual(day10.first_illegal_character("[<(<(<(<{}))><([]([]()"), ")")
        self.assertEqual(day10.first_illegal_character("<{([([[(<>()){}]>(<<{{"), ">")
        self.assertEqual(
            day10.first_illegal_character("[({(<(())[]>[[{[]{<()<>>"), None
        )

    def test_total_syntax_error_score(self):
        self.assertEqual(day10.total_syntax_error_score("example.txt"), 26397)


if __name__ == "__main__":
    unittest.main()
