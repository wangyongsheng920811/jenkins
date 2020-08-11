from API_CG.lib.common_func import *


def get_dict_by_key(key, value, dict_arr):
    for dict in dict_arr:
        if dict[key] == value:
            return dict
    return False


def get_home_list(param={}):
    res = get_response(url='/v3/homes', do='get', param=param, headers=headers_fe, address=config.saas3_api, print_resp=1, description='刷新房源列表')
    assert check_res(res=res, check_str='0', if_print=0)
    set_value('home_list', res['result']['homes'])


def get_home(param):
    set_value('home', get_dict_by_key(key='home_name', value=param['home_name'], dict_arr=get_value('home_list')))
    print_write('----------------------------------------\n获取房源信息:', get_value('home'), '\n-----------------------------------------')


def get_room_list(param={}):
    if 'home_name' in param.keys():
        get_home({'home_name': param['home_name']})
    res = get_response(url='/v3/homes/%s/rooms' % (get_value('home')['id']), do='get', param={}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='刷新房间列表')
    assert check_res(res, '0', if_print=0)
    set_value('room_list', res['result'])


def get_room(param):
    set_value('room', get_dict_by_key(key='room_name', value=param['room_name'], dict_arr=get_value('room_list')))
    print_write('----------------------------------------\n获取房间信息:', get_value('room'), '\n-----------------------------------------')


def add_rooms_1(param):
    get_home({'home_name': param['home_name']})
    # 生成房间列表,并添加到指定房源
    url = '/v3/homes/%s/rooms' % (get_value('home')['id'])
    assert get_value('home')['home_type'] in [1, 2], '房源类型错误'
    if get_value('home')['home_type'] == 2:
        room_map = {}
        for floor in range(1, param['floor_num'] + 1):
            rooms = []
            for room in range(1, param['room_num'] + 1):
                rooms.append({'name': str(floor) + '.' + str(room)})
            room_map[floor] = rooms
        req_param = {'room_map': room_map}
    else:
        rooms = []
        for room in range(1, param['room_num'] + 1):
            rooms.append({'name': str(room).rjust(len(str(param['room_num'])), '0')})
        req_param = {'rooms': rooms}
    res = get_response(url=url, do='post', param=req_param, headers=headers_fe, address=config.saas3_api, print_resp=1, description='给房源添加房间(%s)' % (param['home_name']))
    assert check_res(res, '0')

    # 检查房源房间列表,是否与添加的一致
    res = get_response(url=url, do='get', param={}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='检查房源房间列表')
    assert check_res(res, '0')
    set_value('room_list', res['result'])
    if get_value('home')['home_type'] == 2:
        for floor, rooms in room_map.items():
            for room in rooms:
                flag = False
                for return_room in get_value('room_list'):
                    if room['name'] == return_room['room_name'] and floor == return_room['floor'] and return_room['room_type'] == 1:
                        flag = True
                assert flag
                print_write(floor, '楼', room['name'], '房间检查完成')
    else:
        for room in req_param['rooms']:
            flag = False
            for return_room in get_value('room_list'):
                if room['name'] == return_room['room_name'] and return_room['room_type'] == 1 and return_room['floor'] == None:
                    flag = True
            assert flag, room['name'] + '找不到'
            print_write(room['name'], '房间检查完成')

    # 检查公区默认用电设置和房间详情
    get_room({'room_name': '公区'})
    res = get_response(url='/v3/rooms/%s/elemeter_setting' % (get_value('room')['id']), do='get', param={}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='获取公区用电设置')
    assert check_res(res=res, check_str='0')
    ele_setting = res['result']
    assert ele_setting['pay_type']['value'] == 2, '公区默认不是预付费'
    res = get_response(url='/v3/rooms/%s' % (get_value('room')['id']), do='get', param={}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='检查公区详情')
    for key in ['low_warn', 'ele_price', 'overdraft_amount']:
        assert res['result'][key] == ele_setting[key]['parent_value'], '房间详情中字段错误' + key
    assert res['result']['pay_type'] == 2

    # 检查普通房间用电设置和房间详情
    if get_value('home')['home_type'] == 2:
        get_room({'room_name': '2.2'})
    else:
        get_room({'room_name': '01'})
    res = get_response(url='/v3/rooms/%s/elemeter_setting' % (get_value('room')['id']), do='get', param={}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='获取房间用电设置')
    assert check_res(res=res, check_str='0')
    ele_setting = res['result']
    for key in ['low_warn', 'ele_price', 'overdraft_amount', 'pay_type']:
        assert 'value' not in ele_setting[key].keys(), '房间默认有自定义用电设置' + key
        assert 'parent_value' in ele_setting[key].keys(), '房间没有上一级用电配置' + key
    res = get_response(url='/v3/rooms/%s' % (get_value('room')['id']), do='get', param={}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='检查房间详情')
    for key in ['low_warn', 'ele_price', 'overdraft_amount', 'pay_type']:
        assert res['result'][key] == ele_setting[key]['parent_value'], '房间详情中字段错误' + key


