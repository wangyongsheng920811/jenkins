from API_CG.lib.saas_api_prepare import *



@ddt.ddt
class Run_setting(unittest.TestCase):

    # 绑定无网关门锁
    @ddt.data(
        ['/v3/rooms/' + str(rooms[1]['id']) + '/gateless_locks', 'post', '绑定无网关门锁,sn缺失', {'code': config.lock['code'], 'description': 'test_lit'}, 400000],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/gateless_locks', 'post', '绑定无网关门锁,sn类型错误', {'sn': 10086, 'code': config.lock['code'], 'description': 'test_lit'}, 400000],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/gateless_locks', 'post', '绑定无网关门锁,sn不正确', {'sn': 'lkjl0011170800310086', 'code': config.lock['code'], 'description': 'test_lit'}, 5016],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/gateless_locks', 'post', '绑定无网关门锁,sn格式错误', {'sn': '10086', 'code': config.lock['code'], 'description': 'test_lit'}, 6006],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/gateless_locks', 'post', '绑定无网关门锁,code缺失', {'sn': config.lock['sn'], 'description': 'test_lit'}, 400000],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/gateless_locks', 'post', '绑定无网关门锁,code类型错误', {'sn': config.lock['sn'], 'code': 10086, 'description': 'test_lit'}, 400000],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/gateless_locks', 'post', '绑定无网关门锁,code格式错误', {'sn': config.lock['sn'], 'code': '12344321', 'description': 'test_lit'}, 5040],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/gateless_locks', 'post', '绑定无网关门锁,description缺失', {'sn': config.lock['sn'], 'code': config.lock['code']}, 400000],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/gateless_locks', 'post', '绑定无网关门锁,description类型错误', {'sn': config.lock['sn'], 'code': config.lock['code'], 'description': 10086}, 400000],
        ['/v3/rooms/10086/gateless_locks', 'post', '绑定无网关门锁,room_id不存在的房间', {'sn': config.lock['sn'], 'code': config.lock['code'], 'description': 'test_lit'}, 403004],
        ['/v3/rooms/test/gateless_locks', 'post', '绑定无网关门锁,room_id不是int', {'sn': config.lock['sn'], 'code': config.lock['code'], 'description': 'test_lit'}, 400000],
        ['/v3/rooms/' + str(rooms[0]['id']) + '/gateless_locks', 'post', '绑定外门无网关锁', {'sn': config.lock['sn'], 'code': config.lock['code'], 'description': 'test_lit'}, 0],
        ['/v3/rooms/' + str(rooms[0]['id']) + '/gateless_locks', 'post', '重复绑定无网关门锁', {'sn': config.lock['sn'], 'code': config.lock['code'], 'description': 'test_lit'}, 500316],
        ['/v3/rooms/' + str(rooms[0]['id']) + '/locks/' + config.lock['id'], 'delete', '解绑外门无网关锁', {}, 0, 'unbind', rooms[0]['id']],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/gateless_locks', 'post', '绑定内门无网关锁', {'sn': config.lock['sn'], 'code': config.lock['code'], 'description': 'test_lit'}, 0],
    )
    @ddt.unpack
    def test_01(self, url, method, title, param, check_str, t=10086, extra_param_1='', extra_param_2=''):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1, description=title)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 获取门锁基本信息
    @ddt.data(
        # # # 缺少一条有网关门锁用例
        # ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/' + gateway_config.lock['id'], 'get', '获取门锁基本信息,有网关门锁', {}, 'res["err_code"]==0 and res["result"]["parent"]!="GOD"'],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/' + config.lock['id'], 'get', '获取门锁基本信息,无网关门锁', {}, 'res["err_code"]==0 and res["result"]["parent"]=="GOD"'],
        ['/v3/rooms/' + 'test' + '/locks/' + config.lock['id'], 'get', '获取门锁基本信息,room_id类型错误', {}, 400000],
        ['/v3/rooms/' + '10086' + '/locks/' + config.lock['id'], 'get', '获取门锁基本信息,room_id_不存在', {}, 403004],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/test', 'get', '获取门锁基本信息,device_id类型错误', {}, 400000],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/10086', 'get', '获取门锁基本信息,device_id不存在', {}, 400317],
    )
    @ddt.unpack
    def test_02(self, url, method, title, param, check_str, t=10086, extra_param_1='', extra_param_2=''):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1, description=title)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 获取门锁版本信息
    @ddt.data(
        ['/v3/lock/' + config.lock['sn'], 'get', '获取门锁版本信息', {}, 0],
        ['/v3/lock/lkjl0019180300779007', 'get', '获取门锁版本信息,指纹锁,未绑定', {}, 0],
        ['/v3/lock/10086', 'get', '获取门锁版本信息,sn格式错误', {}, 3027],
        ['/v3/lock/lkjl0011170800310086', 'get', '获取门锁版本信息,sn不存在', {}, 5006],
    )
    @ddt.unpack
    def test_03(self, url, method, title, param, check_str, t=10086, extra_param_1='', extra_param_2=''):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1, description=title)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 获取门锁开门记录
    @ddt.data(
        # # # 缺少一条有网关门锁用例
        # ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/' + gateway_config.lock['id'] + '/events', 'get', '获取门锁开门记录(有网关门锁)', {'start_time': 1, 'end_time': int(time.time()) * 1000}, 0],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/' + config.lock['id'] + '/events', 'get', '获取门锁开门记录', {'start_time': week_before_ms, 'end_time': now_ms}, 0],
        ['/v3/rooms/' + 'test' + '/locks/' + config.lock['id'] + '/events', 'get', '获取门锁开门记录,room_id类型错误', {'start_time': week_before_ms, 'end_time': now_ms}, 400000],
        ['/v3/rooms/' + '10086' + '/locks/' + config.lock['id'] + '/events', 'get', '获取门锁开门记录,room_id不存在', {'start_time': week_before_ms, 'end_time': now_ms}, 403004],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/' + 'test' + '/events', 'get', '获取门锁开门记录,device_id类型错误', {'start_time': week_before_ms, 'end_time': now_ms}, 400000],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/' + '10086' + '/events', 'get', '获取门锁开门记录,device_id不存在', {'start_time': week_before_ms, 'end_time': now_ms}, 400317],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/' + config.lock['id'] + '/events', 'get', '获取门锁开门记录,start_time缺失', {'end_time': now_ms}, 400000],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/' + config.lock['id'] + '/events', 'get', '获取门锁开门记录,start_time范围错误', {'start_time': 0, 'end_time': now_ms}, 400000],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/' + config.lock['id'] + '/events', 'get', '获取门锁开门记录,start_time类型错误', {'start_time': 'test', 'end_time': now_ms}, 400000],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/' + config.lock['id'] + '/events', 'get', '获取门锁开门记录,end_time缺失', {'start_time': week_before_ms}, 400000],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/' + config.lock['id'] + '/events', 'get', '获取门锁开门记录,end_time范围错误', {'start_time': week_before_ms, 'end_time': 0}, 400000],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/' + config.lock['id'] + '/events', 'get', '获取门锁开门记录,end_time类型错误', {'start_time': 'test', 'end_time': 0}, 400000],
    )
    @ddt.unpack
    def test_04(self, url, method, title, param, check_str, t=10086, extra_param_1='', extra_param_2=''):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1, description=title)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # # 重启门锁
    # @ddt.data(
    #     # # # 缺少一条有网关门锁用例
    #     # ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/' + gateway_config.lock['id'] + '/action_restart', 'put', '重启有网关门锁', {}, 0],
    #     ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/' + config.lock['id'] + '/action_restart', 'put', '重启无网关门锁', {}, 5038],
    #     ['/v3/rooms/' + 'test' + '/locks/' + config.lock['id'] + '/action_restart', 'put', '重启门锁,room_id类型错误', {}, 400000],
    #     ['/v3/rooms/' + '10086' + '/locks/' + config.lock['id'] + '/action_restart', 'put', '重启门锁,room_id不存在', {}, 403004],
    #     ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/' + 'test' + '/action_restart', 'put', '重启门锁,dev_id类型错误', {}, 400000],
    #     ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/' + '10086' + '/action_restart', 'put', '重启门锁,dev_id不存在', {}, 500317],
    # )
    # @ddt.unpack
    # def test_05(self, url, method, title, param, check_str, t=10086, extra_param_1='', extra_param_2=''):
    #     print_write('\n----', title, '---------------')
    #     res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1, description=title)
    #     assert check_res(res=res, check_str=check_str)
    #     print_write('----Pass---------------------\n')

    # 解绑门锁
    @ddt.data(
        ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/test', 'delete', '解绑门锁,device_id类型错误', {}, 400000],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/10086', 'delete', '解绑门锁,device_id不存在', {}, 400317],
        ['/v3/rooms/' + 'test' + '/locks/' + config.lock['id'], 'delete', '解绑该设备,room_id类型错误', {}, 400000],
        ['/v3/rooms/' + '10086' + '/locks/' + config.lock['id'], 'delete', '解绑该设备,room_id不存在', {}, 403004],
        ['/v3/rooms/' + str(rooms[1]['id']) + '/locks/' + config.lock['id'], 'delete', '解绑内门无网关锁', {}, 0, 'unbind', rooms[1]['id']],
    )
    @ddt.unpack
    def test_06(self, url, method, title, param, check_str, t=10086, extra_param_1='', extra_param_2=''):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1, description=title)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')



if __name__ == "__main__":
    unittest.main()
