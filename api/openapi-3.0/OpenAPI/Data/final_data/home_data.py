from OpenAPI.Data.source_data.source_home_data import *
from OpenAPI.Lib.get_data_list import *
from OpenAPI.Data.init_data.init_home_data import *

# 初始化房源
# init_home_date()

# 增加房源
empty_file('add_home_cmd')
add_home_class = GetDataList(right_add_home, wrong_add_home, ['home_id', 'home_name'], add_home, 'post')
add_home_cmd = add_home_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(add_home_cmd)

# 更新房源
empty_file('update_home_cmd')
update_home_class = GetDataList(right_update_home, wrong_update_home, [], update_home, 'post')
update_home_cmd = update_home_class.get_all_http_cmd([0], [14001, 15004])

# 删除房源
empty_file('del_home_cmd')
del_home_class = GetDataList(right_del_home, wrong_del_home, [], del_home, 'post')
del_home_cmd = del_home_class.get_all_http_cmd([0], [14001, 15004])
# write_print_list_dic(del_home_cmd)

# 查询房源信息
empty_file('get_home_info_cmd')
get_home_info_class = GetDataList(right_get_home_info, wrong_get_home_info, [], get_home_info, 'get')
get_home_info_cmd = get_home_info_class.get_all_http_cmd([0, 0, 0, 0, 14001], [14001, 0, 0])
# write_print_list_dic(get_home_info_cmd)

# 搜索房源信息
empty_file('search_home_info_cmd')
search_home_class = GetDataList(right_search_home_info, wrong_search_home_info, [], search_home_info, 'get')
search_home_info_cmd = search_home_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(search_home_info_cmd)

# 搜索满足条件的房源数量
empty_file('count_home_info_cmd')
count_home_info_class = GetDataList(right_count_home_info, wrong_count_home_info, [], count_home_info, 'get')
count_home_info_cmd = count_home_info_class.get_all_http_cmd([0], [14001])

# 向房源添加多个房间
empty_file('add_rooms_cmd')
add_rooms_class = GetDataList(right_add_rooms, wrong_add_rooms, ['room_name', 'room_id'], add_rooms, 'post')
add_rooms_cmd = add_rooms_class.get_all_http_cmd([0], [14001, 14001, 15004])
add_rooms_cmd.append([add_rooms, add_rooms + '-openapi-S-不传sp_state', 'post', {'home_id': home_id, 'rooms': [
    {'room_id': get_string(5), 'room_name': get_string(5), 'room_description': get_string(5), 'install_state': '1'},
    {'room_id': get_string(5), 'room_name': get_string(5), 'room_description': get_string(5), 'install_state': 1}]}, 0, 0])
add_rooms_cmd.append([add_rooms, add_rooms + '-openapi-S-不传install_state', 'post', {'home_id': home_id, 'rooms': [
    {'room_id': get_string(5), 'room_name': get_string(5), 'room_description': get_string(5), 'sp_state': '1'},
    {'room_id': get_string(5), 'room_name': get_string(5), 'room_description': get_string(5), 'sp_state': 1}]}, 0, 0])
add_rooms_cmd.append([add_rooms, add_rooms + '-openapi-S-不传sp_state和install_state', 'post', {'home_id': home_id, 'rooms': [
    {'room_id': get_string(5), 'room_name': get_string(5), 'room_description': get_string(5)},
    {'room_id': get_string(5), 'room_name': get_string(5), 'room_description': get_string(5)}]}, 0, 0])
add_rooms_cmd.append([add_rooms, add_rooms + '-openapi-S-sp_state=NULL,install_state=NULL', 'post', {'home_id': home_id, 'rooms': [
    {'room_id': get_string(5), 'room_name': get_string(5), 'room_description': get_string(5), 'install_state': "", 'sp_state': ""},
    {'room_id': get_string(5), 'room_name': get_string(5), 'room_description': get_string(5), 'install_state': None, 'sp_state': None}]}, 0, 0])
add_rooms_cmd.append([add_rooms, add_rooms + '-openapi-F-错误的sp_state=3', 'post', {'home_id': home_id, 'rooms': [
    {'room_id': get_string(5), 'room_name': get_string(5), 'room_description': get_string(5), 'sp_state': '3'},
    {'room_id': get_string(5), 'room_name': get_string(5), 'room_description': get_string(5), 'sp_state': '3'}]}, 14001, 1])
add_rooms_cmd.append([add_rooms, add_rooms + '-openapi-F-错误的sp_state=True', 'post', {'home_id': home_id, 'rooms': [
    {'room_id': get_string(5), 'room_name': get_string(5), 'room_description': get_string(5), 'sp_state': True},
    {'room_id': get_string(5), 'room_name': get_string(5), 'room_description': get_string(5), 'sp_state': True}]}, 14001, 1])
add_rooms_cmd.append([add_rooms, add_rooms + '-openapi-F-错误的install_state=True', 'post', {'home_id': home_id, 'rooms': [
    {'room_id': get_string(5), 'room_name': get_string(5), 'room_description': get_string(5), 'install_state': True},
    {'room_id': get_string(5), 'room_name': get_string(5), 'room_description': get_string(5), 'install_state': True}]}, 14001, 1])
add_rooms_cmd.append([add_rooms, add_rooms + '-openapi-F-错误的install_state=6', 'post', {'home_id': home_id, 'rooms': [
    {'room_id': get_string(5), 'room_name': get_string(5), 'room_description': get_string(5), 'install_state': 6},
    {'room_id': get_string(5), 'room_name': get_string(5), 'room_description': get_string(5), 'install_state': 6}]}, 14001, 1])
# write_print_list_dic(add_rooms_cmd)

# 更新房间信息
empty_file('update_room_cmd')
update_room_class = GetDataList(right_update_room, wrong_update_room, [], update_room, 'post')
update_room_cmd = update_room_class.get_all_http_cmd([0], [14001, 14001, 14001, 15004, 15004])

# 删除房间
empty_file('del_room_cmd')
del_room_class = GetDataList(right_del_room, wrong_del_room, [], del_room, 'post')
del_room_cmd = del_room_class.get_all_http_cmd([0], [14001, 14001, 15004, 15004])
# write_print_list_dic(del_room_cmd)

# 查询房源内设备信息
empty_file('find_home_device_cmd')
find_home_device_class = GetDataList(right_find_home_device, wrong_find_home_device, [], find_home_device, 'post')
find_home_device_cmd = find_home_device_class.get_all_http_cmd([0], [14001, 15004])
# 正确参数
find_home_device_cmd += find_home_device_class.get_http_cmd(find_home_device, 'get', find_home_device_class.get_right_data_list(), [0])
# 错误参数
find_home_device_cmd += find_home_device_class.get_http_cmd(find_home_device, 'get', find_home_device_class.get_wrong_data_list(), [14001, 15004])
# write_print_list_dic(find_home_device_cmd)

# 查询一组房源的设备信息
empty_file('find_home_devices_cmd')
find_home_devices_class = GetDataList(right_find_home_devices, wrong_find_home_devices, [], find_home_devices, 'post')
find_home_devices_cmd = find_home_devices_class.get_all_http_cmd([0], [14001, 15004])
# 正确参数
find_home_devices_cmd += find_home_devices_class.get_http_cmd(find_home_devices, 'get', find_home_devices_class.get_right_data_list(), [0])
# 错误参数
find_home_devices_cmd += find_home_devices_class.get_http_cmd(find_home_devices, 'get', find_home_devices_class.get_wrong_data_list(), [14001, 15004])
# write_print_list_dic(find_home_devices_cmd)
