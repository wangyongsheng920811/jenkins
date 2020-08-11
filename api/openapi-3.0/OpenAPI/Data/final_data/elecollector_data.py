from OpenAPI.Data.source_data.source_elecollector_data import *
from OpenAPI.Lib.get_data_list import *
from OpenAPI.Lib.run_case import *

# 获取房源内所有采集器信息
empty_file('get_elecollector_info_arr_cmd')
get_elecollector_info_arr_class = GetDataList(right_get_elecollector_info_arr, wrong_get_elecollector_info_arr, [], get_elecollector_info_arr, 'get')
get_elecollector_info_arr_cmd = get_elecollector_info_arr_class.get_all_http_cmd([0], [14001, 15006, 15006])
# write_print_list_dic(get_elecollector_info_arr_cmd)
