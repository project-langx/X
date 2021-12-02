from typing import List

from .node import Node
from ...opcode.opcode import OpCode
from ...opcode.op_type import OpType


class BinaryOperatorNode(Node):
    def __init__(self, operator: str, left: Node, right: Node) -> None:
        self.__operator: str = operator
        self.__left: Node = left
        self.__right: Node = right

    @property
    def operator(self) -> str:
        return self.__operator

    @property
    def left(self) -> Node:
        return self.__left

    @property
    def right(self) -> Node:
        return self.__right

    def __eq__(self, __o: object) -> bool:
        if self is __o:
            return True

        if not isinstance(__o, BinaryOperatorNode):
            return False

        return (
            self.operator == __o.operator
            and self.left == __o.left
            and self.right == __o.right
        )

    def walk_and_print(self, tab_level: int) -> str:
        ast_string: str = self._add_tabs(tab_level=tab_level)
        ast_string += "BinaryOperatorNode(\n"
        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += "left=(\n"

        tab_level += 1
        ast_string += self.__left.walk_and_print(tab_level)

        tab_level -= 1
        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += ")\n"

        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += f"op='{self.__operator}'\n"

        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += "right=(\n"
        tab_level += 1

        ast_string += self.__right.walk_and_print(tab_level)

        tab_level -= 1
        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += ")\n"

        return ast_string

    def walk_and_compile(self, opcodes: List[OpCode]) -> None:
        self.__left.walk_and_compile(opcodes)
        self.__right.walk_and_compile(opcodes)

        opcodes.append(OpCode(opcode=OpType[self.__operator], op_value="", op_dtype=""))
