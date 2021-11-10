from collections import namedtuple

from ...opcode.op_type import OpType


const_val = namedtuple("Const", ["value", "dtype"])

class CDecompiler:
    def __init__(self, opcodes):
        self.__opcodes = opcodes

        self.__constant_pool = []
        self.__decompiled_code = []

    def __pop(self):
        return self.__constant_pool.pop()

    def __push(self, value):
        self.__constant_pool.append(value)

    def __add_includes(self):
        includes = []

        for opcode in self.__opcodes:
            if opcode.opcode == OpType.PRINT:
                includes.append("#include <stdio.h>\n")

        self.__decompiled_code.extend(list(set(includes)))

    def __decompile_print(self):
        print_string = "\tprintf("
        top_const = self.__pop()

        if top_const.dtype == "string":
            print_string += f'"%s\\n", "{top_const.value}"'
        elif top_const.dtype == "int":
            print_string += f'"%d\\n", {top_const.value}'
        elif top_const.dtype == "float":
            print_string += f'"%f\\n", {top_const.value}'

        return print_string + ");"

    def __decompile_binary_operation(self, opcode):
        right = self.__pop()
        left = self.__pop()

        result = ""
        if opcode.opcode == OpType.ADD:
            result = f"{left.value} + {right.value}"
        elif opcode.opcode == OpType.SUB:
            result = f"{left.value} - {right.value}"
        elif opcode.opcode == OpType.MUL:
            result = f"{left.value} * {right.value}"
        elif opcode.opcode == OpType.DIV:
            result = f"{left.value} / {right.value}"

        self.__push(const_val(value=result, dtype=left.dtype))

    def decompile(self):
        self.__add_includes()

        self.__decompiled_code.append("int main() {")
        for opcode in self.__opcodes:
            if opcode.opcode == OpType.PRINT:
                self.__decompiled_code.append(self.__decompile_print())
            elif opcode.opcode == OpType.LOAD:
                self.__constant_pool.append(const_val(opcode.op_value, opcode.op_dtype))
            elif opcode.opcode in [OpType.ADD, OpType.SUB, OpType.MUL, OpType.DIV]:
                self.__decompile_binary_operation(opcode)

        self.__decompiled_code.append("\n\treturn 0; \n}")
        return self.__decompiled_code
