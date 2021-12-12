import unittest

from langx.utils.error import Error, TokenizerError, ParseError


class TestError(unittest.TestCase):
    def test_error(self) -> None:
        error_message: str = "Test top-level error"

        error: Error = Error(message=error_message)
        self.assertEqual(error_message, error.message)

        try:
            raise error
        except Error as e:
            self.assertEqual(error_message, e.message)

    def test_tokenizer_error(self) -> None:
        error_message: str = "Test tokenizer error"

        error: Error = TokenizerError(message=error_message)
        self.assertEqual(error_message, error.message)

        try:
            raise error
        except Error as e:
            self.assertEqual(error_message, e.message)

    def test_parse_error(self) -> None:
        error_message: str = "Test parse error"

        error: Error = ParseError(message=error_message)
        self.assertEqual(error_message, error.message)

        try:
            raise error
        except Error as e:
            self.assertEqual(error_message, e.message)
