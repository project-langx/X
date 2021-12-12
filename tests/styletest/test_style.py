import unittest
from mypy import api
import os


class TestStyle(unittest.TestCase):
    def __get_py_files(self):
        py_files = []
        for (dirpath, _, filenames) in os.walk("langx"):
            for filename in filenames:
                if filename.endswith('.py') and "__init__" not in filename and "webdebug" not in dirpath: 
                    py_files.append(os.sep.join([dirpath, filename]))

        return py_files

    def test_style(self):
        py_files = self.__get_py_files()
        result = api.run(py_files)
        self.assertTrue("success" in result[0].lower())