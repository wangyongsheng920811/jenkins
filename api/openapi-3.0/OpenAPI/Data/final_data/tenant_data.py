from OpenAPI.Data.source_data.source_tenant_data import *
from OpenAPI.Lib.get_data_list import *
from OpenAPI.Lib.run_case import *
from OpenAPI.Data.init_data.init_tenant import *

# 添加租客
empty_file('add_tenant_cmd')
add_tenant_class = GetDataList(right_add_tenant, wrong_add_tenant, [], add_tenant, 'post')
add_tenant_cmd = add_tenant_class.get_all_http_cmd([0],
                                                   [14001, 14001, 14001, 14001, 14001, 15004, 14001, 14001, 14001, 14001, 14001, 14001, 14001, 17007, 14001, 14001,
                                                    17007])
add_tenant_cmd.append([add_tenant, add_tenant + '-openapi-S-传入uuid，不传room_id', 'post',
                       {'uuid': lock_uuid, 'tenant_name': get_string(3), 'tenant_phone': '18566260535', 'start_time': now_ms, 'end_time': after_ms}, 0, 0])
add_tenant_cmd.append([add_tenant, add_tenant + '-openapi-S-传入uuid，传入room_id', 'post',
                       {'room_id': room_1001, 'uuid': lock_uuid, 'tenant_name': get_string(3), 'tenant_phone': '18566260535', 'start_time': now_ms,
                        'end_time': after_ms}, 0, 0])
add_tenant_cmd.append([add_tenant, add_tenant + '-openapi-S-传入错误uuid，正确room_id', 'post',
                       {'room_id': room_1001, 'uuid': get_string(10), 'tenant_name': get_string(3), 'tenant_phone': '18566260535', 'start_time': now_ms,
                        'end_time': after_ms}, 0, 0])
add_tenant_cmd.append([add_tenant, add_tenant + '-openapi-F-传入uuid，传入错误room_id', 'post',
                       {'room_id': get_string(10), 'uuid': lock_uuid, 'tenant_name': get_string(3), 'tenant_phone': '18566260535', 'start_time': now_ms,
                        'end_time': after_ms}, 15004, 0])
# write_print_list_dic(add_tenant_cmd)

# 更新租客
empty_file('update_tenant_cmd')
update_tenant_class = GetDataList(right_update_tenant, wrong_update_tenant, [], update_tenant, 'post')
update_tenant_cmd = update_tenant_class.get_all_http_cmd([0, 0, 0, 0, 0, 14001], [14001, 15904, 15004, 14001, 14001, 14001, 14001, 17007, 14001, 17007, 14001])
update_tenant_cmd.append([update_tenant, update_tenant + '-openapi-S-更新租客名字，号码存在', 'post',
                          {'room_id': room_1001, 'tenant_name': 'xxtt', 'tenant_phone': '18512124545'}, 0, 0])
update_tenant_cmd.append([update_tenant, update_tenant + '-openapi-S-更新租客手机号，号码存在', 'post',
                          {'room_id': room_1001, 'tenant_name': 'test', 'tenant_phone': '18076488260'}, 0, 0])
update_tenant_cmd.append([update_tenant, update_tenant + '-openapi-S-更新租约时间，号码存在', 'post',
                          {'room_id': room_1001, 'tenant_name': 'xxtt', 'tenant_phone': '18566260535', 'start_time': now_ms,
                           'end_time': now_ms + 30 * 24 * 3600 * 1000}, 0, 0])
update_tenant_cmd.append([update_tenant, update_tenant + '-openapi-S-更新租客和租约，号码不存在', 'post',
                          {'room_id': room_1001, 'tenant_name': 'xxttyr', 'tenant_phone': '18567675654'}, 0, 0])
update_tenant_cmd.append([update_tenant, update_tenant + '-openapi-S-只传uuid，不传room_id', 'post',
                          {'uuid': lock_uuid, 'tenant_name': get_string(3), 'tenant_phone': '18566260535'}, 0, 0])
update_tenant_cmd.append([update_tenant, update_tenant + '-openapi-S-传入uuid，传入room_id', 'post',
                          {'uuid': lock_uuid, 'room_id': room_1001, 'tenant_name': get_string(3), 'tenant_phone': '18566260535'}, 0, 0])
update_tenant_cmd.append([update_tenant, update_tenant + '-openapi-S-传错误uuid，传正确room_id', 'post',
                          {'uuid': get_string(10), 'room_id': room_1001, 'tenant_name': get_string(3), 'tenant_phone': '18566260535'}, 0, 0])
update_tenant_cmd.append([update_tenant, update_tenant + '-openapi-F-传错误room_id，传正确uuid', 'post',
                          {'uuid': lock_uuid, 'room_id': get_string(10), 'tenant_name': get_string(3), 'tenant_phone': '18566260535'}, 15004, 0])
# write_print_list_dic(update_tenant_cmd)

# 根据房源id获取租客列表
empty_file('list_tenants_by_homeid_cmd')
list_tenants_by_homeid_class = GetDataList(right_list_tenants_by_homeid, wrong_list_tenants_by_homeid, [], list_tenants_by_homeid, 'get')
list_tenants_by_homeid_cmd = list_tenants_by_homeid_class.get_all_http_cmd([0], [14001, 15006, 15006, 14001])
# write_print_list_dic(list_tenants_by_homeid_cmd)

# 根据room_id获取租客信息
empty_file('get_tenant_by_roomid_cmd')
get_tenant_by_roomid_class = GetDataList(right_get_tenant_by_roomid, wrong_get_tenant_by_roomid, [], get_tenant_by_roomid, 'get')
get_tenant_by_roomid_cmd = get_tenant_by_roomid_class.get_all_http_cmd([0], [14001, 15004, 15004, 14001])
# write_print_list_dic(get_tenant_by_roomid_cmd)

# 删除租客
empty_file('delete_tenant_cmd')
delete_tenant_class = GetDataList(right_delete_tenant, wrong_delete_tenant, [], delete_tenant, 'post')
delete_tenant_cmd = delete_tenant_class.get_all_http_cmd([0], [14001, 15904, 15004, 14001, 14001])
# write_print_list_dic(delete_tenant_cmd)
