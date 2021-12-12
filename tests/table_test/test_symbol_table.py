import typing
import unittest

from langx.table.symbol_table import SymbolTable


class TestSymbolTable(unittest.TestCase):
    def setUp(self) -> None:
        self.table = SymbolTable()

    @typing.no_type_check
    def test_add_null_id_name(self) -> None:
        with self.assertRaises(AssertionError):
            self.table.add(None, "1")

    def test_add_empty_id_name(self) -> None:
        with self.assertRaises(AssertionError):
            self.table.add("", "1")

    @typing.no_type_check
    def test_add_null_value(self) -> None:
        with self.assertRaises(AssertionError):
            self.table.add("x", None)

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

    @typing.no_type_check
    def test_get_null_id_name(self) -> None:
        with self.assertRaises(AssertionError):
            self.table.get(None)

    def test_get_empty_id_name(self) -> None:
        with self.assertRaises(AssertionError):
            self.table.get("")

    def test_get_id_non_existent(self) -> None:
        self.assertIsNone(self.table.get("x"))

    def test_get_id_existent(self) -> None:
        self.table.add("x", "1")
        self.assertEqual(self.table.get("x"), "1")
