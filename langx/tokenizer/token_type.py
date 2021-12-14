from enum import Enum


class TokenType(Enum):
    # Keywords
    PRINT: int = 0
    VAR: int = 1

    # Operators
    LEFT_PAREN: int = 2
    RIGHT_PAREN: int = 3
    ADD: int = 4
    SUB: int = 5
    MUL: int = 6
    DIV: int = 7
    ASSIGNMENT: int = 8

    # Types
    STRING: int = 9
    NUMBER: int = 10

    # Special
    NEWLINE: int = 11
    EOF: int = 12
    UNK: int = 13
    IDENTIFIER: int = 14

    def __str__(self) -> str:
        return f"__{self.name.lower()}__: {self.value}"
