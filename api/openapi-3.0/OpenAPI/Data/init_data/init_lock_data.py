from OpenAPI.Lib.MyHead import *
from OpenAPI.Lib.run_case import *


# 检查密码的状态 2 生效  5 冻结
def check_pwd_state(password_id=1234, pwd_state=2):
    pwd_id_flag = False
    fetch_passwords_cmd = [fetch_passwords, 'fetch_passwords-init', 'get', {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid}]
    for i in range(3):
        ret_fetch_passwords = run_case(fetch_passwords_cmd[0], fetch_passwords_cmd[1], fetch_passwords_cmd[2], fetch_passwords_cmd[3], False)
        if not pwd_id_flag:
            for tmp in ret_fetch_passwords['passwords']:
                if tmp == str(password_id):
                    pwd_id_flag = True
                else:
                    continue
        if pwd_id_flag:
            try:
                if ret_fetch_passwords['passwords'][password_id]['pwd_state'] == pwd_state:
                    return True
                else:
                    if i == 2:
                        return False
                    else:
                        time.sleep(2)
                        continue
            except:
                pass
        else:
            return False
    return False


# 检查密码的操作结果 1 进行中 2 失败 3 成功
def check_operation_stage(password_id=1234, operation_stage=3):
    # 判断传入的pwd_id是否存在
    pwd_id_flag = False
    fetch_passwords_cmd = [fetch_passwords, 'fetch_passwords-init', 'get', {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid}]
    for i in range(10):
        ret_fetch_passwords = run_case(fetch_passwords_cmd[0], fetch_passwords_cmd[1], fetch_passwords_cmd[2], fetch_passwords_cmd[3], False)
        if not pwd_id_flag:
            for tmp in ret_fetch_passwords['passwords']:
                if tmp == str(password_id):
                    pwd_id_flag = True
                else:
                    continue
        if pwd_id_flag:
            try:
                if ret_fetch_passwords['passwords'][password_id]['operation_stage'] == int(operation_stage):
                    return True
                else:
                    if i == 9:
                        return False
                    else:
                        time.sleep(1)
                        continue
            except:
                pass
        else:
            return False
    return False


# 获取password_id（update_password和update_password_without_center）
def get_password_id(flag='center'):
    global retrytimes
    add_password_cmd = [add_password, 'add_password-init', 'post',
                        {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid,
                         'phonenumber': phonenumber, 'is_default': 0, 'is_send_location': False, 'password': '123456',
                         'name': 'test', 'permission_begin': now_s, 'permission_end': after_s}]
    add_password_without_center_cmd = [add_password_without_center, 'add_password_without_center-init', 'post',
                                   {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid,
                                    'phonenumber': phonenumber, 'CMD': 1, 'name': get_string(4), 'is_send_msg': False, 'is_send_location': False,
                                    'permission_end': after_s}]
    fetch_passwords_cmd = [fetch_passwords, 'fetch_passwords-init', 'get', {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid}]
    frozen_password_cmd = [frozen_password, 'frozen_password-init', 'post', {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid, 'password_id': 1016}]
    ret_fetch_passwords = run_case(fetch_passwords_cmd[0], fetch_passwords_cmd[1], fetch_passwords_cmd[2], fetch_passwords_cmd[3], False)
    for tmp in ret_fetch_passwords['passwords']:
        if tmp == '999' or tmp == '3000':
            continue
        elif int(tmp) < 3000:
            # 在线密码
            if flag == 'center':
                if check_pwd_state(tmp, 2) and check_operation_stage(tmp, 3):
                    return tmp
            # 冻结的在线密码
            elif flag == 'frozen_center':
                if check_pwd_state(tmp, 5) and check_operation_stage(tmp, 3):
                    return tmp
        elif int(tmp) > 3000:
            # 离线密码
            if flag == 'without_center':
                if check_pwd_state(tmp, 2) and check_operation_stage(tmp, 3):
                    return tmp
            # 冻结的离线密码
            elif flag == 'frozen_without_center':
                if check_pwd_state(tmp, 5) and check_operation_stage(tmp, 3):
                    return tmp
    retrytimes += 1
    if retrytimes > 5:
        return False
    print(retrytimes)
    # 如果不存在，则添加
    if flag == 'center':
        run_case(add_password_cmd[0], add_password_cmd[1], add_password_cmd[2], add_password_cmd[3], False)
        return get_password_id('center')
    elif flag == 'without_center':
        run_case(add_password_without_center_cmd[0], add_password_without_center_cmd[1], add_password_without_center_cmd[2], add_password_without_center_cmd[3], False)
        return get_password_id('without_center')
    elif flag == 'frozen_center':
        frozen_password_cmd[3]['password_id'] = int(get_password_id('center'))
        run_case(frozen_password_cmd[0], frozen_password_cmd[1], frozen_password_cmd[2], frozen_password_cmd[3], False)
        return get_password_id('frozen_center')
    elif flag == 'frozen_without_center':
        frozen_password_cmd[3]['password_id'] = int(get_password_id('without_center'))
        run_case(frozen_password_cmd[0], frozen_password_cmd[1], frozen_password_cmd[2], frozen_password_cmd[3], False)
        return get_password_id('frozen_without_center')


