from API_CG.lib.saas_api_prepare import *


# 房间模块
@ddt.ddt
class Run_setting(unittest.TestCase):
    # 获取多个房源房间列表
    @ddt.data(
        ['获取多个房源的房间列表home_ids参数正确:' + str([home['home_id'], home_update['home_id']]), {'home_ids': str([home['home_id'], home_update['home_id']])}, '0', '/v3/homes/rooms', 'get'],
        ['获取多个房源的房间列表home_ids参数缺失', {}, '400000', '/v3/homes/rooms', 'get'],
        ['获取多个房源的房间列表home_ids参数错误:[54321, 12345]', {'home_ids': '[54321, 12345]'}, '0', '/v3/homes/rooms', 'get'],
        ['获取多个房源的房间列表home_ids类型错误', {'home_ids': 123}, '400000', '/v3/homes/rooms', 'get'],
        ['获取多个房源的房间列表limit参数正确:20', {'home_ids': str([home['home_id'], home_update['home_id']]), 'limit': 20}, '0', '/v3/homes/rooms', 'get'],
        ['获取多个房源的房间列表limit类型错误', {'home_ids': str([home['home_id'], home_update['home_id']]), 'limit': 'test'}, '400000', '/v3/homes/rooms', 'get'],
    )
    @ddt.unpack
    def test_01(self, title, param, check_str, url, method, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 获取多个单源房间列表
    @ddt.data(
        ['获取单个房源的房间列表floor参数正确:None', {}, '0', '/v3/homes/' + str(home['home_id']) + '/rooms', 'get'],
        ['获取单个房源的房间列表floor参数正确:1', {'floor': 1}, '0', '/v3/homes/' + str(home['home_id']) + '/rooms', 'get'],
        ['获取单个房源的房间列表floor参数错误:1.1', {'floor': 1.1}, '400000', '/v3/homes/' + str(home['home_id']) + '/rooms', 'get'],
        ['获取单个房源的房间列表floor类型错误', {'floor': 'test'}, '400000', '/v3/homes/' + str(home['home_id']) + '/rooms', 'get'],
        ['获取单个房源的房间列表with_device参数错误:1', {'with_device': 1}, '"devices" in res["result"][0].keys()',
         '/v3/homes/' + str(home['home_id']) + '/rooms', 'get'],
        ['获取单个房源的房间列表with_device参数错误:2', {'with_device': 2}, '"devices" not in res["result"][0].keys()',
         '/v3/homes/' + str(home['home_id']) + '/rooms', 'get'],
        ['获取单个房源的房间列表with_device类型错误', {'with_device': 'test'}, '400000',
         '/v3/homes/' + str(home['home_id']) + '/rooms', 'get'],
        ['获取单个房源的房间列表with_tenant参数正确:1', {'with_tenant': 1}, '0', '/v3/homes/' + str(home['home_id']) + '/rooms',
         'get'],
        ['获取单个房源的房间列表with_tenant类型错误', {'with_tenant': 'test'}, '400000',
         '/v3/homes/' + str(home['home_id']) + '/rooms', 'get'],
        ['获取单个房源的房间列表empty_room参数正确:2', {'empty_room': 2}, '0', '/v3/homes/' + str(home['home_id']) + '/rooms', 'get'],
        ['获取单个房源的房间列表empty_room参数错误:1', {'empty_room': 1}, 'len(res["result"])>0',
         '/v3/homes/' + str(home['home_id']) + '/rooms', 'get'],
        ['获取单个房源的房间列表empty_room类型错误', {'empty_room': 'test'}, '400000', '/v3/homes/' + str(home['home_id']) + '/rooms',
         'get'],
        ['获取单个房源的房间列表rented_room参数正确:1', {'rented_room': 1}, '0', '/v3/homes/' + str(home['home_id']) + '/rooms',
         'get'],
        ['获取单个房源的房间列表rented_room类型错误', {'rented_room': 'test'}, '400000',
         '/v3/homes/' + str(home['home_id']) + '/rooms', 'get'],
        ['获取单个房源的房间列表exceptional_room参数正确:1', {'exceptional_room': 1}, '0',
         '/v3/homes/' + str(home['home_id']) + '/rooms', 'get'],
        ['获取单个房源的房间列表exceptional_room类型错误', {'exceptional_room': 'test'}, '400000',
         '/v3/homes/' + str(home['home_id']) + '/rooms', 'get'],
        ['获取单个房源的房间列表keyword参数正确:test', {'keyword': 'test'}, '0', '/v3/homes/' + str(home['home_id']) + '/rooms',
         'get'],
        ['获取单个房源的房间列表limit参数正确:20', {'limit': 20}, '0', '/v3/homes/' + str(home['home_id']) + '/rooms', 'get'],
        ['获取单个房源的房间列表limit类型错误', {'limit': 'test'}, '400000', '/v3/homes/' + str(home['home_id']) + '/rooms', 'get'],
        ['获取单个房源的房间列表offset参数正确:20', {'offset': 20}, '0', '/v3/homes/' + str(home['home_id']) + '/rooms', 'get'],
        ['获取单个房源的房间列表offset类型错误', {'offset': 'test'}, '400000', '/v3/homes/' + str(home['home_id']) + '/rooms', 'get'],
        ['获取单个房源的房间列表home_id类型错', {}, '400000', '/v3/homes/test/rooms', 'get'],
        ['获取单个房源的房间列表home_id不存在', {}, '', '/v3/homes/12345/rooms', 'get'],
    )
    @ddt.unpack
    def test_02(self, title, param, check_str, url, method, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 获取房间详情
    @ddt.data(
        ['获取公区房间详情', {}, '0', '/v3/rooms/' + str(rooms[0]['id']), 'get'],
        ['获取普通房间详情', {}, '0', '/v3/rooms/' + str(rooms[1]['id']), 'get'],
        ['获取房间详情,room_id类型错误', {}, '400000', '/v3/rooms/test', 'get'],
        ['获取房间详情,room_id不存在', {}, '', '/v3/rooms/12345', 'get'],
    )
    @ddt.unpack
    def test_03(self, title, param, check_str, url, method, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 获取房间用电设置
    @ddt.data(
        ['获取房间用电设置', {}, '0', '/v3/rooms/' + str(rooms[0]['id']) + '/elemeter_setting', 'get'],
        ['获取房间用电设置', {}, '0', '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'get'],
        ['获取房间用电设置,room_id类型错误', {}, '400000', '/v3/rooms/test' + '/elemeter_setting', 'get'],
        ['获取房间用电设置,room_id不存在', {}, '', '/v3/rooms/12345' + '/elemeter_setting', 'get'],
    )
    @ddt.unpack
    def test_04(self, title, param, check_str, url, method, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 获取公区下的子房间
    @ddt.data(
        ['获取公区下的子房间,room_id为公区房间', {}, 'res["err_code"]==0 and len(res["result"])>10',
         '/v3/rooms/' + str(rooms[0]['id']) + '/rooms', 'get'],
        ['获取公区下的子房间,room_id为普通房间', {}, '400000', '/v3/rooms/' + str(rooms[1]['id']) + '/rooms', 'get'],
        ['获取房间详情,room_id类型错误', {}, '400000', '/v3/rooms/test', 'get'],
        ['获取房间详情,room_id不存在', {}, '', '/v3/rooms/12345', 'get']
    )
    @ddt.unpack
    def test_05(self, title, param, check_str, url, method, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 获取房间充值列表
    @ddt.data(
        ['获取房间充值列表type参数正确:1', {'type': 1, 'startTime': 1, 'endTime': int(time.time())}, '0',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter/charge_list', 'get'],
        ['获取房间充值列表type参数缺失', {'startTime': 1, 'endTime': int(time.time())}, '0',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter/charge_list', 'get'],
        ['获取房间充值列表type参数错误:6.6', {'type': 6.6, 'startTime': 1, 'endTime': int(time.time())}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter/charge_list', 'get'],
        ['获取房间充值列表type类型错误', {'type': 'test', 'startTime': 1, 'endTime': int(time.time())}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter/charge_list', 'get'],
        ['获取房间充值列表type最大值', {'type': 3, 'startTime': 1, 'endTime': int(time.time())}, '0',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter/charge_list', 'get'],
        ['获取房间充值列表startTime参数缺失', {'type': 1, 'endTime': int(time.time())}, '0',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter/charge_list', 'get'],
        ['获取房间充值列表startTime参数错误:11.2', {'type': 1, 'startTime': 11.2, 'endTime': int(time.time())}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter/charge_list', 'get'],
        ['获取房间充值列表startTime大于endTime',
         {'type': 1, 'startTime': int(time.time()) + 3600000, 'endTime': int(time.time())}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter/charge_list', 'get'],
        ['获取房间充值列表startTime类型错误', {'type': 1, 'startTime': 'test', 'endTime': int(time.time())}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter/charge_list', 'get'],
        ['获取房间充值列表endTime参数缺失', {'type': 1, 'startTime': 1}, '0',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter/charge_list',
         'get'],
        ['获取房间充值列表endTime参数错误:-1', {'type': 1, 'startTime': 1, 'endTime': -1}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter/charge_list', 'get'],
        ['获取房间充值列表endTime类型错误', {'type': 1, 'startTime': 1, 'endTime': 'test'}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter/charge_list', 'get'],

    )
    @ddt.unpack
    def test_06(self, title, param, check_str, url, method):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        try:
            assert check_res(res=res, check_str=check_str)
            print_write('----Pass---------------------\n')
        except Exception as err:
            print_write('----Fail---------------------\n')
            print_write(err)
            assert False

    # 获取房间用电记录
    @ddt.data(
        # # # 缺少一条不报错的用例
        ['获取房间用电记录type参数正确:day', {'type': 'day', 'start_time': 1, 'end_time': int(time.time())}, 400049,
         '/v3/rooms/' + str(rooms[1]['id']) + '/electric_record', 'get'],
        ['获取房间用电记录type参数正确:hour', {'type': 'hour', 'start_time': 1, 'end_time': int(time.time())}, 400049,
         '/v3/rooms/' + str(rooms[1]['id']) + '/electric_record', 'get'],
        ['获取房间用电记录type参数缺失', {'start_time': 1, 'end_time': int(time.time())}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/electric_record', 'get'],
        ['获取房间用电记录type参数错误:year', {'type': 'year', 'start_time': 1, 'end_time': int(time.time())}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/electric_record', 'get'],
        ['获取房间用电记录start_time参数缺失', {'type': 'day', 'end_time': int(time.time())}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/electric_record', 'get'],
        ['获取房间用电记录start_time类型错误:11.2', {'type': 'day', 'start_time': 11.2, 'end_time': int(time.time())}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/electric_record', 'get'],
        ['获取房间用电记录start_time范围错误: 0', {'type': 'day', 'start_time': 0, 'end_time': int(time.time())}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/electric_record', 'get'],
        ['获取房间用电记录start_time大于end_time', {'type': 'day', 'start_time': int(time.time()) + 3600000, 'end_time': int(time.time())},
         '400000', '/v3/rooms/' + str(rooms[1]['id']) + '/electric_record', 'get'],
        ['获取房间用电记录start_time类型错误', {'type': 'day', 'start_time': 'test', 'end_time': int(time.time())}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/electric_record', 'get'],
        ['获取房间用电记录end_time参数缺失', {'type': 'day', 'start_time': 0}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/electric_record',
         'get'],
        ['获取房间用电记录end_time范围错误:0', {'type': 'day', 'start_time': 1, 'end_time': -1}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/electric_record', 'get'],
        ['获取房间用电记录end_time类型错误', {'type': 'day', 'start_time': 1, 'end_time': 'test'}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/electric_record', 'get'],
    )
    @ddt.unpack
    def test_07(self, title, param, check_str, url, method, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 修改房间详情
    @ddt.data(
        # 修改公区房间详情
        ['修改公区房间详情room_name参数正确:test', {'room_name': 'test'}, '0', '/v3/rooms/' + str(rooms[0]['id']), 'put'],
        ['修改公区房间详情room_name参数缺失', {}, '400000', '/v3/rooms/' + str(rooms[0]['id']), 'put'],
        ['修改公区房间详情room_name类型错误', {'room_name': 123}, '400000', '/v3/rooms/' + str(rooms[0]['id']), 'put'],
        ['修改公区房间详情alias参数正确:test_alias', {'room_name': 'test', 'alias': 'test_alias'}, '0',
         '/v3/rooms/' + str(rooms[0]['id']),
         'put'],
        ['修改公区房间详情alias类型错误', {'room_name': 'test', 'alias': 123}, '400000', '/v3/rooms/' + str(rooms[0]['id']), 'put'],
        ['修改公区房间详情parent_id参数错误:12345', {'room_name': 'test', 'parent_id': 12345}, '500109',
         '/v3/rooms/' + str(rooms[0]['id']),
         'put'],
        ['修改公区房间详情parent_id参数错误:parent_id为本身', {'room_name': 'test', 'parent_id': rooms[0]['id']}, '0',
         '/v3/rooms/' + str(rooms[0]['id']), 'put'],
        ['修改公区房间详情parent_id参数错误:其它房源的公区id', {'room_name': 'test', 'parent_id': rooms_delete[0]['id']}, '500109',
         '/v3/rooms/' + str(rooms[0]['id']), 'put'],
        ['修改公区房间详情parent_id类型错误', {'room_name': 'test', 'parent_id': 'test'}, '400000',
         '/v3/rooms/' + str(rooms[0]['id']), 'put'],
        ['修改公区房间详情description参数正确:test', {'room_name': 'test', 'description': 'test'}, '0',
         '/v3/rooms/' + str(rooms[0]['id']),
         'put'],
        ['修改公区房间详情description类型错误', {'room_name': 'test', 'description': 123}, '400000',
         '/v3/rooms/' + str(rooms[0]['id']), 'put'],
        # ['修改公区房间详情floor参数正确:0', {'room_name': 'test__haha', 'floor': 1}, '0', '/v3/rooms/' + str(rooms[0]['id']), 'put'],
        ['修改公区房间详情floor参数错误:999', {'room_name': 'test', 'floor': 999}, '400000', '/v3/rooms/' + str(rooms[0]['id']),
         'put'],
        ['修改公区房间详情floor类型错误', {'room_name': 'test', 'floor': 'test'}, '400000', '/v3/rooms/' + str(rooms[0]['id']),
         'put'],
        # 修改普通房间详情
        ['修改普通房间详情room_name参数正确:test', {'room_name': 'test'}, '0', '/v3/rooms/' + str(rooms[1]['id']), 'put'],
        ['修改普通房间详情room_name参数缺失', {}, '400000', '/v3/rooms/' + str(rooms[1]['id']), 'put'],
        ['修改普通房间详情room_name类型错误', {'room_name': 123}, '400000', '/v3/rooms/' + str(rooms[1]['id']), 'put'],
        ['修改普通房间详情parent_id参数正确:rooms[0]["id"]', {'room_name': 'test', 'parent_id': rooms[0]['id']}, '0',
         '/v3/rooms/' + str(rooms[1]['id']), 'put'],
        ['修改普通房间详情parent_id参数错误:12345', {'room_name': 'test', 'parent_id': 12345}, '500109',
         '/v3/rooms/' + str(rooms[1]['id']),
         'put'],
        ['修改普通房间详情parent_id参数错误:非公区房间的id', {'room_name': 'test', 'parent_id': rooms[1]['id']}, '500109',
         '/v3/rooms/' + str(rooms[1]['id']), 'put'],
        ['修改普通房间详情parent_id参数错误:其他房源公区的id', {'room_name': 'test', 'parent_id': rooms_delete[0]['id']}, '500109',
         '/v3/rooms/' + str(rooms[1]['id']), 'put'],
        ['修改普通房间详情parent_id类型错误', {'room_name': 'test', 'parent_id': 'test'}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']), 'put'],
    )
    @ddt.unpack
    def test_08(self, title, param, check_str, url, method, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 更新房间用电设置
    @ddt.unpack
    @ddt.data(
        ['更新房间用电设置overdraft_amount参数正确:1', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 1, 'pay_type': 1}, '0',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置overdraft_amount参数正确:99', {'overdraft_amount': 99, 'low_warn': 3, 'ele_price': 1, 'pay_type': 1}, '0',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置overdraft_amount参数缺失', {'low_warn': 3, 'ele_price': 1, 'pay_type': 1}, '0',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置overdraft_amount参数错误:-1', {'overdraft_amount': -1, 'low_warn': 3, 'ele_price': 1, 'pay_type': 1},
         '400000', '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置overdraft_amount类型错误', {'overdraft_amount': 'test', 'low_warn': 3, 'ele_price': 1, 'pay_type': 1},
         '400000', '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置low_warn参数正确:1', {'overdraft_amount': 1, 'low_warn': 1, 'ele_price': 1, 'pay_type': 1}, '0',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置low_warn参数正确:99', {'overdraft_amount': 1, 'low_warn': 99, 'ele_price': 1, 'pay_type': 1}, '0',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置low_warn参数缺失', {'overdraft_amount': 1, 'ele_price': 1, 'pay_type': 1}, '0',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置low_warn参数错误:0', {'overdraft_amount': 1, 'low_warn': 0.01, 'ele_price': 1, 'pay_type': 1}, '0',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置low_warn参数错误:0', {'overdraft_amount': 1, 'low_warn': 0, 'ele_price': 1, 'pay_type': 1}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置low_warn参数错误:-1', {'overdraft_amount': 1, 'low_warn': -1, 'ele_price': 1, 'pay_type': 1}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置low_warn类型错误', {'overdraft_amount': 1, 'low_warn': 'test', 'ele_price': 1, 'pay_type': 1}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置ele_price参数正确:0.1', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 0.1, 'pay_type': 1}, '0',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置ele_price参数正确:5', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 5, 'pay_type': 1}, '0',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置ele_price参数缺失', {'overdraft_amount': 1, 'low_warn': 3, 'pay_type': 1}, '0',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置ele_price参数错误:0', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 0, 'pay_type': 1}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置ele_price参数错误:6', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 6, 'pay_type': 1}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置ele_price类型错误', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 'test', 'pay_type': 1}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置pay_type参数缺失', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 1}, '403001',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置pay_type参数错误:1.1', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 1, 'pay_type': 1.1}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置pay_type类型错误', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 1, 'pay_type': 'test'}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置pay_type范围错误', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 1, 'pay_type': 0}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置pay_type最大值', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 1, 'pay_type': 2}, '0',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
        ['更新房间用电设置pay_type范围错误', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 1, 'pay_type': 3}, '400000',
         '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter_setting', 'put'],
    )
    def test_09(self, title, param, check_str, url, method, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 房间剩余电量清零
    @ddt.data(
        ['公区房间剩余电量清零', {}, '0', '/v3/rooms/' + str(rooms[0]['id']) + '/elemeters/left/reset', 'post'],
        ['普通房间剩余电量清零', {}, '0', '/v3/rooms/' + str(rooms[1]['id']) + '/elemeters/left/reset', 'post'],
        ['房间剩余电量清零,room_id类型错误', {}, '400000', '/v3/rooms/test/elemeters/left/reset', 'post'],
        ['房间剩余电量清零,room_id不存在', {}, '403004', '/v3/rooms/12345/elemeters/left/reset', 'post'],
    )
    @ddt.unpack
    def test_10(self, title, param, check_str, url, method, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 删除房间
    @ddt.data(
        ['删除公区房间', {}, '400063', '/v3/rooms/' + str(rooms_delete[0]['id']), 'delete'],
        ['删除普通房间', {}, '0', '/v3/rooms/' + str(rooms_delete[1]['id']), 'delete'],
        ['删除房间,room_id类型错误', {}, '400000', '/v3/rooms/test', 'delete'],
        ['删除房间,room_id不存在', {}, '403004', '/v3/rooms/12345', 'delete']
    )
    @ddt.unpack
    def test_10(self, title, param, check_str, url, method, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 导出充值记录列表
    @ddt.data(
        ['导出充值记录列表', {}, os.path.split(os.path.realpath(__file__))[0] + '/../../../CgAPI/API_CG/Run_case/test.xlsx', '/v3/rooms/' + str(rooms[1]['id']) + '/elemeter/charge_list/export']
    )
    @ddt.unpack
    def test_11(self, title, param, save_path, url):
        print_write('\n----', title, '---------------')
        res = requests.get(url=config.saas3_api + url, params=param, headers=headers_fe, verify=False)
        try:
            clear_file(save_path)
            assert res.status_code == 200
            with open(save_path, 'wb') as f:
                f.write(res.content)
            print_write('----Pass---------------------\n')
        except:
            print_write('----Fail---------------------\n')
            exit()


if __name__ == "__main__":
    unittest.main()
