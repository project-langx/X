from abc import abstractmethod


class Node:
    @abstractmethod
    def walk_and_print(self, tab_level):
        pass

    @abstractmethod
    def walk_and_compile(self, opcodes):
        pass

    def _add_tabs(self, tab_level):
        return "\t" * tab_level
