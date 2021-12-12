import unittest
from typing import List
import typing

from langx.opcode.opcode import OpCode
from langx.parser.node.node import Node
from langx.tokenizer.token import Token
from langx.tokenizer.tokenizer import Tokenizer
from langx.parser.parser import Parser
from langx.compiler.compiler import Compiler
from langx.decompiler.python.decompile import PyDecompiler


class TestPythonDecompiler(unittest.TestCase):
    def __get_opcodes_from_source(self, source: str) -> List[OpCode]:
        tokens: List[Token] = Tokenizer(source).generate_tokens()
        ast_root: Node = Parser(tokens).parse()
        return Compiler(ast_root=ast_root).compile()

    @typing.no_type_check
    def test_null_opcodes_list(self) -> None:
        with self.assertRaises(AssertionError):
            PyDecompiler(opcodes=None)

    def test_empty_opcodes_list(self) -> None:
        with self.assertRaises(AssertionError):
            PyDecompiler(opcodes=[])

    def test_decompile_print_number(self) -> None:
        opcodes: List[OpCode] = self.__get_opcodes_from_source("print(1)")

        decompiled_code: List[str] = PyDecompiler(opcodes=opcodes).decompile()
        expected_code: List[str] = ["print(1)"]

        self.assertEqual(decompiled_code, expected_code)

    def test_decompile_print_string(self) -> None:
        opcodes: List[OpCode] = self.__get_opcodes_from_source('print("hello")')

        decompiled_code: List[str] = PyDecompiler(opcodes=opcodes).decompile()
        expected_code: List[str] = ['print("hello")']

        self.assertEqual(decompiled_code, expected_code)

    def test_decompile_print_number_with_int_expr(self) -> None:
        opcodes: List[OpCode] = self.__get_opcodes_from_source(
            "print(1 + 2 * 3 / 4 - 5)"
        )

        decompiled_code: List[str] = PyDecompiler(opcodes=opcodes).decompile()
        expected_code: List[str] = ["print(1 + 2 * 3 // 4 - 5)"]

        self.assertEqual(decompiled_code, expected_code)

    def test_decompile_print_number_with_float_expr(self) -> None:
        opcodes: List[OpCode] = self.__get_opcodes_from_source(
            "print(1.0 + 2.0 * 3.0 / 4.0 - 5.0)"
        )

        decompiled_code: List[str] = PyDecompiler(opcodes=opcodes).decompile()
        expected_code: List[str] = ["print(1.0 + 2.0 * 3.0 / 4.0 - 5.0)"]

        self.assertEqual(decompiled_code, expected_code)