def edit_room(param):
    # 保存房源信息
    if 'home_name' in param.keys():
        get_home_list()
        get_room_list({'home_name': param['home_name']})
    # 获取房间信息
    get_room({'room_name': param['room_name']})
    url = '/v3/rooms/%s' % (get_value('room')['id'])
    res = get_response(url=url, do='put', param={'room_name': param['new_room_name']}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='修改房间信息')
    assert check_res(res=res, check_str='0')

    # 检查房间列表
    old_room = get_value('room')
    get_room_list()
    get_room({'room_name': param['new_room_name']})
    assert get_value('room')['id'] == old_room['id'] and get_value('room')['room_name'] == param['new_room_name'], '检查房间列表不通过'
    print_write('房间列表修改生效！')

    # 检查房间详情
    res = get_response(url=url, do='get', param={}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='检查房间详情')
    assert check_res(res, '0')
    assert res['result']['id'] == get_value('room')['id']
    assert res['result']['room_name'] == param['new_room_name'], '检查房间详情不通过'
    print_write('房间详情检查通过')


def edit_room_ele_setting(param):
    get_room({'room_name': param['room_name']})
    url = '/v3/rooms/%s/elemeter_setting' % (get_value('room')['id'])

    # 更新房间用电配置
    req_param = {'pay_type': param['pay_type'], "low_warn": random.choice([3, 5, 8, 10]), "ele_price": random.randint(10000, 49999) / 10000, "overdraft_amount": random.randint(10000, 99999) / 10000}
    res = get_response(url=url, do='put', param=req_param, headers=headers_fe, address=config.saas3_api, print_resp=1, description='修改房间用电设置')
    if param['pay_type'] == 1 and get_value('room')['room_type'] == 2:
        assert check_res(res, 400904)
        return
    else:
        assert check_res(res, 0)

    # 更新后检查房间用电配置
    res = get_response(url=url, do='get', param={}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='获取房间用电配置')
    assert check_res(res, 0)
    for key in ['pay_type', 'low_warn', 'ele_price', 'overdraft_amount']:
        assert 'value' in res['result'][key].keys(), '设置没有生效' + key
        if req_param['pay_type'] == 2 and key == 'overdraft_amount':
            assert res['result'][key]['value'] == '0.0000', '后付费房间透支额度不是0'
        else:
            assert float(res['result'][key]['value']) == req_param[key], '设置没有生效' + key


def del_room(param):
    get_room({'room_name': param['room_name']})
    res = get_response(url='/v3/rooms/%s' % (get_value('room')['id']), do='delete', param={}, headers=headers_fe, address=config.saas3_api, print_resp=1,
                       description='删除房间(房源:%s,房间:%s)' % (get_value('home')['home_name'], get_value('room')['room_name']))
    assert check_res(res, 0)

    # 刷新房间列表
    get_room_list()
    for room in get_value('room_list'):
        assert room['id'] != get_value('room')['id'], '删除房间失败!'


