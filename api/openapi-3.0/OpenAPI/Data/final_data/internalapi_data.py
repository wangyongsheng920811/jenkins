from OpenAPI.Data.source_data.source_internalapi_data import *
from OpenAPI.Lib.get_data_list import *
from OpenAPI.Lib.run_case import *

# 获取商户是否存在
empty_file('check_is_client_cmd')
check_is_client_class = GetDataList(right_check_is_client, wrong_check_is_client, [], check_is_client, 'get')
check_is_client_cmd = check_is_client_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(check_is_client_cmd)

# 平台取消权限接口
empty_file('unauth_observer_cmd')
unauth_observer_class = GetDataList(right_unauth_observer, wrong_unauth_observer, [], unauth_observer, 'post')
unauth_observer_cmd = unauth_observer_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(unauth_observer_cmd)

# 平台验证权限接口
empty_file('auth_observer_cmd')
auth_observer_class = GetDataList(right_auth_observer, wrong_auth_observer, [], auth_observer, 'post')
auth_observer_cmd = auth_observer_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(auth_observer_cmd)
