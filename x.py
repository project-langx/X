import argparse
import os

from tokenizer import Tokenizer
from parser import RecursiveDescentParser
from tree_walker import TreeWalker


parser = argparse.ArgumentParser(description='X compiler')
parser.add_argument('-i', '--input', help='X code file', type=str)
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
ast_root = RecursiveDescentParser(tokens=tokens).parse()
tree_walker = TreeWalker(root=ast_root)
tree_walker.walk()