from OpenAPI.Lib.MyHead import *

# 根据设备sn查询uuid
right_get_device_uuid = [{'sn': elemeter_A4_sn}, {'dispensable': []}]
wrong_get_device_uuid = {'sn': ['180725051013', 'xxx', 123]}

# 获取设备信息
right_get_device_info = [{'uuid': lock_uuid}, {'dispensable': []}]
wrong_get_device_info = {'uuid': ['xxx', 123]}

# 查询设备操作记录
right_search_device_op_log = [{'home_id': home_id, 'room_id': room_1002,
                               'uuid': lock_uuid, 'operator': '18566260535', 'op_id': '12345',
                               'offset': 0, 'count': 20, 'start_time': before_s, 'end_time': now_s},
                              {'dispensable': ['home_id', 'room_id', 'uuid', 'operator', 'op_id', 'offset', 'count',
                                               'start_time', 'end_time']}]
wrong_search_device_op_log = {'home_id': ['xxx'], 'room_id': ['xxx'],
                              'uuid': ['xxx'], 'operator': ['xxx'], 'op_id': ['1111'],
                              'offset': ['xxx', -1], 'count': ['xxx', -1], 'start_time': ['xxx', 111],
                              'end_time': ['xxx', 111]}

# 查询设备操作记录数量
right_count_device_op_log = [{'home_id': home_id, 'room_id': room_1002,
                              'uuid': lock_uuid, 'operator': '18566260535', 'op_id': '12345',
                              'start_time': before_s, 'end_time': now_s},
                             {'dispensable': ['home_id', 'room_id', 'uuid', 'operator', 'op_id', 'start_time',
                                              'end_time']}]
wrong_count_device_op_log = {'home_id': ['xxx'], 'room_id': ['xxx'],
                             'uuid': ['xxx'], 'operator': ['xxx'], 'op_id': ['1111'],
                             'start_time': ['xxx', 111], 'end_time': ['xxx', 111]}

# 刷新设备信号强度
right_refresh_devices_lqi = [{'home_id': home_id, 'type': '-1', 'uuids': [elecollector_uuid, lock_uuid]}, {'dispensable': ['home_id', 'type', 'uuids']}]
wrong_refresh_devices_lqi = {'home_id': ['xxx'], 'type': ['7', 'xxx'], 'uuids': [['xxx'], elecollector_uuid]}

# 获取设备历史异常记录数量
right_device_count_exceptions = [
    {'uuid': lock_uuid, 'start_time': before_ms, 'end_time': now_ms},
    {'dispensable': ['start_time', 'end_time']}]
wrong_device_count_exceptions = {'uuid': ['xxx'], 'start_time': ['xxx', 111],
                                 'end_time': ['xxx', 111]}

# 获取设备历史异常记录
right_device_fetch_exceptions = [
    {'uuid': lock_uuid, 'offset': 0, 'count': 20, 'start_time': before_ms, 'end_time': now_ms},
    {'dispensable': ['offset', 'count', 'start_time', 'end_time']}]
wrong_device_fetch_exceptions = {'uuid': ['xxx'], 'offset': ['xxx', -1], 'count': ['xxx', -1],
                                 'start_time': ['xxx', 111], 'end_time': ['xxx', 111]}

time_ms_20181101 = 1541001600000
time_ms_20181130 = 1543593599000
time_ms_20170101 = 1483200000000
time_ms_20170131 = 1485792000000

# 获取设备历史异常记录数量
right_device_count_exceptions_old = [
    {'uuid': lock_uuid, 'start_time': time_ms_20181101, 'end_time': time_ms_20181130, 'year': 2018, 'month': 11}, {'dispensable': ['start_time', 'end_time']}]
wrong_device_count_exceptions_old = {'uuid': ['xxx'], 'start_time': ['xxx', 111], 'end_time': ['xxx', 111], 'year': ['xxx'], 'month': [0, 13, 'xxx']}

# 获取设备历史异常记录
right_device_fetch_exceptions_old = [
    {'uuid': lock_uuid, 'offset': 0, 'count': 20, 'start_time': time_ms_20181101, 'end_time': time_ms_20181130, 'year': 2018, 'month': 11},
    {'dispensable': ['offset', 'count', 'start_time', 'end_time']}]
wrong_device_fetch_exceptions_old = {'uuid': ['xxx'], 'offset': ['xxx', -1], 'count': ['xxx', -1], 'start_time': ['xxx', 111], 'end_time': ['xxx', 111],
                                     'year': ['xxx'], 'month': [0, 13, 'xxx']}
