from enum import Enum


class OpType(Enum):
    PRINT: int = 0
    LOAD: int = 1
    LOAD_VAR: int = 2
    MUL: int = 3
    DIV: int = 4
    ADD: int = 5
    SUB: int = 6
    VAR: int = 7
    ASSIGN: int = 8