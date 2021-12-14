from typing import List, NamedTuple

from ...value.value import Value
from ...opcode.opcode import OpCode
from ...opcode.op_type import OpType
from ...utils.check_class import CheckClass


class CDecompiler(CheckClass):
    def __init__(self, opcodes: List[OpCode]) -> None:
        super().__init__(opcodes=opcodes, check_empty_list=True)
        self.__opcodes: List[OpCode] = opcodes

        self.__constant_pool: List[Value] = []
        self.__decompiled_code: List[str] = []

    def __pop(self) -> Value:
        return self.__constant_pool.pop()

    def __push(self, value: Value) -> None:
        self.__constant_pool.append(value)

    def __add_includes(self) -> None:
        includes: List[str] = []

        for opcode in self.__opcodes:
            if opcode.opcode == OpType.PRINT:
                includes.append("#include <stdio.h>\n")

        self.__decompiled_code.extend(list(set(includes)))

    def __decompile_print(self) -> str:
        print_string: str = "\tprintf("
        top_const: Value = self.__pop()

        if top_const.dtype == "string":
            print_string += f'"%s\\n", "{top_const.value}"'
        elif top_const.dtype == "int":
            print_string += f'"%d\\n", {top_const.value}'
        elif top_const.dtype == "float":
            print_string += f'"%f\\n", {top_const.value}'

        return print_string + ");"

    def __decompile_binary_operation(self, opcode: OpCode) -> None:
        right: Value = self.__pop()
        left: Value = self.__pop()

        result: str = ""
        if opcode.opcode == OpType.ADD:
            result = f"{left.value} + {right.value}"
        elif opcode.opcode == OpType.SUB:
            result = f"{left.value} - {right.value}"
        elif opcode.opcode == OpType.MUL:
            result = f"{left.value} * {right.value}"
        elif opcode.opcode == OpType.DIV:
            result = f"{left.value} / {right.value}"

        self.__push(Value(value=result, dtype=left.dtype))

    def decompile(self) -> List[str]:
        self.__add_includes()

        self.__decompiled_code.append("int main() {")
        for opcode in self.__opcodes:
            if opcode.opcode == OpType.PRINT:
                self.__decompiled_code.append(self.__decompile_print())
            elif opcode.opcode == OpType.LOAD:
                self.__constant_pool.append(
                    Value(value=opcode.op_value, dtype=opcode.op_dtype)
                )
            elif opcode.opcode in [OpType.ADD, OpType.SUB, OpType.MUL, OpType.DIV]:
                self.__decompile_binary_operation(opcode)

        self.__decompiled_code.append("\n\treturn 0; \n}")
        return self.__decompiled_code
