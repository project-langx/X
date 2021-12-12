from typing import List

from .node import Node
from ...opcode.opcode import OpCode
from ...opcode.op_type import OpType
from ...utils.check_class import CheckClass


class PrintNode(CheckClass, Node):
    def __init__(self, expr: Node) -> None:
        super().__init__(self, expr=expr)
        self.__expr: Node = expr

    @property
    def expr(self) -> Node:
        return self.__expr

    def __eq__(self, __o: object) -> bool:
        if __o == None:
            return False

        if self is __o:
            return True

        if not isinstance(__o, PrintNode):
            return False

        return self.expr == __o.expr

    def walk_and_print(self, tab_level: int) -> str:
        ast_string: str = self._add_tabs(tab_level=tab_level)
        ast_string += "PrintNode(\n"
        tab_level += 1

        ast_string += self.__expr.walk_and_print(tab_level)

        tab_level -= 1
        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += ")\n"

        return ast_string

    def walk_and_compile(self, opcodes: List[OpCode]) -> None:
        assert opcodes != None

        self.__expr.walk_and_compile(opcodes)

        opcodes.append(OpCode(opcode=OpType.PRINT, op_value="", op_dtype=""))
