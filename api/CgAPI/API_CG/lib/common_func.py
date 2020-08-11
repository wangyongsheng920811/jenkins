import sys, os, re, unittest, time, requests, json, psycopg2, random, string, smtplib
from API_CG.lib.api_config import *
from API_CG.lib.global_var import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from HTMLTestRunner_PY3 import HTMLTestRunner
import API_CG.lib.ddt as ddt

requests.packages.urllib3.disable_warnings()


def print_write(*args, path=path, if_print=1, changeline=1, sep='\t', color='black'):
    # 打印字符串并保存到指定文件
    final_string = ''
    for i in args:
        if type(i) == dict:
            # i = json.dumps(i,indent=4,ensure_ascii=False).replace('\'', '\"')
            i = str(i).replace('\'', '\"')
        final_string = final_string + str(i) + sep
    if if_print == 1:
        final_string_print = final_string
        if color == 'red': final_string_print = '\033[1;31;43m' + final_string + '\033[0m'
        if color == 'blue': final_string_print = '\033[1;34m' + final_string + '\033[0m'
        if color == 'green': final_string_print = '\033[1;32m' + final_string + '\033[0m'
        print(final_string_print)
    f = open(path, 'a')
    if changeline == 1:
        f.write((final_string + '\n').encode("gbk", 'ignore').decode("gbk", "ignore"))
    else:
        f.write(final_string.encode("gbk", 'ignore').decode("gbk", "ignore"))
    f.close()


def clear_file(path=path):
    # 清空指定文件
    try:
        f = open(path, 'r+');
        f.truncate();
        f.close()
    except:
        print('清空文件失败')


# 生成随机6位数,返回整型
def get_numbers(length=6):
    str_tmp = ""
    while len(str_tmp) < length:
        # ch = random.randint(0, 9)
        # str_tmp += str(ch)
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        str_tmp += ch
        # 第一位不能为0，为0则重新开始生成
        if str_tmp[0] == '0':
            str_tmp = ""
    return int(str_tmp)


def sort_apis(apis):
    # 将统计的测试接口去重
    new_apis = []
    for api in apis:
        ids = re.findall('/lkjl\d+?$', api)
        for id in ids:
            api = api.replace(id, '/sn')

        ids = re.findall('/\d+?/', api)
        for id in ids:
            api = api.replace(id, '/id/')

        ids = re.findall('/\d+?$', api)
        for id in ids:
            api = api.replace(id, '/id')
        api = api.replace('/test', '/id')
        new_apis.append(api)
    return set(new_apis)


