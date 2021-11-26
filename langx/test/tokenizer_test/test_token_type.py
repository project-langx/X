import unittest

from ...tokenizer.token_type import TokenType


class TestTokenType(unittest.TestCase):
    def test_str_token_type(self) -> None:
        self.assertEqual(str(TokenType.PRINT), "__print__: 0")

    def test_token_type(self) -> None:
        self.assertEqual(TokenType.PRINT.value, 0)
        self.assertEqual(TokenType.PRINT.name, "PRINT")