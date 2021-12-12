from typing import List
import typing
import unittest
from langx.opcode.opcode import OpCode

from langx.parser.node.node import Node
from langx.tokenizer.token import Token
from langx.tokenizer.tokenizer import Tokenizer
from langx.parser.parser import Parser
from langx.compiler.compiler import Compiler
from langx.decompiler.java.decompile import JavaDecompiler


class TestJavaDecompiler(unittest.TestCase):
    def __get_opcodes_from_source(self, source: str) -> List[OpCode]:
        tokens: List[Token] = Tokenizer(source=source).generate_tokens()
        ast_root: Node = Parser(tokens).parse()
        return Compiler(ast_root=ast_root).compile()

    @typing.no_type_check
    def test_null_opcodes_list(self) -> None:
        with self.assertRaises(AssertionError):
            JavaDecompiler(opcodes=None, decompiled_file_name="Test")

    def test_empty_opcodes_list(self) -> None:
        with self.assertRaises(AssertionError):
            JavaDecompiler(opcodes=[], decompiled_file_name="Test")

    @typing.no_type_check
    def test_null_decompiled_file_name(self) -> None:
        with self.assertRaises(AssertionError):
            JavaDecompiler(opcodes=[], decompiled_file_name=None)

    def test_empty_decompiled_file_name(self) -> None:
        with self.assertRaises(AssertionError):
            JavaDecompiler(opcodes=[], decompiled_file_name="")

    def test_decompile_print_number(self) -> None:
        opcodes: List[OpCode] = self.__get_opcodes_from_source("print(1)")

        decompiled_code: List[str] = JavaDecompiler(
            opcodes=opcodes, decompiled_file_name="Test"
        ).decompile()
        expected_code: List[str] = [
            "class Test {",
            "\tpublic static void main(String[] args) {",
            "\t\tSystem.out.println(1);",
            "\t}\n}",
        ]

        self.assertEqual(decompiled_code, expected_code)

    def test_decompile_print_string(self) -> None:
        opcodes: List[OpCode] = self.__get_opcodes_from_source('print("hello")')

        decompiled_code: List[str] = JavaDecompiler(
            opcodes=opcodes, decompiled_file_name="Test"
        ).decompile()
        expected_code: List[str] = [
            "class Test {",
            "\tpublic static void main(String[] args) {",
            '\t\tSystem.out.println("hello");',
            "\t}\n}",
        ]

        self.assertEqual(decompiled_code, expected_code)

    def test_decompile_print_number_with_expr(self) -> None:
        opcodes: List[OpCode] = self.__get_opcodes_from_source(
            "print(1 + 2 * 3 / 4 - 5)"
        )

        decompiled_code: List[str] = JavaDecompiler(
            opcodes=opcodes, decompiled_file_name="Test"
        ).decompile()
        expected_code: List[str] = [
            "class Test {",
            "\tpublic static void main(String[] args) {",
            "\t\tSystem.out.println(1 + 2 * 3 / 4 - 5);",
            "\t}\n}",
        ]

        self.assertEqual(decompiled_code, expected_code)
