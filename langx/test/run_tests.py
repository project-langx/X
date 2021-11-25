import unittest

from .utils.test_error import TestError
from .utils.test_tree_walker import TestTreeWalker


def run_tests():
    test_classes_to_run = [TestError, TestTreeWalker]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)