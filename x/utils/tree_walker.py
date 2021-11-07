from ..parser.node.number_node import NumberNode
from ..parser.node.string_node import StringNode
from ..parser.node.binary_operator_node import BinaryOperatorNode
from ..parser.node.print_node import PrintNode
from ..parser.node.expr_node import ExprNode


class TreeWalker:
    def __init__(self, root):
        self.__root = root
        

    def __add_tabs(self, tab_level):
        return "\t" * tab_level

    def __check_expr_type_and_walk(self, node, tab_level):
        if type(node) is NumberNode:
            self.__walk_number(node=node, tab_level=tab_level)
        elif type(node) is StringNode:
            self.__walk_string(node=node, tab_level=tab_level)
        elif type(node) is BinaryOperatorNode:
            self.__walk_binary_operator(node=node, tab_level=tab_level)

    def __walk_number(self, node, tab_level):
        print(self.__add_tabs(tab_level=tab_level), end="")
        print(f"NumberNode(value={node.value})")

    def __walk_string(self, node, tab_level):
        print(self.__add_tabs(tab_level=tab_level), end="")
        print(f"StringNode(value={node.value})")

    def __walk_binary_operator(self, node, tab_level):
        print(self.__add_tabs(tab_level=tab_level), end="")
        print(f"BinaryOperatorNode(")
        print(self.__add_tabs(tab_level=tab_level), end="")
        print("left=(")

        tab_level += 1
        self.__check_expr_type_and_walk(node=node.left, tab_level=tab_level)

        tab_level -= 1
        print(self.__add_tabs(tab_level=tab_level), end="")
        print(")")

        print(self.__add_tabs(tab_level=tab_level), end="")
        print(f"op='{node.operator}'")

        print(self.__add_tabs(tab_level=tab_level), end="")
        print(f"right=(")
        tab_level += 1

        self.__check_expr_type_and_walk(node=node.right, tab_level=tab_level)

        tab_level -= 1
        print(self.__add_tabs(tab_level=tab_level), end="")
        print(")")

    def __walk_expr(self, node, tab_level):
        print(self.__add_tabs(tab_level=tab_level), end="")
        print(f"ExprNode(")
        print(self.__add_tabs(tab_level=tab_level), end="")
        print("expr=(")
        tab_level += 1

        self.__check_expr_type_and_walk(node=node.expr, tab_level=tab_level)

        tab_level -= 1
        print(self.__add_tabs(tab_level=tab_level), end="")
        print(")")
        print(self.__add_tabs(tab_level=tab_level), end="")
        print(f"dtype='{node.dtype}'")
        print(self.__add_tabs(tab_level=tab_level), end="")
        print(")")

    def __walk_print(self, node, tab_level):
        print(self.__add_tabs(tab_level=tab_level), end="")
        print(f"PrintNode(")
        tab_level += 1

        self.__walk_expr(node=node.expr, tab_level=tab_level)
        
        tab_level -= 1
        print(self.__add_tabs(tab_level=tab_level), end="")
        print(")")

    def __walk_program(self, node, tab_level):
        print(self.__add_tabs(tab_level=tab_level), end="")
        print(f"ProgramNode(method={node.method})")
        tab_level += 1

        for statement in node.statements:
            if type(statement) is PrintNode:
                self.__walk_print(node=statement, tab_level=tab_level)

    def walk_and_print(self):
        tab_level = 0
        self.__walk_program(node=self.__root, tab_level=tab_level)
