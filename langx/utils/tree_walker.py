class TreeWalker:
    def __init__(self, root):
        self.__root = root

    def walk(self):
        tab_level = 0
        ast_string = self.__root.walk_and_print(tab_level=tab_level)

        return ast_string
