from OpenAPI.Lib.MyHead import *

# 获取网关信息
right_get_center_info = [{'home_id': home_id, 'uuid': gateway_uuid},
                         {'dispensable': ['home_id', 'uuid']}]
wrong_get_center_info = {'home_id': ['xxx'], 'uuid': ['xxx']}

# 获取房源下所有网关信息
right_get_center_info_arr = [{'home_id': home_id},
                             {'dispensable': ['home_id']}]
wrong_get_center_info_arr = {'home_id': ['xxx']}
