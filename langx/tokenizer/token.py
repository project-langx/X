from typing import NamedTuple

from .token_type import TokenType


class Token(NamedTuple):
    type: TokenType
    dtype: str
    value: str
    line_num: int

    def __str__(self) -> str:
        return f"Token(type={str(self.type)}, dtype={self.dtype}, value={self.value}, line_num={self.line_num})"
