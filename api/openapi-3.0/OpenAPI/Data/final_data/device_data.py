from OpenAPI.Data.source_data.source_device_data import *
from OpenAPI.Lib.get_data_list import *
from OpenAPI.Lib.run_case import *

# 获取设备信息
empty_file('get_device_uuid_cmd')
get_device_uuid_class = GetDataList(right_get_device_uuid, wrong_get_device_uuid, [], get_device_uuid, 'get')
get_device_uuid_cmd = get_device_uuid_class.get_all_http_cmd([0], [14001, 15006, 15006, 15006])
# write_print_list_dic(get_device_uuid_cmd)

# 获取设备信息
empty_file('get_device_info_cmd')
get_device_info_class = GetDataList(right_get_device_info, wrong_get_device_info, [], get_device_info, 'get')
get_device_info_cmd = get_device_info_class.get_all_http_cmd([0], [14001, 15006, 15006])
# write_print_list_dic(get_device_info_cmd)

# 查询设备操作记录
empty_file('search_device_op_log_cmd')
search_device_op_log_class = GetDataList(right_search_device_op_log, wrong_search_device_op_log, [], search_device_op_log, 'get')
search_device_op_log_cmd = search_device_op_log_class.get_all_http_cmd([0], [14001])
search_device_op_log_cmd.append([search_device_op_log, search_device_op_log + '-openapi-S-只有uuid', 'get', {'uuid': elemeter_A4_uuid}, 0, 0])
# write_print_list_dic(search_device_op_log_cmd)


# 查询设备操作记录数量
empty_file('count_device_op_log_cmd')
count_device_op_log_class = GetDataList(right_count_device_op_log, wrong_count_device_op_log, [], count_device_op_log, 'get')
count_device_op_log_cmd = count_device_op_log_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(count_device_op_log_cmd)

# 刷新设备信号强度
empty_file('refresh_devices_lqi_cmd')
refresh_devices_lqi_class = GetDataList(right_refresh_devices_lqi, wrong_refresh_devices_lqi, [], refresh_devices_lqi, 'post')
refresh_devices_lqi_cmd = refresh_devices_lqi_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(refresh_devices_lqi_cmd)

# 获取设备历史异常记录数量
empty_file('device_count_exceptions_cmd')
device_count_exceptions_class = GetDataList(right_device_count_exceptions, wrong_device_count_exceptions, [], device_count_exceptions, 'get')
device_count_exceptions_cmd = device_count_exceptions_class.get_all_http_cmd([0], [14001, 15006, 14001, 0, 14001, 14001])
# write_print_list_dic(device_count_exceptions_cmd)

# 获取设备历史异常记录
empty_file('device_fetch_exceptions_cmd')
device_fetch_exceptions_class = GetDataList(right_device_fetch_exceptions, wrong_device_fetch_exceptions, [], device_fetch_exceptions, 'get')
device_fetch_exceptions_cmd = device_fetch_exceptions_class.get_all_http_cmd([0], [14001, 15006, 14001, 14001, 14001, 14001, 14001, 0, 14001, 14001])
# write_print_list_dic(device_fetch_exceptions_cmd)

# 获取设备历史异常记录数量-三个月前
empty_file('device_count_exceptions_old_cmd')
device_count_exceptions_old_class = GetDataList(right_device_count_exceptions_old, wrong_device_count_exceptions_old, [], device_count_exceptions_old, 'get')
device_count_exceptions_old_cmd = device_count_exceptions_old_class.get_all_http_cmd([0], [14001, 15006, 14001, 0, 14001, 14001])
# write_print_list_dic(device_count_exceptions_old_cmd)

# 获取设备历史异常记录-三个月前
empty_file('device_fetch_exceptions_old_cmd')
device_fetch_exceptions_old_class = GetDataList(right_device_fetch_exceptions_old, wrong_device_fetch_exceptions_old, [], device_fetch_exceptions_old, 'get')
device_fetch_exceptions_old_cmd = device_fetch_exceptions_old_class.get_all_http_cmd([0], [14001, 15006, 14001, 14001, 14001, 14001, 14001, 0, 14001, 14001])
# write_print_list_dic(device_fetch_exceptions_old_cmd)
