from collections import namedtuple
from typing import List, NamedTuple

from ...opcode.op_type import OpType
from ...opcode.opcode import OpCode
from ...utils.check_class import CheckClass


class ConstVal(NamedTuple):
    value: str
    dtype: str


class PyDecompiler(CheckClass):
    def __init__(self, opcodes: List[OpCode]):
        super().__init__(opcodes=opcodes, check_empty_list=True)
        self.__opcodes: List[OpCode] = opcodes

        self.__constant_pool: List[ConstVal] = []
        self.__decompiled_code: List[str] = []

    def __pop(self) -> ConstVal:
        return self.__constant_pool.pop()

    def __push(self, value: ConstVal) -> None:
        self.__constant_pool.append(value)

    def __decompile_print(self) -> str:
        print_string: str = "print("
        top_const: ConstVal = self.__pop()

        if top_const.dtype == "string":
            print_string += f'"{top_const.value}"'
        elif top_const.dtype in ["int", "float"]:
            print_string += f"{top_const.value}"

        return print_string + ")"

    def __decompile_binary_operation(self, opcode: OpCode) -> None:
        right: ConstVal = self.__pop()
        left: ConstVal = self.__pop()

        result: str = ""
        if opcode.opcode == OpType.ADD:
            result = f"{left.value} + {right.value}"
        elif opcode.opcode == OpType.SUB:
            result = f"{left.value} - {right.value}"
        elif opcode.opcode == OpType.MUL:
            result = f"{left.value} * {right.value}"
        elif opcode.opcode == OpType.DIV:
            if left.dtype == "int" and right.dtype == "int":
                result = f"{left.value} // {right.value}"
            else:
                result = f"{left.value} / {right.value}"

        self.__push(ConstVal(value=result, dtype=left.dtype))

    def decompile(self) -> List[str]:
        for opcode in self.__opcodes:
            if opcode.opcode == OpType.PRINT:
                self.__decompiled_code.append(self.__decompile_print())
            elif opcode.opcode == OpType.LOAD:
                self.__constant_pool.append(ConstVal(opcode.op_value, opcode.op_dtype))
            elif opcode.opcode in [OpType.ADD, OpType.SUB, OpType.MUL, OpType.DIV]:
                self.__decompile_binary_operation(opcode)

        return self.__decompiled_code
