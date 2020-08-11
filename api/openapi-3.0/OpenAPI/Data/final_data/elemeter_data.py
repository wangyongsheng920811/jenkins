from OpenAPI.Data.source_data.source_elemeter_data import *
from OpenAPI.Lib.get_data_list import *
from OpenAPI.Lib.run_case import *

# 获取电表信息 ##
empty_file('get_elemeter_info_cmd')
get_elemeter_info_class = GetDataList(right_get_elemeter_info, wrong_get_elemeter_info, [], get_elemeter_info, 'get')
get_elemeter_info_cmd = get_elemeter_info_class.get_all_http_cmd([0], [14001, 15006, 0, 15006])
# write_print_list_dic(get_elemeter_info_cmd)

# 设置电表透支额度 ##
empty_file('elemeter_update_overdraft_cmd')
elemeter_update_overdraft_class = GetDataList(right_elemeter_update_overdraft, wrong_elemeter_update_overdraft, [], elemeter_update_overdraft, 'post')
elemeter_update_overdraft_cmd = elemeter_update_overdraft_class.get_all_http_cmd([0], [14001, 14001, 15006, 0, 15006, 14001])
# write_print_list_dic(elemeter_update_overdraft_cmd)

# 电表清零
empty_file('elemeter_reset_by_collector_cmd')
elemeter_reset_by_collector_class = GetDataList(right_elemeter_reset_by_collector, wrong_elemeter_reset_by_collector, [], elemeter_reset_by_collector, 'post')
elemeter_reset_by_collector_cmd = elemeter_reset_by_collector_class.get_all_http_cmd([0], [14001, 15006, 0, 15006])
# write_print_list_dic(elemeter_reset_by_collector_cmd)

# 设置电表最大功率
empty_file('elemeter_update_max_capacity_cmd')
elemeter_update_max_capacity_class = GetDataList(right_elemeter_update_max_capacity, wrong_elemeter_update_max_capacity, [], elemeter_update_max_capacity, 'post')
elemeter_update_max_capacity_cmd = elemeter_update_max_capacity_class.get_all_http_cmd([0], [14001, 14001, 15006, 0, 15006, 14001])
# write_print_list_dic(elemeter_update_max_capacity_cmd)

# 获取电表当前用电量
empty_file('elemeter_read_cmd')
elemeter_read_class = GetDataList(right_elemeter_read, wrong_elemeter_read, [], elemeter_read, 'post')
elemeter_read_cmd = elemeter_read_class.get_all_http_cmd([0], [14001, 15006, 0, 15006])
# write_print_list_dic(elemeter_read_cmd)

# 获取电表历史用电量
empty_file('elemeter_fetch_power_consumption_cmd')
elemeter_fetch_power_consumption_class = GetDataList(right_elemeter_fetch_power_consumption, wrong_elemeter_fetch_power_consumption, [],
                                                     elemeter_fetch_power_consumption, 'get')
elemeter_fetch_power_consumption_cmd = elemeter_fetch_power_consumption_class.get_all_http_cmd([0], [14001, 15006, 0, 15006, 0, 14001, 0, 14001])

# 获取房间用电记录个数
empty_file('elemeter_count_power_history_cmd')
elemeter_count_power_history_class = GetDataList(right_elemeter_count_power_history, wrong_elemeter_count_power_history, [], elemeter_count_power_history, 'get')
elemeter_count_power_history_cmd = elemeter_count_power_history_class.get_all_http_cmd([0], [14001, 15006, 0, 15006, 0, 14001, 0, 14001])

# 获取电表用电记录
empty_file('elemeter_fetch_power_history_cmd')
elemeter_fetch_power_history_class = GetDataList(right_elemeter_fetch_power_history, wrong_elemeter_fetch_power_history, [], elemeter_fetch_power_history, 'get')
elemeter_fetch_power_history_cmd = elemeter_fetch_power_history_class.get_all_http_cmd([0], [14001, 15006, 0, 15006, 14001, 14001, 0, 14001, 0, 14001])
elemeter_fetch_power_history_cmd.append([elemeter_fetch_power_history, elemeter_fetch_power_history + '-openapi-S-只传uuid', 'get', {'uuid': elemeter_A4_uuid}, 0, 0])
elemeter_fetch_power_history_cmd.append([elemeter_fetch_power_history, elemeter_fetch_power_history + '-openapi-S-只传home_id', 'get', {'home_id': home_id}, 0, 0])
elemeter_fetch_power_history_cmd.append(
    [elemeter_fetch_power_history, elemeter_fetch_power_history + '-openapi-S-只传room_id和home_id', 'get', {'home_id': home_id, 'room_id': room_1002}, 0, 0])
