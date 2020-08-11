from API_CG.lib.saas_api_prepare import *


@ddt.ddt
class Run_setting(unittest.TestCase):

    # 绑定无网关门锁
    @ddt.data(
        ['/v3/rooms/test/gateways', 'post', '绑定网关,room_id类型错误', {'sn': config.gateway['sn'], 'description': config.gateway['description']}, '400000'],
        ['/v3/rooms/10086/gateways', 'post', '绑定网关,room_id不存在', {'sn': config.gateway['sn'], 'description': config.gateway['description']}, '403004'],
        ['/v3/rooms/' + str(rooms[0]['id']) + '/gateways', 'post', '绑定网关,sn字段缺失', {'description': config.gateway['description']}, '400000'],
        ['/v3/rooms/' + str(rooms[0]['id']) + '/gateways', 'post', '绑定网关,sn类型错误', {'sn': 10086, 'description': config.gateway['description']}, '400000'],
        ['/v3/rooms/' + str(rooms[0]['id']) + '/gateways', 'post', '绑定网关,sn不存在', {'sn': 'cnjl1008666666666666', 'description': config.gateway['description']}, '5002'],
        ['/v3/rooms/' + str(rooms[0]['id']) + '/gateways', 'post', '绑定网关,description类型错误', {'sn': config.gateway['sn'], 'description': 10086}, '400000'],
        ['/v3/rooms/' + str(rooms[0]['id']) + '/gateways', 'post', '绑定网关,description字段缺失', {'sn': config.gateway['sn']}, '0'],
        ['/v3/rooms/' + str(rooms[0]['id']) + '/gateways/' + config.gateway['id'], 'delete', '解绑网关', {}, '0'],
        ['/v3/rooms/' + str(rooms[0]['id']) + '/gateways', 'post', '绑定网关,参数正确', {'sn': config.gateway['sn'], 'description': config.gateway['description']}, '0'],

    )
    @ddt.unpack
    def test_01(self, url, method, title, param, check_str, t=10086, extra_param_1='', extra_param_2=''):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1, description=title)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 获取网关信息
    @ddt.data(
        ['/v3/rooms/' + str(rooms[0]['id']) + '/gateways/' + config.gateway['id'], 'get', '获取网关信息', {}, '0']
    )
    @ddt.unpack
    def test_02(self, url, method, title, param, check_str, t=10086, extra_param_1='', extra_param_2=''):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1, description=title)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 解绑网关
    @ddt.data(
        ['/v3/rooms/' + str(rooms[0]['id']) + '/gateways/' + config.gateway['id'], 'delete', '解绑网关', {}, '0'],
    )
    @ddt.unpack
    def test_03(self, url, method, title, param, check_str, t=10086, extra_param_1='', extra_param_2=''):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1, description=title)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')



if __name__ == "__main__":
    unittest.main()
