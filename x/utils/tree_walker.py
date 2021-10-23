class TreeWalker:
    def __init__(self, roots):
        self.__roots = roots

    def walk_and_print_one(self, root):
        if root.children:
            print(root, end="\n\t- ")
            for child in root.children:
                TreeWalker(child).walk_and_print_one(child)
        else:
            print(root)

    def walk_and_print(self):
        for root in self.__roots:
            self.walk_and_print_one(root)