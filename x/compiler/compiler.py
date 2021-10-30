from x.opcode.opcode import OpCode
from x.parser.node.print_node import PrintNode
from ..opcode.op_type import OpType


class Compiler:
    def __init__(self, ast_root):
        self.__ast_root = ast_root

        self.__opcodes = []

    def __compile_print_node(self, node):
        op_dtype = node.dtype

        self.__opcodes.append(OpCode(OpType.PRINT, node.expr, op_dtype))

    def __compile_statement(self, statement):
        if type(statement) == PrintNode:
            self.__compile_print_node(statement)

    def __compile_program_node(self, node):
        for statement in node.statements:
            self.__compile_statement(statement)

    def compile(self):
        self.__compile_program_node(self.__ast_root)

        return self.__opcodes
