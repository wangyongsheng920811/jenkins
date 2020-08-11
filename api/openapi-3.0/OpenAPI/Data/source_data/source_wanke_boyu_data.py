from OpenAPI.Lib.MyHead import *

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
