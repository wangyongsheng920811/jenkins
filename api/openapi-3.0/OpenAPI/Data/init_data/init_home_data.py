from OpenAPI.Lib.MyHead import *
from OpenAPI.Lib.run_case import *


# 获取id（home_list里的第一个,非OpenAPI和OpenAPI2）
# home_id为按照返回结果，返回非home_id和home_id2的第一个，room_id为传入home_id里的非公区id
def get_id(flag='home_id', home_id_=home_id):
    ret_id = ''
    search_home_cmd = [search_home_info, 'search_home-init', 'get', {}]
    add_home_cmd = [add_home, 'add_home-init', 'post',
                    {'home_type': 2, 'country': '中国', 'city': '深圳', 'zone': '南山区', 'location': '深南大道', 'block': '深南花园', 'home_id': 'test01_'+get_string(3),
                     'home_name': 'test01_'+get_string(3), 'description': '深南花园描述'}]
    ret_search_home = run_case(search_home_cmd[0], search_home_cmd[1], search_home_cmd[2], search_home_cmd[3], False)
    for tmp in ret_search_home['home_list']:
        if flag == 'home_id':
            # 排除测试房源和房源名称包含test_01的房源
            if tmp['home_id'] not in [home_id, home_id_2]:
                # 房源存在设备，继续
                if tmp['devices']:
                    continue
                ret_id = tmp['home_id']
                break
        elif flag == 'room_id':
            if tmp['home_id'] == home_id_:
                for tmp_room in tmp['rooms']:
                    # 排除公区和测试用的room_id
                    if tmp_room['room_id'] != home_id_ and tmp_room['room_id'] not in [room_1001, room_1002, room_1003]:
                        # 如果房间存在绑定设备，继续
                        if tmp_room['sp_state'] == 2:
                            continue
                        ret_id = tmp_room['room_id']
                        break
    if not ret_id:
        if flag == 'home_id':
            tmp_home_id = add_home_test(1)
            print('tmp_home_id: ', tmp_home_id)
            if tmp_home_id:
                ret_id = tmp_home_id[0]
        elif flag == 'room_id':
            tmp_room_id = add_room_test(home_id_, 1)
            print('home_id: ', home_id_)
            print('tmp_room_id: ', tmp_room_id)
            if tmp_room_id:
                ret_id = tmp_room_id[0]
    return ret_id


# 初始化删除房源接口
def init_del_home():
    del_cmd_num = 3
    cant_del_home = 0
    add_home_cmd = [add_home, 'add_home-init', 'post',
                    {'home_type': 2, 'country': '中国', 'city': '深圳', 'zone': '南山区', 'location': '深南大道', 'block': '深南花园', 'home_id': 'xxx', 'home_name': 'xxx',
                     'description': '深南花园描述'}]
    search_home_cmd = [search_home_info, 'add_home-init', 'get', {}]
    ret_search_home = run_case(search_home_cmd[0], search_home_cmd[1], search_home_cmd[2], search_home_cmd[3], False)
    for tmp in ret_search_home['home_list']:
        if tmp['home_name'] in ['OpenAPI', 'OpenAPI2'] or tmp['devices'] != []:
            cant_del_home += 1
    if len(ret_search_home['home_list']) - cant_del_home < del_cmd_num:
        for i in range(del_cmd_num - len(ret_search_home['home_list']) + cant_del_home):
            add_home_cmd[3]['home_id'] = 'test01_' + get_string(3)
            add_home_cmd[3]['home_name'] = add_home_cmd[3]['home_id']
            ret_add_home = run_case(add_home_cmd[0], add_home_cmd[1], add_home_cmd[2], add_home_cmd[3], False)
    print("初始化删除房源完成")
    return


