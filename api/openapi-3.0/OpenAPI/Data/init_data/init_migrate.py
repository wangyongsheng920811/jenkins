import requests, json, os, sys, psycopg2, pymysql, sshtunnel, platform, ctypes, time, datetime
from collections import OrderedDict
from sshtunnel import SSHTunnelForwarder
from termcolor import *

client_id_migrate = '91834'
'''
18512344321   91834
18511111111   91827
'''
url_migrate = 'http://qa-ci.dding.net:3000/clients/'
url_log = 'http://qa-ci.dding.net:3000/worker/status'

header_migrate = {'Accept': 'application/json, text/plain, */*',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36'}


# 发送http请求
def send_request(api_url='', method='get', api_data={}, address_url=''):
    result = ''
    if method == 'get':
        result = requests.get(url=address_url + api_url, params=api_data, headers=header_migrate)
    elif method == 'post':
        result = requests.post(url=address_url + api_url, data=json.dumps(api_data), headers=header_migrate)
    elif method == 'put':
        result = requests.put(url=address_url + api_url, data=json.dumps(api_data), headers=header_migrate)
    elif method == 'delete':
        result = requests.delete(url=address_url + api_url, params=api_data, headers=header_migrate)
    else:
        print("请求方法错误！")
    # print(result.url)
    # print(result.status_code)
    # print(result.json())
    return result


# 检测是否迁移or回滚成功
def check_migrate_rollback(client_id=client_id_migrate, method='migrate'):
    if method == 'migrate':
        for i in range(3):
            ret_log_m = send_request(api_url=url_log, method='get')
            if client_id not in ret_log_m.json()['status']['dispatcher']['migrates']:
                if i == 2:
                    return False
                else:
                    print('cant get client_id %s status,continue...' % client_id)
                    time.sleep(5)
                    continue
            else:
                return True
    elif method == 'rollback':
        for j in range(10):
            ret_log_b = send_request(api_url=url_log, method='get')
            if client_id not in ret_log_b.json()['status']['dispatcher']['migrates'] and client_id not in ret_log_b.json()['status']['dispatcher']['grays']:
                return True
            else:
                if j == 9:
                    return False
                else:
                    time.sleep(1)
                    continue
    else:
        raise AssertionError('wrong input method: %s' % method)
    return


# 检查商户迁移状态 已经迁移、未迁移
def check_client_if_migrate(client_id=client_id_migrate):
    if check_migrate_rollback(client_id):
        print('client_id %s already migrated!' % client_id)
        return 'migrated'
    elif check_migrate_rollback(client_id, 'rollback'):
        print('client_id %s is not migrated or had rollbacked!' % client_id)
        return 'rollbacked'
    else:
        print('client_id %s cant get status!' % client_id)
        return False


# 迁移商户核心数据
def migrate_client(client_id=client_id_migrate):
    # 根据client_id查询商户信息
    ret_info = send_request(api_url=client_id + '/info', method='get', address_url=url_migrate)
    if 'client' not in ret_info.json():
        raise AssertionError('client_id %s not exit!' % client_id)
    # 商户迁移
    ret_sync = send_request(api_url=client_id + '/sync', method='get', address_url=url_migrate)
    if 'client_id' not in ret_sync.json():
        raise AssertionError('client_id %s is not in migrate response!' % client_id)
    # 查询商户是否迁移成功
    return check_migrate_rollback(client_id)


# 回滚核心数据
def rollback_client(client_id=client_id_migrate):
    # 根据client_id查询商户信息
    ret_info = send_request(api_url=client_id + '/info', method='get', address_url=url_migrate)
    if 'client' not in ret_info.json():
        raise AssertionError('client_id %s is not exit!' % client_id)
    # 回滚商户
    ret_del = send_request(api_url=client_id + '/del', method='get', address_url=url_migrate)
    if 'client_id' not in ret_del.json():
        raise AssertionError('client_id %s is not in rollback response!' % client_id)
    # 查询商户是否回滚成功
    return check_migrate_rollback(client_id, 'rollback')


# 获取当前时间
def get_time():
    now = datetime.datetime.now()
    now_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return now_time


# 检测迁移错误
def check_error(way='off'):
    status_url = ''
    # 线下检测地址
    status_url_off = 'http://qa-ci.dding.net:3000/worker/status'
    # 预迁移检测地址
    status_url_qa = 'http://118.190.136.27:3000/worker/status'
    if way == 'off':
        status_url = status_url_off
    elif way == 'qa':
        status_url = status_url_qa
    ret_status = send_request(status_url, 'get')
    print(ret_status.json()['status'])
    all_error = {}
    for tmp in ret_status.json()['status']:
        if 'worker' in tmp:
            # print('######', tmp, '######')
            # 没有错误则继续
            if not ret_status.json()['status'][tmp]['error']:
                continue
            for content in ret_status.json()['status'][tmp]['error'].keys():
                if 'ok' not in ret_status.json()['status'][tmp]['error'][content].values():
                    # 截取client_id
                    client_id_error_all = list(ret_status.json()['status'][tmp]['error'][content].keys())[0]
                    client_id_error = client_id_error_all[10:]
                    # print(client_id_error)
                    tmp_error = ret_status.json()['status'][tmp]['error'][content][client_id_error_all]
                    # print(tmp_error)
                    # ret_error_json = json.dumps(
                    #     ret_status.json()['status'][tmp]['error'][content][list(ret_status.json()['status'][tmp]['error'][content].keys())[0]], sort_keys=True,
                    #     indent=4, separators=(', ', ': '), ensure_ascii=False)
                    # print(ret_error_json)
                    errors = []
                    for tmp_tmp in tmp_error['errors']:
                        one_error = {}
                        if 'message' in tmp_tmp:
                            one_error.update({'message': tmp_tmp['message']})
                        if 'value' in tmp_tmp:
                            one_error.update({'value': tmp_tmp['value']})
                        errors.append(one_error)
                    all_error.update({'client_id': client_id_error, 'errors': errors, 'sql': tmp_error['sql']})
    # print(all_error)
    # all_error_json = json.dumps(all_error, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)
    # print(all_error_json)
    return all_error


# 打印并写log到文件
def write_print(content, isprint=True, name='log.txt'):
    content = content.replace('\u2006', '')
    with open(name, 'a+') as fl:
        fl.write(content)
    if isprint:
        print(content, end='')
    return


# 检查文件中是否含有传入内容
def check_content(content='', filename='log.txt'):
    with open(filename, 'r') as fl:
        all_content = fl.read()
    if all_content.find(content) == -1:
        return False
    else:
        return True


# 循环检测迁移结果
def loop_check_migrate():
    while True:
        ret = check_error('off')
        if ret:
            ret_json = json.dumps(ret, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)
            ret_list = ret_json.split('\n')
            # 检测errors里的第一个错误不存在则写入
            if not check_content(ret_list[4]+'\n'+ret_list[5]):
                write_print(ret_json+'\n')
        print('sleep 2 sec...', get_time())
        time.sleep(2)


# print(migrate_client('91834'))
# print(rollback_client('91834'))
# check_client_if_migrate('91834')
# loop_check_migrate()


