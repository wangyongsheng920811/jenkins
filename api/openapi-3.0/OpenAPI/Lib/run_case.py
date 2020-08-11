from OpenAPI.Lib.MyHead import *
from OpenAPI.Config.all_api import *
from OpenAPI.Lib.get_token import *
import ssl, re


# 发送http请求
def send_request(api_url='', method='get', api_data={}, address_url=address, way='raw'):
    result = ''
    if method == 'get' or method == 'GET':
        result = requests.get(url=address_url + api_url, params=api_data, headers=headers)
    elif method == 'post' or method == 'POST':
        if way == 'raw':
            result = requests.post(url=address_url + api_url, data=json.dumps(api_data), headers=headers)
        elif way == 'form-data':
            result = requests.post(url=address_url + api_url, files=change_form_data(api_data), headers=headers)
    elif method == 'put' or method == 'PUT':
        result = requests.put(url=address_url + api_url, data=json.dumps(api_data), headers=headers)
    elif method == 'delete' or method == 'DELETE':
        result = requests.delete(url=address_url + api_url, params=api_data, headers=headers)
    else:
        print("请求方法错误！")
    return result


# 获取token值
def get_token(token_class='openapi', send_way='raw'):
    if token_class == 'openapi':
        ret_openapi = send_request(address_url=address_token+access_token, method='post', api_data={'client_id': client_id, 'client_secret': client_secret}, way=send_way)
        # print(address_token)
        # print(ret_openapi.json())
        print('===========')
        # print(ret_openapi.json()['access_token'])
        # return ret_openapi.json()['access_token']
        return '6c0204007af28c195285d4b621ea2fa6462d6b2d988c31adfae819b7d8bded4cc1a56f1a3bf8f1e2fa5edec6117b5bdadf53548abe9ae683ed0138226c548bab'

    elif token_class == 'openplatform':
        return get_openplatform_access_token()
    elif token_class == 'sdk':
        # 截取address_token为address_token_noroute
        index_list = []
        for index in re.finditer('/', address_token):
            index_list.append(index.span())
        # print(address_token)
        ret_sdk = send_request(address_url=address_token[0:index_list[2][0]]+blu_app_token, method='get', api_data={'access_token': get_token(), 'phone': phonenumber})
        # print(ret_sdk.json())
        return ret_sdk.json()['token']
    else:
        raise AssertionError('get_token: 错误的token_class: %s' % token_class)
# print(get_token('openapi'))


# 清空log文件
def empty_log(name='http.log'):
    with open(log_path+name, 'w') as fl:
        fl.write("")
        fl.close()


# 发送http请求并保存结果
def run_case(api_url, name, method, param, isprint=True, ret_type='json', way='raw', iftoken=True):
    global address
    address_copy = copy.deepcopy(address)
    if iftoken:
        global access_token_r
        if access_token_r == '':
            access_token_r = get_token(token_class=(operate_param_file(flag='platform')))
        api_data = {'access_token': access_token_r}
        param.update(api_data)
    start_time = datetime.datetime.now()
    # 如果api_url和address最后一位为/，则去掉address末尾的/字符
    if '/' in api_url and address_copy[-1] == '/':
        index_list = []
        for index in re.finditer('/', address_copy):
            index_list.append(index.span())
        address_copy = address_copy[0:index_list[2][0]]
    # 如果api_url和address最后一位都不为/，则在address末尾增加/v2/
    if '/' not in api_url and address_copy[-1] != '/':
        address_copy = address_copy + '/v2/'
    response = send_request(api_url, method, param, address_url=address_copy, way=way)
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

# print(get_token())
