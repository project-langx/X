class TreeWalker:
    def __init__(self, root):
        self.__root = root

    def walk_and_print(self):
        if self.__root.children:
            print(self.__root, end="\n\t- ")
            for child in self.__root.children:
                TreeWalker(child).walk_and_print()
        else:
            print(self.__root)