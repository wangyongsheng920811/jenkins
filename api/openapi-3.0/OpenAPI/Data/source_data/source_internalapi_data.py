from OpenAPI.Lib.MyHead import *
client_id_xx = '48db710db57c3d8a00e56ca3'
phonenumber_xx = '11066660028'

# 获取商户是否存在
right_check_is_client = [{'phone': phone_num}]
wrong_check_is_client = {'phone': ['xxx', True]}

# 平台取消权限接口
right_unauth_observer = [{'userid': phone_num, 'client_id': client_id}]
wrong_unauth_observer = {'userid': ['xxx', True], 'client_id': ['xxx', True]}

# 平台验证权限接口
right_auth_observer = [{'userid': phone_num, 'client_id': client_id, 'callback_uri': callback_uri}]
wrong_auth_observer = {'userid': ['xxx', True], 'client_id': ['xxx', True], 'callback_uri': ['xxx', True]}

# 网商子账户打款
right_notify = [{''}]
