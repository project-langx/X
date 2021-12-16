from typing import Dict, Optional, Tuple


class SymbolTable:
    def __init__(self) -> None:
        self.__table: Dict[int, Tuple[str, str]] = {}
        self.__id_counter: int = 0

    def __get_id_by_name_dtype(self, id_name: str, dtype: str) -> Optional[int]:
        assert id_name != None and id_name != ""
        assert dtype != None and dtype != ""

        for table_id, (id_name_, dtype_) in self.__table.items():
            if id_name == id_name_ and dtype == dtype_:
                return table_id

        return None

    def add(self, id_name: str, dtype: str) -> None:
        assert id_name != None and id_name != ""
        assert dtype != None

        if self.__id_counter not in self.__table.keys():
            self.__id_counter += 1
            self.__table[self.__id_counter] = (id_name, dtype)
        else:
            table_id: int = self.__get_id_by_name_dtype(id_name, dtype)
            self.__table[table_id] = (id_name, dtype)

        return self.__id_counter

    def get(self, table_id: int) -> Optional[Tuple[str, str]]:
        assert table_id != None and table_id != ""

        return self.__table.get(table_id)

    def __str__(self) -> str:
        table_str: str = ""
        for table_id, (id_name, dtype) in self.__table.items():
            table_str += f"{table_id}: {dtype} {id_name}\n"

        return table_str
