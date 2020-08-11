#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : WangYongsheng
import sys
import unittest
from common.common import Common
from common.HTMLTestRunner_PY3 import HTMLTestRunner


if __name__ == '__main__':
    Common.init(sys.argv[:])
    suites = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover('./', pattern='test_*.py')
    [suites.addTests(i) for i in discover]
    ftp = open('test_report.html', 'wb')
    runner = HTMLTestRunner(stream=ftp, title='Hyperloop-Test-Report', verbosity=2, description='卫斯理')
    result = runner.run(suites)
    if result.failure_count or result.error_count:
        Common.dd_robot(result.success_count, result.failure_count, result.error_count)