def send_result_email(report_path, log_path, email_text, subjuect='SAAS_API', email_sender=sender, email_receiver=receiver, server=smtpserver, pwd=password):
    # 将测试报告和日志发送到指定邮箱
    msg = MIMEMultipart()
    msg.attach(MIMEText(email_text))
    att1 = MIMEText(open(report_path, 'rb').read(), 'base64', 'utf-8')
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'
    msg.attach(att1)
    att2 = MIMEText(open(log_path, 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="test.log"'
    msg.attach(att2)
    msg['from'] = email_sender
    msg['to'] = ','.join(email_receiver)
    msg['subject'] = subjuect
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp = smtplib.SMTP()
    smtp.connect(server, 80)
    smtp.login(sender, pwd)
    smtp.sendmail(sender, receiver, msg.as_string())
    time.sleep(2)
    smtp.quit()
    smtp.close()


def find_case(file_names, find_path):
    # path = '../test_case'
    allsuite = unittest.TestSuite()
    for name in file_names:
        suite = unittest.defaultTestLoader.discover(start_dir=find_path, pattern=name, top_level_dir=find_path)
        for s in suite:
            for case in s:
                allsuite.addTest(case)
    return allsuite


def get_email_text(report_path, use_time):
    try:
        f = open(report_path, 'r', encoding='UTF-8')
        report_info = f.read()
        f.close()
        suc = re.findall('通过.*?(\d+)', report_info)[0]
    except:
        suc = 0
    try:
        fail = re.findall('失败.*?(\d+)', report_info)[0]
    except:
        fail = 0
    api_text = ''
    apis = sort_apis(get_value('apis'))
    for api in apis:
        api_text = api_text + '\n\t' + api
    email_text = '本次测试结果如下:\n\t通过:' + str(suc) + '\n\t失败:' + str(fail) + '\n\t测试时长:' + str(use_time) + 'S\n\t覆盖接口 ' + str(len(apis)) + ' 个:' + api_text
    return email_text


def get_run(file_names=[]):
    # t1 = time.time()
    realpath = os.path.split(os.path.realpath(__file__))[0]  # 获取当前py文件所在目录
    report = os.path.join(realpath + '/../Run_case/Report.html')  # 指定生成报告目录
    # 执行用例并保存报告
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, verbosity=2, title='3.0_api test_report', description='李飞超')
        cases = find_case(file_names=file_names, find_path=realpath + '/../test_case')
        result = runner.run(cases)
    # total_time = int(time.time() - t1)
    # 发送通知邮件
    # result_text = get_email_text(report_path=report, use_time=total_time)
    # send_result_email(report_path=report, log_path=realpath + '/test.log', email_text=result_text)
    # print_write(result_text)
    # if result.failure_count or result.error_count:
    #     dd_robot(result.success_count, result.failure_count, result.error_count)


def dd_robot(success_count, failure_count, error_count):
    # hook = r'https://oapi.dingtalk.com/robot/saccess_token=dc7c20ebd64bb47c4d9e70577f2b7e443b53fca7b7aa4235dfb6a1a78186f022'
    hook = r'https://oapi.dingtalk.com/robot/send?access_token=78334506e004db8ed3129324c0877326ca3c342b87b62f4bb34daa03aeec0fd1'
    # report_url = 'http://qa-ci.dding.net:8081/jenkins/view/5.0/job/hyperloop-auto-test-pipelHyperloop_20Test_20Report'
    content = '''
        SaaSApi接口自动化:  成功: {},  失败: {},  错误: {}
        点击查看详情
        '''.format(success_count, failure_count, error_count)
    atMobiles = '18640573589'
    message = {
        'msgtype': 'text',
        'text': {'content': content},
        'at': {'atMobiles': [atMobiles], 'isAtAll': False}
    }
    requests.post(url=hook, json=message)


def sort_time(timestamp):
    if timestamp < 0 or timestamp > 9990842478504:
        return str(timestamp)
    if timestamp > 9990842478:
        timestamp = int(timestamp / 1000)
    time_local = time.localtime(timestamp)
    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return dt


# def play_music(path='d:\\src\\dingdong.mp3', play_time=3):
#     pygame.mixer.init()
#     pygame.mixer.music.load(path)
#     pygame.mixer.music.play()
#     time.sleep(play_time)
#     pygame.mixer.music.stop()


def mkdir(path):
    # 去除首位空格
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        os.makedirs(path)
        return True


def del_files(dir):
    files = os.listdir(dir)
    for file in files:
        os.remove(dir + '/' + file)


def get_headers(user, url, from_int=2):
    # 通过passport接口获取access_token
    login_param = {'name': user[0], 'pass': user[1], 'from': from_int}
    login_headers = {'Origin': 'http://local.dding.cn', 'Content-Type': 'application/json;charset=UTF-8'}
    res = requests.post(url=url, data=json.dumps(login_param), headers=login_headers, verify=False)
    print_write('\n获取token:\turl:\t', url, if_print=0)
    print_write('获取token:\tparam:\t', login_param, if_print=0)
    print_write('获取token:\trequest_header:\t', login_headers, if_print=0)
    print_write('获取token:\tstatus_code:\t', res.status_code, if_print=0)
    print_write('获取token:\tresponse_headers:\t', res.headers, if_print=0)
    print_write('获取token:\tresp:\t', res.json(), if_print=0)

    # 拼接请求头
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
               'Accept': 'application/json, text/plain, */*',
               'Content-Type': 'application/json; charset=UTF-8',
               'Connection': 'keep-alive',
               'Cookie': res.headers['set-cookie']
               }
    if from_int == 1:
        headers.update({'YD-App': 'ydapp_az'})
    return headers


