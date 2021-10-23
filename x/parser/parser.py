from ..utils.error import ParseError


class Node:
    def __init__(self):
        self.__children = []

    def add_child(self, child):
        self.__children.append(child)

class ValNode(Node):
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @property
    def children(self):
        return None

    def __str__(self):
        return f"ValueNode(value={self.__value})"

class PrintNode(Node):
    def __init__(self, values):
        self.__values = values

    @property
    def children(self):
        return self.__values

    def __str__(self):
        return f"PrintNode()"

class RecursiveDescentParser:
    def __init__(self, tokens):
        self.__tokens = tokens
        self.__root = None

    def __advance(self):
        current_tok = self.__tokens.pop(0)
        return current_tok

    def __string(self, current_tok):
        if current_tok.type == "__string__":
            return ValNode(current_tok.value)

        raise ParseError(f"Expected string")

    def __print(self, current_tok):
        token_sequence = ["__print__", "__left_paren__", "__string__", "__right_paren__"]
        string_val = ""

        for expected_token in token_sequence:
            if current_tok.type == "__string__":
                string_val = self.__string(current_tok=current_tok)
            elif current_tok.type == expected_token:
                current_tok = self.__advance()
            else:
                raise ParseError(f"Expected {expected_token}")

        return PrintNode(values=[string_val])

    def parse(self):
        current_tok = self.__advance()
        self.__root = self.__print(current_tok=current_tok)
        return self.__root