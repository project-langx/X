from typing import List, Optional

from ..opcode.op_type import OpType
from ..opcode.opcode import OpCode
from ..utils.check_class import CheckClass
from ..value.value import Value
from ..memory.memory import Memory


class VM(CheckClass):
    def __init__(self, opcodes: List[OpCode]) -> None:
        super().__init__(opcodes=opcodes, check_empty_list=True)
        self.__opcodes: List[OpCode] = opcodes

        self.__constant_pool: List[Value] = []
        self.__memory: Memory = Memory()

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

    def run(self, show_memory=False) -> Optional[str]:
        for opcode in self.__opcodes:
            if opcode.opcode == OpType.PRINT:
                print(self.__pop().value)
            elif opcode.opcode == OpType.LOAD:
                self.__push(Value(value=opcode.op_value, dtype=opcode.op_dtype))
            elif opcode.opcode in [OpType.ADD, OpType.SUB, OpType.MUL, OpType.DIV]:
                self.__perform_binary_operation(opcode.opcode)
            elif opcode.opcode == OpType.VAR:
                self.__memory.push_to_memory(memory_location=opcode.op_value, value=self.__pop())
            elif opcode.opcode == OpType.ASSIGN:
                self.__memory.push_to_memory(memory_location=opcode.op_value, value=self.__pop())

        if show_memory:
            return str(self.__memory)
