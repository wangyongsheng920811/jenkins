# import paramiko     # Linux下没有这个库，git上版本注释
from OpenAPI.Lib.MyHead import *


def CheckDictValue(value='8d1166e0ee4b26c9a0afbcec88ac155b', dict=dict):
    for tmp in dict.values():
        if type(tmp) == type(value):
            if tmp == value:
                return True
            else:
                continue
        else:
            continue
    return False


# windows下连接测试服务器，发送命令，并获取返回值
def ConnectServer(cmd='cat /home/gitlab-runner/logs/saas-callback-test/access.log'):
    onoffline = operate_param_file(flag='onoffline')
    # if 'win' in sys.platform:
    #     pkey = key_path + 'Identity'
    #     key = paramiko.RSAKey.from_private_key_file(pkey, password='123456')  # 有解密密码
    #     # paramiko.util.log_to_file('paramiko.log')   # log文件地址
    #     ssh = paramiko.SSHClient()
    #     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #     ssh.connect('121.42.140.86', port=4399, username='root', pkey=key)
    #     stdin, stdout, stderr = ssh.exec_command('cat /home/gitlab-runner/logs/saas-callback-test/access.log')
    #     all_callback = stdout.readlines()
    # elif 'linux' in sys.platform:
    if 'linux' in sys.platform:
        if onoffline == 'off':
            all_callback = os.popen('cat /home/gitlab-runner/logs/saas-callback-test/access.log').readlines()
        elif onoffline == 'qa-off':
            all_callback = os.popen('ssh root@121.42.140.86 -p 4399 \"cat /home/gitlab-runner/logs/saas-callback-test/access.log\"').readlines()
        else:
            raise AssertionError('wrong input server:', onoffline)
    else:
        all_callback = ''
        raise AssertionError('platform not in win or linux!')
    return all_callback


def CheckCallback(way='service', event='deviceUninstall', serviceid=123, uuid=elemeter_A1_uuid, looptime=1):
    # 取log中的后三行，进行对比
    for j in range(looptime):
        all_callback = ConnectServer()
        for i in [-1, -2, -3, -4, -5]:
            # 截取其中的json格式部分  str格式
            last_callback_str = all_callback[i].strip()[all_callback[i].strip().find('{"remoteIP'):]
            # 将str格式转换为字典格式
            last_callback_dict = json.loads(last_callback_str)
            # 截取其中的body部分
            last_callback_body = last_callback_dict['req']['body']
            # tmp_json = json.dumps(last_callback_body, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)
            # print(tmp_json)
            print(last_callback_body)
            print('serviceid', serviceid)
            if way == 'service':
                if 'serviceid' not in last_callback_body.keys():
                    continue
                if last_callback_body['serviceid'] == str(serviceid):
                    return True
                else:
                    continue
            elif way == 'event':
                if 'event' not in last_callback_body.keys():
                    continue
                if CheckDictValue(event, last_callback_body) and CheckDictValue(uuid, last_callback_body):
                    return True
                else:
                    continue
            else:
                AssertionError('Wrong way:', way)
            # print(last_callback_body)
            # tmp_json = json.dumps(last_callback_body, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)
            # print(tmp_json)
        time.sleep(2)
    return False


# if CheckCallback(way='service', serviceid="77157", looptime=10):
#     print('ok')
# else:
#     print('no')