def bind_elemeter(param):
    get_room({'room_name': param['room_name']})
    url = '/v3/rooms/%s/elemeters' % (get_value('room')['id'])
    req_param = {'sn': param['ele']['sn'], 'description': param['ele']['description']}
    if 'parent_id' in param.keys():
        req_param['parent_id'] = int(param['parent_id'])
    while True:
        res = get_response(url=url, do='post', param=req_param, headers=headers_fe, address=config.saas3_api, print_resp=1,
                           description='绑定电表%s到房源:%s,房间:%s' % (param['ele']['sn'], get_value('home')['home_name'], param['room_name']))
        if res['err_code'] != 0:
            if res['err_code'] == 3050:
                time.sleep(5)
            else:
                exit()
        else:
            break
    assert check_res(res=res, check_str='0')
    process_id = int(res['result']['process_id'])
    start_time = time.time()
    # 轮询
    while True:
        res = get_response(url=url + '/check', do='post', param={'sn': param['ele']['sn'], 'process_id': process_id}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='轮询')
        end_time = time.time()
        if res['result']['status'] == 2:
            print_write(param['ele']['sn'], ' 绑定成功!')
            print_write('绑定用时：', str(int(end_time - start_time)), 'S')
            break
        # 轮询超时后重绑
        if end_time - start_time > 180:
            print_write(param['ele']['sn'], ' 绑定超时!')
            while True:
                res = get_response(url=url, do='post', param=req_param, headers=headers_fe, address=config.saas3_api, print_resp=1,
                                   description='绑定电表%s到房源:%s,房间:%s' % (param['ele']['sn'], get_value('home')['home_name'], param['room_name']))
                if res['err_code'] != 0:
                    if res['err_code'] == 3050:
                        time.sleep(5)
                    else:
                        exit()
                else:
                    break
            assert check_res(res=res, check_str=0)
            process_id = int(res['result']['process_id'])
            start_time = time.time()
        time.sleep(3)

    # 绑定成功后检查房源设备列表
    res = get_response(url='/v3/homes/%s/devices' % (get_value('home')['id']), do='get', param={}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='检查房源设备列表')
    home_devs = res['result']
    dev_flag = False
    for dev in home_devs:
        if param['ele']['sn'] == dev['sn'] and param['ele']['description'] == dev['description']:
            print_write('房间找到设备:', dev)
            dev_flag = True
    assert dev_flag == True, '房源找不到绑定设备'

    # 检查房间设备列表
    res = get_response(url='/v3/rooms/%s' % (get_value('room')['id']), do='get', param={}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='检查房间设备列表')
    room_devs = res['result']['devices']
    dev_flag = False
    for dev in room_devs:
        if param['ele']['sn'] == dev['sn'] and param['ele']['description'] == dev['description']:
            print_write('房间找到设备:', dev)
            dev_flag = True
    assert dev_flag == True, '房间找不到绑定设备'


def add_branch(param):
    res = get_response(url='/v3/branches', do='post', param={'name': param['name']}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='创建门店(%s)' % param['name'])
    assert check_res(res=res, check_str=0)
    get_branch_list()
    assert get_dict_by_key(key='id', value=res['result']['branch_id'], dict_arr=get_value('branch_list')), '列表中找不到新增的门店'
    print_write('列表中找到新增门店id')


def get_branch_list(param={}):
    # 获取门店列表
    res = get_response(url='/v3/branches/all', do='get', param={}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='刷新门店列表')
    assert check_res(res, 0)
    res['result'].append({'id': 0, 'name': 'default'})
    set_value('branch_list', res['result'])


def get_branch(param):
    # 获取门店信息
    set_value('branch', get_dict_by_key(key='name', value=param['name'], dict_arr=get_value('branch_list')))


def del_branch(param):
    get_branch(param)
    res = get_response(url='/v3/branches/%s' % str(get_value('branch')['id']), do='delete', param={}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='删除门店')
    assert check_res(res, 0)

    # 确认门店列表中找不到该门店
    flag = False
    res = get_response(url='/v3/branches', do='get', param={'keyword': param['name']}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='搜索门店')
    for branch in res['result']['list']:
        if branch['id'] == get_value('branch')['id']:
            flag = True
    assert not flag, '门店未删除成功'
    print_write('门店已删除')
    # 刷新门店列表
    get_branch_list()


