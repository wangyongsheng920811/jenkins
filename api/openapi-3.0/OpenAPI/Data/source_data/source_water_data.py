from OpenAPI.Lib.MyHead import *

# 设置房间水表付费模式
right_update_room_water_pay_type = [{'room_id': room_1001, 'uuid': water_cold_uuid, 'pay_type': 2}, {'dispensable': ['room_id', 'uuid']}]
wrong_update_room_water_pay_type = {'room_id': ['xxx'], 'uuid': ['xxx'], 'pay_type': [0, 'xxx']}

# 设置房间水表透支额度
right_update_watermeter_overdraft = [{'uuid': water_cold_uuid, 'room_id': room_1001, 'meter_type': 1, 'overdraft': 1000},
                                     {'dispensable': ['uuid', 'room_id', 'meter_type']}]
wrong_update_watermeter_overdraft = {'uuid': ['xxx'], 'room_id': ['xxx'], 'meter_type': [0, 'xxx'], 'overdraft': [10000, 'xxx']}

# 向水表充值
right_watermeter_charge = [{'uuid': water_cold_uuid, 'meter_type': 1, 'room_id': room_1001, 'amount': 100}, {'dispensable': ['uuid', 'meter_type', 'room_id']}]
wrong_watermeter_charge = {'uuid': ['xxx'], 'meter_type': [0, 'xxx'], 'room_id': ['xxx'], 'amount': [-1, 'xxx']}

# 水表剩余水量清零
right_watermeter_charge_reset = [{'uuid': water_cold_uuid, 'meter_type': 1, 'room_id': room_1001}, {'dispensable': ['uuid', 'meter_type', 'room_id']}]
wrong_watermeter_charge_reset = {'uuid': ['xxx'], 'meter_type': [0, 'xxx'], 'room_id': ['xxx']}

# 获取水表充值记录条数
right_count_watermeter_charge_record = [{'uuid': water_cold_uuid, 'room_id': room_1001, 'meter_type': 1, 'start_time': before_ms, 'end_time': after_ms},
                                        {'dispensable': ['uuid', 'room_id', 'meter_type', 'start_time', 'end_time']}]
wrong_count_watermeter_charge_record = {'uuid': ['xxx'], 'room_id': ['xxx'], 'meter_type': [0, 'xxx'], 'start_time': [-1, 'xxx'], 'end_time': [-1, 'xxx']}

# 获取水表充值记录
right_watermeter_charge_records = [
    {'uuid': water_cold_uuid, 'room_id': room_1001, 'meter_type': 1, 'count': 10, 'offset': 0, 'start_time': before_ms, 'end_time': after_ms},
    {'dispensable': ['uuid', 'room_id', 'meter_type', 'count', 'offset', 'start_time', 'end_time']}]
wrong_watermeter_charge_records = {'uuid': ['xxx'], 'room_id': ['xxx'], 'meter_type': [0, 'xxx'], 'count': [-1, 'xxx'], 'offset': [-1, 'xxx'],
                                   'start_time': [-1, 'xxx'], 'end_time': [-1, 'xxx']}

# 绑定水表网关
right_add_water_gateway = [{'home_id': home_id, 'description': '水表采集器描述-测试', 'uuid': water_gw_uuid}, {'dispensable': ['home_id', 'description']}]
wrong_add_water_gateway = {'home_id': ['xxx'], 'uuid': ['xxx']}

# 解绑水表网关
right_del_water_gateway = [{'uuid': water_gw_uuid}, {'dispensable': []}]
wrong_del_water_gateway = {'uuid': ['xxx']}

# 替换水表网关
right_replace_water_gateway = [{'uuid': water_gw_uuid, 'old_uuid': water_gw_uuid}, {'dispensable': []}]
wrong_replace_water_gateway = {'uuid': ['xxx'], 'old_uuid': ['xxx']}

# 绑定水表
right_add_watermeter = [{'room_id': room_1001, 'description': '水表描述-测试', 'uuid': water_cold_uuid, 'gateway_uuid': water_gw_uuid}, {'dispensable': ['room_id', 'description']}]
wrong_add_watermeter = {'room_id': ['xxx'], 'uuid': ['xxx'], 'gateway_uuid': ['xxx']}

# 获取添加水表状态
right_add_watermeter_status = [{'uuid': water_cold_uuid, 'manufactory': 'ym'}, {'dispensable': ['manufactory']}]
wrong_add_watermeter_status = {'uuid': ['xxx'], 'manufactory': ['xxx']}

# 解绑水表
right_del_watermeter = [{'uuid': water_cold_uuid, 'manufactory': 'ym'}, {'dispensable': ['manufactory']}]
wrong_del_watermeter = {'uuid': ['xxx'], 'manufactory': ['xxx']}

# 获取水表采集器信息
right_get_water_gateway_info = [{'uuid': water_gw_uuid}, {'dispensable': []}]
wrong_get_water_gateway_info = {'uuid': ['xxx']}

# 获取水表信息
right_get_watermeter_info = [{'uuid': water_cold_uuid, 'manufactory': 'ym'}, {'dispensable': ['manufactory']}]
wrong_get_watermeter_info = {'uuid': ['xxx'], 'manufactory': ['xxx']}

# 获取水表读数
right_read_watermeter = [{'uuid': water_cold_uuid, 'manufactory': 'ym'}, {'dispensable': ['manufactory']}]
wrong_read_watermeter = {'uuid': ['xxx'], 'manufactory': ['xxx']}

# 查询获取水表读数进度
right_read_watermeter_status = [{'uuid': water_cold_uuid, 'manufactory': 'ym'}, {'dispensable': ['manufactory']}]
wrong_read_watermeter_status = {'uuid': ['xxx'], 'manufactory': ['xxx']}

# 获取水表抄表记录条数
right_count_meter_record = [{'uuid': water_cold_uuid, 'manufactory': 'ym', 'room_id': room_1001, 'type': 2, 'begin': before_ms, 'end': now_ms},
                            {'dispensable': ['uuid', 'manufactory', 'room_id', 'type', 'begin', 'end']}]
wrong_count_meter_record = {'uuid': ['xxx'], 'manufactory': ['xxx'], 'room_id': ['xxx'], 'type': [3, 'xxx'], 'begin': ['xxx', after_ms],
                            'end': ['xxx', before_ms - 3600000 * 24]}

# 获取水表抄表记录
right_get_meter_record = [
    {'uuid': water_cold_uuid, 'manufactory': 'ym', 'room_id': room_1001, 'type': 2, 'count': 10, 'offset': 0, 'begin': before_ms, 'end': now_ms},
    {'dispensable': ['uuid', 'manufactory', 'room_id', 'type', 'count', 'offset', 'begin', 'end']}]
wrong_get_meter_record = {'uuid': ['xxx'], 'manufactory': ['xxx'], 'room_id': ['xxx'], 'type': [3, 'xxx'], 'count': ['xxx'], 'offset': ['xxx'],
                          'begin': ['xxx', after_ms], 'end': ['xxx', before_ms - 3600000 * 24]}
