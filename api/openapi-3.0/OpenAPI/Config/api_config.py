# 请求头
headers = {'Accept': 'application/json, text/plain, */*',
           'Content-Type': 'application/json; charset=UTF-8',
           'Connection': 'keep-alive',
           'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36"}

headerss = {'Accept': 'application/json, text/plain, */*', 'Content-Type': 'application/json; charset=UTF-8', 'Connection': 'keep-alive'}

# headers_20 = {'Accept': 'application/json, text/plain, */*',
#               'Content-Type': 'application/json; charset=UTF-8',
#               'Connection': 'keep-alive',
#               'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36"}

# 请求接口所在服务器
# 2.0 线下
# self
# address_20_off = 'http://118.190.15.117:6001/openapi/v1/'
address_20_off = 'http://yundingsaastest.dding.net:6001/openapi/v1/'
# address_20_off = 'http://yundingsaastest.dding.net:6001'
# noroute
address_20_off_noroute = 'http://yundingsaastest.dding.net:6001'
# pms  (4.0)
address_20_off_pms = 'http://yundingsaastest.dding.net:6001/pms/v1/'
# sdk
address_20_off_sdk = 'http://yundingsaastest.dding.net:6001'
# token
address_token_20_off = 'http://yundingsaastest.dding.net:6001/openapi/v1/'

# 3.0 线下(默认)
# self
address = 'http://qa-saas.dding.net:7003/v2/'
# address = 'http://121.42.140.86:7003/v2/'
# address = 'http://121.42.140.86:7003'
# noroute
address_noroute = 'http://121.42.140.86:7003'
# pms (4.0)
address_pms = 'http://121.42.140.86:7003/pms/v1/'
# sdk
address_sdk = 'http://qa-saas.dding.net:7005'
# token
address_token = 'http://qa-saas.dding.net:7003/v2/'

# 3.0 线下（另一套环境）
# self
address_30_off_qa = 'http://qa-saas3.dding.net:7003/v2/'
# noroute
address_30_off_qa_noroute = 'http://qa-saas3.dding.net:7003'
# pms (4.0)
address_30_off_qa_pms = 'http://qa-saas3.dding.net:7003/pms/v1/'
# sdk
address_30_off_qa_sdk = 'http://qa-saas3.dding.net:7005'
# token
address_token_30_off_qa = 'http://qa-saas3.dding.net:7003/v2/'

# 3.0 线上
# self
address_30_on = 'http://saas-openapi.dding.net/v2/'
# address_30_on = 'http://saas-openapi.dding.net'
# noroute
address_30_on_noroute = 'http://saas-openapi.dding.net'
# pms (4.0)
address_30_on_pms = 'http://saas-openapi.dding.net/pms/v1/'
# sdk
address_30_on_sdk = 'http://saas-openapi.dding.net'
# token
address_token_30_on = 'http://saas-openapi.dding.net/v2/'

# 2.0 线上
# self
address_20_on = 'http://lockapi.dding.net/openapi/v1/'
# noroute
address_20_on_noroute = 'http://lockapi.dding.net'
# pms (4.0)
address_20_on_pms = 'http://lockapi.dding.net/pms/v1/'
# sdk
address_20_on_sdk = 'http://lockapi.dding.net'
# token
address_token_20_on = 'http://lockapi.dding.net/openapi/v1/'

# 特殊场景
# address_xx = 'http://lockapi.dding.net/openapi/v1/'
# address_xx = 'http://yundingsaastest.dding.net:6001/openapi/v1/'
# address_xx = 'http://yundingsaastest.dding.net:6001/pms/v1/'
address_xx = 'http://121.42.140.86:7003/v2/'
# address_xx = 'https://saas-openapi.dding.net'
address_token_xx = 'http://121.42.140.86:7003/v2/'

# openplatform 线下地址,默认
openplatform_url = 'http://dev-gate.dding.net:7080'

# openplatform 线上地址
openplatform_url_on = 'https://open.dding.net'

# openplatform 商户账号密码,线下 默认
user_name_openplatform = '18588888888'
user_pwd_openplatform = '123456'

# openplatform 商户账号密码,线上
user_name_openplatform_on = '18566666666'
user_pwd_openplatform_on = '123456'

# 测试环境地址
login_url = 'http://yundingsaastest.dding.net:9012/theme/login.html'

# 2.0 线下 18566666666(9012)
client_id_20_off = '30b8bc367b993b52561d25f9'
client_secret_20_off = '3a94d3d5c190ffd6b1645701f5e2a4f0'

# 3.0 线下(默认) 18566666668
client_id = 'f944be7c64c64e497f7f18c7'
client_secret = '1913700c6e0639fa45261c1a63aed8f3'
# 3.0 线下 18566260535
# client_id = 'da1a90423126757fbc16d5f0'
# client_secret = 'e590a100b8eac34b3b66643cf74be4d0'

# 3.0 线上 18566666666
client_id_30_on = 'dee87a498ab925f6064772b9'
client_secret_30_on = 'a5a605520e2d2830a0ac7a6a58a5be85'

# 3.0 线上 18566260535
# client_id_30_on = '8a2dd447f145c30ec642c818'
# client_secret_30_on = 'c103ebd29d15f981146df864456e51541e740052'

# liuyue 3.0 线上
# client_id_30_on = 'c516b1cbe9e3d752fc148836'
# client_secret_30_on = '6185820c317587df50a8783bd29ec13e'

# 2.0 线上迁移商户 18598765432
# client_id_20_xx = 'd92c8fe35fdbb1c82957c6c8'
# client_secret_20_xx = '13be593ead96d7ecf237dd75e7b22b6f'

# 2.0 线上 18566666666
client_id_20_on = '0c401ea67e0ee0f5d8523c7d'
client_secret_20_on = 'd1c14be9774c1c20ad7423dd3482efc1'

# 2.0 线上 蘑菇对接商户 迁移
# client_id_20_xx = '542a2f9e3764956478c76113'
# client_secret_20_xx = '7c6ff8908726fac28b0743899cad4ba0'

# 2.0 线下迁移商户 18587654321
# client_id_xx = '4d0dd3b71aa7970f1a982325'
# client_secret_xx = '38253f72833ace4820deeda4e233337d'

# 2.0 线上迁移商户 yaos 15989486910
# client_id_20_xx = '48db710db57c3d8a00e56ca3'
# client_secret_20_xx = '67a427131625749c29e97797a8f43c5c'

# 2.0 线上 liuy 18076488260
# client_id_20_xx = '0760b31b9a86d901d396d181'
# client_secret_20_xx = 'fb9218c3cc8ae69ab4d61b9e5cd8b1f7'

# 3.0 线下 yangs 11066660028
client_id_xx = 'e035cd987c5a9d77de47d525'
client_secret_xx = '69c933271092886dab3c294b6349a515'

# self
access_token_r = ''
# 3.0 线下
access_token_30_off = 'a4f16d94b554eba2aa12abde0afffa4ad6f423336debd161c0de1c57faff67919ec156606107db524dbf37050b92e427f625f368fa0f4a9b2d5d9ac0f1447281'
# 3.0 线上
access_token_30_on = 'e3403c44a56a1b8142bcd1d7534ca9597e4a50152243cf224e50bf0564816d626331ca7c86bf29fa50ba549410e9571b2faf35e7a0b360424fd9e934275d303b'
# 2.0 线下
access_token_20_off = 'e18206e633f8af9ba55c6df7365717f67d27e09b197850e021a764abdd822045e281c611635795e068c5d88ce42ac31e82beb1311b474680cc63db7c8db69d94'
# 2.0 线上
access_token_20_on = '1d44081afdfe5efa7f888eeaf9552fee50e9cfda987cb279139d5a681054e4fa6a051c4ba545d0aed0d0d289f38cb40b7acfdeb46b000153301a1dd68f85321d'
# 2.0 迁移商户 18512344321
access_token_xx = '749783fc3e6c319951465207c3179f35eabc0474cfc9b30ed00297c002eda6908d4b3cf2fa6bacbd174954d56df25e5e7e7abbf97f47e5b576963eb50eac054f'
# 3.0 线下 sdk
access_token_sdk_30_off = 'caa7f2974a89e95c6d7fe683769ed9cd926a8519951a50dfc5d4c2073701557a9d7cbbbb4866ecee554439080c176fad4df4f23eeabb2da6323abaf48f8b0c6c'
