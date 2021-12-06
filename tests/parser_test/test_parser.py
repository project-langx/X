import unittest

from langx.tokenizer.token_type import TokenType
from langx.tokenizer.tokenizer import Tokenizer


class TestParser(unittest.TestCase):
    def __get_tokens_from_source(self, source):
        return Tokenizer(source=source).generate_tokens()

    def test_parse_print_number(self):
        tokens = self.__get_tokens_from_source("print(1)")

        self.assertEqual(len(tokens), 6)
        self.assertEqual(tokens[0].type, TokenType.PRINT)
        self.assertEqual(tokens[1].type, TokenType.LEFT_PAREN)
        self.assertEqual(tokens[2].type, TokenType.NUMBER)
        self.assertEqual(tokens[3].type, TokenType.RIGHT_PAREN)

    def test_parse_print_string(self):
        tokens = self.__get_tokens_from_source("print(\"hello\")")

        self.assertEqual(len(tokens), 6)
        self.assertEqual(tokens[0].type, TokenType.PRINT)
        self.assertEqual(tokens[1].type, TokenType.LEFT_PAREN)
        self.assertEqual(tokens[2].type, TokenType.STRING)
        self.assertEqual(tokens[3].type, TokenType.RIGHT_PAREN)

    def test_parse_print_number_expr(self):
        tokens = self.__get_tokens_from_source("print(1 + 2 * 3 / 4 - 5)")

        self.assertEqual(len(tokens), 14)
        self.assertEqual(tokens[0].type, TokenType.PRINT)
        self.assertEqual(tokens[1].type, TokenType.LEFT_PAREN)
        self.assertEqual(tokens[2].type, TokenType.NUMBER)
        self.assertEqual(tokens[3].type, TokenType.ADD)
        self.assertEqual(tokens[4].type, TokenType.NUMBER)
        self.assertEqual(tokens[5].type, TokenType.MUL)
        self.assertEqual(tokens[6].type, TokenType.NUMBER)
        self.assertEqual(tokens[7].type, TokenType.DIV)
        self.assertEqual(tokens[8].type, TokenType.NUMBER)
        self.assertEqual(tokens[9].type, TokenType.SUB)
        self.assertEqual(tokens[10].type, TokenType.NUMBER)
        self.assertEqual(tokens[11].type, TokenType.RIGHT_PAREN)
        