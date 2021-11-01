from ..parser.node.print_node import PrintNode
from ..parser.node.expr_node import ExprNode


class TreeWalker:
    def __init__(self, root):
        self.__root = root

    def __walk_statement(self, node):
        print("\t", end="")
        print(node)

    def __walk_program(self, node):
        print(f"ProgramNode(method={node.method})")
        for statement in node.statements:
            self.__walk_statement(statement)

    def walk_and_print(self):
        self.__walk_program(self.__root)
