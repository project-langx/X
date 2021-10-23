from x.parser.node.print_node import PrintNode


class Compiler:
    def __init__(self, ast_roots):
        self.__ast_roots = ast_roots

    def compile(self):
        opcodes = []

        for ast_root in self.__ast_roots:
            opcode = ast_root.walk()
            opcodes.append(opcode)

        return opcodes
        