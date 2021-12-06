import unittest

from langx.tokenizer.tokenizer import Tokenizer
from langx.parser.parser import Parser
from langx.compiler.compiler import Compiler
from langx.decompiler.python.decompile import PyDecompiler


class TestCDecompiler(unittest.TestCase):
    def __get_opcodes_from_source(self, source):
        tokens = Tokenizer(source).generate_tokens()
        ast = Parser(tokens).parse()
        return Compiler(ast).compile()

    def test_decompile_print_number(self):
        opcodes = self.__get_opcodes_from_source("print(1)")

        decompiled_code = PyDecompiler(opcodes=opcodes).decompile()

        self.assertEqual(decompiled_code, ['print(1)'])

    def test_decompile_print_string(self):
        opcodes = self.__get_opcodes_from_source('print("hello")')

        decompiled_code = PyDecompiler(opcodes=opcodes).decompile()

        self.assertEqual(decompiled_code, ['print("hello")'])

    def test_decompile_print_number_with_int_expr(self):
        opcodes = self.__get_opcodes_from_source('print(1 + 2 * 3 / 4 - 5)')

        decompiled_code = PyDecompiler(opcodes=opcodes).decompile()

        self.assertEqual(decompiled_code, ['print(1 + 2 * 3 // 4 - 5)'])

    def test_decompile_print_number_with_float_expr(self):
        opcodes = self.__get_opcodes_from_source('print(1.0 + 2.0 * 3.0 / 4.0 - 5.0)')

        decompiled_code = PyDecompiler(opcodes=opcodes).decompile()

        self.assertEqual(decompiled_code, ['print(1.0 + 2.0 * 3.0 / 4.0 - 5.0)'])