from ..parser.node.number_node import NumberNode
from ..parser.node.string_node import StringNode
from ..parser.node.binary_operator_node import BinaryOperatorNode
from ..parser.node.print_node import PrintNode
from ..parser.node.expr_node import ExprNode


class TreeWalker:
    def __init__(self, root):
        self.__root = root
        
        self.__ast_string = ""

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
        self.__ast_string += self.__add_tabs(tab_level=tab_level)
        self.__ast_string += f"NumberNode(value={node.value})\n"

    def __walk_string(self, node, tab_level):
        self.__ast_string += self.__add_tabs(tab_level=tab_level)
        self.__ast_string += f"StringNode(value={node.value})\n"

    def __walk_binary_operator(self, node, tab_level):
        self.__ast_string += self.__add_tabs(tab_level=tab_level)
        self.__ast_string += f"BinaryOperatorNode(\n"
        self.__ast_string += self.__add_tabs(tab_level=tab_level)
        self.__ast_string += f"left=(\n"

        tab_level += 1
        self.__check_expr_type_and_walk(node=node.left, tab_level=tab_level)

        tab_level -= 1
        self.__ast_string += self.__add_tabs(tab_level=tab_level)
        self.__ast_string += f")\n"

        self.__ast_string += self.__add_tabs(tab_level=tab_level)
        self.__ast_string += f"op='{node.operator}'\n"

        self.__ast_string += self.__add_tabs(tab_level=tab_level)
        self.__ast_string += f"right=(\n"
        tab_level += 1

        self.__check_expr_type_and_walk(node=node.right, tab_level=tab_level)

        tab_level -= 1
        self.__ast_string += self.__add_tabs(tab_level=tab_level)
        self.__ast_string += f")\n"

    def __walk_expr(self, node, tab_level):
        self.__ast_string += self.__add_tabs(tab_level=tab_level)
        self.__ast_string += f"ExprNode(\n"
        self.__ast_string += self.__add_tabs(tab_level=tab_level)
        self.__ast_string += f"expr=(\n"
        tab_level += 1

        self.__check_expr_type_and_walk(node=node.expr, tab_level=tab_level)

        tab_level -= 1
        self.__ast_string += self.__add_tabs(tab_level=tab_level)
        self.__ast_string += ")\n"
        self.__ast_string += self.__add_tabs(tab_level=tab_level)
        self.__ast_string += f"dtype='{node.dtype}'\n"
        self.__ast_string += self.__add_tabs(tab_level=tab_level)
        self.__ast_string += f")\n"

    def __walk_print(self, node, tab_level):
        self.__ast_string += self.__add_tabs(tab_level=tab_level)
        self.__ast_string += f"PrintNode(\n"
        tab_level += 1

        self.__walk_expr(node=node.expr, tab_level=tab_level)
        
        tab_level -= 1
        self.__ast_string += self.__add_tabs(tab_level=tab_level)
        self.__ast_string += ")\n"

    def __walk_program(self, node, tab_level):
        self.__ast_string += self.__add_tabs(tab_level=tab_level)
        self.__ast_string += f"ProgramNode(method={node.method})\n"
        tab_level += 1

        for statement in node.statements:
            if type(statement) is PrintNode:
                self.__walk_print(node=statement, tab_level=tab_level)

    def walk(self):
        tab_level = 0
        self.__walk_program(node=self.__root, tab_level=tab_level)

        return self.__ast_string