# write_print_list_dic(elemeter_fetch_power_history_cmd)

# 获取含公摊的电表用电记录
empty_file('elemeter_fetch_power_history_with_pool_cmd')
elemeter_fetch_power_history_with_pool_class = GetDataList(right_elemeter_fetch_power_history_with_pool, wrong_elemeter_fetch_power_history_with_pool, [],
                                                           elemeter_fetch_power_history_with_pool, 'get')
elemeter_fetch_power_history_with_pool_cmd = elemeter_fetch_power_history_with_pool_class.get_all_http_cmd([0], [14001, 15006, 0, 15006, 14001, 14001, 0, 14001, 0,
                                                                                                                 14001])
elemeter_fetch_power_history_with_pool_cmd.append(
    [elemeter_fetch_power_history_with_pool, elemeter_fetch_power_history_with_pool + '-openapi-S-只传uuid', 'get', {'uuid': elemeter_A4_uuid}, 0, 0])
# write_print_list_dic(elemeter_fetch_power_history_with_pool_cmd)

# 设置电表合闸
empty_file('elemeter_switch_on_cmd')
elemeter_switch_on_class = GetDataList(right_elemeter_switch_on, wrong_elemeter_switch_on, [], elemeter_switch_on, 'post')
elemeter_switch_on_cmd = elemeter_switch_on_class.get_all_http_cmd([0], [14001, 15006, 0, 15006])

# 设置电表跳闸
empty_file('elemeter_switch_off_cmd')
elemeter_switch_off_class = GetDataList(right_elemeter_switch_off, wrong_elemeter_switch_off, [], elemeter_switch_off, 'post')
elemeter_switch_off_cmd = elemeter_switch_off_class.get_all_http_cmd([0], [14001, 15006, 0, 15006])

# 设置房间强制跳闸状态
empty_file('elemeter_force_open_cmd')
elemeter_force_open_class = GetDataList(right_elemeter_force_open, wrong_elemeter_force_open, [], elemeter_force_open, 'post')
elemeter_force_open_cmd = elemeter_force_open_class.get_all_http_cmd([0], [14001, 14001, 15006, 0, 15006, 14001])

# 发起电表同步
empty_file('elemeter_syn_data_cmd')
elemeter_syn_data_class = GetDataList(right_elemeter_syn_data, wrong_elemeter_syn_data, [], elemeter_syn_data, 'post')
elemeter_syn_data_cmd = elemeter_syn_data_class.get_all_http_cmd([0], [14001, 15006, 0, 15006])

# 设置房间付费模式
empty_file('set_room_pay_type_cmd')
set_room_pay_type_class = GetDataList(right_set_room_pay_type, wrong_set_room_pay_type, [], set_room_pay_type, 'post')
set_room_pay_type_cmd = set_room_pay_type_class.get_all_http_cmd([0], [14001, 0, 15006, 14001, 14001])
# write_print_list_dic(set_room_pay_type_cmd)

# 向电表内充电
empty_file('elemeter_charge_cmd')
elemeter_charge_class = GetDataList(right_elemeter_charge, wrong_elemeter_charge, [], elemeter_charge, 'post')
elemeter_charge_cmd = elemeter_charge_class.get_all_http_cmd([0], [14001, 14001, 15006, 15066, 15006, 14001])
# write_print_list_dic(elemeter_charge_cmd)

# 向电表内充值
empty_file('elemeter_charge_fees_cmd')
elemeter_charge_fees_class = GetDataList(right_elemeter_charge_fees, wrong_elemeter_charge_fees, [], elemeter_charge_fees, 'post')
elemeter_charge_fees_cmd = elemeter_charge_fees_class.get_all_http_cmd([0], [14001, 14001, 15006, 15066, 15006, 14001, 14001])
# write_print_list_dic(elemeter_charge_fees_cmd)

