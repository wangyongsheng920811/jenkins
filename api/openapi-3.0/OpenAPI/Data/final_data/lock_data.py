from OpenAPI.Data.source_data.source_lock_data import *
from OpenAPI.Lib.get_data_list import *
from OpenAPI.Lib.run_case import *

# 获取门锁状态信息
empty_file('get_lock_info_cmd')
get_lock_info_class = GetDataList(right_get_lock_info, wrong_get_lock_info, [], get_lock_info, 'get')
get_lock_info_cmd = get_lock_info_class.get_all_http_cmd([0], [14001, 15006, 0, 15006])
get_lock_info_cmd.append([get_lock_info, get_lock_info + '-openapi-S-只传uuid', 'get', {'uuid': lock_uuid}, 0, 0])
get_lock_info_cmd.append([get_lock_info, get_lock_info + '-openapi-S-只传home_id', 'get', {'home_id': home_id}, 0, 0])
get_lock_info_cmd.append([get_lock_info, get_lock_info + '-openapi-S-只传home_id和room_id', 'get', {'room_id': room_1001, 'home_id': home_id}, 0, 0])
# write_print_list_dic(get_lock_info_cmd)

# 获取门锁中已添加的密码信息
empty_file('fetch_passwords_cmd')
fetch_passwords_class = GetDataList(right_fetch_passwords, wrong_fetch_passwords, [], fetch_passwords, 'get')
fetch_passwords_cmd = fetch_passwords_class.get_all_http_cmd([0], [14001, 15006, 0, 15006])

# 获取超级管理员密码
empty_file('get_default_password_plaintext_cmd')
get_default_password_plaintext_class = GetDataList(right_get_default_password_plaintext, wrong_get_default_password_plaintext, [], get_default_password_plaintext,
                                                   'get')
get_default_password_plaintext_cmd = get_default_password_plaintext_class.get_all_http_cmd([0], [14001, 15006, 0, 15006])

# 获取动态密码
empty_file('get_dynamic_password_plaintext_cmd')
get_dynamic_password_plaintext_class = GetDataList(right_get_dynamic_password_plaintext, wrong_get_dynamic_password_plaintext, [], get_dynamic_password_plaintext,
                                                   'get')
get_dynamic_password_plaintext_cmd = get_dynamic_password_plaintext_class.get_all_http_cmd([0], [14001, 15006, 0, 15006])

# 添加在线密码
empty_file('add_password_cmd')
add_password_class = GetDataList(right_add_password, wrong_add_password, [], add_password, 'post')
add_password_cmd = add_password_class.get_all_http_cmd([0], [14001, 14001, 15006, 0, 15006, 0, 14001, 14001, 14001, 14001, 422, 14001, 0, 0, 0, 14001, 14001, 14001])
# write_print_list_dic(add_password_cmd)

# 添加激活码密码
empty_file('add_password_without_center_cmd')
add_password_without_center_class = GetDataList(right_add_password_without_center, wrong_add_password_without_center, [], add_password_without_center, 'post')
add_password_without_center_cmd = add_password_without_center_class.get_all_http_cmd([0],
                                                                                     [14001, 14001, 14001, 14001, 15006, 0, 15006, 0, 14001, 14001, 14001, 14001,
                                                                                      14001, 14001, 5039, 14001])
add_password_without_center_cmd.append(
    [add_password_without_center, add_password_without_center + '-openapi-S-CMD为2', 'post',
     {'home_id': home_id, 'uuid': lock_uuid, 'phonenumber': phonenumber, 'name': 'test', 'CMD': 2, 'permission_end': after_s, 'is_send_msg': True}, 0, 0])
add_password_without_center_cmd.append(
    [add_password_without_center, add_password_without_center + '-openapi-S-CMD为3', 'post',
     {'home_id': home_id, 'uuid': lock_uuid, 'phonenumber': phonenumber, 'name': 'test', 'CMD': 3, 'permission_end': after_s, 'is_send_msg': True}, 0, 0])
# write_print_list_dic(add_password_without_center_cmd)

# 修改密码
empty_file('update_password_cmd')
update_password_class = GetDataList(right_update_password, wrong_update_passwrod, [], update_password, 'post')
update_password_cmd = update_password_class.get_all_http_cmd([0],
                                                             [14001, 14001, 14001, 14001, 15006, 0, 15006, 14001, 14001, 14001, 14001, 14001, 14001, 14001, 14001,
                                                              14001, 14001, 14001, 14001, 14001])
# write_print_list_dic(update_password_cmd)

# 修改激活码密码
empty_file('update_password_without_center_cmd')
update_password_without_center_class = GetDataList(right_update_password_without_center, wrong_update_password_without_center, [], update_password_without_center,
                                                   'post')
update_password_without_center_cmd = update_password_without_center_class.get_all_http_cmd([0],
                                                                                           [14001, 14001, 14001, 14001, 14001, 15006, 0, 15006, 14001, 14001, 15006,
                                                                                            14001, 14001, 14001, 14001, 5039, 14001])
# write_print_list_dic(update_password_without_center_cmd)

# 删除密码
empty_file('delete_password_cmd')
delete_password_class = GetDataList(right_delete_password, wrong_delete_password, [], delete_password, 'post')
delete_password_cmd = delete_password_class.get_all_http_cmd([0], [14001, 14001, 15006, 0, 15006, 14001, 5006])

# 冻结密码
empty_file('frozen_password_cmd')
frozen_password_class = GetDataList(right_frozen_password, wrong_frozen_password, [], frozen_password, 'post')
frozen_password_cmd = frozen_password_class.get_all_http_cmd([0], [14001, 14001, 15006, 0, 15006, 14001, 5006])

# 冻结密码
empty_file('unfrozen_password_cmd')
unfrozen_password_class = GetDataList(right_unfrozen_password, wrong_unfrozen_password, [], unfrozen_password, 'post')
unfrozen_password_cmd = unfrozen_password_class.get_all_http_cmd([0], [14001])

# 查询开锁记录
empty_file('get_lock_events_cmd')
get_lock_events_class = GetDataList(right_get_lock_events, wrong_get_lock_events, [], get_lock_events, 'get')
get_lock_events_cmd = get_lock_events_class.get_all_http_cmd([0], [14001, 15006, 0, 15006, 14001, 14001, 14001, 14001, 14001, 0, 14001, 0])

# 统计门锁开门记录数量
empty_file('count_lock_events_cmd')
count_lock_events_class = GetDataList(right_count_lock_events, wrong_count_lock_events, [], count_lock_events, 'get')
count_lock_events_cmd = count_lock_events_class.get_all_http_cmd([0], [14001, 15006, 0, 15006, 14001, 14001, 14001, 14001, 14001, 0, 14001, 14001])
