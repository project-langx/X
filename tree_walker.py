class TreeWalker:
    def __init__(self, root):
        self.__root = root

    def walk(self):
        if self.__root.children:
            print(self.__root, end="\n\t- ")
            for child in self.__root.children:
                TreeWalker(child).walk()
        else:
            print(self.__root)