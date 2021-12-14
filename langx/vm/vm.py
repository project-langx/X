from typing import List, Union

from ..opcode.op_type import OpType
from ..opcode.opcode import OpCode
from ..utils.check_class import CheckClass
from ..value.value import Value


class VM(CheckClass):
    def __init__(self, opcodes: List[OpCode]) -> None:
        super().__init__(opcodes=opcodes, check_empty_list=True)
        self.__opcodes: List[OpCode] = opcodes

        self.__constant_pool: List[Value] = []

    def __pop(self) -> Value:
        return self.__constant_pool.pop()

    def __push(self, constant: Value) -> None:
        self.__constant_pool.append(constant)

    def __perform_binary_operation(self, opcode: OpType) -> None:
        right: Value = self.__pop()
        left: Value = self.__pop()

        if opcode == OpType.ADD:
            self.__push(left + right)
        elif opcode == OpType.SUB:
            self.__push(left - right)
        elif opcode == OpType.MUL:
            self.__push(left * right)
        elif opcode == OpType.DIV:
            if left.dtype == "int" and right.dtype == "int":
                self.__push(left // right)
            else:
                self.__push(left / right)

    def run(self) -> None:
        for opcode in self.__opcodes:
            if opcode.opcode == OpType.PRINT:
                print(self.__pop().value)
            elif opcode.opcode == OpType.LOAD:
                self.__push(Value(value=opcode.op_value, dtype=opcode.op_dtype))
            elif opcode.opcode in [OpType.ADD, OpType.SUB, OpType.MUL, OpType.DIV]:
                self.__perform_binary_operation(opcode.opcode)
