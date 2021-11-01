from ...opcode.op_type import OpType


class CppDecompiler:
    def __init__(self, opcodes):
        self.__opcodes = opcodes

        self.__decompiled_code = []

    def __add_includes(self):
        includes = []

        for opcode in self.__opcodes:
            if opcode.opcode == OpType.PRINT:
                includes.append("#include <iostream>\n")

        self.__decompiled_code.extend(list(set(includes)))

    def __decompile_print(self, opcode):
        print_string = "\tstd::cout << "
        if opcode.op_dtype == "string":
            print_string += f'"{opcode.op_value}"'
        elif opcode.op_dtype == "number":
            print_string += f"{opcode.op_value}"

        return print_string + " << std::endl;"

    def decompile(self):
        self.__add_includes()

        self.__decompiled_code.append("int main() {")
        for opcode in self.__opcodes:
            if opcode.opcode == OpType.PRINT:
                self.__decompiled_code.append(self.__decompile_print(opcode))

        self.__decompiled_code.append("\n\treturn 0; \n}")
        return self.__decompiled_code
