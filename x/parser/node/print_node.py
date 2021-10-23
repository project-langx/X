from .node import Node
from ...opcode.opcode import OpCode
from ...opcode.op_type import OpType


class PrintNode(Node):
    def __init__(self, values):
        self.__values = values

    @property
    def children(self):
        return self.__values

    def __str__(self):
        return f"PrintNode()"

    def walk(self):
        opcode = OpCode(OpType.PRINT, self.__values)
        return opcode