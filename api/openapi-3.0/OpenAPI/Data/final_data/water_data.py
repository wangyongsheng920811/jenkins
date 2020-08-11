from OpenAPI.Data.source_data.source_water_data import *
from OpenAPI.Lib.get_data_list import *
from OpenAPI.Lib.run_case import *

# 设置房间水表付费模式
empty_file('update_room_water_pay_type_cmd')
update_room_water_pay_type_class = GetDataList(right_update_room_water_pay_type, wrong_update_room_water_pay_type, [], update_room_water_pay_type, 'post')
update_room_water_pay_type_cmd = update_room_water_pay_type_class.get_all_http_cmd([0], [14001])

# 设置房间水表透支额度
empty_file('update_watermeter_overdraft_cmd')
update_watermeter_overdraft_class = GetDataList(right_update_watermeter_overdraft, wrong_update_watermeter_overdraft, [], update_watermeter_overdraft, 'post')
update_watermeter_overdraft_cmd = update_watermeter_overdraft_class.get_all_http_cmd([0], [14001])

# 向水表充值
empty_file('watermeter_charge_cmd')
watermeter_charge_class = GetDataList(right_watermeter_charge, wrong_watermeter_charge, [], watermeter_charge, 'post')
watermeter_charge_cmd = watermeter_charge_class.get_all_http_cmd([0], [14001])

# 水表剩余水量清零
empty_file('watermeter_charge_reset_cmd')
watermeter_charge_reset_class = GetDataList(right_watermeter_charge_reset, wrong_watermeter_charge_reset, [], watermeter_charge_reset, 'post')
watermeter_charge_reset_cmd = watermeter_charge_reset_class.get_all_http_cmd([0], [14001])

# 获取水表充值记录条数
empty_file('count_watermeter_charge_record_cmd')
count_watermeter_charge_record_class = GetDataList(right_count_watermeter_charge_record, wrong_count_watermeter_charge_record, [], count_watermeter_charge_record,
                                                   'get')
count_watermeter_charge_record_cmd = count_watermeter_charge_record_class.get_all_http_cmd([0], [14001])

# 获取水表充值记录
empty_file('watermeter_charge_records_cmd')
watermeter_charge_records_class = GetDataList(right_watermeter_charge_records, wrong_watermeter_charge_records, [], watermeter_charge_records, 'get')
watermeter_charge_records_cmd = watermeter_charge_records_class.get_all_http_cmd([0], [14001])

# 绑定水表网关
empty_file('add_water_gateway_cmd')
add_water_gateway_class = GetDataList(right_add_water_gateway, wrong_add_water_gateway, [], add_water_gateway, 'post')
add_water_gateway_cmd = add_water_gateway_class.get_all_http_cmd([0], [14001])

# 解绑水表网关
empty_file('del_water_gateway_cmd')
del_water_gateway_class = GetDataList(right_del_water_gateway, wrong_del_water_gateway, [], del_water_gateway, 'post')
del_water_gateway_cmd = del_water_gateway_class.get_all_http_cmd([0], [14001])

# 替换水表网关
empty_file('replace_water_gateway_cmd')
replace_water_gateway_class = GetDataList(right_replace_water_gateway, wrong_replace_water_gateway, [], replace_water_gateway, 'post')
replace_water_gateway_cmd = replace_water_gateway_class.get_all_http_cmd([0], [14001])

# 绑定水表
empty_file('add_watermeter_cmd')
add_watermeter_class = GetDataList(right_add_watermeter, wrong_add_watermeter, [], add_watermeter, 'post')
add_watermeter_cmd = add_watermeter_class.get_all_http_cmd([0], [14001])

# 获取添加水表状态
empty_file('add_watermeter_status_cmd')
add_watermeter_status_class = GetDataList(right_add_watermeter_status, wrong_add_watermeter_status, [], add_watermeter_status, 'get')
add_watermeter_status_cmd = add_watermeter_status_class.get_all_http_cmd([0], [14001])

# 解绑水表
empty_file('del_watermeter_cmd')
del_watermeter_class = GetDataList(right_del_watermeter, wrong_del_watermeter, [], del_watermeter, 'post')
del_watermeter_cmd = del_watermeter_class.get_all_http_cmd([0], [14001])