def check_res(res, check_str='', if_print=1):
    if check_str == '':
        return True
    check_str = str(check_str)
    if check_str.isdigit():
        if 'err_code' in res.keys():
            check_str = 'res["err_code"]==' + check_str
        else:
            check_str = 'res["ErrNo"]==' + check_str
    if check_str == '!0':
        if 'err_code' in res.keys():
            check_str = 'res["err_code"]!=0'
        else:
            check_str = 'res["ErrNo"]!=0'
    if 'err_code' in res.keys():
        if res['err_code'] < 1000 and res['err_code'] != 0:
            print_write('Commen error!')
            return False
    if if_print == 1:
        print_write('预期:', check_str)
    try:
        exec('flag = (' + str(check_str) + ')')
    except:
        print_write('判断语句错误!')
        exit(99)
    if locals()['flag'] == True:
        return True
    else:
        return False


def get_response(url, do, address, headers={}, param={}, print_resp=0, description='----', time_out=200, log_path=path, **args):
    new_apis = get_value('apis')
    new_apis.append(do + ':' + url)
    set_value('apis', new_apis)
    url = address + url
    t1 = time.time()
    if do == 'get':
        response = requests.get(url=url, params=param, headers=headers, verify=False)
    elif do == 'post':
        if 'file' in args.keys():
            response = requests.post(url=url, headers=headers, verify=False, files=args['file'])
        else:
            response = requests.post(url=url, json=param, headers=headers, verify=False)
    elif do == 'put':
        response = requests.put(url=url, json=param, headers=headers, verify=False)
    elif do == 'delete':
        response = requests.delete(url=url, params=param, headers=headers, verify=False)
    else:
        print("请求方法错误!")
    t2 = time.time()
    try:
        print_write('\n--------' + description + '(' + get_time_str(t1) + ')' + '--------',
                    '\nstatus_code:\t', response.status_code,
                    '\nmethod:\t', do,
                    '\nurl:\t', response.url,
                    '\nparam:\t', param,
                    '\nrequest_headers\t', headers,
                    # '\nresp:\t', json.dumps(response.json(), indent=4, ensure_ascii=False),
                    '\nresp:\t', response.json(),
                    '\nuse_time\t', t2 - t1,
                    '\n----------------------------------------------\n',
                    if_print=print_resp, path=log_path)
    except:
        print_write('请求失败,重试...', color=color3)
        time.sleep(3)
        return get_response(url=url.replace(address, ''), do=do, param=param, print_resp=print_resp, description=description,
                            headers=headers, address=address, time_out=time_out)
    assert t2 - t1 < time_out, 'Time out!!!!!!'
    if t2 - t1 >= time_out:
        print_write(url, '     time out!!!!!!!')
    return response.json()


# 获取openapi_token
def get_token(client_id, client_secret, address, print_resp=1):
    param = {'client_id': client_id, 'client_secret': client_secret}
    res = get_response(url='/access_token', param=param, do='post', headers=headers_without_token, address=address, description='openapi获取token', print_resp=print_resp)
    return res['access_token']


def get_string(length):
    return ''.join(random.sample(string.ascii_letters + string.digits, length))


def get_values(rule, description):
    values = []
    for right_value in rule['right_values']:
        values.append([right_value, description + rule['name'] + '参数正确:' + str(right_value), '0'])
    values.append([None, description + rule['name'] + '参数缺失', str(rule['must'])])
    if 'wrong_values' in rule.keys():
        for wrong_value in rule['wrong_values']:
            values.append(
                [wrong_value[0], description + rule['name'] + '参数错误:' + str(wrong_value[0]), str(wrong_value[1])])
    if rule['type'] == 'str':
        if 'not_check_type' not in rule.keys():
            values.append([123, description + rule['name'] + '类型错误', '400000'])
        if 'range' in rule.keys():
            values.append([get_string(rule['range'][0] - 1), description + rule['name'] + '范围错误', '400000'])
            values.append([get_string(rule['range'][0]), description + rule['name'] + '最小值', '0'])
            values.append([get_string(rule['range'][1]), description + rule['name'] + '最大值', '0'])
            values.append([get_string(rule['range'][1] + 1), description + rule['name'] + '范围错误', '400000'])
    elif rule['type'] == 'int':
        if 'not_check_type' not in rule.keys():
            values.append(['test', description + rule['name'] + '类型错误', '400000'])
        if 'range' in rule.keys():
            values.append([rule['range'][0] - 1, description + rule['name'] + '范围错误', '400000'])
            values.append([rule['range'][0], description + rule['name'] + '最小值', '0'])
            values.append([rule['range'][1], description + rule['name'] + '最大值', '0'])
            values.append([rule['range'][1] + 1, description + rule['name'] + '范围错误', '400000'])
    new_values = []
    new_values1 = []
    for value in values:
        if value[0] not in new_values1:
            new_values1.append(value[0])
            new_values.append(value)
    return new_values


