from collections import namedtuple


Token = namedtuple('Token', ['type', 'value', 'line_num'])

class Tokenizer:
    def __init__(self, source):
        self.__source = source
        self.__line_num = 1
        self.__pointer = 0
        self.__lexeme = ""

        self.__tokens = []

    def __is_keyword(self):
        while self.__source[self.__pointer].isalpha():
            self.__lexeme += self.__source[self.__pointer]
            self.__pointer += 1
        self.__pointer -= 1

        if self.__lexeme == "print":
            return "__print__"

    def __is_string(self):
        self.__pointer += 1
        while self.__source[self.__pointer] != '"':
            self.__lexeme += self.__source[self.__pointer]
            self.__pointer += 1

        return "__string__"

    def generate_tokens(self):
        while self.__pointer < len(self.__source):
            self.__lexeme = ""
            if self.__source[self.__pointer].isalpha():
                self.__tokens.append(Token(self.__is_keyword(), self.__lexeme, self.__line_num))
            elif self.__source[self.__pointer] == '(':
                self.__tokens.append(Token('__left_paren__', "", self.__line_num))
            elif self.__source[self.__pointer] == ')':
                self.__tokens.append(Token('__right_paren__', "", self.__line_num))
            elif self.__source[self.__pointer] == '"':
                self.__tokens.append(Token(self.__is_string(), self.__lexeme, self.__line_num))
            elif self.__source[self.__pointer] == "\n":
                self.__line_num += 1
                self.__tokens.append(Token('__newline__', "", self.__line_num))

            self.__pointer += 1

        return self.__tokens