# 初始化删除冻结密码,删除已冻结密码，并返回可删除冻结的密码id列表
def init_delete_frozen_password():
    password_id = []
    add_password_cmd = [add_password, 'add_password-init', 'post',
                        {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid,
                         'phonenumber': phonenumber, 'is_default': 0, 'is_send_location': False, 'password': '123456',
                         'name': 'test', 'permission_begin': now_s, 'permission_end': after_s}]
    fetch_passwords_cmd = [fetch_passwords, 'fetch_passwords-init', 'get', {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid}]
    delete_password_cmd = [delete_password, 'delete_password-init', 'post',
                           {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid, 'password_id': 123}]
    ret_fetch_passwords = run_case(fetch_passwords_cmd[0], fetch_passwords_cmd[1], fetch_passwords_cmd[2], fetch_passwords_cmd[3], False)
    with open(param_path + 'delete_password_cmd') as fl:
        del_pwd_num = len(fl.readlines())
    with open(param_path + 'frozen_password_cmd') as fl:
        del_pwd_num += len(fl.readlines())
    # 统计非管理员和非冻结的密码,如果大于需要的密码数，直接返回，否则，补齐后返回
    for tmp in ret_fetch_passwords['passwords']:
        if tmp == '999':
            continue
        try:
            if ret_fetch_passwords['passwords'][tmp]['pwd_state'] == 2:
                password_id.append(tmp)
            else:
                delete_password_cmd[3]['password_id'] = int(tmp)
                run_case(delete_password_cmd[0], delete_password_cmd[1], delete_password_cmd[2], delete_password_cmd[3], False)
        except:
            pass
    if len(password_id) < del_pwd_num:
        for i in range(del_pwd_num - len(password_id)):
            ret_add_password_cmd = run_case(add_password_cmd[0], add_password_cmd[1], add_password_cmd[2], add_password_cmd[3], False)
            while check_operation_stage(ret_add_password_cmd['id'], 2) or check_operation_stage(ret_add_password_cmd['id'], 3):
                break
            password_id.append(ret_add_password_cmd['id'])
    ret_fetch_passwords = run_case(fetch_passwords_cmd[0], fetch_passwords_cmd[1], fetch_passwords_cmd[2], fetch_passwords_cmd[3], False)
    if len(ret_fetch_passwords['passwords']) - 1 >= del_pwd_num:
        print('初始化删除密码完成')
    else:
        print('初始化删除密码失败')
        print('need: '+str(del_pwd_num)+'\nactural: '+str(len(ret_fetch_passwords['passwords'])-1))
    return password_id


# 清空密码
def empty_lock_password(ifhold = True):
    print('开始清空密码')
    fetch_passwords_cmd = [fetch_passwords, 'fetch_passwords-init', 'get', {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid}]
    delete_password_cmd = [delete_password, 'delete_password-init', 'post',
                           {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid, 'password_id': 123}]
    ret_fetch_passwords = run_case(fetch_passwords_cmd[0], fetch_passwords_cmd[1], fetch_passwords_cmd[2], fetch_passwords_cmd[3], False)
    for tmp in ret_fetch_passwords['passwords']:
        # 管理员密码
        if tmp == '999' or tmp == '3000':
            continue
        else:
            # 保留生效和冻结的密码
            if ifhold:
                if check_pwd_state(tmp, 2):
                    print(tmp, '属于生效密码，continue...')
                    continue
                elif check_pwd_state(tmp, 5):
                    print(tmp, '属于冻结密码，continue...')
                    continue
            print(tmp, '删除！')
            delete_password_cmd[3]['password_id'] = int(tmp)
            run_case(delete_password_cmd[0], delete_password_cmd[1], delete_password_cmd[2], delete_password_cmd[3], False)
    ret_fetch_passwords_2 = run_case(fetch_passwords_cmd[0], fetch_passwords_cmd[1], fetch_passwords_cmd[2], fetch_passwords_cmd[3], False)
    print(ret_fetch_passwords_2['passwords'].keys())
    print('清空密码完成')
    return


