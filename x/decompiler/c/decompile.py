from ...opcode.op_type import OpType


class CDecompiler:
    def __init__(self, opcodes):
        self.__opcodes = opcodes

        self.__decompiled_code = []

    def __add_includes(self):
        includes = []

        for opcode in self.__opcodes:
            if opcode.opcode == OpType.PRINT:
                includes.append("#include <stdio.h>\n")

        self.__decompiled_code.extend(list(set(includes)))

    def __decompile_print(self, opcode):
        print_string = "\tprintf("
        for op_value in opcode.op_values:
            if opcode.op_dtype == "__string__":
                print_string += f"\"%s\", \"{op_value}\""
            elif opcode.op_dtype == "__number__":
                print_string += f"\"%d\", {op_value}"

        return print_string + ");"

    def decompile(self):
        self.__add_includes()

        self.__decompiled_code.append("int main() {")
        for opcode in self.__opcodes:
            if opcode.opcode == OpType.PRINT:
                self.__decompiled_code.append(self.__decompile_print(opcode))

        self.__decompiled_code.append("\n\treturn 0; \n}")
        return self.__decompiled_code