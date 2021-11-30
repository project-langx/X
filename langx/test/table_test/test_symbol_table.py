import unittest

from ...table.symbol_table import SymbolTable


class TestSymbolTable(unittest.TestCase):
    def setUp(self) -> None:
        self.table = SymbolTable()

    def test_add_first_entry(self) -> None:
        self.table.add("x", "1")

        self.assertEqual(self.table.get("x"), "1")

    def test_add_replace_value(self) -> None:
        self.table.add("x", "1")
        self.table.add("x", "2")

        self.assertEqual(self.table.get("x"), "2")

    def test_add_multiple_entries(self) -> None:
        self.table.add("x", "1")
        self.table.add("y", "2")

        self.assertEqual(self.table.get("x"), "1")
        self.assertEqual(self.table.get("y"), "2")

    def test_get_id_non_existent(self) -> None:
        self.assertIsNone(self.table.get("x"))

    def test_get_id_existent(self) -> None:
        self.table.add("x", "1")
        self.assertEqual(self.table.get("x"), "1")
