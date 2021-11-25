import unittest

from ...parser.node.number_node import NumberNode
from ...parser.node.string_node import StringNode
from ...parser.node.binary_operator_node import BinaryOperatorNode
from ...parser.node.expr_node import ExprNode
from ...parser.node.print_node import PrintNode
from ...parser.node.program_node import ProgramNode
from ...utils.tree_walker import TreeWalker


class TestTreeWalker(unittest.TestCase):
    def test_walk_number_node(self):
        int_node: Node = NumberNode(value="3", dtype="int")
        float_node: Node = NumberNode(value="3.14", dtype="float")

        tree_walker: TreeWalker = TreeWalker(root=int_node)
        self.assertEqual(tree_walker.walk(), "NumberNode(value=3)\n")

        tree_walker: TreeWalker = TreeWalker(root=float_node)
        self.assertEqual(tree_walker.walk(), "NumberNode(value=3.14)\n")

    def test_walk_string_node(self):
        string_node: Node = StringNode(value="hello", dtype="str")

        tree_walker: TreeWalker = TreeWalker(root=string_node)
        self.assertEqual(tree_walker.walk(), "StringNode(value=hello)\n")

    def test_walk_binary_operator_node(self):
        left_node: Node = NumberNode(value="3", dtype="int")
        right_node: Node = NumberNode(value="4", dtype="int")
        binary_operator_node: Node = BinaryOperatorNode(operator="__add__", left=left_node, right=right_node)

        tree_walker: TreeWalker = TreeWalker(root=binary_operator_node)
        self.assertEqual(tree_walker.walk().split("\n"), ['BinaryOperatorNode(', 'left=(', '\tNumberNode(value=3)',
                                                          ')', "op='__add__'", 'right=(',
                                                          '\tNumberNode(value=4)', ')', ''])

    def test_walk_expr_node(self):
        left_node: Node = NumberNode(value="3", dtype="int")
        right_node: Node = NumberNode(value="4", dtype="int")
        binary_operator_node: Node = BinaryOperatorNode(operator="__add__", left=left_node, right=right_node)
        expr_node: Node = ExprNode(expr=binary_operator_node, dtype="int")

        tree_walker: TreeWalker = TreeWalker(root=expr_node)
        self.assertEqual(tree_walker.walk().split("\n"), ['ExprNode(', 'expr=(', '\tBinaryOperatorNode(',
                                                          '\tleft=(', '\t\tNumberNode(value=3)', '\t)',
                                                          "\top='__add__'", '\tright=(', '\t\tNumberNode(value=4)',
                                                          '\t)', ')', "dtype='int'", ')', ''])

    def test_walk_print_node(self):
        left_node: Node = NumberNode(value="3", dtype="int")
        right_node: Node = NumberNode(value="4", dtype="int")
        binary_operator_node: Node = BinaryOperatorNode(operator="__add__", left=left_node, right=right_node)
        expr_node: Node = ExprNode(expr=binary_operator_node, dtype="int")
        print_node: Node = PrintNode(expr=expr_node)

        tree_walker: TreeWalker = TreeWalker(root=print_node)
        self.assertEqual(tree_walker.walk().split("\n"), ['PrintNode(', '\tExprNode(', '\texpr=(',
                                                          '\t\tBinaryOperatorNode(', '\t\tleft=(',
                                                          '\t\t\tNumberNode(value=3)', '\t\t)',
                                                          "\t\top='__add__'", '\t\tright=(',
                                                          '\t\t\tNumberNode(value=4)', '\t\t)', '\t)',
                                                          "\tdtype='int'", '\t)', ')', ''])

    def test_walk_program_node(self):
        left_node: Node = NumberNode(value="3", dtype="int")
        right_node: Node = NumberNode(value="4", dtype="int")
        binary_operator_node: Node = BinaryOperatorNode(operator="__add__", left=left_node, right=right_node)
        expr_node: Node = ExprNode(expr=binary_operator_node, dtype="int")
        print_node: Node = PrintNode(expr=expr_node)

        string_node: Node = StringNode(value="hello", dtype="str")
        print_node_1: Node = PrintNode(expr=string_node)

        statements: List[Node] = [print_node, print_node_1]
        program_node: Node = ProgramNode(method="main", statements=statements)

        tree_walker: TreeWalker = TreeWalker(root=program_node)
        self.assertEqual(tree_walker.walk().split("\n"), ['ProgramNode(method=main)', '\tPrintNode(',
                                                          '\t\tExprNode(', '\t\texpr=(',
                                                          '\t\t\tBinaryOperatorNode(', '\t\t\tleft=(',
                                                          '\t\t\t\tNumberNode(value=3)', '\t\t\t)',
                                                          "\t\t\top='__add__'", '\t\t\tright=(',
                                                          '\t\t\t\tNumberNode(value=4)', '\t\t\t)',
                                                          '\t\t)', "\t\tdtype='int'", '\t\t)', '\t)',
                                                          '\tPrintNode(', '\t\tStringNode(value=hello)', '\t)', ''])
