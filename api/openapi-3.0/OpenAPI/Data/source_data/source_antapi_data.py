from OpenAPI.Lib.MyHead import *

'''
兼容支付宝分账接口
antapi/v1/lock/info
antapi/v1/lock/password_id
antapi/v1/tenant/info
antapi/v1/tenant/home
antapi/v1/tenant/place_transaction
antapi/v1/elemeter/info
antapi/v1/elemeter/amount_record
antapi/v1/elemeter/charge_record
antapi/v1/watermeter/info
antapi/v1/watermeter/amount_record
'''
# 获取门锁信息
right_antapi_get_lock_info = [{'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid}, {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_antapi_get_lock_info = {'home_id': ['xxx', True, None], 'room_id': ['xxx', True, None], 'uuid': ['xxx', True, None]}

# 获取租客密码id
right_antapi_get_lock_passwordid = [{'phone': phonenumber, 'uuid': lock_uuid}, {'dispensable': ['phone', 'uuid']}]
wrong_antapi_get_lock_passwordid = {'phone': ['10000000000', True, None], 'uuid': ['xxx', True, None]}

# 获取租客信息
right_antapi_get_tenant_info = [{'phone': phonenumber, 'name': 'test'}, {'dispensable': ['name']}]
wrong_antapi_get_tenant_info = {'phone': ['10000000000', True, None], 'name': ['xxx', True, None]}

# 获取租客房源信息
right_antapi_get_tenant_home = [{'phone': phonenumber, 'name': 'test', 'uuid': lock_uuid}, {'dispensable': ['name']}]
wrong_antapi_get_tenant_home = {'phone': ['10000000000', True, None], 'name': ['xxx', True, None], 'uuid': ['xxx', True, None]}

# 发起支付
right_antapi_tenant_place_transaction = [{'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid, 'pay_type': 2, 'pay_openid': 'ewq345ert344edt34', 'fees': 10}]
wrong_antapi_tenant_place_transaction = {'home_id': ['xxx', True, None], 'room_id': ['xxx', True, None], 'uuid': ['xxx', True, None], 'pay_type': [3, True, None],
                                  'pay_openid': ['xxx', True, None], 'fees': [-1, True, None]}

# 获取电表信息
right_antapi_get_elemeter_info = [{'home_id': home_id, 'room_id': room_1001, 'uuid': elemeter_A1_uuid}, {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_antapi_get_elemeter_info = {'home_id': ['xxx', True, None], 'room_id': ['xxx', True, None], 'uuid': ['xxx', True, None]}

# 获取电表电量记录
right_antapi_get_elemeter_amount_record = [
    {'home_id': home_id, 'room_id': room_1001, 'uuid': elemeter_A1_uuid, 'offset': 0, 'count': 20, 'start_time': before_ms, 'end_time': now_ms},
    {'dispensable': ['home_id', 'room_id', 'uuid', 'offset', 'count', 'start_time', 'end_time']}]
wrong_antapi_get_elemeter_amount_record = {'home_id': ['xxx', True, None], 'room_id': ['xxx', True, None], 'uuid': ['xxx', True, None], 'offset': [-1, True, None],
                                    'count': [-1, True, None], 'start_time': ['xxx', True, None], 'end_time': ['xxx', True, None]}

# 获取电表充值记录
right_antapi_get_elemeter_charge_record = [
    {'home_id': home_id, 'room_id': room_1002, 'uuid': elemeter_A4_uuid, 'offset': 0, 'count': 20, 'start_time': before_ms, 'end_time': now_ms},
    {'dispensable': ['home_id', 'room_id', 'uuid', 'offset', 'count', 'start_time', 'end_time']}, {'option': {'offset': [5], 'count': [5]}}]
wrong_antapi_get_elemeter_charge_record = {'home_id': ['xxx', True, None], 'room_id': ['xxx', True, None], 'uuid': ['xxx', True, None], 'offset': [-1, True, None],
                                    'count': [-1, True, None], 'start_time': ['xxx', True, None], 'end_time': ['xxx', True, None]}

# 获取水表基本信息
right_antapi_get_watermeter_info = [{'uuid': water_cold_uuid, 'manufactory': 'ym'}, {'option': {'uuid': [water_hot_uuid]}}]
wrong_antapi_get_watermeter_info = {'uuid': ['xxx', True, None], 'manufactory': ['xxx', True, None]}

# 获取水表水量记录
right_antapi_get_watermeter_amount_record = [{'uuid': water_cold_uuid, 'manufactory': 'ym', 'offset': 0, 'count': 20, 'begin': before_ms, 'end': now_ms},
                                      {'dispensable': ['offset', 'count', 'begin', 'end']}, {'option': {'offset': [5], 'count': [5]}}]
wrong_antapi_get_watermeter_amount_record = {'uuid': ['xxx', True, None], 'manufactory': ['xxx', True, None], 'offset': [-1, True, None], 'count': [-1, True, None],
                                      'begin': ['xxx', True, None], 'end': ['xxx', True, None]}
