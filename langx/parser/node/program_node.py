from typing import List

from .node import Node
from ...opcode.opcode import OpCode
from ...utils.check_class import CheckClass


class ProgramNode(CheckClass, Node):
    def __init__(self, method: str, statements: List[Node]) -> None:
        super().__init__(
            self,
            method=method,
            statements=statements,
            check_empty_str=True,
            check_empty_list=True,
        )
        self.__method: str = method
        self.__statements: List[Node] = statements

    @property
    def method(self) -> str:
        return self.__method

    @property
    def statements(self) -> List[Node]:
        return self.__statements

    def __eq__(self, __o: object) -> bool:
        if __o == None:
            return False

        if self is __o:
            return True

        if not isinstance(__o, ProgramNode):
            return False

        for self_statement, o_statement in zip(self.statements, __o.statements):
            if self_statement != o_statement:
                return False

        return self.method == __o.method

    def walk_and_print(self, tab_level: int) -> str:
        ast_string: str = self._add_tabs(tab_level=tab_level)
        ast_string += f"ProgramNode(method={self.__method})\n"
        tab_level += 1

        for statement in self.__statements:
            ast_string += statement.walk_and_print(tab_level)

        return ast_string

    def walk_and_compile(self, opcodes: List[OpCode]) -> None:
        assert opcodes != None

        for statement in self.__statements:
            statement.walk_and_compile(opcodes)
