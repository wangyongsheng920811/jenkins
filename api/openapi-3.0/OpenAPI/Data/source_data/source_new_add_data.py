from OpenAPI.Lib.MyHead import *
from OpenAPI.Data.init_data.init_ticket_data import *

'''
蘑菇对接新增三个接口
get_client_setting  获取商户设置
get_home_setting    获取公摊设置
get_elecollector_info   获取采集器信息

线下杨思账号（迁移）
home_id = '5bf512017581fc6191035206'
elecollector_uuid = '08e37f273d6f02c07463528c0f88b3f8'

线上蘑菇对接账号
home_id = '5bf22a8a80269a1504a7c700'
elecollector_uuid = 'd64f62bdc85eace78726d0035265c017'
'''
# 获取采集器信息
right_get_elecollector_info = [{'home_id': home_id, 'uuid': elecollector_uuid}, {'dispensable': ['home_id', 'uuid']}]
wrong_get_elecollector_info = {'home_id': ['xxx', True, None], 'uuid': ['xxx', True, None]}

# 获取公摊设置
right_get_home_setting = [{'home_id': home_id}]
wrong_get_home_setting = {'home_id': ['xxx', True, None]}

# 获取商户设置
right_get_client_setting = [{}]
wrong_get_client_setting = {}

# 获取房间下工单
right_get_ticket_by_room = [{'room_id': room_1001, 'service_type': 2}]
wrong_get_ticket_by_room = {'room_id': ['xxx'], 'service_type': [3, 'xxx']}

# 获取房间安装状态
right_find_home_state = [{'home_id': home_id}]
wrong_find_home_state = {'home_id': ['xxx', True]}

# 添加房间
right_add_room = [{'home_id': home_id, 'room_id': get_string(3), 'room_name': get_string(5), 'room_description': 'add_room_test'},
                  {'dispensable': ['room_description']}]
wrong_add_room = {'home_id': ['xxx', True], 'room_id': [True], 'room_name': [True]}

# 电费充值(含公摊)
right_elemeter_charge_fees_with_pool = [{'home_id': home_id, 'room_id': room_1002, 'uuid': elemeter_A4_uuid, 'fees': 3.3, 'eleprice_way': 1, 'trade_num': 'xxx'},
                                        {'dispensable': ['home_id', 'room_id', 'uuid', 'eleprice_way', 'trade_num']}, {'option': {'eleprice_way': [2]}}]
wrong_elemeter_charge_fees_with_pool = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'fees': ['xxx'], 'eleprice_way': [3, 'xxx'],
                                        'trade_num': ['xxxx']}

# 获取房间电量值
right_room_elemeter_amount = [{'home_id': home_id, 'room_id': room_1002, 'uuid': elemeter_A4_uuid}, {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_room_elemeter_amount = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx']}

# 获取房间电量值
right_get_room_amount = [{'home_id': home_id, 'room_id': room_1002, 'uuid': elemeter_A4_uuid}, {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_get_room_amount = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx']}

# 电量充值(含公摊)
right_elemeter_charge_with_pool = [{'home_id': home_id, 'room_id': room_1002, 'uuid': elemeter_A4_uuid, 'amount': 1.1, 'trade_num': 'xxx'},
                                   {'dispensable': ['home_id', 'room_id', 'uuid', 'trade_num']}]
wrong_elemeter_charge_with_pool = {'home_id': ['xxx', True], 'room_id': ['xxx', True], 'uuid': ['xxx', True], 'amount': ['xxx', True], 'trade_num': ['xxxx', True]}

# 采集房源下的同类型设备读数
right_meter_records_by_homeid = [{'mtoken': access_token_r, 'project_code': project_code, 'meter_type': 3, 'date': before_d}, {'dispensable': ['date']},
                                 {'option': {'meter_type': [1, 2]}}]
wrong_meter_records_by_homeid = {'project_code': ['xxx', True], 'meter_type': ['xxx', 4, True], 'date': [True]}

# 实时采集电表读数
right_realtime_query = [{'mtoken': access_token_r, 'device_id': room_1001_uid + '_3'}]
wrong_realtime_query = {'device_id': ['xxx', True]}

# 跳合闸开关
right_elemeter_control = [{'mtoken': access_token_r, 'device_id': room_1001_uid + '_3', 'control_type': 1}, {'option': {'control_type': [0]}}]
wrong_elemeter_control = {'device_id': ['xxx', True], 'control_type': ['xxx', True, 2]}

# 获取电表电量记录
right_amount_record = [{'home_id': home_id, 'room_id': room_1001, 'uuid': elemeter_A4_uuid, 'offset': 0, 'count': 3, 'begin': before_ms, 'end': now_ms+3*3600000},
                       {'dispensable': ['home_id', 'room_id', 'uuid', 'offset', 'count', 'begin', 'end']}, {'option': {'offset': [5], 'count': [10]}}]
wrong_amount_record = {'home_id': ['xxx', True], 'room_id': ['xxx', True], 'uuid': ['xxx', True], 'offset': ['xxx'], 'count': ['xxx'],
                       'begin': ['xxx', after_ms], 'end': ['xxx', before_ms - 3600000 * 24]}

# 小程序授权和回调地址设置
right_client_setting_by_3rd = [{'event_callback': callback_uri, 'async_callback': callback_uri, 'alipay_auth': 1},
                               {'dispensable': ['event_callback', 'async_callback', 'alipay_auth']}]
wrong_client_setting_by_3rd = {'event_callback': [True], 'async_callback': [True], 'alipay_auth': [0, 3, 'xxx']}

# 获取剩余电量（针对麻雀公寓新增的接口）
right_elemeter_last_power_history_with_pool = [{'home_id': home_id, 'room_id': room_1002, 'uuid': elemeter_A4_uuid}, {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_elemeter_last_power_history_with_pool = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx']}
