#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : WangYongsheng
import unittest
from common.common import Common
from common.my_ddt import *


@ddt
class User(unittest.TestCase):
    '''设置管理-员工列表'''

    @file_data(common_test=1)
    def test_000_common(self, payload):
        '''通用测试'''
        Common.check(self, payload)

    @file_data()
    def test_001_get_role_ids(self, payload):
        '''获取所有角色id'''
        res = Common.check(self, payload)
        User.role_ids = [i.get('id') for i in res.json().get('data')]

    @file_data()
    def test_002_add_user(self, payload):
        '''创建用户'''
        User.user_name = 'AutoTest{}'.format(Common.format_time())
        User.phone = '1{}'.format(Common.format_time()[4:])
        User.role_ids = Common.random_list(User.role_ids)
        payload['params']['userName'] = User.user_name
        payload['params']['roleIds'] = User.role_ids
        payload['params']['phone'] = User.phone
        res = Common.check(self, payload)
        User.user_id = res.json().get('data').get('id')
        User.user_status = 1

    @file_data()
    def test_003_get_user_details(self, payload):
        '''获取用户详情'''
        payload['path'] = payload['path'].format(User.user_id)
        res = Common.check(self, payload)
        self.assertEqual(User.user_name, res.json().get('data').get('userName'), msg=res.json())
        self.assertEqual(User.phone, res.json().get('data').get('phone'), msg=res.json())
        self.assertEqual(User.user_status, res.json().get('data').get('status'), msg=res.json())
        self.assertEqual(sorted(User.role_ids), sorted([role.get('id') for role in res.json().get('data').get('roles')]), msg=res.json())

    @file_data()
    def test_004_update_user(self, payload):
        '''更新用户'''
        User.user_name = 'Update{}'.format(User.user_name)
        User.phone = '1{}'.format(Common.format_time()[4:])
        User.role_ids = Common.random_list(User.role_ids)
        payload['path'] = payload['path'].format(User.user_id)
        payload['params']['userName'] = User.user_name
        payload['params']['roleIds'] = User.role_ids
        payload['params']['phone'] = User.phone
        Common.check(self, payload)
        self.test_003_get_user_details_test_001_get_user_details()

    @file_data()
    def test_005_frozen_user(self, payload):
        '''冻结用户'''
        payload['path'] = payload['path'].format(User.user_id)
        Common.check(self, payload)
        User.user_status = 2
        self.test_003_get_user_details_test_001_get_user_details()

    @file_data()
    def test_006_unfrozen_user(self, payload):
        '''解冻用户'''
        payload['path'] = payload['path'].format(User.user_id)
        Common.check(self, payload)
        User.user_status = 1
        self.test_003_get_user_details_test_001_get_user_details()

    @file_data()
    def test_007_leave_user(self, payload):
        '''离职 用户'''
        payload['path'] = payload['path'].format(User.user_id)
        Common.check(self, payload)
        User.user_status = 3
        self.test_003_get_user_details_test_001_get_user_details()
