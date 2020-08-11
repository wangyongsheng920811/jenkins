from OpenAPI.Lib.MyHead import *
from OpenAPI.Config.all_api import *
import ssl

# 区分2.0和3.0
api_config = '3.0 线下'

# 默认 3.0 线下
cookie_url = 'http://dev-gate.dding.net:7080/login'
request_url = 'http://qa-saas.dding.net:9001'
origin_url = 'http://qa-saas.dding.net:9001'
usr_name = '18566666668'
pwd = '123456'

# 3.0 线上
cookie_url_30_on = 'https://passport.dding.net/login'
request_url_30_on = 'https://manageapi.dding.net'
origin_url_30_on = 'https://manage.dding.net'
usr_name_30_on = ''
pwd_30_on = ''

# 3.0 线下
cookie_url_30_off = 'http://dev-gate.dding.net:7080/login'
request_url_30_off = 'http://qa-saas.dding.net:7002'
origin_url_30_off = 'http://qa-saas.dding.net:9001'
usr_name_30_off = '18512344321'
pwd_30_off = '123456'

# 2.0 线上
cookie_url_20_on = 'https://passport.dding.net/login'
request_url_20_on = 'https://device.dding.net'
origin_url_20_on = 'https://device.dding.net'
usr_name_20_on = ''
pwd_20_on = ''

# 2.0 线下
cookie_url_20_off = 'https://passport.dding.net/login'
request_url_20_off = 'http://yundingsaastest.dding.net:9012'
origin_url_20_off = 'http://yundingsaastest.dding.net:9012'
usr_name_20_off = '18512344321'
pwd_20_off = '123456'

# 公共部分
fromint = 2


# 配置参数
def get_param(api='30_off'):
    global cookie_url, request_url, origin_url, role_url, device_url, usr_name, pwd, role_type, api_config, device_sn, phone_url
    if api == '30_off':
        cookie_url = cookie_url_30_off
        request_url = request_url_30_off
        origin_url = origin_url_30_off
        usr_name = usr_name_30_off
        pwd = pwd_30_off
        api_config = '3.0 线下'
        return
    elif api == '30_on':
        cookie_url = cookie_url_30_on
        request_url = request_url_30_on
        origin_url = origin_url_30_on
        usr_name = usr_name_30_on
        pwd = pwd_30_on
        api_config = '3.0 线上'
        return
    elif api == '20_off':
        cookie_url = cookie_url_20_off
        request_url = request_url_20_off
        origin_url = origin_url_20_off
        usr_name = usr_name_20_off
        pwd = pwd_20_off
        api_config = '2.0 线下'
        return
    elif api == '20_on':
        cookie_url = cookie_url_20_on
        request_url = request_url_20_on
        origin_url = origin_url_20_on
        usr_name = usr_name_20_on
        pwd = pwd_20_on
        api_config = '2.0 线上'
        return
    else:
        return False


# 发送http请求
def send_request(api_url='', method='get', api_data={}, header={}, address_url=request_url):
    result = ''
    if header == {}:
        header = get_headers()
    if method == 'get':
        result = requests.get(url=address_url + api_url, params=api_data, headers=header)
    elif method == 'post':
        result = requests.post(url=address_url + api_url, data=json.dumps(api_data), headers=header)
    elif method == 'put':
        result = requests.put(url=address_url + api_url, data=json.dumps(api_data), headers=header)
    elif method == 'delete':
        result = requests.delete(url=address_url + api_url, params=api_data, headers=header)
    else:
        print("请求方法错误！")
    # print(result.url)
    # print(result.status_code)
    # print(result.json())
    return result


# 获取cookie
def get_cookie():
    header = {'Origin': origin_url, 'Content-Type': 'application/json;charset=UTF-8'}
    ret = send_request(method='post', address_url=cookie_url, api_data={'name': usr_name, 'pass': pwd, 'from': fromint}, header=header)
    # print(ret.json())
    return ret.headers['set-cookie']


# 获取headers
def get_headers(platform='saasapi'):
    headers = {'Accept': 'application/json, text/plain, */*',
               'Content-Type': 'application/json; charset=UTF-8',
               'Connection': 'keep-alive',
               # 'Host': 'manageapi.dding.net',
               # 'Origin': 'http://qa-saas.dding.net:9001',
               # 'Referer': 'http://qa-saas.dding.net:9001',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
               'Cookie': get_cookie()
               }
    if fromint == 1:
        headers.update({'YD-App': 'ydapp_az'})
    return headers


# 清空log文件
def empty_log(name='http.log'):
    with open(log_path+name, 'w') as fl:
        fl.write("")
        fl.close()


# 发送http请求并保存结果
def run_case(api_url, name, method, param, isprint=True, ret_type='json'):
    start_time = datetime.datetime.now()
    response = send_request(api_url, method, param)
    end_time = datetime.datetime.now()
    if ret_type == 'str':
        param_head = param
        response_head = response.json()
    elif ret_type == 'json':
        param_head = json.dumps(param, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)
        response_head = json.dumps(response.json(), sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)
    else:
        return False
    write_print("\n-----" + name + "-----\n" + start_time.strftime("%Y-%m-%d %H:%M:%S.%f") + "\nmethod: " + method + "\nurl: " + response.url + "\nparam: " + str(
        param_head) + "\ncode: " + str(response.status_code) + "\nresp: " + str(response_head) + "\nrun_time: " + str(
        end_time - start_time) + "\n-------------------------\n", isprint)
    return response.json()


# 解绑电表
def UbindElemeter(home_id_b='1746539770', room_id_b='1568734847', elemeter_id_b='93277047'):
    ret_unbind = run_case('/v3/rooms/'+room_id_b+'/elemeters/'+elemeter_id_b, '解绑电表A1', 'delete', {}, isprint=False)
    time.sleep(2)
    ret_elemeter = run_case('/v3/homes/'+home_id_b+'/devices', '查询电表状态', 'get', {}, isprint=False)
    for device_tmp in ret_elemeter['result']:
        if device_tmp['sn'] == '170918000640':
            return False
        else:
            continue
    return True


# 绑定电表
def BindElemeter(room_id_b='1568734847', elemeter_sn_b='170918000640', parent_id_b=113853730, model_b='DDSU1225'):
    ret_bind = run_case('/v3/rooms/' + room_id_b + '/elemeters', '绑定电表A1', 'post',
                        {'description': '电表A1-0640', 'sn': elemeter_sn_b, 'parent_id': parent_id_b, 'model': model_b}, isprint=False)
    for i in range(10):
        ret_state = run_case('/v3/rooms/' + room_id_b + '/elemeters/check', '查询绑定状态', 'post',
                             {'sn': elemeter_sn_b, 'process_id': int(ret_bind['result']['process_id'])}, isprint=False)
        if ret_state['result']['status'] == 2:
            return True
        time.sleep(2)
    return False


# if BindElemeter():
#     print('绑定成功')
# if UbindElemeter():
#     print('解绑成功')
