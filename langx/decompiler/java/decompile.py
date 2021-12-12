from collections import namedtuple
from typing import List, NamedTuple, Any

from ...value.value import Value
from ...opcode.op_type import OpType
from ...opcode.opcode import OpCode
from ...utils.check_class import CheckClass


class JavaDecompiler(CheckClass):
    def __init__(self, opcodes: List[OpCode], decompiled_file_name: str) -> None:
        super().__init__(
            opcodes=opcodes,
            decompiled_file_name=decompiled_file_name,
            check_empty_list=True,
        )
        self.__opcodes: List[OpCode] = opcodes
        self.__decompiled_file_name: str = decompiled_file_name

        self.__constant_pool: List[Value] = []
        self.__decompiled_code: List[str] = []

    def __pop(self) -> Value:
        return self.__constant_pool.pop()

    def __push(self, value: Value) -> None:
        self.__constant_pool.append(value)

    def __decompile_print(self) -> str:
        print_string: str = "\t\tSystem.out.println("
        top_const: Value = self.__pop()

        if top_const.dtype == "string":
            print_string += f'"{top_const.value}"'
        elif top_const.dtype in ["int", "float"]:
            print_string += f"{top_const.value}"

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
        self.__decompiled_code.append(f"class {self.__decompiled_file_name}" + " {")
        self.__decompiled_code.append("\tpublic static void main(String[] args) {")

        for opcode in self.__opcodes:
            if opcode.opcode == OpType.PRINT:
                self.__decompiled_code.append(self.__decompile_print())
            elif opcode.opcode == OpType.LOAD:
                self.__constant_pool.append(
                    Value(value=opcode.op_value, dtype=opcode.op_dtype)
                )
            elif opcode.opcode in [OpType.ADD, OpType.SUB, OpType.MUL, OpType.DIV]:
                self.__decompile_binary_operation(opcode)

        self.__decompiled_code.append("\t}\n}")
        return self.__decompiled_code
