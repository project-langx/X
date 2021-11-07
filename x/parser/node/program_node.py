class ProgramNode:
    def __init__(self, method, statements):
        self.__method = method
        self.__statements = statements

    @property
    def method(self):
        return self.__method

    @property
    def statements(self):
        return self.__statements
