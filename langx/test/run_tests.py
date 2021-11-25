import unittest
from typing import List, Any

from .utils_test.test_error import TestError
from .utils_test.test_tree_walker import TestTreeWalker
from .tokenizer_test.test_token import TestToken


def run_tests() -> None:
    test_classes_to_run: List[Any] = [TestError, TestTreeWalker, TestToken]

    loader: unittest.TestLoader = unittest.TestLoader()

    suites_list: List[unittest.TestSuite] = []
    for test_class in test_classes_to_run:
        suite: unittest.TestSuite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite: unittest.TestSuite = unittest.TestSuite(suites_list)

    runner: unittest.TextTestRunner = unittest.TextTestRunner()
    runner.run(big_suite)
