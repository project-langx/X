from ..opcode.op_type import OpType


class VM:
    def __init__(self, opcodes):
        self.__opcodes = opcodes

    def run(self):
        for opcode in self.__opcodes:
            if opcode.opcode == OpType.PRINT:
                print(opcode.op_value)