# 获取水表网关信息
empty_file('get_water_gateway_info_cmd')
get_water_gateway_info_class = GetDataList(right_get_water_gateway_info, wrong_get_water_gateway_info, [], get_water_gateway_info, 'get')
get_water_gateway_info_cmd = get_water_gateway_info_class.get_all_http_cmd([0], [14001, 14015])
# write_print_list_dic(get_water_gateway_info_cmd)

# 获取水表信息
empty_file('get_watermeter_info_cmd')
get_watermeter_info_class = GetDataList(right_get_watermeter_info, wrong_get_watermeter_info, [], get_watermeter_info, 'get')
get_watermeter_info_cmd = get_watermeter_info_class.get_all_http_cmd([0], [14001, 14015, 0])
get_watermeter_info_cmd.append([get_watermeter_info, get_watermeter_info + '-openapi-S-uuid为sn', 'get', {'uuid': water_hot_sn}, 'info', 0])
# write_print_list_dic(get_watermeter_info_cmd)

# 获取水表读数
empty_file('read_watermeter_cmd')
read_watermeter_class = GetDataList(right_read_watermeter, wrong_read_watermeter, [], read_watermeter, 'get')
read_watermeter_cmd = read_watermeter_class.get_all_http_cmd([0], [14001, 14015, 0])
read_watermeter_cmd.append([read_watermeter, read_watermeter + '-openapi-S-uuid为sn', 'get', {'uuid': water_hot_sn}, 0, 0])
# write_print_list_dic(read_watermeter_cmd)

# 获取水表读数进度
empty_file('read_watermeter_status_cmd')
read_watermeter_status_class = GetDataList(right_read_watermeter_status, wrong_read_watermeter_status, [], read_watermeter_status, 'get')
read_watermeter_status_cmd = read_watermeter_status_class.get_all_http_cmd([0], [14001, 14015, 0])
read_watermeter_status_cmd.append([read_watermeter_status, read_watermeter_status + '-openapi-S-uuid为sn', 'get', {'uuid': water_hot_sn}, 'reading', 0])
# write_print_list_dic(read_watermeter_status_cmd)

# 获取水表抄表记录条数
empty_file('count_meter_record_cmd')
count_meter_record_class = GetDataList(right_count_meter_record, wrong_count_meter_record, [], count_meter_record, 'get')
count_meter_record_cmd = count_meter_record_class.get_all_http_cmd([0], [14015, 0, 0])
count_meter_record_cmd.append(
    [count_meter_record, count_meter_record + '-openapi-S-不传begin和end', 'get', {'uuid': water_hot_uuid, 'manufactory': 'ym', 'room_id': room_1001, 'type': 2},
     'count', 0])
count_meter_record_cmd.append([count_meter_record, count_meter_record + '-openapi-S-uuid为sn', 'get', {'uuid': water_hot_sn}, 'count', 0])
# write_print_list_dic(count_meter_record_cmd)

# 获取水表抄表记录
empty_file('get_meter_record_cmd')
get_meter_record_class = GetDataList(right_get_meter_record, wrong_get_meter_record, [], get_meter_record, 'get')
get_meter_record_cmd = get_meter_record_class.get_all_http_cmd([0], [14015, 0, 0])
get_meter_record_cmd.append([get_meter_record, get_meter_record + '-openapi-S-不传begin和end', 'get',
                             {'uuid': water_hot_uuid, 'manufactory': 'ym', 'room_id': room_1001, 'type': 2, 'count': 10, 'offset': 0}, 'records', 0])
get_meter_record_cmd.append([get_meter_record, get_meter_record + '-openapi-S-uuid为sn', 'get', {'uuid': water_hot_sn}, 'records', 0])
get_meter_record_cmd.append([get_meter_record, get_meter_record + '-openapi-S-uuid为uuid', 'get', {'uuid': water_hot_uuid}, 'records', 0])
get_meter_record_cmd.append([get_meter_record, get_meter_record + '-openapi-S-只传uuid和manufactory', 'get', {'uuid': water_hot_uuid, 'manufactory': 'ym'}, 'records', 0])
get_meter_record_cmd.append([get_meter_record, get_meter_record + '-openapi-S-只传room_id和type', 'get', {'type': 2, 'room_id': room_1001}, 'records', 0])
# write_print_list_dic(get_meter_record_cmd)
