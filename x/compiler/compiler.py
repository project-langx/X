from x.parser.node.print_node import PrintNode


class Compiler:
    def __init__(self, ast_root):
        self.__ast_root = ast_root

    def compile(self):
        opcodes = []

        opcode = self.__ast_root.walk()
        opcodes.append(opcode)

        return opcodes
        