import unittest
from typing import List

from ...tokenizer.tokenizer import Tokenizer
from ...tokenizer.token import Token
from ...tokenizer.token_type import TokenType


class TestTokenizer(unittest.TestCase):
    def test_tokenizer_print(self) -> None:
        tokenizer: Tokenizer = Tokenizer("print(")
        tokens: List[Token] = tokenizer.generate_tokens()

        self.assertEqual(
            tokens[0], Token(type=TokenType.PRINT, dtype="", value="print", line_num=1)
        )

    def test_tokenizer_left_paren(self) -> None:
        tokenizer: Tokenizer = Tokenizer("(")
        tokens: List[Token] = tokenizer.generate_tokens()

        self.assertEqual(
            tokens[0], Token(type=TokenType.LEFT_PAREN, dtype="", value="", line_num=1)
        )

    def test_tokenizer_right_paren(self) -> None:
        tokenizer: Tokenizer = Tokenizer(")")
        tokens: List[Token] = tokenizer.generate_tokens()

        self.assertEqual(
            tokens[0], Token(type=TokenType.RIGHT_PAREN, dtype="", value="", line_num=1)
        )

    def test_tokenizer_add(self) -> None:
        tokenizer: Tokenizer = Tokenizer("+")
        tokens: List[Token] = tokenizer.generate_tokens()

        self.assertEqual(
            tokens[0], Token(type=TokenType.ADD, dtype="", value="", line_num=1)
        )

    def test_tokenizer_sub(self) -> None:
        tokenizer: Tokenizer = Tokenizer("-")
        tokens: List[Token] = tokenizer.generate_tokens()

        self.assertEqual(
            tokens[0], Token(type=TokenType.SUB, dtype="", value="", line_num=1)
        )

    def test_tokenizer_mul(self) -> None:
        tokenizer: Tokenizer = Tokenizer("*")
        tokens: List[Token] = tokenizer.generate_tokens()

        self.assertEqual(
            tokens[0], Token(type=TokenType.MUL, dtype="", value="", line_num=1)
        )

    def test_tokenizer_div(self) -> None:
        tokenizer: Tokenizer = Tokenizer("/")
        tokens: List[Token] = tokenizer.generate_tokens()

        self.assertEqual(
            tokens[0], Token(type=TokenType.DIV, dtype="", value="", line_num=1)
        )

    def test_tokenizer_string(self) -> None:
        tokenizer: Tokenizer = Tokenizer('"Hello"')
        tokens: List[Token] = tokenizer.generate_tokens()

        self.assertEqual(
            tokens[0],
            Token(type=TokenType.STRING, dtype="string", value="Hello", line_num=1),
        )

    def test_tokenizer_number_int(self) -> None:
        tokenizer: Tokenizer = Tokenizer("123\n")
        tokens: List[Token] = tokenizer.generate_tokens()

        self.assertEqual(
            tokens[0],
            Token(type=TokenType.NUMBER, dtype="int", value="123", line_num=1),
        )

    def test_tokenizer_number_float(self) -> None:
        tokenizer: Tokenizer = Tokenizer("123.456\n")
        tokens: List[Token] = tokenizer.generate_tokens()

        self.assertEqual(
            tokens[0],
            Token(type=TokenType.NUMBER, dtype="float", value="123.456", line_num=1),
        )

    def test_tokenizer_newline(self) -> None:
        tokenizer: Tokenizer = Tokenizer("\n")
        tokens: List[Token] = tokenizer.generate_tokens()

        self.assertEqual(
            tokens[0], Token(type=TokenType.NEWLINE, dtype="", value="", line_num=1)
        )

    def test_tokenizer_eof(self) -> None:
        tokenizer: Tokenizer = Tokenizer("")
        tokens: List[Token] = tokenizer.generate_tokens()

        self.assertEqual(
            tokens[-1], Token(type=TokenType.EOF, dtype="", value="", line_num=2)
        )
