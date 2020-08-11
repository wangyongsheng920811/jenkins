from OpenAPI.Lib.MyHead import *

# 增加房源
right_add_home = [{'home_type': 2, 'country': '中国', 'city': '深圳', 'zone': '南山区',
                   'location': '深南大道', 'block': '深南花园', 'home_id': 'home_bb',
                   'home_name': 'test01', 'description': '深南花园描述'},
                  {'dispensable': ['home_type', 'description']}]
wrong_add_home = {'home_type': [3, 'test']}

# 更新房源
right_update_home = [{'home_id': home_id_2, 'location': get_string(5), 'home_name': 'OpenAPI2',
                      'description': get_string(10)},
                     {'dispensable': ['location', 'home_name', 'description']}]
wrong_update_home = {'home_id': ['abababa']}

# 删除房源
right_del_home = [{'home_id': 'xxx'}]
wrong_del_home = {'home_id': ['hello']}

# 查询房源
right_get_home_info = [{'home_id': home_id, 'uuid': elemeter_A4_uuid, 'manufactory': 'ym'},
                       {'dispensable': ['home_id', 'uuid', 'manufactory']}]
wrong_get_home_info = {'home_id': ['xxx'], 'uuid': ['xxx'], 'manufactory': ['xxx']}

# 查询房源内设备信息
right_find_home_device = [{'home_id': home_id}, {'dispensable': []}]
wrong_find_home_device = {'home_id': ['xxx']}

# 查询一组房源的设备信息
right_find_home_devices = [{'home_id': [home_id_2, home_id]}]
wrong_find_home_devices = {'home_id': ['xxx', ['xxx', 'sss']]}

# 搜索房源信息
right_search_home_info = [{'home_name': 'OpenAPI', 'city': '北京市', 'zone': '东城区', 'block': '测试', 'location': '测试', 'offset': 0, 'count': 20},
                          {'dispensable': ['home_name', 'city', 'zone', 'block', 'location', 'offset', 'count']}, {'option': {'offset': [5], 'count': [5]}}]
wrong_search_home_info = {'offset': [-1, 'test'], 'count': [-1, 'test']}

# 查询满足条件房源数量
right_count_home_info = [{'home_name': 'OpenAPI', 'city': '北京市', 'zone': '东城区', 'block': '测试', 'location': '测试'},
                         {'dispensable': ['home_name', 'city', 'zone', 'block', 'location']}]
wrong_count_home_info = {}


def get_room_basic():
    room_basic = {'room_id': get_string(5), 'room_name': get_string(5), 'room_description': get_string(3), 'sp_state': '1', 'install_state': '1'}
    return room_basic


# 向房源添加多个房间
right_add_rooms = [{'home_id': home_id, 'rooms': [get_room_basic(), get_room_basic()]}, {'dispensable': []}]
wrong_add_rooms = {'home_id': ['xxx']}

# 更新房间
right_update_room = [
    {'home_id': home_id, 'room_id': room_1003, 'room_name': get_string(4), 'room_description': get_string(4)},
    {'dispensable': ['room_description']}]
wrong_update_room = {'home_id': ['xxx'], 'room_id': ['xxx']}

# 删除房间
right_del_room = [{'home_id': home_id, 'room_id': '2OH'},
                  {'dispensable': []}]
wrong_del_room = {'home_id': ['xxx'], 'room_id': ['xxx']}
