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
        values = [val.value for val in self.__values]
        opcode = OpCode(opcode=OpType.PRINT, op_values=values, op_dtype=self.__values[0].type)
        return opcode