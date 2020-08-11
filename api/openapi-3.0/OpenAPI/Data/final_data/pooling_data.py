from OpenAPI.Data.source_data.source_pooling_data import *
from OpenAPI.Lib.get_data_list import *
from OpenAPI.Lib.run_case import *

# 获取房源公摊设置
empty_file('get_home_setting_cmd')
get_home_setting_class = GetDataList(right_get_home_setting, wrong_get_home_setting, [], get_home_setting, 'get')
get_home_setting_cmd = get_home_setting_class.get_all_http_cmd([0], [14001, 15006, 15006, 14001])
# write_print_list_dic(get_home_setting_cmd)

# 获取商户设置公摊配置
empty_file('get_client_setting_cmd')
get_client_setting_class = GetDataList(right_get_client_setting, wrong_get_client_setting, [], get_client_setting, 'get')
get_client_setting_cmd = get_client_setting_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(get_client_setting_cmd)

# 控制商户公摊状态开启关闭
empty_file('switch_client_pooling_state_cmd')
switch_client_pooling_state_class = GetDataList(right_switch_client_pooling_state, wrong_switch_client_pooling_state, [], switch_client_pooling_state, 'post')
switch_client_pooling_state_cmd = switch_client_pooling_state_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(switch_client_pooling_state_cmd)

# 设置商户公摊模式
empty_file('set_client_pooling_area_cmd')
set_client_pooling_area_class = GetDataList(right_set_client_pooling_area, wrong_set_client_pooling_area, [], set_client_pooling_area, 'post')
set_client_pooling_area_cmd = set_client_pooling_area_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(set_client_pooling_area_cmd)

# 控制房源公摊状态开启关闭
empty_file('switch_home_pooling_state_cmd')
switch_home_pooling_state_class = GetDataList(right_switch_home_pooling_state, wrong_switch_home_pooling_state, [], switch_home_pooling_state, 'post')
switch_home_pooling_state_cmd = switch_home_pooling_state_class.get_all_http_cmd([0], [14001, 14001, 15004, 14001, 14001, 14001, 14001, 14001])
# write_print_list_dic(switch_home_pooling_state_cmd)

# 设置房源公摊模式
empty_file('set_home_pooling_area_cmd')
set_home_pooling_area_class = GetDataList(right_set_home_pooling_area, wrong_set_home_pooling_area, [], set_home_pooling_area, 'post')
set_home_pooling_area_cmd = set_home_pooling_area_class.get_all_http_cmd([0], [14001, 14001, 15004])
# write_print_list_dic(set_home_pooling_area_cmd)

# 设置房源权重
empty_file('update_pooling_weight_cmd')
update_pooling_weight_class = GetDataList(right_update_pooling_weight, wrong_update_pooling_weight, [], update_pooling_weight, 'post')
update_pooling_weight_cmd = update_pooling_weight_class.get_all_http_cmd([0], [14001, 14001, 0, 15004, 14001, 14001, 15004, 14001, 14001])
# write_print_list_dic(update_pooling_weight_cmd)

# 获取房源权重
empty_file('get_pooling_weight_cmd')
get_pooling_weight_class = GetDataList(right_get_pooling_weight, wrong_get_pooling_weight, [], get_pooling_weight, 'get')
get_pooling_weight_cmd = get_pooling_weight_class.get_all_http_cmd([0], [14001, 15004, 15004, 14001])
# write_print_list_dic(get_pooling_weight_cmd)
