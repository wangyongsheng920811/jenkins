from OpenAPI.Data.source_data.source_new_add_data import *
from OpenAPI.Lib.get_data_list import *
from OpenAPI.Lib.run_case import *

'''
蘑菇对接新增三个接口
get_client_setting  获取商户设置
get_home_setting    获取公摊设置
get_elecollector_info   获取采集器信息

线下杨思账号（迁移）
home_id = '5bf512017581fc6191035206'
elecollector_uuid = '08e37f273d6f02c07463528c0f88b3f8'

线上蘑菇对接账号
home_id = '5bf22a8a80269a1504a7c700'
elecollector_uuid = 'd64f62bdc85eace78726d0035265c017'

qianyi
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

yangs
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

# 获取商户设置
empty_file('get_client_setting_cmd')
get_client_setting_class = GetDataList(right_get_client_setting, wrong_get_client_setting, [], get_client_setting, 'get')
get_client_setting_cmd = get_client_setting_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(get_client_setting_cmd)

# 获取公摊设置
empty_file('get_home_setting_cmd')
get_home_setting_class = GetDataList(right_get_home_setting, wrong_get_home_setting, [], get_home_setting, 'get')
get_home_setting_cmd = get_home_setting_class.get_all_http_cmd([0], [14001, 15006, 15006, 14001])
# write_print_list_dic(get_home_setting_cmd)

# 获取采集器信息
empty_file('get_elecollector_info_cmd')
get_elecollector_info_class = GetDataList(right_get_elecollector_info, wrong_get_elecollector_info, [], get_elecollector_info, 'get')
get_elecollector_info_cmd = get_elecollector_info_class.get_all_http_cmd([0], [0, 0, 0, 15006, 15006, 0])
get_elecollector_info_cmd.append([get_elecollector_info, get_elecollector_info + '-F-缺失home_id和uuid', 'get', {}, 14001, 0])
get_elecollector_info_cmd.append([get_elecollector_info, get_elecollector_info + '-F-不传uuid且home_id不存在', 'get', {'home_id': 'xxx'}, 15006, 0])
get_elecollector_info_cmd.append([get_elecollector_info, get_elecollector_info + '-F-不传uuid且home_id类型错误', 'get', {'home_id': True}, 15006, 0])
get_elecollector_info_cmd.append([get_elecollector_info, get_elecollector_info + '-F-不传uuid且home_id为null', 'get', {'home_id': None}, 14001, 0])
get_elecollector_info_cmd.append([get_elecollector_info, get_elecollector_info + '-F-不传home_id且uuid错误', 'get', {'uuid': 'xxx'}, 15006, 0])
get_elecollector_info_cmd.append([get_elecollector_info, get_elecollector_info + '-F-不传home_id且uuid类型错误', 'get', {'uuid': True}, 15006, 0])
get_elecollector_info_cmd.append([get_elecollector_info, get_elecollector_info + '-F-不传home_id且uuid为null', 'get', {'uuid': None}, 14001, 0])
# write_print_list_dic(get_elecollector_info_cmd)


# 临时测试用
# 工单验证（房源编号（home_id和alias不一致时报错））
# home_id = '5bf512017581fc6191035206'  '5bf512017581fc6191035222'
new_cmd = [
    [add_ticket, '测试用', 'post', {'home_id': home_id, 'service_target': 1, 'service_type': 1, 'room_ids': ['xxxxxxxx'],
                                 'subscribe': {'date': before_ms, 'time': 100, 'name': '测试-请忽略', 'phone': '18566260535'}}, 0, 0],
    # ['search_home_info', 'search_home_info', 'get', {}, 0, 0],
    # ['get_home_info', 'get_home_info', 'get', {'uuid': elemeter_A4_uuid}, 0, 0],
    # ['find_home_device', 'find_home_device', 'post', {'home_id': home_id}, 0, 0],
    # ['find_home_devices', 'find_home_devices', 'post', {'home_id': [home_id, elemeter_A4_uuid]}, 0, 0],
    # ['device_fetch_exceptions', 'find_home_devices', 'get', {'uuid': 'a43718299ca38ff38194c3266af679d5', 'count': 50}, 0, 0]
]

# 获取房间下工单
empty_file('get_ticket_by_room_cmd')
get_ticket_by_room_class = GetDataList(right_get_ticket_by_room, wrong_get_ticket_by_room, [], get_ticket_by_room, 'get')
get_ticket_by_room_cmd = get_ticket_by_room_class.get_all_http_cmd([0], [14001, 14001, 15004])
# write_print_list_dic(get_ticket_by_room_cmd)

# 获取房间安装状态
empty_file('find_home_state_cmd')
find_home_state_class = GetDataList(right_find_home_state, wrong_find_home_state, [], find_home_state, 'post')
find_home_state_cmd = find_home_state_class.get_all_http_cmd([0], [14001, 15004])
find_home_state_cmd += find_home_state_class.get_http_cmd(find_home_state, 'get', find_home_state_class.get_right_data_list(), [0])
find_home_state_cmd += find_home_state_class.get_http_cmd(find_home_state, 'get', find_home_state_class.get_wrong_data_list(), [14001, 15004, 15004])
# write_print_list_dic(find_home_state_cmd)

# 添加房间
empty_file('add_room_cmd')
add_room_class = GetDataList(right_add_room, wrong_add_room, [], 'add_room', 'post')
add_room_cmd = add_room_class.get_all_http_cmd([0], [14001, 14001, 14001, 15004])
# write_print_list_dic(add_room_cmd)

# 电费充值(含公摊)
empty_file('elemeter_charge_fees_with_pool_cmd')
elemeter_charge_fees_with_pool_class = GetDataList(right_elemeter_charge_fees_with_pool, wrong_elemeter_charge_fees_with_pool, [], elemeter_charge_fees_with_pool,
                                                   'post')
elemeter_charge_fees_with_pool_cmd = elemeter_charge_fees_with_pool_class.get_all_http_cmd([0], [14001, 0, 14001, 0, 14001, 15006, 14001, 14001, 14001, 14043, 14001,
                                                                                                 15066])
# write_print_list_dic(elemeter_charge_fees_with_pool_cmd)

# 获取房间电量值
empty_file('room_elemeter_amount_cmd')
room_elemeter_amount_class = GetDataList(right_room_elemeter_amount, wrong_room_elemeter_amount, [], room_elemeter_amount, 'get')
room_elemeter_amount_cmd = room_elemeter_amount_class.get_all_http_cmd([0], [0, 0, 15006])
# write_print_list_dic(room_elemeter_amount_cmd)

# 获取房间电量值
empty_file('get_room_amount_cmd')
get_room_amount_class = GetDataList(right_get_room_amount, wrong_get_room_amount, [], get_room_amount, 'get')
get_room_amount_cmd = get_room_amount_class.get_all_http_cmd([0], [0, 0, 15006])
# write_print_list_dic(get_room_amount_cmd)

# 电量充值(含公摊)
empty_file('elemeter_charge_with_pool_cmd')
elemeter_charge_with_pool_class = GetDataList(right_elemeter_charge_with_pool, wrong_elemeter_charge_with_pool, [], elemeter_charge_with_pool, 'post')
elemeter_charge_with_pool_cmd = elemeter_charge_with_pool_class.get_all_http_cmd([0], [14001, 0, 14001, 0, 14001, 15006, 14001, 14001, 14001, 15066])
# write_print_list_dic(elemeter_charge_with_pool_cmd)

# 采集房源下的同类型设备读数
empty_file('meter_records_by_homeid_cmd')
meter_records_by_homeid_class = GetDataList(right_meter_records_by_homeid, wrong_meter_records_by_homeid, [], meter_records_by_homeid, 'post')
meter_records_by_homeid_cmd = meter_records_by_homeid_class.get_all_http_cmd([0], [15001, 14001, 14001, 15004, 14001, 14001, 14001, 0])
# write_print_list_dic(meter_records_by_homeid_cmd)

# 实时采集电表读数
empty_file('realtime_query_cmd')
realtime_query_class = GetDataList(right_realtime_query, wrong_realtime_query, [], realtime_query, 'post')
realtime_query_cmd = realtime_query_class.get_all_http_cmd([0], [15001])
# write_print_list_dic(realtime_query_cmd)

# 跳合闸开关
empty_file('elemeter_control_cmd')
elemeter_control_class = GetDataList(right_elemeter_control, wrong_elemeter_control, [], elemeter_control, 'post')
elemeter_control_cmd = elemeter_control_class.get_all_http_cmd([0], [15001])
# write_print_list_dic(elemeter_control_cmd)

# 获取电表电量记录
empty_file('amount_record_cmd')
amount_record_class = GetDataList(right_amount_record, wrong_amount_record, [], amount_record, 'get')
amount_record_cmd = amount_record_class.get_all_http_cmd([0], [15001])
amount_record_cmd.append([amount_record, amount_record + '-openapi-S-只传uuid', 'get', {'uuid': elemeter_A4_uuid}, 0, 0])
# write_print_list_dic(amount_record_cmd)

# 小程序授权和回调地址设置
empty_file('client_setting_by_3rd_cmd')
client_setting_by_3rd_class = GetDataList(right_client_setting_by_3rd, wrong_client_setting_by_3rd, [], client_setting_by_3rd, 'post')
client_setting_by_3rd_cmd = client_setting_by_3rd_class.get_all_http_cmd([0], [14001])
client_setting_by_3rd_cmd.append([client_setting_by_3rd, client_setting_by_3rd + '-openapi-S-只传event_callback', 'post', {'event_callback': 'xxx'}, 0, 0])
client_setting_by_3rd_cmd.append([client_setting_by_3rd, client_setting_by_3rd + '-openapi-S-只传async_callback', 'post', {'async_callback': 'xxx'}, 0, 0])
client_setting_by_3rd_cmd.append([client_setting_by_3rd, client_setting_by_3rd + '-openapi-S-只传alipay_auth', 'post', {'alipay_auth': 2}, 0, 0])
# write_print_list_dic(client_setting_by_3rd_cmd)

# 获取剩余电量（针对麻雀公寓新增的接口）
empty_file('elemeter_last_power_history_with_pool_cmd')
elemeter_last_power_history_with_pool_class = GetDataList(right_elemeter_last_power_history_with_pool, wrong_elemeter_last_power_history_with_pool, [],
                                                          elemeter_last_power_history_with_pool, 'get')
elemeter_last_power_history_with_pool_cmd = elemeter_last_power_history_with_pool_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(elemeter_last_power_history_with_pool_cmd)
