from typing import Dict, Optional, Tuple


class SymbolTable:
    def __init__(self) -> None:
        self.__table: Dict[int, Tuple[str, str]] = {}
        self.__id_counter: int = 0

    def add(self, id_name: str, dtype: str) -> None:
        assert id_name != None and id_name != ""
        assert dtype != None

        self.__id_counter += 1
        self.__table[self.__id_counter] = (id_name, dtype)

        return self.__id_counter

    def get(self, table_id: int) -> Optional[Tuple[str, str]]:
        assert table_id != None and table_id != ""

        return self.__table.get(table_id)
