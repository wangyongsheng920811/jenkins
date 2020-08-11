from API_CG.lib.saas_api_prepare import *

# 租客模块
@ddt.ddt
class Run_setting(unittest.TestCase):
    param_add_ticket = {"subscribe": {"name": "saas_api_test", "phone": "11111111111", "note": "1", "expected_time": week_later_ms, "expected_period": 1},
                        "contact_person": {"name": "saas_api_test", "phone": "11111111111"}, "home_id": home['home_id'], "faults": [{"room_id": rooms[0]['id']}],
                        "service_target": 1}
    vr_resource_id = ''.join(random.sample(string.ascii_letters + string.digits, 8))

    @ddt.data(
        # # 添加租客
        ['获取用户信息', '/v3/user/info', 'get', {}, '0', 'get_client_id'],
        ['获取操作日志', '/v3/operations', 'get', {'start_time': week_before_ms, 'end_time': now_ms}, '0'],
        ['获取操作类型', '/v3/operations/types', 'get', {}, '0'],
        ['获取异常列表', '/v3/exception_device_list', 'get', {'exception_type': 1001,'limit':10,'offset':0}, '0'],
        # ['获取过保修设备列表', '/v3/expired_device_list', 'get', {'exception_type': 100}, '0'],
        ['获取安装工单列表', '/v3/tickets/1', 'get', {}, '0'],
        ['获取维修工单列表', '/v3/tickets/2', 'get', {}, '0'],
        ['获取拆卸工单列表', '/v3/tickets/3', 'get', {}, '0'],
        ['获取重装工单列表', '/v3/tickets/4', 'get', {}, '0'],
        ['新建工单', '/v3/tickets/1', 'post', param_add_ticket, '0', 'add_ticket'],
        ['工单详情', '/v3/tickets/:ticket_id/show', 'get', {'service_type': 1}, '0'],
        ['工单日志', '/v3/tickets/:ticket_id/history', 'get', {}, '0'],
        ['关闭工单', '/v3/tickets/:ticket_id/shut_ticket', 'put', {'description': 'test'}, '0'],
        ['添加角色', '/v3/roles', 'post', {"name": "test", "permission_ids": [], "description": "test"}, '0', 'add_role'],
        ['角色列表', '/v3/roles', 'get', {}, '0'],
        ['角色详情', '/v3/roles/:role_id', 'get', {}, '0'],
        ['修改角色', '/v3/roles/:role_id', 'put', {"name": "update", "permission_ids": [], "description": "description"}, '0'],
        ['删除角色', '/v3/roles/:role_id', 'delete', {}, '0'],
        ['添加员工', '/v3/users', 'post', {"role_id": 101, "name": "test", "telephone": "11067679998", "description": "test", "country_code": "86"}, '0', 'add_user'],
        ['员工列表', '/v3/users', 'get', {}, '0'],
        ['员工详情', '/v3/users/:user_id', 'get', {}, '0'],
        ['修改员工', '/v3/users/:user_id', 'put', {"role_id": 102, "name": "update"}, '0'],
        ['删除员工', '/v3/users/:user_id', 'delete', {}, '0'],
        ['导出员工', '/v3/users', '姓名,手机号码,所属门店,角色', {'download': 'true'}, '0', 'download'],
        ['权限列表', '/v3/permissions', 'get', {}, '0'],
        ['设备报表', '/v3/device_states', 'get', {}, '0'],
        ['设备统计', '/v3/device_states/statistics', 'get', {}, '0'],
        ['报表导出', '/v3/device_states/export', '设备SN', {}, '0', 'download'],
        ['交付统计', '/v3/device_deliver', 'get', {}, '0'],
        ['交付导出', '/v3/device_deliver/export', '交付时间', {}, '0', 'download'],
        ['异常报表', '/v3/devices/exception', 'get', {'exception_type':1006}, '0'],
        ['电表抄表报表', '/v3/reports/elemeter_readed_amount', 'get', {}, '0'],
        ['电表抄表报表导出', '/v3/reports/elemeter_readed_amount/action_export', '房源编号', {}, '0','download'],
        ['水表抄表报表', '/v3/reports/watermeter_readed_amount', 'get', {}, '0'],
        ['水表抄表报表导出', '/v3/reports/watermeter_readed_amount/action_export', '房源编号', {}, '0', 'download'],
        ['用电统计报表', '/v3/homes/rooms/electric_stat', 'get', {'branch_id': 0, 'home_ids': 'all', 'pay_type': 3, 'start_time': week_before_ms, 'end_time': now_ms}, '0'],
        ['用电统计报表导出', '/v3/homes/rooms/electric_stat', '统计开始时间', {'download': 'true', 'branch_id': 0, 'home_ids': 'all', 'pay_type': 3, 'start_time': week_before_ms, 'end_time': now_ms}, '0',
        'download'],
        ['获取商户用电配置', '/v3/clients/elemeter_setting', 'get', {}, '0'],
        ['修改商户用电配置', '/v3/clients/elemeter_setting', 'put', {'pay_type': 2}, '0'],
        ['门店自定义配置列表', '/v3/clients/elemeter_setting/list', 'get', {'type': 1}, '0'],
        ['导出门店自定义配置列表', '/v3/clients/elemeter_setting/export', '门店', {}, '0', 'download'],
        ['获取门店用电配置', '/v3/branches/' + str(branch['id']) + '/elemeter_setting', 'get', {}, '0'],
        ['修改门店用电配置', '/v3/branches/' + str(branch['id']) + '/elemeter_setting', 'put', {'pay_type': 2}, '0'],
        ['房源自定义用电配置列表', '/v3/branches/' + str(branch['id']) + '/elemeter_setting/list', 'get', {'type': 1}, '0'],
        ['导出房源自定义用电配置列表', '/v3/branches/' + str(branch['id']) + '/elemeter_setting/export', '房源地址', {}, '0', 'download'],
        ['获取商户门锁配置', '/v3/lock_setting', 'get', {'type': 'client', 'value': ':client_id'}, '0'],
        ['修改商户门锁配置', '/v3/lock_setting', 'post', {"enable_alarm": False, "value": 91880, "type": "client", "model": "self"}, '0'],
        ['门店自定义门锁配置列表', '/v3/lock_setting/sub_list', 'get', {'type': 'client', 'value': ':client_id'}, '0'],
        ['租客充值记录', '/v3/tenant_orders', 'get', {}, '0'],
        ['租客充值记录导出', '/v3/tenant_orders/export', '订单号', {}, '0', 'download'],
        ['代缴账单查询', '/v3/agency_pay/inst_bills', 'get', {'sub_biz_type':'ELECTRIC'}, '0'],
        ['房源电费信息', '/v3/agency_pay/homes', 'get', {}, '0'],
        ['(银联)获取支付省份列表', '/v3/pay_provinces', 'get', {'platform': '1'}, '0'],
        ['(银联)获取支付地区列表', '/v3/pay_countys', 'get', {'platform': '1', 'parent_id': '1'}, '0'],
        ['(银联)获取支付城市列表', '/v3/pay_citys', 'get', {'platform': '1', 'parent_id': '13'}, '0'],
        ['(银联)获取联行号', '/v3/pay_banks', 'get', {'platform': '1'}, '0'],
        ['(支付宝)获取支付省份列表', '/v3/pay_provinces', 'get', {'platform': '2'}, '0'],
        ['(支付宝)获取支付城市列表', '/v3/pay_citys', 'get', {'platform': '2', 'parent_id': '110000'}, '0'],
        ['(支付宝)获取支付地区列表', '/v3/pay_countys', 'get', {'platform': '2', 'parent_id': '110100'}, '0'],
        ['(支付宝)获取联行号', '/v3/pay_banks', 'get', {'platform': '2', 'keyword': 1}, '0'],
        ['获取支付宝短信验证码', '/v3/ali_pay/send_authcode', 'get', {'phone_num': 18806642362}, '0'],
        ['商户进件信息查询', '/v3/ali_pay/merchant_register_query', 'get', {}, '0'],
        ['商户入驻信息查询', '/v3/ali_pay/merchant_info', 'get', {}, '0'],
        ['商户超管手机号码', '/v3/clients/admin/phone', 'get', {}, '0'],
        ['商户支付账户查询', '/v3/pay_accounts/info', 'get', {}, '0'],
        ['商户入驻信息查询', '/v3/clients/finance', 'get', {}, '0'],
        ['clients/finance', '/v3/clients/finance', 'get', {}, '0'],
        ['(银联)手续费承担方查询', '/v3/audit', 'get', {'audit_type': 1}, '0'],
        ['(支付宝)手续费承担方查询', '/v3/audit', 'get', {'audit_type': 2}, '0'],
        ['获取上一个完成的审核单据数据', '/v3/audit/prev', 'get', {'audit_type': 1, 'branch_id': 0}, '400091'],
        ['手续费承担方设置', '/v3/clients/poundage_type', 'put', {'poundage_type': 1}, '0'],
        ['行业范围查询', '/v3/industry', 'get', {}, '0'],
        ['网商银行账户查询', '/v3/mybank/accounts', 'get', {}, '0'],
        ['库存设备查询', '/v3/device_statistics', 'get', {}, '0'],
        ['产品型号查询', '/v3/device_products', 'get', {}, '0'],
        ['商城订单查询', '/v3/biz_orders', 'get', {}, '0'],
        ['订单详情查询', '/v3/biz_orders/813892892/biz_order_devices', 'get', {}, '0'],
        ['获取代缴账户信息', '/v3/agency_pay/account/info', 'get', {}, '400013'],
        ['查询缴费机构列表', '/v3/agency_pay/institutions', 'get', {'sub_biz_type': 'ELECTRIC'}, '400000'],
        ['绑定VR房源', '/v3/3dnest/home_bind', 'post', {'home_id': 1273371933, 'resource_id': vr_resource_id}, '0'],
        ['VR房源信息', '/v3/vr_home/home_info', 'get', {'resource_id': vr_resource_id}, '0'],
        ['添加同租人', '/v3/leases/1679317398/co_tenants', 'post', {"co_tenants": [{"tenant_id": renter_66, "relationship": "亲属"}]}, '0'],
        ['删除同租人', '/v3/co_tenants/'+str(renter_66), 'delete', {"lease_id": 1679317398}, '0'],
        ['获取门锁信息', '/v3/rooms/1680272836/locks/476336315', 'get', {}, '0'],
        ['修改门锁信息', '/v3/rooms/1680272836/devices/476336315', 'put', {"description": "门锁-0936"}, '0'],
        ['功能码列表', '/v3/rooms/1680272836/locks/476336315/auth_code', 'get', {}, '0'],
        ['开门记录', '/v3/rooms/1680272836/locks/476336315/events', 'get', {'start_time': week_before_ms, 'end_time': now_ms}, '0'],
        ['门锁动态密码', '/v3/rooms/1680272836/locks/476336315/dynamic_passwords', 'get', {}, '0'],
        ['门锁异常记录', '/v3/rooms/1680272836/devices/476336315/exceptions', 'get', {}, '0'],
        ['门锁授权记录', '/v3/rooms/1680272836/locks/476336315/pwds_fps', 'get', {}, '0'],
        ['门锁管理密码', '/v3/rooms/1680272836/locks/476336315/admin_passwords', 'get', {}, '0'],
        ['修改门锁管理密码', '/v3/rooms/1680272836/locks/476336315/admin_passwords', 'get', {"is_default": True, "permission_status": 1, "password": str(get_numbers(6))}, '0'],
        ['新增离线密码', '/v3/rooms/1680272836/locks/476336315/activation_passwords', 'post',
         {"name": "api_tester", "phonenumber": "13267153508", "country_code": "86", "permission_status": 1, "is_send_location": False, "password_type": 2}, '0', 'add_password'],
        ['删除离线密码', '/v3/rooms/1680272836/locks/476336315/passwords/:password_id', 'delete', {}, '0'],

        # ['新增授权', '/v3/rooms/1680272836/locks/476336315/pwds_fps', 'get', {}, '0'],

        # 帮助中心
        ['帮助中心集合', '/v3/tip_class', 'get', {}, '0'],
        ['帮助中心标题', '/v3/tips', 'get', {}, '0'],
        ['帮助中心内容', '/v3/tips/47267711', 'get', {}, '0'],

    )
    @ddt.unpack
    def test_01(self, title, url, method, param, check_str='', t=0, other_param={}):
        print_write('\n----', title, '---------------')
        if ':ticket_id' in url:
            url = url.replace(':ticket_id', str(get_value('ticket_id')))
        if ':role_id' in url:
            url = url.replace(':role_id', str(get_value('role_id')))
        if ':user_id' in url:
            url = url.replace(':user_id', str(get_value('user_id')))
        if ':password_id' in url:
            url = url.replace(':password_id', str(get_value('password_id')))
        if 'value' in param.keys() and param['value'] == ':client_id':
            param['value'] = get_value('client_id')

        if t == 'download':
            res = requests.get(url=config.saas3_api + url, params=param, headers=headers_fe)
            assert res.status_code == 200
            result = res.content.decode(encoding='utf-8', errors='ignore')
            print_write(result)
            assert method in result
            print_write('----Pass---------------------\n')
            return
        if t == 'upload':
            jpg = open(check_str, 'rb')
            file = {'file': ('test_100.jpg', jpg, 'image/png')}
            res = get_response(url=url, do=method, param=param, file=file, headers=headers_fe, print_resp=1, description=title, address=config.saas3_api)
            assert check_res(res=res, check_str='0')
            return

        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1, description=title)
        assert check_res(res=res, check_str=check_str)

        if t == 'add_ticket':
            set_value('ticket_id', res['result']['id'])
        if t == 'add_role':
            set_value('role_id', res['result']['id'])
        if t == 'add_user':
            set_value('user_id', res['result']['id'])
        if t == 'get_client_id':
            set_value('client_id', res['result']['client_id'])
        if t == 'add_password':
            set_value('password_id', res['result']['password_id'])

        print_write('----Pass---------------------\n')


if __name__ == "__main__":
    unittest.main()
