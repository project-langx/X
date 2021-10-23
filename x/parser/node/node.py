class Node:
    def __init__(self):
        self.__children = []

    def add_child(self, child):
        self.__children.append(child)