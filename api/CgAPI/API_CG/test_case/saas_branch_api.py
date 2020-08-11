from API_CG.lib.saas_api_prepare import *


# 门店模块
@ddt.ddt
class Run_setting(unittest.TestCase):

    # 新建门店
    @ddt.data(
        ['/v3/branches', 'post', '新建门店', {'name': branch_root}, '0'],
        ['/v3/branches', 'post', '新建门店:name重复', {'name': branch['name']}, '400126'],
        ['/v3/branches', 'post', '新建门店:name为空', {'name': ''}, '400000'],
        ['/v3/branches', 'post', '新建门店:name字段缺失', {'name': ''}, '400000'],
        ['/v3/branches', 'post', '新建门店:name为空格', {'name': ' '}, '400000'],

        # 修改分店账户(/branches/:branch_id/account) (需要手机验证码  无法测试)
        # 设置提现开关(/branches/:branch_id/set_cash)(需要手机验证码  无法测试)
        # 门店按房源、房间获取列表(/branches/:branch_id/elemeter_setting/list)(未测试)
        # 导出门店导出自定义配置(/v3/branches/:branch_id/elemeter_setting/export)(未测试)
    )
    @ddt.unpack
    def test_01(self, url, method, title, param, check_str, t=10086, extra_param_1='', extra_param_2=''):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 获取门店信息
    @ddt.data(
        ['/v3/branches/' + str(branch['id']), 'get', '获取门店信息', {}, '0', 3],
        ['/v3/branches/12345', 'get', '获取门店信息,id不存在', {}, '403004'],
        ['/v3/branches/test', 'get', '获取门店信息,id类型错误', {}, '400000'],
    )
    @ddt.unpack
    def test_02(self, url, method, title, param, check_str, t=10086, extra_param_1='', extra_param_2=''):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 修改门店信息
    @ddt.data(
        ['/v3/branches/' + str(branch_update['id']), 'put', '更新门店信息', {'name': branch_update['name'] + 'updated'}, '0', 4],
        ['/v3/branches/' + str(branch_update['id']), 'get', '检查更新是否成功', {}, 'res["err_code"]==0 and res["result"]["name"]=="' + branch_update['name'] + 'updated"', 5],
        ['/v3/branches/' + str(branch_update['id']), 'put', '更新门店信息,name为空', {'name': ''}, '400000', 6],
        ['/v3/branches/' + str(branch_update['id']), 'put', '更新门店信息,name字段缺失', {}, '400000', 7],
        ['/v3/branches/' + str(branch_update['id']), 'put', '更新门店信息,name重复', {'name': branch['name']}, '400126', 8],
        ['/v3/branches/' + str(branch_update['id']), 'put', '更新门店信息,name为空格', {'name': ' '}, '400000', 8],
        ['/v3/branches/12345', 'put', '更新门店信息,id不存在', {'name': '前台接口新建门店_' + '3'}, '403004'],
        ['/v3/branches/test', 'put', '更新门店信息,id类型错误', {'name': '前台接口新建门店_' + '4'}, '400000'],
    )
    @ddt.unpack
    def test_03(self, url, method, title, param, check_str, t=10086, extra_param_1='', extra_param_2=''):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 获取门店用电设置
    @ddt.data(
        ['/v3/branches/' + str(branch['id']) + '/elemeter_setting', 'get', '获取门店用电设置,检查是否默认为商户设置', {},
         '"value" not in res["result"]["pay_type"].keys() and '
         '"value" not in res["result"]["low_warn"].keys() and '
         '"value" not in res["result"]["ele_price"].keys() and '
         '"value" not in res["result"]["overdraft_amount"].keys()', 11],
        ['/v3/branches/12345/elemeter_setting', 'get', '获取门店用电设置,id不存在', {}, '403004'],
        ['/v3/branches/test/elemeter_setting', 'get', '获取门店用电设置,id类型错误', {}, '400000'],
    )
    @ddt.unpack
    def test_04(self, url, method, title, param, check_str, t=10086, extra_param_1='', extra_param_2=''):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 修改门店用电设置 pay_type: 1-预付费 2-后付费(设置时没有带的参数都会设置成继承上一级(null))
    @ddt.data(
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,预付费,其它参数完整',
         {'pay_type': 1, 'low_warn': 8, 'overdraft_amount': 99, 'ele_price': 5}, '0', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'get', '修改后检查设置 ', {},
         'res["result"]["pay_type"]["value"]==1 and  res["result"]["low_warn"]["value"]==8 and '
         'res["result"]["ele_price"]["value"]=="5.0000" and res["result"]["overdraft_amount"]["value"]=="99.0000"', 11],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,预付费,ele_price字段缺失',
         {'pay_type': 1, 'low_warn': 8, 'overdraft_amount': 99}, '0', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,预付费,ele_price大于5',
         {'pay_type': 1, 'low_warn': 8, 'overdraft_amount': 99, 'ele_price': 6}, '400000', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,预付费,ele_price为0',
         {'pay_type': 1, 'low_warn': 8, 'overdraft_amount': 99, 'ele_price': 0}, '400000', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,预付费,ele_price类型错误',
         {'pay_type': 1, 'low_warn': 8, 'overdraft_amount': 99, 'ele_price': 'a'}, '400000', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,预付费,ele_price为空',
         {'pay_type': 1, 'low_warn': 8, 'overdraft_amount': 99, 'ele_price': None}, '0', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,预付费,low_warn字段缺失',
         {'pay_type': 1, 'overdraft_amount': 99, 'ele_price': 5}, '400000', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,预付费,low_warn类型错误',
         {'pay_type': 1, 'low_warn': 'test', 'overdraft_amount': 99, 'ele_price': 5}, '400000', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,预付费,low_warn为float',
         {'pay_type': 1, 'low_warn': 5.1, 'overdraft_amount': 99, 'ele_price': 5}, '400000', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,预付费,low_warn为0',
         {'pay_type': 1, 'low_warn': 0, 'overdraft_amount': 99, 'ele_price': 5}, '400000', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,预付费,overdraft_amount字段缺失',
         {'pay_type': 1, 'low_warn': 8, 'ele_price': 5}, '400000', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,预付费,overdraft_amount类型错误',
         {'pay_type': 1, 'low_warn': 8, 'overdraft_amount': 'test', 'ele_price': 5}, '400000', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,预付费,overdraft_amount为空',
         {'pay_type': 1, 'low_warn': 8, 'overdraft_amount': None, 'ele_price': 5}, '400000', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,预付费,overdraft_amount为float',
         {'pay_type': 1, 'low_warn': 8, 'overdraft_amount': 99.9, 'ele_price': 5}, '0', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,预付费,overdraft_amount为0',
         {'pay_type': 1, 'low_warn': 8, 'overdraft_amount': 0, 'ele_price': 5}, '400000', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,后付费', {'pay_type': 2}, '0', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'get', '修改后检查设置', {},
         'res["result"]["pay_type"]["value"]==2 and '
         '"value" not in res["result"]["low_warn"].keys() and '
         '"value" not in res["result"]["ele_price"].keys() and '
         '"value" not in res["result"]["overdraft_amount"].keys()', 11],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,后付费时,overdraft_amount,low_warn不生效,电价生效',
         {'pay_type': 2, 'low_warn': 8, 'overdraft_amount': 3, 'ele_price': 4}, '0', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'get', '修改后检查设置 ', {},
         'res["result"]["pay_type"]["value"]==2 and  '
         '"value" not in res["result"]["low_warn"].keys() and '
         'res["result"]["ele_price"]["value"]=="4.0000" and '
         '"value" not in res["result"]["overdraft_amount"].keys()', 11, '123'],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,pay_type:0', {'pay_type': 0}, '400000', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,pay_type:3', {'pay_type': 3}, '400000', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,pay_type类型错误', {'pay_type': 1.1}, '400000', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,pay_type为空', {'pay_type': None}, '0', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'put', '修改门店用电设置,无参数,即全部设置继承商户', {}, '0', 12],
        ['/v3/branches/' + str(branch_update['id']) + '/elemeter_setting', 'get', '修改后检查设置', {},
         '"value" not in res["result"]["pay_type"].keys() and '
         '"value" not in res["result"]["low_warn"].keys() and '
         '"value" not in res["result"]["ele_price"].keys() and '
         '"value" not in res["result"]["overdraft_amount"].keys()', 11],
        ['/v3/branches/12345/elemeter_setting', 'put', '修改门店用电设置,id不存在', {}, '403004'],
        ['/v3/branches/test/elemeter_setting', 'put', '修改门店用电设置,id类型错误', {}, '400000'],
    )
    @ddt.unpack
    def test_05(self, url, method, title, param, check_str, t=10086, extra_param_1='', extra_param_2=''):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 获取所有门店列表
    @ddt.data(
        ['/v3/branches/all', 'get', '获取所有门店列表', {}, '0'],
    )
    @ddt.unpack
    def test_06(self, url, method, title, param, check_str, t=10086, extra_param_1='', extra_param_2=''):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 获取门店列表
    @ddt.data(
        ['/v3/branches', 'get', '获取门店列表,无参数', {}, '0'],
        ['/v3/branches', 'get', '获取门店列表:limit为空', {'limit': ''}, '400000'],
        ['/v3/branches', 'get', '获取门店列表:limit=0', {'limit': 10}, 'len(res["result"]["list"])!=0'],
        ['/v3/branches', 'get', '获取门店列表:limit=10000', {'limit': 40}, 'len(res["result"]["list"]) in (10000,res["result"]["count"])'],
        ['/v3/branches', 'get', '获取门店列表:offset为空', {'offset': ''}, '400000'],
        ['/v3/branches', 'get', '获取门店列表:offset=0', {'offset': 0}, '0'],
        ['/v3/branches', 'get', '获取门店列表:offset=10000', {'offset': 40, 'limit': 20}, 'len(res["result"]["list"]) in (0,20,res["result"]["count"]-10000)'],
        ['/v3/branches', 'get', '获取门店列表:keyword为空', {'keyword': ''}, '0'],
        ['/v3/branches', 'get', '获取门店列表:keyword不为空', {'keyword': branch_root}, 'res["result"]["count"]!=0'],
    )
    @ddt.unpack
    def test_07(self, url, method, title, param, check_str, t=10086, extra_param_1='', extra_param_2=''):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        print_write(res)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 删除门店
    @ddt.data(
        ['/v3/branches/' + str(branch_delete['id']), 'delete', '门店下有房源时无法删除', {}, '400124', 1],
        ['/v3/branches/' + str(branch_delete['id']), 'delete', '删除门店,无参数', {}, '0'],
        ['/v3/branches/12345', 'delete', '删除门店,id不存在', {}, '403004'],
        ['/v3/branches/test', 'delete', '删除门店,id类型错误', {}, '400000'],
    )
    @ddt.unpack
    def test_08(self, url, method, title, param, check_str, t=10086, extra_param_1='', extra_param_2=''):
        print_write('\n----', title, '---------------')
        if t == 1:
            res = get_response(url='/v3/homes/' + str(home['home_id']), do='put', param={'branch_id':int(branch_delete['id'])}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='给门店增加房源')
            assert check_res(res,'0')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        if t == 1:
            res = get_response(url='/v3/homes/' + str(home['home_id']), do='put', param={'branch_id':0}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='将门店下的房源清除')
            assert check_res(res,'0')
        print_write('----Pass---------------------\n')



if __name__ == "__main__":
    unittest.main()
