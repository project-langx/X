from .node import Node
from ...opcode.opcode import OpCode
from ...opcode.op_type import OpType


class BinaryOperatorNode(Node):
    def __init__(self, operator, left, right):
        self.__operator = operator
        self.__left = left
        self.__right = right

    @property
    def operator(self):
        return self.__operator

    @property
    def left(self):
        return self.__left

    @property
    def right(self):
        return self.__right

    def walk_and_print(self, tab_level):
        ast_string = self._add_tabs(tab_level=tab_level)
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

    def walk_and_compile(self, opcodes):
        self.__left.walk_and_compile(opcodes)
        self.__right.walk_and_compile(opcodes)

        opcodes.append(OpCode(opcode=OpType[self.__operator], op_value="", op_dtype=""))
