from typing import Dict, Optional


class SymbolTable:
    def __init__(self) -> None:
        self.table: Dict[str, str] = {}

    def add(self, id_name: str, value: str) -> None:
        self.table[id_name] = value

    def get(self, id_name: str) -> Optional[str]:
        return self.table.get(id_name)
