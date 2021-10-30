from ..parser.node.print_node import PrintNode
from ..parser.node.program_node import ProgramNode


class TreeWalker:
    def __init__(self, root):
        self.__root = root

    def __walk_print_node(self, node):
        print(f"PrintNode(expr={node.expr})")

    def __walk_statement(self, node):
        print("\t", end="")
        if type(node) == PrintNode:
            self.__walk_print_node(node)

    def __walk_program(self, node):
        print(f"ProgramNode(method={node.method})")
        for statement in node.statements:
            self.__walk_statement(statement)

    def walk_and_print(self):
        self.__walk_program(self.__root)
