from API_CG.lib.common_func import *
# ready = True
if 'ready' not in globals().keys():
    del_test_data(headers=headers_fe)
    print_write('---开始准备测试数据.')
    # 接口自动化,通用变量定义
    renter_idcard_root = '4303041949090900'
    renter_phone_root = '110868600'
    renter_name_root = 'renter_'
    branch_root = 'branch_'
    home_name_root = 'home_'
    # 初始数据生成
    provinces, province, cities, city, districts, district = get_province(headers=headers_fe)
    branch = new_branch(name=branch_root + 'static', headers=headers_fe)
    branch_update = new_branch(name=branch_root + 'update', headers=headers_fe)
    branch_delete = new_branch(name=branch_root + 'delete', headers=headers_fe)
    home = new_home(name=home_name_root + 'static', alias=home_name_root + 'static', headers=headers_fe, address=config.saas3_api)
    home_update = new_home(name=home_name_root + 'update', alias=home_name_root + 'update', headers=headers_fe, address=config.saas3_api)
    home_delete = new_home(name=home_name_root + 'delete', alias=home_name_root + 'delete', headers=headers_fe, address=config.saas3_api)
    add_rooms(home_id=home['home_id'], room_num=20, headers=headers_fe)
    add_rooms(home_id=home_update['home_id'], room_num=20, headers=headers_fe)
    add_rooms(home_id=home_delete['home_id'], room_num=20, headers=headers_fe)
    rooms = get_home_rooms(home_id=home['home_id'], headers=headers_fe)['result']
    rooms_delete = get_home_rooms(home_id=home_update['home_id'], headers=headers_fe)['result']
    renter_66 = new_renter(name=renter_name_root + '66', phone='11086870096', headers=headers_fe)
    renter_67 = new_renter(name=renter_name_root + '67', phone='11086870097', headers=headers_fe)
    renter_68 = new_renter(name=renter_name_root + '68', phone='11086870098', headers=headers_fe)
    print_write('---准备测试数据完成.')
    ready = True
