import argparse
import os

from .tokenizer.tokenizer import Tokenizer
from .parser.parser import RecursiveDescentParser
from .utils.tree_walker import TreeWalker
from .compiler.compiler import Compiler
from .vm.vm import VM


def entry():
    parser = argparse.ArgumentParser(description='X compiler')
    parser.add_argument('-i', '--input', type=str, help='X code file')
    parser.add_argument('-t', '--tokens', action='store_true', help='Print tokens')
    parser.add_argument('-p', '--parse', action='store_true', help='Print parse tree')
    parser.add_argument('-c', '--compile', action='store_true', help='Print opcodes')
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f"File {args.input} not found!")
        exit(1)

    extension = os.path.splitext(args.input)[-1][1:]
    if(extension != "x"):
        print(f"File {args.input} is not a X file!")
        exit(1)

    with open(args.input, 'r') as f:
        source = f.read()

    tokens = Tokenizer(source).generate_tokens()

    if args.tokens:
        for token in tokens:
            print(token)

    ast_roots = RecursiveDescentParser(tokens=tokens).parse()

    if args.parse:
        TreeWalker(roots=ast_roots).walk_and_print()

    opcodes = Compiler(ast_roots=ast_roots).compile()

    if args.compile:
        for opcode in opcodes:
            print(opcode)

    VM(opcodes=opcodes).run()