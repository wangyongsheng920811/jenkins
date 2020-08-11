from OpenAPI.Lib.MyHead import *

# 获取门锁状态信息
right_get_lock_info = [{'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid}, {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_get_lock_info = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx']}

# 获取门锁中已添加的密码信息
right_fetch_passwords = [{'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid}, {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_fetch_passwords = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx']}

# 获取超级管理员密码
right_get_default_password_plaintext = [{'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid}, {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_get_default_password_plaintext = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx']}

# 获取动态密码
right_get_dynamic_password_plaintext = [{'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid}, {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_get_dynamic_password_plaintext = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx']}

# 添加在线密码
right_add_password = [
    {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid, 'phonenumber': phonenumber, 'is_default': 0, 'is_send_location': True, 'password': str(get_numbers()),
     'encrypted_password': encrypted_password_123456, 'name': get_string(4), 'permission_begin': now_s, 'permission_end': after_s},
    {'dispensable': ['home_id', 'room_id', 'uuid', 'is_send_location', 'password', 'encrypted_password', 'permission_begin', 'permission_end', 'phonenumber', 'name']}]
wrong_add_password = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'phonenumber': ['123'], 'is_default': [2, 'xxx'], 'is_send_location': ['xxx', 123],
                      'password': ['123', 'xxxxxx'], 'encrypted_password': ['123', 'xxxxxx'], 'name': [True], 'permission_begin': [123, 'xxx'], 'permission_end': [123, 'xxx']}

# 添加激活码密码
right_add_password_without_center = [
    {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid, 'phonenumber': phonenumber, 'CMD': 1, 'name': get_string(4), 'is_send_msg': True,
     'is_send_location': True, 'permission_end': after_s}, {'dispensable': ['home_id', 'room_id', 'uuid', 'is_send_msg', 'is_send_location', 'phonenumber', 'name']}]
wrong_add_password_without_center = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'phonenumber': ['123'], 'CMD': [4, 'xxx'], 'is_send_msg': ['xxx', 123],
                                     'name': [True], 'is_send_location': ['xxx', 123], 'permission_end': [123, 'xxx']}

# 修改密码
right_update_password = [
    {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid, 'password_id': 1045, 'password': str(get_numbers()),
     'encrypted_password': encrypted_password_123456, 'is_send_location': True, 'phonenumber': phonenumber, 'name': get_string(4), 'permission_begin': (now_s + 60), 'permission_end': (after_s + 60)},
    {'dispensable': ['home_id', 'room_id', 'uuid', 'password', 'encrypted_password', 'is_send_location', 'phonenumber', 'name']}]
wrong_update_passwrod = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'password_id': ['xxx', 123], 'password': ['123', 'xxxxxx'],
                         'name': [True], 'encrypted_password': ['123', 'xxxxxx'], 'is_send_location': ['xxx', 123], 'phonenumber': ['123'], 'permission_begin': [123, 'xxx'], 'permission_end': [123, 'xxx']}

# 修改激活码密码
right_update_password_without_center = [
    {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid, 'phonenumber': phonenumber, 'password_id': 3046, 'name': get_string(4), 'is_send_msg': True,
     'is_send_location': True, 'permission_end': (after_s + 3600 * 24)}, {'dispensable': ['home_id', 'room_id', 'uuid', 'is_send_msg', 'is_send_location']}]
wrong_update_password_without_center = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'phonenumber': ['123'], 'password_id': ['xxx', 123],
                                        'name': [True], 'is_send_msg': ['xxx', 123], 'is_send_location': ['xxx', 123], 'permission_end': [123, 'xxx']}

# 删除密码
right_delete_password = [{'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid, 'password_id': 1036}, {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_delete_password = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'password_id': ['xxx', 123]}

# 冻结密码
right_frozen_password = [{'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid, 'password_id': 1036}, {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_frozen_password = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'password_id': ['xxx', 123]}

# 解冻密码
right_unfrozen_password = [{'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid, 'password_id': 1016}, {'dispensable': ['home_id', 'room_id', 'uuid']}]
wrong_unfrozen_password = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'password_id': ['xxx', 123]}

# 查询门锁开门记录
right_get_lock_events = [{'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid, 'offset': 0, 'count': 20, 'start_time': before_s, 'end_time': now_s},
                         {'dispensable': ['home_id', 'room_id', 'uuid', 'offset', 'count', 'start_time', 'end_time']}]
wrong_get_lock_events = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'offset': ['xxx', -1], 'count': ['xxx', -1], 'start_time': ['xxx', 111],
                         'end_time': ['xxx', 111]}

# 统计门锁开门记录数量
right_count_lock_events = [{'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid, 'start_time': before_s, 'end_time': now_s},
                           {'dispensable': ['home_id', 'room_id', 'uuid', 'start_time', 'end_time']}]
wrong_count_lock_events = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'start_time': ['xxx', 111],
                           'end_time': ['xxx', 111]}

# 添加在线密码（如果有装修密码会删除）
right_add_password_with_del_decorate_pwd = [
    {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid, 'phonenumber': phonenumber, 'is_default': 0, 'is_send_location': True, 'password': str(get_numbers()),
     'name': get_string(4), 'permission_begin': now_s, 'permission_end': after_s},
    {'dispensable': ['home_id', 'room_id', 'uuid', 'is_send_location', 'password', 'permission_begin', 'permission_end', 'phonenumber', 'name']}]
wrong_add_password_with_del_decorate_pwd = {'home_id': ['xxx'], 'room_id': ['xxx'], 'uuid': ['xxx'], 'phonenumber': ['123'], 'is_default': [2, 'xxx'], 'is_send_location': ['xxx', 123],
                      'password': ['123', 'xxxxxx'], 'name': [True], 'permission_begin': [123, 'xxx'], 'permission_end': [123, 'xxx']}
