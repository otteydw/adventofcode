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

    def test_is_incomplete(self):
        self.assertEqual(day10.is_incomplete("{([(<{}[<>[]}>{[]{[(<()"), False)
        self.assertEqual(day10.is_incomplete("[[<[([]))<([[{}[[()]]]"), False)
        self.assertEqual(day10.is_incomplete("[{[{({}]{}}([{[{{{}}([]"), False)
        self.assertEqual(day10.is_incomplete("[<(<(<(<{}))><([]([]()"), False)
        self.assertEqual(day10.is_incomplete("<{([([[(<>()){}]>(<<{{"), False)
        self.assertEqual(day10.is_incomplete("[({(<(())[]>[[{[]{<()<>>"), True)

    def test_autocomplete_score(self):
        self.assertEqual(day10.autocomplete_score("}}]])})]"), 288957)
        self.assertEqual(day10.autocomplete_score(")}>]})"), 5566)
        self.assertEqual(day10.autocomplete_score("}}>}>))))"), 1480781)
        self.assertEqual(day10.autocomplete_score("]]}}]}]}>"), 995444)
        self.assertEqual(day10.autocomplete_score("])}>"), 294)

    def test_find_completion_string(self):
        self.assertEqual(
            day10.find_completion_string("[({(<(())[]>[[{[]{<()<>>"), "}}]])})]"
        )
        self.assertEqual(
            day10.find_completion_string("[(()[<>])]({[<{<<[]>>("), ")}>]})"
        )
        self.assertEqual(
            day10.find_completion_string("(((({<>}<{<{<>}{[]{[]{}"), "}}>}>))))"
        )
        self.assertEqual(
            day10.find_completion_string("{<[[]]>}<{[{[{[]{()[[[]"), "]]}}]}]}>"
        )
        self.assertEqual(
            day10.find_completion_string("<{([{{}}[<[[[<>{}]]]>[]]"), "])}>"
        )

    def test_middle_autocomplete_score(self):
        self.assertEqual(day10.middle_autocomplete_score("example.txt"), 288957)


if __name__ == "__main__":
    unittest.main()