# 初始化删除房间接口
# 如果房源下去除必须的房间后小于测试用房间数，则补齐
def init_del_room():
    del_cmd_num = 5
    add_rooms_cmd = [add_rooms, 'add_rooms-init', 'post', {'home_id': home_id, 'rooms': [
        {'room_id': get_string(3), 'room_name': get_string(3), 'room_description': '测试', 'sp_state': '1', 'install_state': '1'}]}]
    search_home_cmd = [search_home_info, 'search_home_info-init', 'get', {}]
    ret_search_home = run_case(search_home_cmd[0], search_home_cmd[1], search_home_cmd[2], search_home_cmd[3], False)
    for tmp_home in ret_search_home['home_list']:
        if tmp_home['home_name'] == 'OpenAPI':
            if len(tmp_home['rooms']) - 4 < del_cmd_num:
                for i in range(del_cmd_num - len(tmp_home['rooms']) + 4):
                    add_rooms_cmd[3]['rooms'][0]['room_id'] = add_rooms_cmd[3]['rooms'][0]['room_name'] = get_string(3)
                    ret_add_rooms = run_case(add_rooms_cmd[0], add_rooms_cmd[1], add_rooms_cmd[2], add_rooms_cmd[3], False)
    print('初始化删除房间完成')
    return


# 查询并删除所有房源信息
# 保留home_name=OpenAPI&OpenAPI2和存在设备的房源用于测试设备接口
def init_home_date():
    all_home_id = []
    # 查询所有房源
    search_home_ret = run_case(search_home_info, 'search_home_info-init', 'get', {}, False)
    for tmp in search_home_ret['home_list']:
        if tmp['home_name'] == 'OpenAPI' or tmp['home_name'] == 'OpenAPI2' or tmp['devices'] != []:
            continue
        all_home_id.append(tmp['home_id'])

    # 删除所有房源
    for tmp in all_home_id:
        if tmp == home_id or tmp == home_id_2:
            continue
        del_home_ret = run_case(del_home, 'del_home-init', 'post', {'home_id': tmp}, False)

    # OpenAPI下只保留公区,1001,1002,1003房间
    for tmp in search_home_ret['home_list']:
        if tmp['home_name'] == 'OpenAPI':
            for tmp_room in tmp['rooms']:
                if tmp_room['room_id'] not in [room_pub, room_1001, room_1002, room_1003]:
                    ret = run_case(del_room, 'del_room-init', 'post', {'home_id': home_id, 'room_id': tmp_room['room_id']}, False)
    print("初始化房源完成")
    return


def search_all_home():
    # result = send_request(access_token, 'post', {'client_id': '8a2dd447f145c30ec642c818', 'client_secret': 'c103ebd29d15f981146df864456e51541e740052'})
    search_home_ret = run_case(search_home_info, 'search_home_info_init', 'get', {'offset': 0, 'count': 20})
    # search_home_json = json.dumps(search_home_ret.json(), sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)
    # print(search_home_json)
    return


# 增加房源
def add_home_test(count=3):
    home_ids = []
    add_home_cmd = [add_home, 'add_home-test', 'post',
                    {'home_type': 2, 'country': '中国', 'city': '深圳', 'zone': '南山区', 'location': '深南大道', 'block': '深南花园', 'home_id': 'xxx', 'home_name': 'xxx',
                     'description': '深南花园描述'}]
    for i in range(count):
        add_home_cmd[3]['home_id'] = 'test_' + get_string(3)
        add_home_cmd[3]['home_name'] = add_home_cmd[3]['home_id']
        ret_add_home = run_case(add_home_cmd[0], add_home_cmd[1], add_home_cmd[2], add_home_cmd[3], False)
        home_ids.append(ret_add_home['home_id'])
    return home_ids


# 增加房间
def add_room_test(home_id_test=home_id, count=5):
    room_ids = []
    add_rooms_cmd = [add_rooms, 'add_rooms-test', 'post', {'home_id': home_id_test, 'rooms': [
        {'room_id': 'test', 'room_name': 'test', 'room_description': '测试', 'sp_state': '1', 'install_state': '1'}]}]
    for i in range(count):
        add_rooms_cmd[3]['rooms'][0]['room_id'] = add_rooms_cmd[3]['rooms'][0]['room_name'] = 'room_id_' + get_string(3)
        ret_add_rooms = run_case(add_rooms_cmd[0], add_rooms_cmd[1], add_rooms_cmd[2], add_rooms_cmd[3], False)
        room_ids.append(add_rooms_cmd[3]['rooms'][0]['room_id'])
    return room_ids


# search_all_home()
# add_room_test()
# add_home_test(10)
# empty_log()
# init_home_date()
# print(get_id('room_id', get_id('home_id')))
# init_del_home()
# init_del_room()

