import typing
import unittest
from typing import List

from langx.parser.parser import Parser
from langx.tokenizer.token import Token
from langx.tokenizer.token_type import TokenType
from langx.tokenizer.tokenizer import Tokenizer


class TestParser(unittest.TestCase):
    def __get_tokens_from_source(self, source: str) -> List[Token]:
        return Tokenizer(source=source).generate_tokens()

    @typing.no_type_check
    def test_null_tokens_list(self) -> None:
        with self.assertRaises(AssertionError):
            Parser(tokens=None)

    def test_empty_tokens_list(self) -> None:
        with self.assertRaises(AssertionError):
            Parser(tokens=[])

    def test_parse_print_number(self) -> None:
        tokens: List[Token] = self.__get_tokens_from_source("print(1)")

        self.assertEqual(len(tokens), 6)
        self.assertEqual(tokens[0].type, TokenType.PRINT)
        self.assertEqual(tokens[1].type, TokenType.LEFT_PAREN)
        self.assertEqual(tokens[2].type, TokenType.NUMBER)
        self.assertEqual(tokens[3].type, TokenType.RIGHT_PAREN)

    def test_parse_print_string(self) -> None:
        tokens: List[Token] = self.__get_tokens_from_source('print("hello")')

        self.assertEqual(len(tokens), 6)
        self.assertEqual(tokens[0].type, TokenType.PRINT)
        self.assertEqual(tokens[1].type, TokenType.LEFT_PAREN)
        self.assertEqual(tokens[2].type, TokenType.STRING)
        self.assertEqual(tokens[3].type, TokenType.RIGHT_PAREN)

    def test_parse_print_number_expr(self) -> None:
        tokens: List[Token] = self.__get_tokens_from_source("print(1 + 2 * 3 / 4 - 5)")

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
