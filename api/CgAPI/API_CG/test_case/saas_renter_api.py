from API_CG.lib.saas_api_prepare import *


# 租客模块
@ddt.ddt
class Run_setting(unittest.TestCase):

    # 租客管理
    @ddt.data(
        # 添加租客
        ['/v3/tenants', 'post', '添加租客', {'name': renter_name_root + '00', 'id_card': renter_idcard_root + '00', 'phone': renter_phone_root + '00', 'note': 'test'}, '0', 0],
        ['/v3/tenants', 'post', '添加租客', {'name': renter_name_root + '50', 'id_card': renter_idcard_root + '50', 'phone': renter_phone_root + '50', 'note': 'test'}, '0', 1],
        ['/v3/tenants', 'post', '添加租客', {'name': renter_name_root + '51', 'id_card': renter_idcard_root + '51', 'phone': renter_phone_root + '51', 'note': 'test'}, '0', 2],
        ['/v3/tenants', 'post', '添加租客:name为空', {'name': '', 'id_card': renter_idcard_root + '01', 'phone': renter_phone_root + '01', 'note': 'test'}, '400000', 101],
        ['/v3/tenants', 'post', '添加租客:name字段缺失', {'id_card': renter_idcard_root + '02', 'phone': renter_phone_root + '02', 'note': 'test'}, '400000', 102],
        ['/v3/tenants', 'post', '添加租客:name特殊字符', {'name': renter_name_root + '"%~  _/!@#*&\'\\', 'id_card': renter_idcard_root + '03', 'phone': renter_phone_root + '03'}, '400000', 103],
        ['/v3/tenants', 'post', '添加租客:name为空格', {'name': ' ', 'id_card': renter_idcard_root + '04', 'phone': renter_phone_root + '04'}, '400000', 104],
        ['/v3/tenants', 'post', '添加租客:name重复', {'name': renter_name_root + '00', 'id_card': renter_idcard_root + '05', 'phone': renter_phone_root + '05', 'note': 'test'}, '0', 105],
        ['/v3/tenants', 'post', '添加租客:id_card为空', {'name': renter_name_root + '11', 'id_card': '', 'phone': renter_phone_root + '11', 'note': 'test'}, '0', 201],
        ['/v3/tenants', 'post', '添加租客:id_card字段缺失', {'name': renter_name_root + '12', 'phone': renter_phone_root + '12', 'note': 'test'}, '0', 202],
        ['/v3/tenants', 'post', '添加租客:id_card为非数字', {'name': renter_name_root + '13', 'id_card': renter_idcard_root + 'QQ', 'phone': renter_phone_root + '13', 'note': 'test'}, '400000', 203],
        ['/v3/tenants', 'post', '添加租客:id_card长度错误', {'name': renter_name_root + '35', 'id_card': renter_idcard_root, 'phone': renter_phone_root + '35', 'note': 'test'}, '400000', 203],
        ['/v3/tenants', 'post', '添加租客:id_card包含X', {'name': renter_name_root + '14', 'id_card': renter_idcard_root + '1X', 'phone': renter_phone_root + '14', 'note': 'test'}, '0', 204],
        ['/v3/tenants', 'post', '添加租客:id_card重复', {'name': renter_name_root + '15', 'id_card': renter_idcard_root + '00', 'phone': renter_phone_root + '15', 'note': 'test'}, '400146', 105],
        ['/v3/tenants', 'post', '添加租客:phone为空', {'name': renter_name_root + '21', 'id_card': renter_idcard_root + '21', 'phone': '', 'note': 'test'}, '400000', 301],
        ['/v3/tenants', 'post', '添加租客:phone字段缺失', {'name': renter_name_root + '22', 'id_card': renter_idcard_root + '22', 'note': 'test'}, '400000', 302],
        ['/v3/tenants', 'post', '添加租客:phone长度错误', {'name': renter_name_root + '23', 'id_card': renter_idcard_root + '23', 'phone': '999999999999', 'note': 'test'}, '400000', 303],
        ['/v3/tenants', 'post', '添加租客:phone为非数字', {'name': renter_name_root + '24', 'id_card': renter_idcard_root + '24', 'phone': '1106666XXXX', 'note': 'test'}, '400000', 304],
        ['/v3/tenants', 'post', '添加租客:phone已存在', {'name': renter_name_root + '25', 'id_card': renter_idcard_root + '25', 'phone': renter_phone_root + '00', 'note': 'test'}, '400146', 305],
        ['/v3/tenants', 'post', '添加租客:note为空', {'name': renter_name_root + '31', 'id_card': renter_idcard_root + '31', 'phone': renter_phone_root + '31', 'note': ''}, '0', 401],
        ['/v3/tenants', 'post', '添加租客:note为空格', {'name': renter_name_root + '32', 'id_card': renter_idcard_root + '32', 'phone': renter_phone_root + '32', 'note': ' '}, '0', 402],
        ['/v3/tenants', 'post', '添加租客:note字段缺失', {'name': renter_name_root + '33', 'id_card': renter_idcard_root + '33', 'phone': renter_phone_root + '33'}, '0', 403],

        # 查询租客列表
        ['/v3/tenants', 'get', '查询租客,无参数', {}, 'len(res["result"]["list"]) in (20,res["result"]["count"])', 5],
        ['/v3/tenants', 'get', '查询租客,限制0个', {'limit': 0}, 'len(res["result"]["list"])==0', 501],
        ['/v3/tenants', 'get', '查询租客,限制1000个', {'limit': 1000}, 'len(res["result"]["list"]) in (1000,res["result"]["count"])', 502],
        ['/v3/tenants', 'get', '查询租客,限制10000个', {'limit': 10000}, 'len(res["result"]["list"]) in (10000,res["result"]["count"])', 503],
        ['/v3/tenants', 'get', '查询租客,limit类型不对', {'limit': 'abc'}, '400000', 504],
        ['/v3/tenants', 'get', '查询租客,limit为空', {'limit': ''}, '400000', 505],
        ['/v3/tenants', 'get', '查询租客,从第0个开始', {'offset': 0}, '0', 511],
        ['/v3/tenants', 'get', '查询租客,从第10000个开始', {'offset': 10000}, 'len(res["result"]["list"]) in (0,20,res["result"]["count"]-10000)', 512],
        ['/v3/tenants', 'get', '查询租客,offset类型不对', {'offset': '4.4'}, '400000', 513],
        ['/v3/tenants', 'get', '查询租客,offset为空', {'offset': ''}, '400000', 514],
        ['/v3/tenants', 'get', '查询租客,只有type', {'type': 1}, '0', 521],
        ['/v3/tenants', 'get', '查询租客,只有keyword', {'keyword': 1}, '0', 522],
        ['/v3/tenants', 'get', '查询租客,按姓名搜索', {'type': 1, 'keyword': renter_name_root, 'limit': 10000}, 'res["err_code"]==0 and res["result"]["count"]!=0', 523, renter_name_root, 'name'],
        ['/v3/tenants', 'get', '查询租客,按手机号搜索', {'type': 2, 'keyword': renter_phone_root, 'limit': 10000}, 'res["err_code"]==0 and res["result"]["count"]!=0', 524, renter_phone_root, 'phone'],
        ['/v3/tenants', 'get', '查询租客,按身份证搜索', {'type': 3, 'keyword': renter_idcard_root}, 'res["err_code"]==0 and res["result"]["count"]!=0', 525, renter_idcard_root, 'id_card'],
        ['/v3/tenants', 'get', '查询租客,type为空', {'type': '', 'keyword': renter_idcard_root}, '400000', 526],
        ['/v3/tenants', 'get', '查询租客,keyword为空', {'type': 3, 'keyword': ''}, '0', 527],

        # 查询租客详情
        ['', 'get', '请求租客详情', {}, 'res["err_code"]==0', 6],
        ['/v3/tenants/54321', 'get', '请求租客详情,renter_id不存在', {}, 'res["err_code"]==403004', 601],
        ['/v3/tenants/abc', 'get', '请求租客详情,renter_id类型错误', {}, 'res["err_code"]==400000', 602],

        # 修改租客信息
        ['/v3/tenants', 'put', '修改租客,phone不变', {'name': renter_name_root + '99', 'id_card': renter_idcard_root + '99', 'phone': renter_phone_root + '00', 'note': 'test'}, '0', 701],
        ['/v3/tenants', 'put', '修改租客,phone变化', {'name': renter_name_root + '99', 'id_card': renter_idcard_root + '99', 'phone': renter_phone_root + '99', 'note': 'test'}, '0', 701],
        ['/v3/tenants', 'put', '修改租客,phone为空', {'name': renter_name_root + '99', 'id_card': renter_idcard_root + '99', 'phone': '', 'note': 'test'}, '0', 701],
        ['/v3/tenants', 'put', '修改租客,phone字段缺失', {'name': renter_name_root + '99', 'id_card': renter_idcard_root + '99', 'note': 'test'}, '0', 701, renter_phone_root],
        ['/v3/tenants', 'put', '修改租客,phone长度错误', {'name': renter_name_root + '99', 'id_card': renter_idcard_root + '99', 'phone': renter_phone_root, 'note': 'test'}, '400000', 701],
        ['/v3/tenants', 'put', '修改租客,phone类型错误', {'name': renter_name_root + '99', 'id_card': renter_idcard_root + '99', 'phone': renter_phone_root + 'XX', 'note': 'test'}, '400000', 701],
        ['/v3/tenants', 'put', '修改租客,phone与其他租客重复', {'name': renter_name_root + '99', 'id_card': renter_idcard_root + '99', 'phone': renter_phone_root + '66', 'note': 'test'}, '0', 701],
        ['/v3/tenants', 'put', '修改租客:name为空', {'name': '', 'id_card': renter_idcard_root + '99', 'phone': renter_phone_root + '00', 'note': 'test'}, '400000', 702],
        ['/v3/tenants', 'put', '修改租客:name字段缺失', {'id_card': renter_idcard_root + '99', 'phone': renter_phone_root + '00', 'note': 'test'}, '400000', 703],
        ['/v3/tenants', 'put', '修改租客:name特殊字符', {'name': renter_name_root + '"%~  _/!@#*&\'\\', 'id_card': renter_idcard_root + '99', 'phone': renter_phone_root + '00', 'note': 'test'}, '400000', 704],
        ['/v3/tenants', 'put', '修改租客:name为空格', {'name': ' ', 'id_card': renter_idcard_root + '00', 'phone': renter_phone_root + '00', 'note': 'test'}, '400000', 705],
        ['/v3/tenants', 'put', '修改租客:name重复', {'name': renter_name_root + '66', 'id_card': renter_idcard_root + '00', 'phone': renter_phone_root + '00', 'note': 'test'}, '0', 706],
        ['/v3/tenants', 'put', '修改租客:id_card为空', {'name': renter_name_root + '00', 'id_card': '', 'phone': renter_phone_root + '00', 'note': 'test'}, '0', 707],
        ['/v3/tenants', 'put', '修改租客:id_card字段缺失', {'name': renter_name_root + '00', 'phone': renter_phone_root + '00', 'note': 'test'}, '0', 708],
        ['/v3/tenants', 'put', '修改租客:id_card为非数字', {'name': renter_name_root + '00', 'id_card': renter_idcard_root + 'QQ', 'phone': renter_phone_root + '00', 'note': 'test'}, '400000', 709],
        ['/v3/tenants', 'put', '修改租客:id_card包含X', {'name': renter_name_root + '00', 'id_card': renter_idcard_root + '2X', 'phone': renter_phone_root + '00', 'note': 'test'}, '0', 710],
        ['/v3/tenants', 'put', '修改租客:id_card重复', {'name': renter_name_root + '00', 'id_card': renter_idcard_root + '50', 'phone': renter_phone_root + '00', 'note': 'test'}, '400146', 711],
        ['/v3/tenants', 'put', '修改租客:id_card长度错误', {'name': renter_name_root + '00', 'id_card': renter_idcard_root, 'phone': renter_phone_root + '00', 'note': 'test'}, '400000', 709],
        ['/v3/tenants', 'put', '修改租客:note为空', {'name': renter_name_root + '00', 'id_card': renter_idcard_root + '00', 'phone': renter_phone_root + '00', 'note': ''}, '0', 717],
        ['/v3/tenants', 'put', '修改租客:note为空格', {'name': renter_name_root + '00', 'id_card': renter_idcard_root + '00', 'phone': renter_phone_root + '00', 'note': ' '}, '0', 718],
        ['/v3/tenants', 'put', '修改租客:note字段缺失', {'name': renter_name_root + '00', 'id_card': renter_idcard_root + '00', 'phone': renter_phone_root + '00'}, '0', 719],

        # 删除租客
        ['/v3/tenants/test', 'delete', '删除租客,ID为非数字', {}, '400000', 801],
        ['/v3/tenants/10086', 'delete', '删除租客,ID不正确', {}, '403004', 803],
        ['/v3/tenants/', 'delete', '删除租客', {}, '0', 804],

        # 删除残留数据
        ['/v3/tenants', 'get', '删除残留数据', {'type': 2, 'keyword': renter_phone_root}, '0', 999],
    )
    @ddt.unpack
    def test_01(self, url, method, title, param, check_str, t, extra_param_1='', extra_param_2=''):
        print_write('\n----', str(t), '.', title, '---------------')
        if t == 6 or (700 < t < 800) or t == 804:
            url = '/v3/tenants/' + str(globals()['renter_id'])
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        try:
            assert check_res(res=res, check_str=check_str)
            if t == 0:
                global renter_id
                renter_id = res['result']['tenant_id']
            if t in (525, 523, 524):
                for renter in res['result']['list']:
                    print(renter[extra_param_2])
                    assert extra_param_1 in renter[extra_param_2]
            if t == 701:
                res = get_response(url=url, do='get', param={}, headers=headers_fe, address=config.saas3_api, print_resp=1)
                assert check_res(res=res, check_str='res["err_code"]==0 and res["result"]["phone"]=="' + str(renter_phone_root) + '00"')
            if t == 999:
                for renter in res['result']['list']:
                    res_del = get_response(url='/v3/tenants/' + str(renter['id']), do='delete', headers=headers_fe, address=config.saas3_api)
                    assert check_res(res_del, '0')
            print_write('----Pass---------------------\n')
        except:
            print_write('----Fail---------------------\n')
            assert False

    # 租赁相关
    right_start_time = int(time.time() * 1000)
    right_end_time = right_start_time + 604800000

    @ddt.data(
        # 租客入住
        ['租客入住,参数正确', {'lease_start': right_start_time, 'lease_end': right_end_time, 'note': 'test'}, '0', '/v3/tenants/' + str(renter_67) + '/rooms/' + str(rooms[1]['id']), 'post', 1],
        ['租客入住,start大于end', {'lease_start': right_end_time, 'lease_end': right_start_time, 'note': 'test'}, '400145', '/v3/tenants/' + str(renter_67) + '/rooms/' + str(rooms[1]['id']), 'post'],
        ['租客入住,lease_start参数缺失', {'lease_end': right_end_time, 'note': 'test'}, '400000', '/v3/tenants/' + str(renter_67) + '/rooms/' + str(rooms[2]['id']), 'post'],
        ['租客入住,lease_start错误', {'lease_start': 0, 'lease_end': right_end_time, 'note': 'test'}, '400000', '/v3/tenants/' + str(renter_67) + '/rooms/' + str(rooms[3]['id']), 'post'],
        ['租客入住,lease_start类型错误', {'lease_start': 'test', 'lease_end': right_end_time, 'note': 'test'}, '400000', '/v3/tenants/' + str(renter_67) + '/rooms/' + str(rooms[4]['id']), 'post'],
        ['租客入住,lease_end参数缺失', {'lease_start': right_start_time, 'note': 'test'}, '400000', '/v3/tenants/' + str(renter_67) + '/rooms/' + str(rooms[5]['id']), 'post'],
        ['租客入住,lease_end错误', {'lease_start': right_start_time, 'lease_end': 0, 'note': 'test'}, '400000', '/v3/tenants/' + str(renter_67) + '/rooms/' + str(rooms[7]['id']), 'post'],
        ['租客入住,lease_end类型错误', {'lease_start': right_start_time, 'lease_end': 'test', 'note': 'test'}, '400000', '/v3/tenants/' + str(renter_67) + '/rooms/' + str(rooms[8]['id']), 'post'],
        ['租客入住,note参数缺失', {'lease_start': right_start_time, 'lease_end': right_end_time}, '0', '/v3/tenants/' + str(renter_67) + '/rooms/' + str(rooms[9]['id']), 'post'],
        ['租客入住,note类型错误', {'lease_start': right_start_time, 'lease_end': right_start_time, 'note': 12345}, '400000', '/v3/tenants/' + str(renter_67) + '/rooms/' + str(rooms[10]['id']), 'post'],
        ['租客入住到公区', {'lease_start': right_start_time, 'lease_end': right_end_time, 'note': 'test'}, '400100', '/v3/tenants/' + str(renter_67) + '/rooms/' + str(rooms[0]['id']), 'post'],
        # 修改租期
        ['修改租期,lease_end小于开始日期', {'lease_end': right_start_time}, '400145', '', 'put', 2],
        ['修改租期,lease_end小于0', {'lease_end': -1}, '400000', '', 'put', 2],
        ['修改租期,lease_end类型错误', {'lease_end': 'test'}, '400000', '', 'put', 2],
        ['修改租期,lease_end字段缺失', {}, '400000', '', 'put', 2],
        ['修改租期,lease_id不存在', {'lease_end': right_end_time}, '403004', '/v3/leases/12345', 'put'],
        ['修改租期,lease_id类型错误', {'lease_end': right_end_time}, '400000', '/v3/leases/test', 'put'],
        ['修改租期,参数正确', {'lease_end': right_end_time}, '0', '', 'put', 2],
        # 冻结
        ['冻结租客,lease_id类型错误', {}, '400000', '/v3/leases/test/frozen', 'post'],
        ['冻结租客,lease_id不存在', {}, '403004', '/v3/leases/12345/frozen', 'post'],
        ['冻结租客,成功', {}, '0', '', 'post', 3],
        ['冻结状态为已冻结的租客', {}, '0', '', 'post', 3],
        # 解冻
        ['解冻租客,lease_id类型错误', {}, '400000', '/v3/leases/test/unfrozen', 'post'],
        ['解冻租客,lease_id不存在', {}, '403004', '/v3/leases/12345/unfrozen', 'post'],
        ['解冻租客,成功', {}, '0', '', 'post', 4],
        ['解冻状态为未冻结的租客', {}, '0', '', 'post', 4],
        # 退租
        ['退租,lease_id不存在', {}, '403004', '/v3/leases/12345', 'delete'],
        ['退租,lease_id类型错误', {}, '400000', '/v3/leases/test', 'delete'],
        ['退租,参数正确', {}, '0', '', 'delete', 2],

        # #添加同租人
        # ['租客入住', {'lease_start': right_start_time, 'lease_end': right_end_time, 'note': 'test'}, '0',
        #  '/v3/tenants/' + str(renter_67) + '/rooms/' + str(rooms_2[1]['id']), 'post', 1],
        # ['添加同租人,co_tenants字段缺失',{},'400000','','post'],
        # ['添加同租人,co_tenants字段缺失', {}, '400000', '', 'post'],

        # 清除测试数据
        ['clear_leases', [renter_66, renter_67, renter_68], '', '', '']
    )
    @ddt.unpack
    def test_02(self, title, param, check_str, url, method, t=0):
        print_write('\n----', title, '---------------')
        if t == 2:
            url = '/v3/leases/' + str(globals()['lease_id'])
        if t == 3:
            url = '/v3/leases/' + str(globals()['lease_id']) + '/frozen'
        if t == 4:
            url = '/v3/leases/' + str(globals()['lease_id']) + '/unfrozen'
        if title == 'clear_leases':
            for renter in param:
                try:
                    leases = get_response(url='/v3/tenants/' + str(renter), do='get',address=config.saas3_api,headers=headers_fe,description='获取租客信息')['result']['lease_list']
                except KeyError:
                    leases = []
                for lease in leases:
                    get_response(url='/v3/leases/' + str(lease['id']), do='delete',address=config.saas3_api,headers=headers_fe,description='退租')
            return
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        try:
            assert check_res(res=res, check_str=check_str)
            if t == 1:
                global lease_id
                lease_id = res['result']['lease_id']
            print_write('----Pass---------------------\n')
        except Exception as err:
            print_write('----Fail---------------------\n')
            print_write(err)
            assert False


if __name__ == "__main__":
    unittest.main()
