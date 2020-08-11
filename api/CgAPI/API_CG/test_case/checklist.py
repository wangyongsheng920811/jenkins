from API_CG.lib.test_func import *

del_test_data(headers=headers_fe)


@ddt.ddt
class Run_setting(unittest.TestCase):
    # 门店模块
    @ddt.data(
        ['新建门店A', 'add_branch', {'name': branch_A}],
        ['新建门店B', 'add_branch', {'name': branch_B}],
        ['新建门店C', 'add_branch', {'name': branch_C}],
        ['新建门店D', 'add_branch', {'name': branch_D}],
        ['获取门店列表', 'get_branch_list'],
        ['删除门店D', 'del_branch', {'name': branch_D}],
        ['修改门店C', 'edit_branch', {'branch_name': branch_C, 'new_name': branch_E}],
        ['修改商户用电设置', 'update_client_ele_settings'],
        ['获取门店用电设置', 'get_branch_ele_settings', {'name': branch_A}],
        ['修改门店用电设置', 'update_branch_ele_settings', {'name': branch_A}],
    )
    @ddt.unpack
    def test_01(self, title, func_name, param={}):
        print_write('\n====%s========================' % title)
        exec(func_name + '(param=param)')
        print_write('====Pass========================\n')

    # 房源模块
    @ddt.data(
        ['新建房源:A/分散/门店A', 'add_home', {'home_name': home_A, 'branch_name': branch_A, 'home_type': 1}],
        ['新建房源:B/集中/门店B', 'add_home', {'home_name': home_B, 'branch_name': branch_B, 'home_type': 2}],
        ['新建房源:C/集中/总店', 'add_home', {'home_name': home_C, 'branch_name': 'default', 'home_type': 2}],
        ['新建房源:D/分散/总店', 'add_home', {'home_name': home_D, 'branch_name': 'default', 'home_type': 1}],
        ['检查门店A下的房源A', 'find_home_by_branch', {'branch_name': branch_A, 'home_names': [home_A]}],
        ['检查门店B下的房源B', 'find_home_by_branch', {'branch_name': branch_B, 'home_names': [home_B]}],
        ['检查门店0下的房源C', 'find_home_by_branch', {'branch_name': 'default', 'home_names': [home_C]}],
        ['批量修改房源A,门店为E', 'edit_homes_branch', {'branch_name': branch_E, 'home_names': [home_A]}],
        ['批量修改房源D,门店为A', 'edit_homes_branch', {'branch_name': branch_A, 'home_names': [home_D]}],
        ['批量修改房源BC,门店为总店', 'edit_homes_branch', {'branch_name': 'default', 'home_names': [home_B, home_C]}],
        ['修改房源详情', 'edit_home', {'new_name': home_E, 'branch_name': branch_E, 'home_name': home_B}],
        ['检查房源默认为关闭公摊,独立电表', 'get_home_pool_settings', {'home_name': home_A, 'pool_settings': {'use_pool': False, 'pool_area_type': 2}}],
        ['修改房源公摊为开启公摊,总电表', 'edit_home_pool_settings', {'home_name': home_A, 'req_param': {'pool_area_type': 1, 'use_pool': True, 'pool_type': 1, 'ratios': {}}}],
        ['获取分店房源默认用电设置', 'get_home_ele_settings', {'home_name': home_D, 'check': 'check_init'}],
        ['获取分店房源默认用电设置', 'get_home_ele_settings', {'home_name': home_C, 'check': 'check_init'}],
        ['修改房源用电设置', 'update_home_ele_settings', {'home_name': home_A,
                                                  'req_param': {"pay_type": random.choice([1, 2]), "low_warn": random.choice([3, 5, 8, 10]), "ele_price": random.randint(10000, 49999) / 10000,
                                                                "overdraft_amount": random.randint(10000, 99999) / 10000}}],
        ['新增管家', 'add_house_manager', house_manager_A],
        ['分配房源给管家', 'edit_home_manager', {'home_name': home_A}],
        ['删除管家', 'del_house_manager'],
        ['删除房源', 'delete_home', {'home_name': home_A}],
    )
    @ddt.unpack
    def test_02(self, title, func_name, param={}):
        print_write('\n====%s========================' % title)
        exec(func_name + '(param=param)')
        print_write('====Pass========================\n')

    # 房间+电表
    @ddt.data(
        ['获取房源列表', 'get_home_list', {'limit': 50}],
        ['集中式房源添加房间,并检查默认用电设置', 'add_rooms_1', {'home_name': home_C, 'floor_num': 5, 'room_num': 3}],
        ['修改房间信息', 'edit_room', {'new_room_name': '2.1.updated', 'room_name': '2.1'}],
        ['修改房间为预付费', 'edit_room_ele_setting', {'room_name': '2.2', 'pay_type': 1}],
        ['修改房间为后付费', 'edit_room_ele_setting', {'room_name': '2.2', 'pay_type': 2}],
        ['修改公区为预付费', 'edit_room_ele_setting', {'room_name': '公区', 'pay_type': 1}],
        ['修改公区为后付费', 'edit_room_ele_setting', {'room_name': '公区', 'pay_type': 2}],
        ['分散式房源添加房间,并检查默认用电设置', 'add_rooms_1', {'home_name': home_D, 'room_num': 20}],
        ['修改房间信息', 'edit_room', {'new_room_name': '零五', 'room_name': '05'}],
        ['删除房间01', 'del_room', {'room_name': '01'}],
        ['删除房间02', 'del_room', {'room_name': '02'}],
        ['绑定AMG到公区', 'bind_elemeter', {'room_name': '公区', 'ele': config.amg}],
        ['绑定A1P到房间03', 'bind_elemeter', {'room_name': '03', 'ele': config.a1p, 'parent_id': config.amg['id']}],
        ['绑定A3到房间04', 'bind_elemeter', {'room_name': '04', 'ele': config.a3, 'parent_id': config.amg['id']}],
    )
    @ddt.unpack
    def test_03(self, title, func_name, param={}):
        print_write('\n====%s========================' % title)
        exec(func_name + '(param=param)')
        print_write('====Pass========================\n')


if __name__ == "__main__":
    unittest.main()
