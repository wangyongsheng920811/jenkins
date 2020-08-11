from OpenAPI.Data.source_data.source_gateway_data import *
from OpenAPI.Lib.get_data_list import *
from OpenAPI.Lib.run_case import *

# 获取网关信息
empty_file('get_center_info_cmd')
get_center_info_class = GetDataList(right_get_center_info, wrong_get_center_info, [], get_center_info, 'get')
get_center_info_cmd = get_center_info_class.get_all_http_cmd([0], [0, 15006])
# write_print_list_dic(get_center_info_cmd)

# 获取房源下所有网关信息
empty_file('get_center_info_arr_cmd')
get_center_info_arr_class = GetDataList(right_get_center_info_arr, wrong_get_center_info_arr, [], get_center_info_arr, 'get')
get_center_info_arr_cmd = get_center_info_arr_class.get_all_http_cmd([0], [15006])
