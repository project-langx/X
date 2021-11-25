class SymbolTable:
    def __init__(self):
        self.table = {}

    def add(self, id_name, value):
        self.table[id_name] = value

    def get(self, id_name):
        return self.table.get(id_name)