def test():
    frozen_password_id = []
    delete_password_id = []
    tmp_id = {}
    fetch_passwords_cmd = [fetch_passwords, 'fetch_passwords-init', 'get', {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid}]
    delete_password_cmd = [delete_password, 'delete_password-init', 'post',
                           {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid, 'password_id': 123}]
    frozen_password_cmd = [frozen_password, 'frozen_password-init', 'post',
                           {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid, 'password_id': 1016}]
    unfrozen_password_cmd = [unfrozen_password, 'unfrozen_password-init', 'post',
                             {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid, 'password_id': 1016}]
    add_password_cmd = [add_password, 'add_password-init', 'post',
                        {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid,
                         'phonenumber': phonenumber, 'is_default': 0, 'is_send_location': True, 'password': '123456',
                         'name': 'test', 'permission_begin': now_s, 'permission_end': after_s}]
    add_password_without_center_cmd = [add_password_without_center, 'add_password_without_center-init', 'post',
                                       {'home_id': home_id, 'room_id': room_1001, 'uuid': lock_uuid,
                                        'phonenumber': phonenumber, 'CMD': 1, 'name': 'test', 'is_send_msg': True, 'is_send_location': True,
                                        'permission_end': after_s}]
    # ret_frozen_password = run_case(frozen_password_cmd[0], frozen_password_cmd[1], frozen_password_cmd[2], frozen_password_cmd[3])
    # for i in range(2):
    #     run_case(add_password_cmd[0], add_password_cmd[1], add_password_cmd[2], add_password_cmd[3], True)
    for i in range(6):
        run_case(add_password_cmd[0], add_password_cmd[1], add_password_cmd[2], add_password_cmd[3], True)
        # run_case(add_password_without_center_cmd[0], add_password_without_center_cmd[1], add_password_without_center_cmd[2], add_password_without_center_cmd[3], True)
        time.sleep(2)

    ret_fetch_passwords = run_case(fetch_passwords_cmd[0], fetch_passwords_cmd[1], fetch_passwords_cmd[2], fetch_passwords_cmd[3], False)
    for tmp in ret_fetch_passwords['passwords']:
        tmp_id.update(
            {tmp: {'pwd_state': ret_fetch_passwords['passwords'][tmp]['pwd_state'], 'operation_stage': ret_fetch_passwords['passwords'][tmp]['operation_stage']}})
    tmp_id = json.dumps(tmp_id, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)
    print(tmp_id)
    # print(ret_fetch_passwords['passwords']['1016']['pwd_state'])
    # print(ret_fetch_passwords['passwords']['1016']['operation_stage'])

    # ret_unfrozen_password = run_case(unfrozen_password_cmd[0], unfrozen_password_cmd[1], unfrozen_password_cmd[2], unfrozen_password_cmd[3])
    # for tmp in ret_fetch_passwords['passwords']:
    #     if tmp == '999':
    #         continue
    #     elif ret_fetch_passwords['passwords'][tmp]['pwd_state'] == 5:
    #         frozen_password_id.append(tmp)
    #     else:
    #         delete_password_id.append(tmp)
    # print(delete_password_id)
    # print(frozen_password_id)
    return


# test()
# empty_lock_password()
# print(get_password_id('frozen_without_center'))
# print(get_password_id('frozen_center'))
# print(get_password_id('without_center'))
# print(get_password_id('center'))
# empty_lock_password('3.0')
# print(init_delete_frozen_password())
# test('2.0')
# 3.0  1012 1015 1017 3026 3027 3028
# 2.0  1031 1032 1033 3025 3026 3027
# empty_lock_password(True)
# print(get_password_id('frozen_without_center'))
# print(check_pwd_state(1234, 5))


