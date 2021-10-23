from ...opcode.op_type import OpType


class PyDecompiler:
    def __init__(self, opcodes):
        self.__opcodes = opcodes

        self.__decompiled_code = []


    def __decompile_print(self, opcode):
        print_string = "print("
        for op_value in opcode.op_values:
            if opcode.op_dtype == "__string__":
                print_string += f"\"{op_value}\""
            elif opcode.op_dtype == "__number__":
                print_string += f"{op_value}"

        return print_string + ")"

    def decompile(self):
        for opcode in self.__opcodes:
            if opcode.opcode == OpType.PRINT:
                self.__decompiled_code.append(self.__decompile_print(opcode))

        return self.__decompiled_code