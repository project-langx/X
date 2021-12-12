import unittest
import io
from contextlib import redirect_stdout
from typing import List
import typing

from langx.opcode.opcode import OpCode
from langx.parser.node.node import Node
from langx.tokenizer.token import Token
from langx.tokenizer.tokenizer import Tokenizer
from langx.parser.parser import Parser
from langx.compiler.compiler import Compiler
from langx.vm.vm import VM


class TestVM(unittest.TestCase):
    def __get_opcodes_from_source(self, source: str) -> List[OpCode]:
        tokens: List[Token] = Tokenizer(source).generate_tokens()
        ast_root: Node = Parser(tokens).parse()
        return Compiler(ast_root=ast_root).compile()

    @typing.no_type_check
    def test_vm_null_opcodes(self) -> None:
        with self.assertRaises(AssertionError):
            VM(opcodes=None)

    def test_vm_empty_opcodes(self) -> None:
        with self.assertRaises(AssertionError):
            VM(opcodes=[])

    def test_vm_print_number(self) -> None:
        opcodes: List[OpCode] = self.__get_opcodes_from_source("print(1)")

        with io.StringIO() as buf, redirect_stdout(buf):
            VM(opcodes=opcodes).run()
            output: str = buf.getvalue()

        self.assertEqual(output, "1\n")

    def test_vm_print_string(self) -> None:
        opcodes: List[OpCode] = self.__get_opcodes_from_source('print("hello")')

        with io.StringIO() as buf, redirect_stdout(buf):
            VM(opcodes=opcodes).run()
            output: str = buf.getvalue()

        self.assertEqual(output, "hello\n")

    def test_vm_print_number_expr_add_mul(self) -> None:
        opcodes: List[OpCode] = self.__get_opcodes_from_source("print(1 + 2 * 3)")

        with io.StringIO() as buf, redirect_stdout(buf):
            VM(opcodes=opcodes).run()
            output: str = buf.getvalue()

        self.assertEqual(output, "7\n")

    def test_vm_print_number_expr_sub_div(self) -> None:
        opcodes: List[OpCode] = self.__get_opcodes_from_source("print(4 - 8 / 2)")

        with io.StringIO() as buf, redirect_stdout(buf):
            VM(opcodes=opcodes).run()
            output: str = buf.getvalue()

        self.assertEqual(output, "0\n")