def get_param(rules=[], desc=''):
    results = []
    url_flag = False
    if 'url' in rules[0].keys() and 'method' in rules[0].keys():
        url, method = rules[0]['url'], rules[0]['method']
        url_flag = True
    for rule in rules:
        locals()[rule['name']] = get_values(rule, desc)
    for rule in rules:
        for value in locals()[rule['name']]:
            # print_write(locals()[rule['name']])
            locals()['result' + rule['name'] + str(value[0])] = {}
            for x in rules:
                if x['name'] == rule['name']:
                    # if value[0] != None:
                    locals()['result' + rule['name'] + str(value[0])].update({x['name']: value[0]})
                else:
                    locals()['result' + rule['name'] + str(value[0])].update({x['name']: locals()[x['name']][0][0]})
            empty_keys = []
            # print_write(value, locals()['result' + rule['name'] + str(value[0])])
            for key in locals()['result' + rule['name'] + str(value[0])].keys():
                if locals()['result' + rule['name'] + str(value[0])][key] == None:
                    empty_keys.append(key)
            for empty_key in empty_keys:
                locals()['result' + rule['name'] + str(value[0])].pop(empty_key)
            if url_flag:
                # print_write(value, locals()['result' + rule['name'] + str(value[0])])
                results.append([value[1], locals()['result' + rule['name'] + str(value[0])], value[2], url, method])
            else:
                # print_write(value,locals()['result' + rule['name'] + str(value[0])])
                results.append([value[1], locals()['result' + rule['name'] + str(value[0])], value[2]])
    new_results = []
    new_results2 = []
    for result in results:
        if result[1] not in new_results2:
            new_results2.append(result[1])
            new_results.append(result)
    return new_results


def get_province(headers):
    res = get_response(url='/v3/provinces', do='get', headers=headers, address=config.saas3_api, description='获取省份列表')
    assert res['err_code'] == 0 and len(res['result']) > 10
    provinces = res['result']
    while True:
        province = random.choice(provinces)
        res = get_response(url='/v3/cities', do='get', param={'province_id': province['id']}, headers=headers, address=config.saas3_api, description='获取城市列表')
        assert res['err_code'] == 0 and len(res['result']) > 0
        cities = res['result']
        city = random.choice(cities)
        res = get_response(url='/v3/districts', do='get', param={'city_id': city['id']}, headers=headers, address=config.saas3_api, description='获取区域列表')
        assert res['err_code'] == 0
        if len(res['result']) > 0:
            districts = res['result']
            district = random.choice(districts)
            break
        print_write('城市区域为空,重新获取...')
    return provinces, province, cities, city, districts, district


def new_branch(name, headers):
    res = get_response(url='/v3/branches', do='post', param={'name': name}, headers=headers, address=config.saas3_api,
                       description='创建门店(' + name + ')')
    try:
        branch_id = res['result']['branch_id']
        branch = {'name': name, 'id': branch_id}
    except:
        print_write('创建门店失败:', res)
        exit(998)
    return branch


def new_home(headers, name='test', type=1, branch_id=None, home_address='测试地址', block='测试小区', district='南山区', city='深圳市',
             province='广东省', description='描述', alias='别名', number='门牌号', street='街道', address=''):
    param = {
        'home_name': name,
        'branch_id': branch_id,
        'home_type': type,
        'address': home_address,
        'block': block,
        'district': district,
        'city': city,
        'province': province,
        'country': '中国',
        'description': description,
        'alias': alias,
        'number': number,
        'street': street
    }
    if branch_id == None:
        param.pop('branch_id')
    res = get_response(url='/v3/homes', do='post', param=param, headers=headers, address=address
                       , description='创建房源(' + name + ')')
    try:
        home = res['result']
    except:
        print_write('创建房源失败:', res)
    home.update({'name': name, 'alias': alias})
    return home


