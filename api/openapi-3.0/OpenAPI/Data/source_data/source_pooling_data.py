from OpenAPI.Lib.MyHead import *

'''
公摊接口
/v2/switch_client_pooling_state
/v2/set_client_pooling_area
/v2/switch_home_pooling_state
/v2/set_home_pooling_area
/v2/update_pooling_weight
/v2/get_pooling_weight
'''

# 获取房源公摊设置
right_get_home_setting = [{'home_id': home_id}]
wrong_get_home_setting = {'home_id': ['xxx', True, None]}

# 获取商户设置公摊配置
right_get_client_setting = [{}]
wrong_get_client_setting = {}

# 控制商户公摊状态开启关闭
right_switch_client_pooling_state = [{'pooling_state': '1'}]
wrong_switch_client_pooling_state = {'pooling_state': ['3', True, None]}

# 设置商户公摊模式  1 总电表 2 独立电表
right_set_client_pooling_area = [{'pooling_area': '2'}]
wrong_set_client_pooling_area = {'pooling_area': ['3', True, None]}

# 控制房源公摊状态开启关闭 1 open 2 close
right_switch_home_pooling_state = [{'home_id': home_id, 'pooling_state': '1'}, {'option': {'pooling_state': ['2', 1, 2]}}]
wrong_switch_home_pooling_state = {'home_id': ['xxx', True, None], 'pooling_state': ['3', True, None]}

# 设置房源公摊模式 1 总电表 2 独立电表
right_set_home_pooling_area = [{'home_id': home_id, 'pooling_area': '2'}]
wrong_set_home_pooling_area = {'home_id': ['xxx', True, None], 'pooling_area': ['3', True, None]}

# 设置房源权重
right_update_pooling_weight = [{'home_id': home_id, 'pooling_weight': {room_1001: 3, room_1002: 7}, 'total_pooling_weight': 10}]
wrong_update_pooling_weight = {'home_id': ['xxx', True, None], 'pooling_weight': [{'xxx': 3, room_1002: 7}, 'xxx', None]}

# 获取房源权重
right_get_pooling_weight = [{'home_id': home_id}]
wrong_get_pooling_weight = {'home_id': ['xxx', True, None]}

