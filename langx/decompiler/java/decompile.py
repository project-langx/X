from collections import namedtuple

from ...opcode.op_type import OpType


const_val = namedtuple("Const", ["value", "dtype"])

class JavaDecompiler:
    def __init__(self, opcodes, decompiled_file_name):
        self.__opcodes = opcodes
        self.__decompiled_file_name = decompiled_file_name

        self.__constant_pool = []
        self.__decompiled_code = []

    def __pop(self):
        return self.__constant_pool.pop()

    def __push(self, value):
        self.__constant_pool.append(value)

    def __decompile_print(self):
        print_string = "\t\tSystem.out.println("
        top_const = self.__pop()

        if top_const.dtype == "string":
            print_string += f'"{top_const.value}"'
        elif top_const.dtype in ["int", "float"]:
            print_string += f"{top_const.value}"

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
        self.__decompiled_code.append(f"class {self.__decompiled_file_name}" + " {")
        self.__decompiled_code.append("\tpublic static void main(String[] args) {")
        for opcode in self.__opcodes:
            if opcode.opcode == OpType.PRINT:
                self.__decompiled_code.append(self.__decompile_print())
            elif opcode.opcode == OpType.LOAD:
                self.__constant_pool.append(const_val(opcode.op_value, opcode.op_dtype))
            elif opcode.opcode in [OpType.ADD, OpType.SUB, OpType.MUL, OpType.DIV]:
                self.__decompile_binary_operation(opcode)

        self.__decompiled_code.append("\t}\n}")
        return self.__decompiled_code
