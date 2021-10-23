from ...opcode.op_type import OpType


class JavaDecompiler:
    def __init__(self, opcodes, decompiled_file_name):
        self.__opcodes = opcodes
        self.__decompiled_file_name = decompiled_file_name

        self.__decompiled_code = []


    def __decompile_print(self, opcode):
        print_string = "\t\tSystem.out.println("
        for op_value in opcode.op_values:
            if opcode.op_dtype == "__string__":
                print_string += f"\"{op_value}\""
            elif opcode.op_dtype == "__number__":
                print_string += f"{op_value}"

        return print_string + ");"

    def decompile(self):
        self.__decompiled_code.append(f"class {self.__decompiled_file_name}" + " {")
        self.__decompiled_code.append("\tpublic static void main(String[] args) {")
        for opcode in self.__opcodes:
            if opcode.opcode == OpType.PRINT:
                self.__decompiled_code.append(self.__decompile_print(opcode))
        self.__decompiled_code.append("\t}\n}")

        return self.__decompiled_code