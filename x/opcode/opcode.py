class OpCode:
    def __init__(self, opcode, op_values):
        self.__opcode = opcode
        self.__op_values = op_values

    def __str__(self):
        op_values = []
        for op_value in self.__op_values:
            op_values.append(str(op_value))

        opcode = str(self.__opcode)
        opcode = opcode.split(".")[1]

        return f"{opcode}: {op_values}"

    @property
    def opcode(self):
        return self.__opcode

    @property
    def op_values(self):
        return self.__op_values