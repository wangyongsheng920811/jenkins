from OpenAPI.Lib.get_data_list import *
from OpenAPI.Lib.MyHead import *
from OpenAPI.Lib.run_case import *

'''qianyi
gw_uuid = 'd51544228b14011727b1be67ddf67748'
ele_A1Z_uuid = '0077f226c34227f23edf3b8fc7a3aa02'
elecollector_uuid = 'd64f62bdc85eace78726d0035265c017'
lock_uuid = 'b1085351fdbb03c87e388454f951dd6b'
ele_A1_uuid = '889e8f9ef2faff9c0ea6c95bee52e30c'
ele_A3_uuid = '3d1e06cd04c377eaf7421e579e0a99ae'
ele_AMG_uuid = 'da7579d09b6120657b2ef61006a63537'
ele_AMW_uuid = 'a43718299ca38ff38194c3266af679d5'
home_id = '5bf22a8a80269a1504a7c700'
client_key = '542a2f9e3764956478c76113'
client_secret = '7c6ff8908726fac28b0743899cad4ba0'
'''

''' yangs
gw_uuid = '40759d4b37b4a7e194795b64a15873c6'
ele_A1Z_uuid = 'ce60c531819c43096b07c6428408572a'
elecollector_uuid = '08e37f273d6f02c07463528c0f88b3f8'
ele_A1_uuid = '6762441a57f9b5a1971aa4d632c66e3d'
ele_A3_uuid = 'dc7de1f936465f860531578cf25d982e'
home_id = '5bf512017581fc6191035206'
client_key = '212fcdf58d1d5d57bcaade98'
client_secret = 'a66eb937ab46093a7c0bd22eae68772d'
lock_uuid = '9de2ae5a3ae2ec41439d53d680121c92'
'''


# 转换成int型
def change_type(content={'home_id': 'null', 'password_id': '123'}):
    for tmp in content.keys():
        if content[tmp] == 'null':
            content[tmp] = None
        elif content[tmp] == 'false':
            content[tmp] = False
        elif content[tmp] == 'true':
            content[tmp] = True
        else:
            content[tmp] = int(content[tmp])
    return content


# 处理字典值
def change_dict(content={'"uuid"': '"xxxxxxx"', '"offset"': '"0"', '"count"': '0', '"home_id"': 'null'}):
    wrong_content = {}
    right_content = {}
    for tmp in content.keys():
        tmp_key = tmp
        tmp_value = content[tmp]
        if tmp.find('\"') != -1:
            tmp_key = tmp.replace('\"', '')
        if content[tmp].find('\"') != -1:
            tmp_value = content[tmp].replace('\"', '')
            right_content.update({tmp_key: tmp_value})
        else:
            wrong_content.update(change_type({tmp_key: tmp_value}))
    right_content.update(wrong_content)
    return right_content


# 格式化数据
def format_data(flag=0):
    one_param = {}
    one_cmd = []
    all_cmd = []
    with open(test_case_path + '/data.txt', 'r') as fl:
        excel_data = fl.readlines()
    for i in range(len(excel_data)):
        data_tmp = excel_data[i].strip().split('\t')
        for tmp in data_tmp[2:]:
            tmp_tmp = tmp.split(':')
            one_param.update({tmp_tmp[0]: tmp_tmp[1]})
        one_param = change_dict(one_param)
        one_cmd.append(data_tmp[0])
        one_cmd.append(data_tmp[1])
        one_cmd.append(str(i) + ". " + data_tmp[1])
        one_cmd.append(one_param)
        # 不包含密码相关操作
        if flag == 0:
            # if 'password' not in data_tmp[1] and 'client' not in data_tmp[1] and 'home_set' not in data_tmp[1] and 'elecollector' not in data_tmp[1]:
            if 'password' not in data_tmp[1]:
                all_cmd.append(one_cmd)
        # 只有密码相关操作
        elif flag == 1:
            if 'password' in data_tmp[1]:
                all_cmd.append(one_cmd)
        # 所有操作
        else:
            all_cmd.append(one_cmd)
        # 不包含密码相关操作
        # if 'password' not in data_tmp[1] and 'lock' not in data_tmp[1] and 'client' not in data_tmp[1] and 'home_set' not in data_tmp[1]:
        #     all_cmd.append(one_cmd)
        one_cmd = []
        one_param = {}
    with open(test_case_path + '/format_data_cmd', 'w') as fl:
        for tmp2 in all_cmd:
            fl.write(str(tmp2) + '\n')
    return all_cmd


