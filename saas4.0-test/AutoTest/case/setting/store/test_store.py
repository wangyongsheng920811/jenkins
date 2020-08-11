#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : WangYongsheng
import unittest
from common.common import Common
from common.my_ddt import *


@ddt
class Store(unittest.TestCase):
    '''设置管理-分店列表'''

    @file_data(common_test=1)
    def test_common(self, payload):
        '''通用测试'''
        Common.check(self, payload)

    @file_data()
    def test_001_add_store(self, payload):
        '''新增门店'''
        Store.store_name = 'AutoTest{}'.format(Common.format_time())
        payload['params']['storeName'] = Store.store_name
        res = Common.check(self, payload)
        Store.store_id = res.json().get('data').get('id')

    @file_data()
    def test_002_update_store(self, payload):
        '''编辑门店'''
        Store.update_store_name = 'Update{}'.format(Store.store_name)
        payload['path'] = payload['path'].format(Store.store_id)
        payload['params']['storeName'] = payload['params']['storeName'].format(Store.update_store_name)
        Common.check(self, payload)

    @file_data()
    def test_003_store_info(self, payload):
        '''门店详情'''
        Store.store_name = 'Update{}'.format(Store.store_name)
        payload['path'] = payload['path'].format(Store.store_id)
        res = Common.check(self, payload)
        self.assertEqual(Store.update_store_name, res.json().get('data').get('storeName'), msg=res.json())

    @file_data()
    def test_004_store_house(self, payload):
        '''门店房源列表'''
        payload['path'] = payload['path'].format(Store.store_id)
        Common.check(self, payload)

    @file_data()
    def test_005_user_by_store(self, payload):
        '''门店下用户列表'''
        payload['path'] = payload['path'].format(Store.store_id)
        Common.check(self, payload)
