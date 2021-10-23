class OpCode:
    def __init__(self, opcode, op_values):
        self.__opcode = opcode
        self.__op_values = op_values

    def __str__(self):
        op_values = []
        for op_value in self.__op_values:
            op_values.append(str(op_value))

        return f"{self.__opcode}: {op_values}"