# print(format_data(1))
# print(change_type())
# format_data(2)
def get_password_cmd():
    right_cmd = []
    all_cmd = format_data(1)
    for tmp_cmd in all_cmd:
        print(tmp_cmd)
        for tmp_right in right_cmd:
            print(tmp_right)
            if tmp_cmd[1] not in tmp_right:
                right_cmd.append(tmp_cmd)
    return right_cmd


# print(get_password_cmd())

password_cmds = [
    ['GET', 'fetch_passwords', '1. fetch_passwords', {'uuid': lock_uuid, 'offset': '0', 'count': '50'}],
    ['GET', 'get_default_password_plaintext', '2. get_default_password_plaintext', {'uuid': lock_uuid, 'offset': '0', 'count': '50'}],
    ['POST', 'unfrozen_password', '3. unfrozen_password', {'uuid': lock_uuid, 'offset': '0', 'count': '50', 'password_id': 1005}],
    ['POST', 'update_password', '4. update_password',
     {'uuid': lock_uuid, 'offset': '0', 'count': '50', 'name': None, 'password_id': 1012, 'password': '985225',
      'encrypted_password': 'kKOeJ23H27pUJ2tVVUZC2Q==', 'is_send_location': False, 'phonenumber': '18566260535'}],
    ['POST', 'delete_password', '5. delete_password',
     {'uuid': lock_uuid, 'offset': '0', 'count': '50', 'home_id': None, 'room_id': None, 'password_id': 1010}],
    ['POST', 'frozen_password', '6. frozen_password', {'uuid': lock_uuid, 'offset': '0', 'count': '50', 'password_id': 1002}],
    ['GET', 'get_dynamic_password_plaintext', '7. get_dynamic_password_plaintext', {'uuid': lock_uuid, 'offset': '0', 'count': '50'}],
    ['POST', 'add_password', '8. add_password',
     {'uuid': lock_uuid, 'offset': '0', 'count': '50', 'home_id': None, 'room_id': None, 'phonenumber': '18566260535', 'name': '测试',
      'is_default': 0, 'is_send_location': False, 'encrypted_password': None, 'permission_begin': 1542069120, 'permission_end': 1551400320}],
    ['POST', 'add_password', '9. add_password',
     {'uuid': lock_uuid, 'offset': '0', 'count': '50', 'home_id': None, 'room_id': None,
      'is_default': 0, 'is_send_location': True, 'encrypted_password': None, 'permission_begin': 1542069120, 'permission_end': 1551400320}],
    ['POST', 'add_password_without_center', '10. add_password_without_center',
     {'uuid': lock_uuid, 'offset': '0', 'count': '50', 'home_id': None, 'room_id': None,
      'is_send_msg': True, 'is_send_location': False, 'permission_end': 1544677200, 'CMD': 1}],
    ['post', 'update_password_without_center', '11. update_password_without_center',
     {'uuid': lock_uuid, 'phonenumber': '18566260535', 'password_id': 3040, 'name': '0000', 'is_send_msg': True, 'is_send_location': True,
      'permission_end': 1543669771}]
]

'''update
'permission_begin': 1541827560, 'permission_end': 1557676740,
, 'permission_status': '1'
add
'phonenumber': '18566260535', 'name': '测试', 
, 'permission_begin': 1542069120, 'permission_end': 1551400320
'''
