#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : WangYongsheng
import unittest
from common.common import Common
from common.my_ddt import *


@ddt
class Setting(unittest.TestCase):
    '''设置管理-角色权限'''

    def random_roles(self):
        '''获取随机个数的随机角色信息'''
        roles = Common.random_list(Setting.roles_permissions)
        role_ids = [role.get('role_id') for role in roles]
        role_permissions = []
        for role in roles:
            role_permissions += role.get('role_permission')
        print(role_ids)
        print(role_permissions)
        print(set(role_permissions))
        return role_ids, list(set(role_permissions))

    @file_data(common_test=1)
    def test_common(self, payload):
        '''通用测试'''
        Common.check(self, payload)

    @file_data()
    def test_001_get_all_roles(self, payload):
        '''获取商户所有角色'''
        res = Common.check(self, payload)
        Setting.roles = res.json().get('data')

    @file_data()
    def test_002_permissions_by_id(self, payload):
        '''根据id查询角色对应权限'''
        path = payload['path']
        role_ids = [role.get('id') for role in Setting.roles]
        roles_permissions = []
        for role_id in role_ids:
            payload['path'] = path.format(role_id)
            res = Common.check(self, payload)
            roles_permissions.append({'role_id': role_id, 'role_permission': [permission.get('id') for permission in res.json().get('data')]})
        Setting.roles_permissions = roles_permissions

    @file_data()
    def test_003_add_role(self, payload):
        '''新增角色'''
        Setting.role_name = 'AutoTest{}'.format(Common.format_time())
        Setting.role_ids = self.random_roles()[0]
        payload['params']['name'] = Setting.role_name
        payload['params']['roleIds'] = Setting.role_ids
        payload['params']['permissionIds'] = self.random_roles()[1]
        res = Common.check(self, payload)
        Setting.role_id = res.json().get('data').get('id')

    @file_data()
    def test_004_roles_contain(self, payload):
        '''角色从属关系'''
        payload['path'] = payload['path'].format(Setting.role_id)
        res = Common.check(self, payload)
        tmp = [i.get('id') for i in res.json().get('data')]
        for i in Setting.role_ids:
            self.assertIn(i, tmp, msg=Setting.role_ids)

    @file_data()
    def test_005_get_role_info(self, payload):
        '''根据id获取角色信息'''
        payload['path'] = payload['path'].format(Setting.role_id)
        res = Common.check(self, payload)
        self.assertEqual(Setting.role_id, res.json().get('data').get('id'), msg=res.json())
        self.assertEqual(Setting.role_name, res.json().get('data').get('name'), msg=res.json())

    @file_data()
    def test_006_update_role(self, payload):
        '''更新角色'''
        Setting.update_role_name = 'Update' + Setting.role_name
        payload['path'] = payload['path'].format(Setting.role_id)
        payload['params']['roleId'] = Setting.role_id
        payload['params']['name'] = Setting.update_role_name
        payload['params']['roleIds'] = self.random_roles()[0]
        payload['params']['permissionIds'] = self.random_roles()[1]
        Common.check(self, payload)

    @file_data()
    def test_007_delete_role(self, payload):
        '''删除角色'''
        payload['path'] = payload['path'].format(Setting.role_id)
        Common.check(self, payload)
