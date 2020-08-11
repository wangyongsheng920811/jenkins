import unittest
from OpenAPI.Lib.MyHead import *


def find_case(test_cases=[]):
    suite = unittest.TestSuite()
    for tmp in test_cases:
        allsuite = unittest.defaultTestLoader.discover(start_dir=test_case_path, pattern=tmp, top_level_dir=test_case_path)
        for s in allsuite:
            for case in s:
                suite.addTest(case)
    return suite
