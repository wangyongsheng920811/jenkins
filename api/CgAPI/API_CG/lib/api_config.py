import time, os

class Off_config:

    # 测试环境地址
    saas3_api = 'http://qa-saas.dding.net:7001'
    saas3_manage = 'http://qa-saas.dding.net:7002'
    saas3_openapi = 'http://qa-saas.dding.net:7003/v2'
    saas3_sdk = 'http://qa-saas.dding.net:7005'
    saas2_openapi = 'http://yundingsaastest.dding.net:5001/openapi/v1'
    saas2_api = 'http://yundingsaastest.dding.net:9012'
    passport = 'http://dev-gate.dding.net:7080/login'
    user_fe = ['11067679999', '123456']
    user_manage = ['11066660030', '123456']
    user_install = ['11066660036', '123456']
    lock = {'sn': 'lkjl0011170800347575', 'code': '9994-4409', 'id': '1090680326'}
    gateway = {'sn': 'cnjl0003180400001087', 'id': '1624524893', 'description': '线下网关'}
    amg = {'sn': '180422070297', 'id': '561279608', 'description': '线下amg_0297'}
    a1p = {'sn': '180625100501', 'id': '1510344019', 'description': '线下A1P_0501'}
    a3 = {'sn': '170306020001', 'id': '1012800766', 'description': '线下A3_0001'}

class Qa_config:
    # 测试环境地址
    saas3_api = 'http://qa-saas3.dding.net:7001'
    saas3_manage = 'http://qa-saas3.dding.net:7002'
    saas3_openapi = 'http://qa-saas3.dding.net:7003/v2'
    saas3_sdk = 'http://qa-saas3.dding.net:7005'
    saas2_openapi = 'http://yundingsaastest.dding.net:5001/openapi/v1'
    saas2_api = 'http://yundingsaastest.dding.net:9012'
    passport = 'http://dev-gate.dding.net:7080/login'
    user_fe = ['11067679999', '123456']
    user_manage = ['11066660030', '123456']
    user_install = ['11066660036', '123456']
    lock = {'sn': 'lkjl0011170800347575', 'code': '9994-4409', 'id': '1090680326'}
    gateway = {'sn': 'cnjl0003180400001087', 'id': '1624524893', 'description': '线下网关'}
    amg = {'sn': '180422070297', 'id': '561279608', 'description': '线下amg_0297'}
    a1p = {'sn': '180625100501', 'id': '1510344019', 'description': '线下A1P_0501'}
    a3 = {'sn': '170306020001', 'id': '1012800766', 'description': '线下A3_0001'}

class On_config:
    # 正式环境地址
    saas3_api = 'https://api.dding.net'
    saas3_manage = 'https://manageapi.dding.net'
    saas3_openapi = 'https://saas-openapi.dding.net/v2'
    saas2_openapi = 'http://lockapi.dding.net/openapi/v1'
    saas2_api = 'https://device.dding.net'
    passport = 'https://passport.dding.net/login'
    user_fe = ['18888880000', 'q888888']
    user_manage = ['18806642362', 'q888888']
    user_install = ['15266661111', '123123']
    lock = {'sn': 'lkjl0011170800347575', 'code': '9994-4409', 'id': '2085753724'}
    gateway = {'sn': 'cnjl0009180500542375', 'id': '400534663', 'description': '绑定线上网关'}
    amg = {'sn': '', 'id': '', 'description': ''}
    a1p = {'sn': '', 'id': '', 'description': ''}
    a3 = {'sn': '', 'id': '', 'description': ''}


# 邮件相关变量
smtpserver = 'SMTP.alibaba.com'
sender = 'saas_test@dding.cn'
receiver = ['yaosheng@dding.cn']
password = 'Ddingtest123'
path = os.path.split(os.path.realpath(__file__))[0] + '/test.log'

# 颜色定义
color1 = 'blue'
color2 = 'green'
color3 = 'red'

# 请求头
headers_without_token = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                         'Accept': 'application/json, text/plain, */*',
                         'Content-Type': 'application/json; charset=UTF-8',
                         'Connection': 'keep-alive'}

# 时间相关
now_ms = int(time.time() * 1000)
week_before_ms = now_ms - 3600 * 24 * 7 * 1000
week_later_ms = now_ms + 3600 * 24 * 7 * 1000
month_before_ms = now_ms - 3600 * 24 * 30 * 1000
month_later_ms = now_ms + 3600 * 24 * 30 * 1000

# 密码状态定义
operations = {
    '1': '添加',
    '2': '删除',
    '3': '修改',
    '4': '冻结',
    '5': '解冻'
}
stages = {
    '1': '进行中',
    '2': '失败',
    '3': '成功',
}
states = {
    '1': '不可用',
    '2': '已生效',
    '3': '将生效',
    '4': '已过期',
    '5': '被冻结'
}


# 业务流程变量
branch_A = 'branch_A'
branch_B = 'branch_B'
branch_C = 'branch_C'
branch_D = 'branch_D'
branch_E = 'branch_E'
home_A = 'home_A'
home_B = 'home_B'
home_C = 'home_C'
home_D = 'home_D'
home_E = 'home_E'
house_manager_A = {"role_id": 104, "name": "house_manager_A", "telephone": "19988881111", "description": "测试管家", "country_code": "86"}