# 查询电表充值结果
empty_file('elemeter_charge_query_cmd')
elemeter_charge_query_class = GetDataList(right_elemeter_charge_query, wrong_elemeter_charge_query, [], elemeter_charge_query, 'get')
elemeter_charge_query_cmd = elemeter_charge_query_class.get_all_http_cmd([0, 0, 0, 14001], [15006, 0])

# 获取电表充值记录个数
empty_file('elemeter_count_charge_history_cmd')
elemeter_count_charge_history_class = GetDataList(right_elemeter_count_charge_history, wrong_elemeter_count_charge_history, [], elemeter_count_charge_history, 'get')
elemeter_count_charge_history_cmd = elemeter_count_charge_history_class.get_all_http_cmd([0], [14001, 15006, 0, 15006, 0, 14001, 14001, 14001])

# 获取电表充值记录
empty_file('elemeter_fetch_charge_history_cmd')
elemeter_fetch_charge_history_class = GetDataList(right_elemeter_fetch_charge_history, wrong_elemeter_fetch_charge_history, [], elemeter_fetch_charge_history, 'get')
elemeter_fetch_charge_history_cmd = elemeter_fetch_charge_history_class.get_all_http_cmd([0], [14001, 15006, 15006, 15006, 14001, 14001, 0, 14001, 0, 14001])
# write_print_list_dic(elemeter_fetch_charge_history_cmd)

# 电表剩余电量清零
empty_file('elemeter_charge_reset_cmd')
elemeter_charge_reset_class = GetDataList(right_elemeter_charge_reset, wrong_elemeter_charge_reset, [], elemeter_charge_reset, 'post')
elemeter_charge_reset_cmd = elemeter_charge_reset_class.get_all_http_cmd([0], [14001, 15006, 0, 15006])

# 设置电价计算方式
empty_file('elemeter_set_eleprice_way_cmd')
elemeter_set_eleprice_way_class = GetDataList(right_elemeter_set_eleprice_way, wrong_elemeter_set_eleprice_way, [], elemeter_set_eleprice_way, 'post')
elemeter_set_eleprice_way_cmd = elemeter_set_eleprice_way_class.get_all_http_cmd([0], [14001, 14001, 15006, 0, 15006, 14001, 14001])
# write_print_list_dic(elemeter_set_eleprice_way_cmd)

# 获取房间电价及使用的计价方式
empty_file('elemeter_get_price_and_way_cmd')
elemeter_get_price_and_way_class = GetDataList(right_elemeter_get_price_and_way, wrong_elemeter_get_price_and_way, [], elemeter_get_price_and_way, 'get')
elemeter_get_price_and_way_cmd = elemeter_get_price_and_way_class.get_all_http_cmd([0], [14001])

# 设置房源电价
empty_file('elemeter_set_eleprice_by_home_cmd')
elemeter_set_eleprice_by_home_class = GetDataList(right_elemeter_set_eleprice_by_home, wrong_elemeter_set_eleprice_by_home, [], elemeter_set_eleprice_by_home, 'post')
elemeter_set_eleprice_by_home_cmd = elemeter_set_eleprice_by_home_class.get_all_http_cmd([0], [14001])

# 设置商户或房间电价
empty_file('elemeter_set_eleprice_cmd')
elemeter_set_eleprice_class = GetDataList(right_elemeter_set_eleprice, wrong_elemeter_set_eleprice, [], elemeter_set_eleprice, 'post')
elemeter_set_eleprice_cmd = elemeter_set_eleprice_class.get_all_http_cmd([0], [14001])

# 获取房间电量值
empty_file('room_elemeter_amount_cmd')
room_elemeter_amount_class = GetDataList(right_room_elemeter_amount, wrong_room_elemeter_amount, [], room_elemeter_amount, 'get')
room_elemeter_amount_cmd = room_elemeter_amount_class.get_all_http_cmd([0], [0, 0, 15006])
# write_print_list_dic(room_elemeter_amount_cmd)
