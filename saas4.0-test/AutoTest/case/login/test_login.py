#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : WangYongsheng
import unittest
from common.common import Common
from common.my_ddt import *


@ddt
class Login(unittest.TestCase):
    '''登陆模块'''

    @file_data(common_test=1)
    def test_000_common(self, payload):
        '''通用测试'''
        Common.check(self, payload)
        if 'logout' in payload.get('path'):
            Common.init(Common.section)