def add_rooms(home_id, room_num, headers):
    url = '/v3/homes/' + str(home_id) + '/rooms'
    rooms = []
    for i in range(1, room_num + 1):
        rooms.append({'name': str(i).rjust(len(str(room_num)), '0')})
    param = {'rooms': rooms}
    res = get_response(url=url, do='post', param=param, headers=headers, address=config.saas3_api,
                       description='给房源' + str(home_id) + '新增房间' + str(room_num) + '个')
    assert check_res(res=res, check_str='0', if_print=0)


def new_renter(name, phone, headers):
    param = {'name': name, 'phone': phone}
    res = get_response(url='/v3/tenants', param=param, do='post', address=config.saas3_api, headers=headers, description='添加测试租客')
    print(res)
    assert check_res(res=res, check_str='0', if_print=0)
    return res['result']['tenant_id']


def del_test_data(headers):
    home_ids = []
    empty_home_ids = []
    limit = 50
    offset = 0
    print_write('---开始清除测试数据.')
    # 获取所有房源id
    while True:
        res = get_response(url='/v3/homes', do='get', param={'limit': limit, 'offset': offset}, headers=headers, address=config.saas3_api, description='获取房源列表')
        assert check_res(res=res, check_str='0', if_print=0)
        for home in res['result']['homes']:
            home_ids.append(home['id'])
        if len(res['result']['homes']) != limit:
            assert len(home_ids) == res['result']['count']
            break
        else:
            offset = offset + limit
    # print_write('所有房源:', home_ids)

    # 找到测试amg并解绑
    for home_id in home_ids:
        res = get_response(url='/v3/homes/' + str(home_id) + '/rooms', do='get', param={'with_device': 1}, headers=headers, address=config.saas3_api, description='获取房源列表')
        room_list = res['result']
        for room in room_list:
            devs = room['devices']
            for dev in devs:
                if dev['sn'] == config.amg['sn']:
                    amg_room_id = room['id']
                    res = get_response(url='/v3/rooms/' + str(amg_room_id) + '/elemeters/' + str(config.amg['id']), do='delete', address=config.saas3_api, description='解绑测试amg', headers=headers_fe)

    # 筛选出没有设备和租客的房源id
    res = get_response(url='/v3/homes/rooms', do='get', param={'home_ids': str(home_ids)}, headers=headers, address=config.saas3_api, description='筛选空房源')
    assert check_res(res=res, check_str='0', if_print=0)
    for home_id in home_ids:
        # 跳过指定房源
        if home_id in [477038977, 881137972, 1060510172]:
            continue
        is_empty = 1
        home = res['result'][str(home_id)]
        for room in home:
            if room['has_device'] != False or room['has_tenant'] != False:
                is_empty = 0
        if is_empty == 1:
            empty_home_ids.append(home_id)

    # 批量删除筛选出的房源
    for home_id in empty_home_ids:
        res = get_response(url='/v3/homes/' + str(home_id), do='delete', param={}, headers=headers, address=config.saas3_api, description='删除空房源(' + str(home_id) + ')')
        assert check_res(res=res, check_str='0', if_print=0)
        # print_write('删除房源成功:', home_id, if_print=1)
    # 删除所有可删除的门店
    res = get_response(url='/v3/branches', do='get', param={'offset': 0, 'limit': 10, 'keyword': ''}, headers=headers, address=config.saas3_api, description='获取门店列表')
    assert check_res(res=res, check_str='0', if_print=0)
    branches = res['result']['list']
    for branch in branches:
        if branch['id'] in [1602444227]:
            continue
        res = get_response(url='/v3/branches/' + str(branch['id']), do='delete', param={}, headers=headers, address=config.saas3_api, description='尝试删除门店(' + str(branch['id']) + ')')

    # 删除所有可删除的租客
    empty_ids = []
    res = get_response(url='/v3/tenants', do='get', param={'limit': 10000}, headers=headers, address=config.saas3_api, description='获取租客列表')
    assert check_res(res=res, check_str='0', if_print=0)
    for renter in res['result']['list']:
        if renter['lease'] != True:
            empty_ids.append(renter['id'])
    del_num = 0
    for id in empty_ids:
        res = get_response(url='/v3/tenants/' + str(id), do='delete', param={}, headers=headers, address=config.saas3_api, description='删除租客(' + str(id) + ')')
        assert check_res(res=res, check_str='0', if_print=0)
        del_num = del_num + 1
    print_write('---清除测试数据完成.')


