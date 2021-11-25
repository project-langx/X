import unittest

from ...tokenizer.token import Token


class TestToken(unittest.TestCase):
    def test_create_token(self):
        token: Token = Token(type="__number__", dtype="int", value="3", line_num=1)

        self.assertEqual(token.type, "__number__")
        self.assertEqual(token.dtype, "int")
        self.assertEqual(token.value, "3")
        self.assertEqual(token.line_num, 1)