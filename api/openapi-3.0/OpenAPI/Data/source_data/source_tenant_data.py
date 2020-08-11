from OpenAPI.Lib.MyHead import *

'''
租客接口
/v2/add_tenant
/v2/update_tenant
/v2/list_tenants_by_homeid
/v2/get_tenant_by_roomid
/v2/delete_tenant
'''

# 添加租客
right_add_tenant = [{'room_id': room_1001, 'tenant_name': 'test', 'tenant_phone': '18566260535', 'start_time': now_ms, 'end_time': after_ms},
                    {'dispensable': []}]
wrong_add_tenant = {'room_id': ['xxx', True, None], 'tenant_name': [True, None], 'tenant_phone': ['xxx', True, None], 'start_time': [after_ms+1, 'xxx', None],
                    'end_time': [before_ms, 'xxx', None]}

# 更新租客
right_update_tenant = [{'room_id': room_1001, 'tenant_name': get_string(5), 'tenant_phone': '18076488260', 'start_time': now_ms, 'end_time': after_ms},
                       {'dispensable': ['tenant_name', 'tenant_phone', 'start_time', 'end_time']}]
wrong_update_tenant = {'room_id': [room_1003, 'xxx', True], 'tenant_name': [True], 'tenant_phone': ['xxx', True],
                       'start_time': [after_ms + 1, 'xxx'], 'end_time': [before_ms, 'xxx']}

# 根据房源id获取租客列表
right_list_tenants_by_homeid = [{'home_id': home_id}, {'dispensable': []}]
wrong_list_tenants_by_homeid = {'home_id': ['xxx', True, None]}

# 根据room_id获取租客信息
right_get_tenant_by_roomid = [{'room_id': room_1001}, {'dispensable': []}]
wrong_get_tenant_by_roomid = {'room_id': ['xxx', True, None]}

# 删除租客
right_delete_tenant = [{'room_id': room_1001}]
wrong_delete_tenant = {'room_id': [room_1003, 'xxx', True, None]}


