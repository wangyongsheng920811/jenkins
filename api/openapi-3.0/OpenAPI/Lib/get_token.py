from OpenAPI.Lib.MyHead import *

code_url_1 = openplatform_url + '/open/v1/authorize'
code_url_2 = openplatform_url + '/open/v1/login_grant'
code_url_3 = openplatform_url + '/open/v1/oauth/grant_code'
access_token_url = openplatform_url + '/open/v1/oauth/token'
client_id_openplatform_off = 'passportoauth2testclientidzfzszszsffs'
client_secret_openplatform_off = 'passportoauth2testclientsecretfdffswamwaxbwcbwwaldd'
# 权限：密码操作、网关信息、网关操作。。。。。
scope = 'pwd_op,gateway_mg,gateway_op,ble_op,water_mg,water_op,elemeter_mg,elemeter_op,apartment_mg,lock_mg,ticket_mg'

header_openplatform = {'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Connection': 'keep-alive',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}


# 获取openplatform的token_code
def get_token_code(user_name=user_name_openplatform, pwd=user_pwd_openplatform):
    api_data_1 = {'client_id': client_id_openplatform_off, 'redirect_uri': 'http://dev-gate.dding.net:4086/url_post',
                  'scope': scope, 'state': 'sdfasfd'}
    ret_1 = requests.get(url=code_url_1, params=api_data_1, headers=header_openplatform)
    # print(ret_1.json())
    # print(ret_1.url)

    api_data_2 = {'client_id': client_id_openplatform_off, 'scope': scope, 'phone': user_name, 'password': pwd, 'country_code': '+86',
                  'session_id': ret_1.json()['session_id']}
    ret_2 = requests.post(url=code_url_2, data=api_data_2, headers=header_openplatform)
    # print(ret_2.url)
    # print(ret_2.json())

    api_data_3 = {'state': 'sdfasfd', 'client_id': client_id_openplatform_off, 'redirect_uri': 'http://dev-gate.dding.net:4086/url_post', 'scope': scope,
                  'response_type': 'code', 'session_id': ret_2.json()['session_id']}
    ret_3 = requests.get(url=code_url_3, params=api_data_3, headers=header_openplatform)
    # print(ret_3.url)
    return ret_3.url[ret_3.url.find('code=') + 5:ret_3.url.find('&state')]


# 获取access_token a0546bff7d95d39a52b0fd5224d207c66732bfed
def get_openplatform_access_token(token='access_token'):
    api_data = {'code': get_token_code(), 'client_id': client_id_openplatform_off, 'client_secret': client_secret_openplatform_off, 'grant_type': 'authorization_code'}
    ret_access_token = requests.post(url=access_token_url, data=api_data, headers=header_openplatform)
    ret_access_token_json = json.dumps(ret_access_token.json(), sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)
    write_print(ret_access_token_json, isprint=False)
    write_print('\n', isprint=False)
    if token == 'access_token':
        return ret_access_token.json()['access_token']
    elif token == 'refresh_token':
        return ret_access_token.json()['refresh_token']
    else:
        raise AssertionError('get_openplatform_access_token: 错误的token')


# 通过refresh_token刷新token和refresh_token
def refresh_token(refresh_token='', token='access_token'):
    api_data = {'refresh_token': refresh_token, 'client_id': client_id_openplatform_off, 'client_secret': client_secret_openplatform_off,
                'grant_type': 'refresh_token'}
    ret_tmp = requests.post(url=access_token_url, data=api_data, headers=header_openplatform)
    ret_token_json = json.dumps(ret_tmp.json(), sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)
    write_print(ret_token_json, isprint=False)
    write_print('\n', isprint=False)
    if token == 'access_token':
        return ret_tmp.json()['access_token']
    elif token == 'refresh_token':
        return ret_tmp.json()['refresh_token']
    else:
        raise AssertionError('refresh_token: 错误的token')


# get_access_token()
# refresh_token()
# print(get_token_code())
# print(get_access_token())
# print(refresh_token(get_openplatform_access_token('refresh_token')))
# print(get_openplatform_access_token('refresh_token'))
