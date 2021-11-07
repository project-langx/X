from ..opcode.op_type import OpType


class VM:
    def __init__(self, opcodes):
        self.__opcodes = opcodes

        self.__constant_pool = []

    def __pop(self):
        return self.__constant_pool.pop()

    def __push(self, constant):
        self.__constant_pool.append(constant)

    def __cast_to_type(self, value, dtype):
        if dtype == 'int':
            return int(value)
        elif dtype == 'float':
            return float(value)
        elif dtype == 'string':
            return str(value)

    def __perform_binary_operation(self, opcode, operation):
        right = self.__pop()
        left = self.__pop()

        if opcode == OpType.ADD:
            self.__push(left + right)
        elif opcode == OpType.SUB:
            self.__push(left - right)
        elif opcode == OpType.MUL:
            self.__push(left * right)
        elif opcode == OpType.DIV:
            if type(left) == int and type(right) == int:
                self.__push(left // right)
            else:
                self.__push(left / right)

    def run(self):
        for opcode in self.__opcodes:
            if opcode.opcode == OpType.PRINT:
                print(self.__pop())
            elif opcode.opcode == OpType.LOAD:
                self.__push(self.__cast_to_type(opcode.op_value, dtype=opcode.op_dtype))
            elif opcode.opcode in [OpType.ADD, OpType.SUB, OpType.MUL, OpType.DIV]:
                self.__perform_binary_operation(opcode.opcode, operation=opcode.op_value)