# 数据库查询
def query_db(query_sql, database='saas_migrate', user='dev_saas_migrate', password='kkk7UNJnmkjjjbvv',
             host='pgm-bp11y8ho614t6ka67o.pg.rds.aliyuncs.com', port='3432', if_print=0):
    print_write('--------\nsql:\t', query_sql, if_print=if_print)
    conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
    cursor = conn.cursor()
    cursor.execute(query_sql)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    print_write('res:\t', result, '\n--------\n', if_print=if_print)
    return result


def get_time_str(timestamp=0, format="%Y-%m-%d %H:%M:%S"):
    timestamp = int(timestamp)
    if timestamp < 0 or timestamp > 9990842478504:
        return str(timestamp)
    if timestamp > 9990842478:
        timestamp = int(timestamp / 1000)
    time_local = time.localtime(timestamp)
    # print(time_local)
    dt = time.strftime(format, time_local)
    return dt


def get_device_info_from_paas(uuid, user_id):
    res = get_response(url='/get_device_info', do='get', param={'UserId': user_id, 'UUID': uuid}
                       , description='paas获取电表信息', headers=headers_without_token
                       , address='http://dev-gate.dding.net:4086')
    dev = res['device']
    dev_info = {
        '设备SN号': dev['hardware_info']['sn'],
        '绑定时间': sort_time(dev['bind_time']),
        '在线状态': str(dev['onoff_line']),
        '在线状态更新时间': sort_time(dev['onoff_time']),
        '电表读数': str(dev['consume_amount']),
        '读数更新时间': sort_time(dev['consume_amount_time']),
        '充值电量': str(dev['power_total']),
        '电量更新时间': sort_time(dev['power_total_time']),
        '透支额度': str(dev['overdraft']),
        '透支额度更新时间': sort_time(dev['overdraft_time']),
        '充值状态': dev['charge_stage'],
        '充值状态更新时间': sort_time(dev['charge_stage_time']),
        '本地合闸': str(dev['enable_state']),
        '本地合闸更新时间': sort_time(dev['enable_state_time']),
        '预期合闸': str(dev['control_switch']),
        '电表剩余电量': float(dev['power_total']) - float(dev['consume_amount'])
    }
    return dev, dev_info


def get_home_rooms(home_id, headers, with_device=None, with_tenant=None):
    res = get_response(url='/v3/homes/' + str(home_id) + '/rooms', do='get', param={'with_device': with_device, 'with_tenant': with_tenant}, headers=headers, address=config.saas3_api,
                       description='获取房间id')
    assert check_res(res, '0', if_print=0)
    return res


def get_key_secret_saas2(telephone):
    print_write('login....')
    manager_headers = get_headers(user=['15989486910', 'qwert12345'], url='https://passport.dding.net/login')
    res = get_response(url='/api/v1/get_client_by_user', address=config.saas2_api_offline, do='get', param={'user_id': telephone}, headers=manager_headers, description='获取商户信息')
    return res['client']['client_key'], res['client']['client_secret']


def get_key_secret_saas3(telephone):
    query_result = query_db(query_sql='SELECT "client".client_key,"client".client_secret FROM "user","client" '
                                      'where "user".client_id="client"."id"  AND "client".status=1'
                                      'AND "user".status=1 AND  "user".telephone = \'' + str(telephone) + '\'')
    return query_result[0][0], query_result[0][1]


clear_file()
if get_value('environment') == 'onoffline=on':
    print_write('线上环境!')
    config = On_config
elif get_value('environment') == 'onoffline=qa-off':
    print_write('线下环境2!')
    config = Qa_config
else:
    print_write('线下环境1!')
    config = Off_config

headers_fe = get_headers(user=config.user_fe, url=config.passport)
headers_manage = get_headers(user=config.user_manage, url=config.passport)
headers_install_app = get_headers(user=config.user_install, from_int=1, url=config.passport)
# key, sec = get_key_secret_saas3(config.user_fe[0])
# openapi_token = get_token(client_id=key, client_secret=sec,address=config.saas3_openapi ,print_resp=0)
