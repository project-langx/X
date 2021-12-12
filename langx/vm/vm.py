from typing import List, Any

from ..opcode.op_type import OpType
from ..opcode.opcode import OpCode
from ..utils.check_class import CheckClass


class VM(CheckClass):
    def __init__(self, opcodes: List[OpCode]) -> None:
        super().__init__(opcodes=opcodes, check_empty_list=True)
        self.__opcodes: List[OpCode] = opcodes

        self.__constant_pool: List[str] = []

    def __pop(self) -> str:
        return self.__constant_pool.pop()

    def __push(self, constant: Any) -> None:
        self.__constant_pool.append(constant)

    def __cast_to_type(self, value: str, dtype: str) -> Any:
        if dtype == "int":
            return int(value)
        elif dtype == "float":
            return float(value)
        elif dtype == "string":
            return str(value)

    def __perform_binary_operation(self, opcode: OpType) -> None:
        right: Any = self.__pop()
        left: Any = self.__pop()

        if opcode == OpType.ADD:
            self.__push(left + right)
        elif opcode == OpType.SUB:
            self.__push(left - right)
        elif opcode == OpType.MUL:
            self.__push(left * right)
        elif opcode == OpType.DIV:
            if type(left) == int and type(right) == int:
                self.__push(left // right)
            else:
                self.__push(left / right)

    def run(self) -> None:
        for opcode in self.__opcodes:
            if opcode.opcode == OpType.PRINT:
                print(self.__pop())
            elif opcode.opcode == OpType.LOAD:
                self.__push(self.__cast_to_type(opcode.op_value, dtype=opcode.op_dtype))
            elif opcode.opcode in [OpType.ADD, OpType.SUB, OpType.MUL, OpType.DIV]:
                self.__perform_binary_operation(opcode.opcode)
