class OpCode:
    def __init__(self, opcode, op_value, op_dtype):
        self.__opcode = opcode
        self.__op_value = op_value
        self.__op_dtype = op_dtype

    def __str__(self):
        opcode = str(self.__opcode)
        opcode = opcode.split(".")[1]

        if self.__op_value == "" and self.__op_dtype == "":
            return str(self.__opcode).split(".")[1]

        return f"{opcode} {self.__op_value} {self.__op_dtype}"

    @property
    def opcode(self):
        return self.__opcode

    @property
    def op_value(self):
        return self.__op_value

    @property
    def op_dtype(self):
        return self.__op_dtype
