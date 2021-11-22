from typing import List

from .node import Node
from ...opcode.opcode import OpCode


class ProgramNode(Node):
    def __init__(self, method: str, statements: List[Node]) -> None:
        self.__method: str = method
        self.__statements: List[Node] = statements

    @property
    def method(self) -> str:
        return self.__method

    @property
    def statements(self) -> List[Node]:
        return self.__statements

    def walk_and_print(self, tab_level: int) -> str:
        ast_string: str = self._add_tabs(tab_level=tab_level)
        ast_string += f"ProgramNode(method={self.__method})\n"
        tab_level += 1

        for statement in self.__statements:
            ast_string += statement.walk_and_print(tab_level)

        return ast_string

    def walk_and_compile(self, opcodes: List[OpCode]) -> None:
        for statement in self.__statements:
            statement.walk_and_compile(opcodes)
