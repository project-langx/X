from .node import Node
from ...opcode.opcode import OpCode
from ...opcode.op_type import OpType


class PrintNode(Node):
    def __init__(self, expr):
        self.__expr = expr

    @property
    def expr(self):
        return self.__expr

    def walk_and_print(self, tab_level):
        ast_string = self._add_tabs(tab_level=tab_level)
        ast_string += f"PrintNode(\n"
        tab_level += 1

        ast_string += self.__expr.walk_and_print(tab_level)
        
        tab_level -= 1
        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += ")\n"

        return ast_string

    def walk_and_compile(self, opcodes):
        self.__expr.walk_and_compile(opcodes)

        opcodes.append(OpCode(opcode=OpType.PRINT, op_value="", op_dtype=""))