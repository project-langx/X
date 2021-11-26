from typing import List, Tuple

from ..utils.error import TokenizerError
from .token import Token
from .token_type import TokenType


class Tokenizer:
    def __init__(self, source: str) -> None:
        self.__source: str = source
        self.__line_num: int = 1
        self.__pointer: int = 0
        self.__lexeme: str = ""

        self.__tokens: List[Token] = []

    def __is_keyword(self) -> TokenType:
        while self.__source[self.__pointer].isalpha():
            self.__lexeme += self.__source[self.__pointer]
            self.__pointer += 1
        self.__pointer -= 1

        if self.__lexeme == "print":
            return TokenType.PRINT

        return TokenType.UNK

    def __is_string(self) -> TokenType:
        self.__pointer += 1
        while self.__source[self.__pointer] != '"':
            self.__lexeme += self.__source[self.__pointer]
            self.__pointer += 1

        return TokenType.STRING

    def __is_number(self) -> Tuple[TokenType, str]:
        is_float: bool = False
        while (
            self.__source[self.__pointer].isdigit()
            or self.__source[self.__pointer] == "."
        ):
            self.__lexeme += self.__source[self.__pointer]
            self.__pointer += 1

        self.__pointer -= 1

        if self.__lexeme.count(".") > 1:
            raise TokenizerError(
                message="A number cannot have more than one decimal points!"
            )

        if self.__lexeme.count(".") == 1:
            is_float = True

        return TokenType.NUMBER, "float" if is_float else "int"

    def __operator(self) -> TokenType:
        if self.__source[self.__pointer] == "+":
            return TokenType.ADD
        elif self.__source[self.__pointer] == "-":
            return TokenType.SUB
        elif self.__source[self.__pointer] == "*":
            return TokenType.MUL
        elif self.__source[self.__pointer] == "/":
            return TokenType.DIV

        return TokenType.UNK

    def generate_tokens(self) -> List[Token]:
        while self.__pointer < len(self.__source):
            self.__lexeme = ""
            if self.__source[self.__pointer].isalpha():
                self.__tokens.append(
                    Token(self.__is_keyword(), "", self.__lexeme, self.__line_num)
                )
            elif self.__source[self.__pointer] == "(":
                self.__tokens.append(
                    Token(TokenType.LEFT_PAREN, "", "", self.__line_num)
                )
            elif self.__source[self.__pointer] == ")":
                self.__tokens.append(
                    Token(TokenType.RIGHT_PAREN, "", "", self.__line_num)
                )
            elif self.__source[self.__pointer] in ["+", "-", "*", "/"]:
                operator = self.__operator()
                self.__tokens.append(Token(operator, "", "", self.__line_num))
            elif self.__source[self.__pointer] == '"':
                self.__tokens.append(
                    Token(self.__is_string(), "string", self.__lexeme, self.__line_num)
                )
            elif self.__source[self.__pointer].isdigit():
                number, dtype = self.__is_number()
                self.__tokens.append(
                    Token(number, dtype, self.__lexeme, self.__line_num)
                )
            elif self.__source[self.__pointer] == "\n":
                self.__line_num += 1
                self.__tokens.append(
                    Token(TokenType.NEWLINE, "", "", self.__line_num - 1)
                )

            self.__pointer += 1

        self.__tokens.append(Token(TokenType.NEWLINE, "", "", self.__line_num))
        self.__tokens.append(Token(TokenType.EOF, "", "", self.__line_num + 1))

        return self.__tokens
