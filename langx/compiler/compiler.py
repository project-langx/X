class Compiler:
    def __init__(self, ast_root):
        self.__ast_root = ast_root

    def compile(self):
        opcodes = []
        self.__ast_root.walk_and_compile(opcodes)

        return opcodes
