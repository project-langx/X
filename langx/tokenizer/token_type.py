from enum import Enum


class TokenType(Enum):
    # Keywords
    PRINT: int = 0

    # Operators
    LEFT_PAREN: int = 1
    RIGHT_PAREN: int = 2
    ADD: int = 3
    SUB: int = 4
    MUL: int = 5
    DIV: int = 6

    # Types
    STRING: int = 7
    NUMBER: int = 8

    # Special
    NEWLINE: int = 9
    EOF: int = 10

    def __str__(self) -> str:
        return f"__{self.name.lower()}__"