def edit_branch(param):
    update_param = {'name': param['new_name']}
    get_branch({'name': param['branch_name']})
    res = get_response(url='/v3/branches/%s' % (get_value('branch')['id']), do='put', param=update_param, headers=headers_fe, address=config.saas3_api, print_resp=1,
                       description='编辑门店%s名称为%s' % (param['branch_name'], param['new_name']))
    get_branch_list()
    assert get_dict_by_key(key='name', value=param['new_name'], dict_arr=get_value('branch_list')), '修改名称失败'


def update_client_ele_settings(param):
    update_param = {"pay_type": random.choice([1, 2]),
                    "low_warn": random.choice([3, 5, 8, 10]),
                    "ele_price": random.randint(10000, 49999) / 10000,
                    "overdraft_amount": random.randint(10000, 99999) / 10000,
                    'use_pool': False,
                    'pool_area_type': 2,
                    }
    res = get_response(url='/v3/clients/elemeter_setting', do='put', param=update_param, headers=headers_fe, address=config.saas3_api, print_resp=1, description='修改商户用电设置')
    assert check_res(res, 0)

    # 检查修改是否生效
    res = get_response(url='/v3/clients/elemeter_setting', do='get', param=param, headers=headers_fe, address=config.saas3_api, print_resp=1, description='获取商户用电设置')
    assert check_res(res, '0')
    client_ele_settings = res['result']
    assert client_ele_settings['pay_type'] == update_param['pay_type']
    assert client_ele_settings['low_warn'] == update_param['low_warn']
    assert float(client_ele_settings['ele_price']) == update_param['ele_price']
    assert float(client_ele_settings['overdraft_amount']) == update_param['overdraft_amount']
    print_write('商户配置修改成功')
    set_value('client_ele_settings', client_ele_settings)


def get_branch_ele_settings(param, check=True):
    get_branch(param)
    res = get_response(url='/v3/branches/%s/elemeter_setting' % str(get_value('branch')['id']), do='get', param={}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='获取门店用电设置')
    assert check_res(res, 0)
    branch_ele_settings = res['result']
    if check:
        assert 'value' not in [branch_ele_settings['pay_type'].keys(), branch_ele_settings['low_warn'].keys(), branch_ele_settings['ele_price'].keys(), branch_ele_settings['overdraft_amount'].keys()]
        assert branch_ele_settings['pay_type']['parent_value'] == get_value('client_ele_settings')['pay_type']
        assert branch_ele_settings['low_warn']['parent_value'] == get_value('client_ele_settings')['low_warn']
        assert branch_ele_settings['ele_price']['parent_value'] == get_value('client_ele_settings')['ele_price']
        assert branch_ele_settings['overdraft_amount']['parent_value'] == get_value('client_ele_settings')['overdraft_amount']
    set_value('branch_ele_settings', branch_ele_settings)


def update_branch_ele_settings(param):
    get_branch(param)
    update_param = {"pay_type": random.choice([1, 2]),
                    "low_warn": random.choice([3, 5, 8, 10]),
                    "ele_price": random.randint(10000, 49999) / 10000,
                    "overdraft_amount": random.randint(10000, 99999) / 10000,
                    }
    res = get_response(url='/v3/branches/%s/elemeter_setting' % str(get_value('branch')['id']), do='put', param=update_param, headers=headers_fe, address=config.saas3_api, print_resp=1,
                       description='修改门店用电设置时')
    assert check_res(res, 0)

    # 检查更新是否生效
    get_branch_ele_settings(param, check=False)
    assert get_value('branch_ele_settings')['pay_type']['value'] == update_param['pay_type']
    assert float(get_value('branch_ele_settings')['ele_price']['value']) == update_param['ele_price']
    if update_param['pay_type'] == 1:
        assert get_value('branch_ele_settings')['low_warn']['value'] == update_param['low_warn']
        assert float(get_value('branch_ele_settings')['overdraft_amount']['value']) == update_param['overdraft_amount']


