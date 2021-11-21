from .node import Node
from ...opcode.opcode import OpCode
from ...opcode.op_type import OpType


class StringNode(Node):
    def __init__(self, value, dtype):
        self.__value = value
        self.__dtype = dtype

    @property
    def value(self):
        return self.__value

    def walk_and_print(self, tab_level):
        ast_string = self._add_tabs(tab_level=tab_level)
        ast_string += f"StringNode(value={self.__value})\n"

        return ast_string

    def walk_and_compile(self, opcodes):
        opcodes.append(OpCode(opcode=OpType.LOAD, op_value=self.__value, op_dtype=self.__dtype))