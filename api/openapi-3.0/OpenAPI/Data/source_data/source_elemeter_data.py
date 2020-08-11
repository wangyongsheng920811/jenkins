from OpenAPI.Lib.MyHead import *

# 获取电表基本信息
right_get_elemeter_info = [{'home_id': home_id, 'room_id': room_1001, 'uuid': elemeter_A1_uuid}, {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_get_elemeter_info = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx']}

# 设置电表透支额度
right_elemeter_update_overdraft = [
    {'home_id': home_id, 'room_id': room_1001, 'uuid': elemeter_A1_uuid, 'overdraft': 10.1},
    {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_elemeter_update_overdraft = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'overdraft': ['xxx']}

# 电表清零
right_elemeter_reset_by_collector = [{'home_id': home_id, 'room_id': room_1001, 'uuid': elemeter_A1_uuid}, {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_elemeter_reset_by_collector = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx']}

# 设置电表最大功率
right_elemeter_update_max_capacity = [{'home_id': home_id, 'room_id': room_1001, 'uuid': elemeter_A1_uuid, 'capacity': 10.1},
                                      {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_elemeter_update_max_capacity = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'capacity': ['xxx']}

# 获取电表当前用电量
right_elemeter_read = [{'home_id': home_id, 'room_id': room_1002, 'uuid': elemeter_A4_uuid}, {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_elemeter_read = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx']}

# 获取电表历史用电量
right_elemeter_fetch_power_consumption = [{'home_id': home_id, 'room_id': room_1001, 'uuid': elemeter_A1_uuid, 'start_time': before_s, 'end_time': now_s},
                                          {'dispensable': ['home_id', 'room_id', 'uuid', 'start_time', 'end_time']}]
wrong_elemeter_fetch_power_consumption = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'],
                                          'start_time': [123, 'xxx'], 'end_time': [123, 'xxx']}

# 获取房间用电量个数
right_elemeter_count_power_history = [{'home_id': home_id, 'room_id': room_1001, 'uuid': elemeter_A1_uuid, 'start_time': before_s, 'end_time': now_s},
                                      {'dispensable': ['home_id', 'room_id', 'uuid', 'start_time', 'end_time']}]
wrong_elemeter_count_power_history = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'],
                                      'start_time': [123, 'xxx'], 'end_time': [123, 'xxx']}

# 获取电表用电记录
right_elemeter_fetch_power_history = [{'home_id': home_id, 'room_id': room_1001, 'uuid': elemeter_A1_uuid, 'offset': 0, 'count': 5, 'start_time': before_s, 'end_time': after_s},
                                      {'dispensable': ['home_id', 'room_id', 'uuid', 'offset', 'count', 'start_time', 'end_time']}, {'option': {'offset': [3], 'count': [3]}}]
wrong_elemeter_fetch_power_history = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'offset': ['xxx'],
                                      'count': ['xxx'], 'start_time': [123, 'xxx'], 'end_time': [123, 'xxx']}

# 获取含公摊的电表用电记录
right_elemeter_fetch_power_history_with_pool = [
    {'home_id': home_id, 'room_id': room_1002, 'uuid': elemeter_A4_uuid, 'offset': 0, 'count': 5, 'start_time': before_s, 'end_time': after_s},
    {'dispensable': ['home_id', 'room_id', 'uuid', 'offset', 'count', 'start_time', 'end_time']}, {'option': {'offset': [3], 'count': [3]}}]
wrong_elemeter_fetch_power_history_with_pool = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'offset': ['xxx'], 'count': ['xxx'],
                                                'start_time': [123, 'xxx'], 'end_time': [123, 'xxx']}

# 设置电表合闸
right_elemeter_switch_on = [{'home_id': home_id, 'room_id': room_1001, 'uuid': elemeter_A1_uuid}, {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_elemeter_switch_on = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx']}

# 设置电表跳闸
right_elemeter_switch_off = [{'home_id': home_id, 'room_id': room_1001, 'uuid': elemeter_A1_uuid}, {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_elemeter_switch_off = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx']}

# 设置房间强制跳闸状态
right_elemeter_force_open = [{'room_id': room_1001, 'uuid': elemeter_A1_uuid, 'force_open': 1}, {'dispensable': ['room_id', 'uuid']}, {'option': {'force_open': [2]}}]
wrong_elemeter_force_open = {'room_id': ['xxx'], 'uuid': ['xxx'], 'force_open': ['xxx', 3]}

# 发起电表同步
right_elemeter_syn_data = [{'home_id': home_id, 'room_id': room_1001, 'uuid': elemeter_A1_uuid}, {'dispensable': ['home_id', 'room_id', 'uuid']},
                           {'option': {'uuid': [elemeter_A4_uuid]}}]
wrong_elemeter_syn_data = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx']}

# 设置房间付费模式
right_set_room_pay_type = [{'room_id': room_1001, 'uuid': elemeter_A1_uuid, 'pay_type': 1, 'overdraft': 5}, {'dispensable': ['room_id', 'uuid', 'overdraft']},
                           {'option': {'pay_type': [2]}}]
wrong_set_room_pay_type = {'room_id': ['xxx'], 'uuid': ['xxx'], 'pay_type': ['xxx', -1], 'overdraft': ['xxx']}

# 向电表内充电
right_elemeter_charge = [{'home_id': home_id, 'room_id': room_1002, 'uuid': elemeter_A4_uuid, 'amount': 1.1, 'trade_num': get_string(3)},
                         {'dispensable': ['home_id', 'room_id', 'uuid', 'trade_num']}]
wrong_elemeter_charge = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'amount': ['xxx'], 'trade_num': ['xxx']}

# 向电表内充值
right_elemeter_charge_fees = [{'home_id': home_id, 'room_id': room_1002, 'uuid': elemeter_A4_uuid, 'fees': 3.3, 'eleprice_way': 1, 'trade_num': get_string(3)},
                              {'dispensable': ['home_id', 'room_id', 'uuid', 'eleprice_way', 'trade_num']}, {'option': {'eleprice_way': [2]}}]
wrong_elemeter_charge_fees = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'fees': ['xxx'], 'eleprice_way': ['xxx', 3], 'trade_num': ['xxx']}

# 查询电表充值结果
right_elemeter_charge_query = [{'trade_num': 'test', 'serial_no': '18092215463198385'}, {'dispensable': ['trade_num', 'serial_no']}]
wrong_elemeter_charge_query = {'trade_num': ['xxx'], 'serial_no': ['xxx']}

# 获取电表充值记录个数
right_elemeter_count_charge_history = [{'home_id': home_id, 'room_id': room_1002, 'uuid': elemeter_A4_uuid, 'start_time': before_s, 'end_time': now_s},
                                       {'dispensable': ['home_id', 'room_id', 'uuid', 'start_time', 'end_time']}]
wrong_elemeter_count_charge_history = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'start_time': [123, 'xxx'], 'end_time': [123, 'xxx']}

# 获取电表充值记录
right_elemeter_fetch_charge_history = [{'home_id': home_id, 'room_id': room_1002, 'uuid': elemeter_A4_uuid, 'offset': 0, 'count': 5, 'start_time': before_s, 'end_time': after_s},
                                       {'dispensable': ['home_id', 'room_id', 'uuid', 'offset', 'count', 'start_time', 'end_time']}, {'option': {'offset': [3], 'count': [3]}}]
wrong_elemeter_fetch_charge_history = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'offset': ['xxx'],
                                       'count': ['xxx'], 'start_time': [123, 'xxx'], 'end_time': [123, 'xxx']}

# 电表剩余电量清零
right_elemeter_charge_reset = [{'home_id': home_id, 'room_id': room_1001, 'uuid': elemeter_A1_uuid}, {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_elemeter_charge_reset = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx']}

# 设置电价计算方式
right_elemeter_set_eleprice_way = [{'home_id': home_id, 'room_id': room_1001, 'uuid': elemeter_A1_uuid, 'eleprice_way': 1},
                                   {'dispensable': ['home_id', 'room_id', 'uuid']}, {'option': {'eleprice_way': [2]}}]
wrong_elemeter_set_eleprice_way = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'eleprice_way': [4, 'xxx']}

# 获取房间电价及使用的计价方式
right_elemeter_get_price_and_way = [{'home_id': home_id, 'room_id': room_1002, 'uuid': elemeter_A4_uuid}, {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_elemeter_get_price_and_way = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx']}

# 设置房源电价
right_elemeter_set_eleprice_by_home = [{'home_id': home_id, 'eleprice': get_numbers(1)}, {'dispensable': []}]
wrong_elemeter_set_eleprice_by_home = {'home_id': ['xxx'], 'eleprice': ['xxx']}

# 设置商户或房间电价
right_elemeter_set_eleprice = [
    {'home_id': home_id, 'room_id': room_1002, 'uuid': elemeter_A4_uuid, 'room_eleprice': 1, 'client_eleprice': get_numbers(1)},
    {'dispensable': ['home_id', 'room_id', 'uuid', 'room_eleprice', 'client_eleprice']}]
wrong_elemeter_set_eleprice = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'room_eleprice': [-1, 'xxx'], 'client_eleprice': [-1, 'xxx']}

# 获取房间电量值
right_room_elemeter_amount = [{'home_id': home_id, 'room_id': room_1001, 'uuid': elemeter_A1_uuid}, {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_room_elemeter_amount = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx']}