def add_home(param):
    get_branch({'name': param['branch_name']})
    provinces, province, cities, city, districts, district = get_province(headers=headers_fe)
    req_param = {
        'home_name': param['home_name'],  # 房源名称
        'branch_id': get_value('branch')['id'],  # 门店ID   0:总店
        'home_type': param['home_type'],  # 房源类型 1:分散  2:集中
        'address': 'address',
        'block': 'block_',
        'district': district['name'],
        'city': city['name'],
        'province': province['name'],
        'country': '中国',
        'description': 'description',
        'alias': param['home_name'],
        'number': 'number',
        'street': '_street_'
    }
    res = get_response(url='/v3/homes', do='post', param=req_param, headers=headers_fe, address=config.saas3_api, print_resp=1, description='新建房源')
    assert check_res(res, 0)

    # 检查新增房源结果
    get_home_list()
    get_home({'home_name': req_param['home_name']})
    assert get_value('home')['home_name'] == req_param['home_name'], '房源名称找不到'
    assert get_value('home')['branch_id'] == req_param['branch_id'], '所属门店不正确'
    assert get_value('home')['home_type'] == req_param['home_type'], '房源类型不正确'


def find_home_by_branch(param):
    get_branch({'name': param['branch_name']})
    res = get_response(url='/v3/homes', do='get', param={'branch_id': get_value('branch')['id']}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='按门店搜索房源')
    assert check_res(res, 0)
    for home_name in param['home_names']:
        flag = False
        for home in res['result']['homes']:
            assert home['branch_id'] == get_value('branch')['id']
            if home['home_name'] == home_name:
                flag = True
        assert flag
        print_write('找到房源', home_name)

        # ['批量修改房源BC,门店为C', '/v3/homes/branch', 'post', {}, '0', 'edit homes branch', {'branch_name': 'default', 'home_names': [home_B, home_C]}],

        #    #     if t == 'edit homes branch':
        #         home_ids = []
        #         homes = get_response(url='/v3/homes', do='get', param={}, headers=headers_fe, address=config.saas3_api, print_resp=1, description='获取房源列表')['result']
        #         for home_name in other_param['home_names']:
        #             home_ids.append(get_dict_by_key(key='home_name', value=home_name, dict_arr=home_list)['id'])
        #         param['branch_id'] = branch_id
        #         param['home_ids'] = home_ids


def edit_homes_branch(param):
    home_ids = []
    get_branch({'name': param['branch_name']})
    for home_name in param['home_names']:
        home_ids.append(get_dict_by_key(key='home_name', value=home_name, dict_arr=get_value('home_list'))['id'])

    update_param = {'branch_id': get_value('branch')['id'], 'home_ids': home_ids}
    res = get_response(url='/v3/homes/branch', do='post', param=update_param, headers=headers_fe, address=config.saas3_api, print_resp=1,
                       description='批量修改房源%s门店为%s' % (param['home_names'], param['branch_name']))
    assert check_res(res, 0)
    get_home_list()
    for home_id in home_ids:
        home = get_dict_by_key(key='id', value=home_id, dict_arr=get_value('home_list'))
        assert home['branch_id'] == get_value('branch')['id'], str(home['home_name'] + ' 修改失败')


def edit_home(param):
    get_home({'home_name': param['home_name']})
    get_branch({'name': param['branch_name']})
    update_param = {'home_name': param['new_name'], 'branch_id': get_value('branch')['id']}
    res = get_response(url='/v3/homes/%s' % str(get_value('home')['id']), do='put', param=update_param, headers=headers_fe, address=config.saas3_api, print_resp=1,
                       description='修改房源:%s' % update_param['home_name'])
    get_home_list()
    get_home({'home_name': param['new_name']})
    assert get_value('home')['home_name'] == param['new_name']
    assert get_value('home')['branch_id'] == get_value('branch')['id']


def get_home_pool_settings(param):
    get_home({'home_name': param['home_name']})
    res = get_response(url='/v3/homes/%s/pool_setting' % get_value('home')['id'], do='get', param={}, headers=headers_fe, address=config.saas3_api, print_resp=1,
                       description='获取房源公摊设置(%s)' % get_value('home')['home_name'])
    if 'pool_settings' in param.keys():
        assert res['result'] == param['pool_settings'], '公摊设置不符合预期'
        print_write('公摊设置符合预期')
    set_value('home_pool_settings', res['result'])


