import unittest

from langx.tokenizer.token import Token
from langx.tokenizer.token_type import TokenType


class TestToken(unittest.TestCase):
    def test_create_token(self) -> None:
        token: Token = Token(type=TokenType.NUMBER, dtype="int", value="3", line_num=1)

        self.assertEqual(token.type, TokenType.NUMBER)
        self.assertEqual(token.dtype, "int")
        self.assertEqual(token.value, "3")
        self.assertEqual(token.line_num, 1)
