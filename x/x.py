import argparse
import os
import sys

from .tokenizer.tokenizer import Tokenizer
from .parser.parser import Parser
from .utils.tree_walker import TreeWalker
from .compiler.compiler import Compiler
from .vm.vm import VM
from .decompiler.c.decompile import CDecompiler
from .decompiler.cpp.decompile import CppDecompiler
from .decompiler.java.decompile import JavaDecompiler
from .decompiler.python.decompile import PyDecompiler


def entry():
    parser = argparse.ArgumentParser(description="X compiler")
    parser.add_argument("-i", "--input", type=str, help="X code file")
    parser.add_argument("-t", "--tokens", action="store_true", help="Print tokens")
    parser.add_argument("-p", "--parse", action="store_true", help="Print parse tree")
    parser.add_argument("-c", "--compile", action="store_true", help="Print opcodes")
    parser.add_argument("--decompile-c", action="store_true", help="Compile to C code")
    parser.add_argument(
        "--decompile-cpp", action="store_true", help="Compile to C++ code"
    )
    parser.add_argument(
        "--decompile-java", action="store_true", help="Compile to Java code"
    )
    parser.add_argument(
        "--decompile-cs", action="store_true", help="Compile to C# code"
    )
    parser.add_argument(
        "--decompile-py", action="store_true", help="Compile to Python code"
    )
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"File {args.input} not found!")
        exit(1)

    with open(args.input, "r") as f:
        source = f.read()

    tokens = Tokenizer(source).generate_tokens()

    if args.tokens:
        print("-" * 50)
        for token in tokens:
            print(token)
        print("-" * 50)

    ast_root = Parser(tokens=tokens).parse()

    if args.parse:
        print("-" * 50)
        print(TreeWalker(root=ast_root).walk())
        print("-" * 50)

    opcodes = Compiler(ast_root=ast_root).compile()

    if args.compile:
        print("-" * 50)
        for opcode in opcodes:
            print(opcode)
        print("-" * 50)

    if args.decompile_c:
        decompiled_c_code = CDecompiler(opcodes=opcodes).decompile()

        decompiled_c_file_path = ".".join(args.input.split(".")[:-1]) + ".c"
        with open(decompiled_c_file_path, "w") as f:
            f.write("\n".join(decompiled_c_code))

        print(f"C code written to {decompiled_c_file_path}")

        sys.exit()
    elif args.decompile_cpp:
        decompiled_cpp_code = CppDecompiler(opcodes=opcodes).decompile()

        decompiled_cpp_file_path = ".".join(args.input.split(".")[:-1]) + ".cpp"
        with open(decompiled_cpp_file_path, "w") as f:
            f.write("\n".join(decompiled_cpp_code))

        print(f"C++ code written to {decompiled_cpp_file_path}")

        sys.exit()
    elif args.decompile_java:
        decompiled_java_file_name = ".".join(args.input.split(".")[:-1]).capitalize()
        decompiled_java_code = JavaDecompiler(
            opcodes=opcodes, decompiled_file_name=decompiled_java_file_name
        ).decompile()

        decompiled_java_file_path = decompiled_java_file_name + ".java"
        with open(decompiled_java_file_path, "w") as f:
            f.write("\n".join(decompiled_java_code))

        print(f"Java code written to {decompiled_java_file_path}")

        sys.exit()
    elif args.decompile_py:
        decompiled_py_code = PyDecompiler(opcodes=opcodes).decompile()

        decompiled_py_file_path = ".".join(args.input.split(".")[:-1]) + ".py"
        with open(decompiled_py_file_path, "w") as f:
            f.write("\n".join(decompiled_py_code))

        print(f"Python code written to {decompiled_py_file_path}")

        sys.exit()

    VM(opcodes=opcodes).run()