def edit_home_pool_settings(param):
    get_home({'home_name': param['home_name']})
    res = get_response(url='/v3/homes/%s/pool_setting' % str(get_value('home')['id']), do='put', param=param['req_param'],
                       headers=headers_fe, address=config.saas3_api, print_resp=1, description='修改房源公摊设置(%s)' % get_value('home')['home_name'])
    assert check_res(res, 0)
    if 'ratios' in param['req_param'].keys():
        param['req_param'].pop('ratios')
    get_home_pool_settings({'home_name': param['home_name'], 'pool_settings': param['req_param']})


def get_home_ele_settings(param):
    get_home({'home_name': param['home_name']})
    res = get_response(url='/v3/homes/%s/elemeter_setting' % str(get_value('home')['id']), do='get', param={},
                       headers=headers_fe, address=config.saas3_api, print_resp=1, description='获取房源用电设置(%s)' % get_value('home')['home_name'])
    assert check_res(res, 0)
    if 'check' in param.keys():
        if param['check'] == 'check_init':
            for key in res['result']:
                assert 'value' not in res['result'][key].keys(), '房源用电设置没有继承上一级'
                assert 'value' not in res['result'][key].keys(), '房源用电设置没有上一级'
            print_write('房源默认继承上一级用电配置.')
        else:
            assert res['result']['pay_type']['value'] == param['check']['pay_type'], '付费模式与设置的不一致'
            assert float(res['result']['ele_price']['value']) == param['check']['ele_price'], '电价与设置的不一致'
            if param['check']['pay_type'] == 1:
                assert res['result']['low_warn']['value'] == param['check']['low_warn'], 'low_warm设置失败'
                assert float(res['result']['overdraft_amount']['value']) == param['check']['overdraft_amount'], '透支额度设置失败'
            print_write('检查房源用电设置成功.')


def update_home_ele_settings(param):
    get_home({'home_name': param['home_name']})
    res = get_response(url='/v3/homes/%s/elemeter_setting' % str(get_value('home')['id']), do='put', param=param['req_param'],
                       headers=headers_fe, address=config.saas3_api, print_resp=1, description='修改房源用电设置(%s)' % get_value('home')['home_name'])
    assert check_res(res, 0)
    get_home_ele_settings({'home_name': param['home_name'], 'check': param['req_param']})


def add_house_manager(param):
    res = get_response(url='/v3/users', do='post', param=param, headers=headers_fe, address=config.saas3_api, print_resp=1, description='新增管家')
    assert check_res(res, 0)
    set_value('manager_id', res['result']['id'])


def del_house_manager(param):
    res = get_response(url='/v3/users/%s' % str(get_value('manager_id')), do='delete', param=house_manager_A, headers=headers_fe, address=config.saas3_api, print_resp=1, description='删除管家')
    assert check_res(res, 0)


def edit_home_manager(param):
    get_home({'home_name': param['home_name']})
    req_param = {'user_ids': [get_value('manager_id')], 'home_ids': [get_value('home')['id']]}
    res = get_response(url='/v3/homes/users', do='post',
                       param=req_param, headers=headers_fe, address=config.saas3_api, print_resp=1,
                       description='将房源%s分配给管家%s' % (get_value('home')['home_name'], str(get_value('manager_id'))))
    assert check_res(res, 0)

    res = get_response(url='/v3/homes', do='get', param={'user_id': get_value('manager_id')}, headers=headers_fe,
                       address=config.saas3_api, print_resp=1, description='检查管家房源')
    assert check_res(res, 0)
    assert res['result']['count'] == 1
    assert res['result']['homes'][0]['id'] == req_param['home_ids'][0], '房源id不正确'
    assert res['result']['homes'][0]['home_name'] == param['home_name'], '房源名称不正确'
    assert res['result']['homes'][0]['branch_id'] == 0, '门店错误'


def delete_home(param):
    get_home({'home_name': param['home_name']})
    res = get_response(url='/v3/homes/%d' % get_value('home')['id'], do='delete', param={},
                       headers=headers_fe, address=config.saas3_api, print_resp=1, description='删除房源%s' % get_value('home')['home_name'])
    assert check_res(res, 0)
    get_home_list()
    assert not get_dict_by_key(key='home_name', value=param['home_name'], dict_arr=get_value('home_list')), '删除房源失败'
