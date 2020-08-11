from OpenAPI.Lib.get_data_list import *
from OpenAPI.Lib.MyHead import *
from OpenAPI.Lib.run_case import *
from OpenAPI.Data.source_data.source_ticket import *

# 添加工单
empty_file('add_ticket_cmd')
add_ticket_cmd = []
add_ticket_cmd.append([add_ticket, '添加安装工单,网关', 'post', {'home_id': home_id, 'service_target': 1, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                         'subscribe': {'date': before_ms, 'time': 100, 'name': '李飞超', 'phone': '18566260535'}}, '', 0])
add_ticket_cmd.append([add_ticket, '添加安装工单,门锁', 'post', {'home_id': home_id, 'service_target': 2, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                         'subscribe': {'date': before_ms, 'time': 100, 'name': '李飞超', 'phone': '18566260535'}}, '', 0])
add_ticket_cmd.append([add_ticket, '添加安装工单,电表', 'post', {'home_id': home_id, 'service_target': 3, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                         'subscribe': {'date': before_ms, 'time': 100, 'name': '李飞超', 'phone': '18566260535'}}, '', 0])
add_ticket_cmd.append([add_ticket, '添加安装工单,home_id不存在', 'post', {'home_id': 'test', 'service_target': 1, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                                 'subscribe': {'date': before_ms, 'time': 100, 'name': '李飞超', 'phone': '18566260535'}}, 15006,
                       1])
add_ticket_cmd.append([add_ticket, '添加安装工单,home_id字段缺失', 'post', {'service_target': 1, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                                  'subscribe': {'date': before_ms, 'time': 100, 'name': '李飞超', 'phone': '18566260535'}}, 14001,
                       1])
add_ticket_cmd.append([add_ticket, '添加安装工单,service_target=0', 'post', {'home_id': home_id, 'service_target': 0, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                                       'subscribe': {'date': before_ms, 'time': 100, 'name': '李飞超', 'phone': '18566260535'}},
                       14001, 1])
add_ticket_cmd.append([add_ticket, '添加安装工单,service_target=4', 'post', {'home_id': home_id, 'service_target': 4, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                                       'subscribe': {'date': before_ms, 'time': 100, 'name': '李飞超', 'phone': '18566260535'}},
                       14001, 1])
add_ticket_cmd.append([add_ticket, '添加安装工单,service_target类型错误', 'post',
                       {'home_id': home_id, 'service_target': 1.1, 'service_type': 1, 'room_ids': [home_id, room_1001],
                        'subscribe': {'date': before_ms, 'time': 100, 'name': '李飞超', 'phone': '18566260535'}}, 14001, 1])
add_ticket_cmd.append([add_ticket, '添加安装工单,service_target字段缺失', 'post', {'home_id': home_id, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                                         'subscribe': {'date': before_ms, 'time': 100, 'name': '李飞超', 'phone': '18566260535'}},
                       14001, 1])
add_ticket_cmd.append([add_ticket, '添加安装工单,room_ids不存在', 'post', {'home_id': home_id, 'service_target': 2, 'service_type': 1, 'room_ids': ['abc', 'test'],
                                                                  'subscribe': {'date': before_ms, 'time': 100, 'name': '李飞超', 'phone': '18566260535'}}, 15006,
                       1])
add_ticket_cmd.append([add_ticket, '添加安装工单,room_ids字段缺失', 'post', {'home_id': home_id, 'service_target': 2, 'service_type': 1,
                                                                   'subscribe': {'date': before_ms, 'time': 100, 'name': '李飞超', 'phone': '18566260535'}}, 14001,
                       1])
add_ticket_cmd.append(
    [add_ticket, '添加安装工单,subscribe类型错误', 'post', {'home_id': home_id, 'service_target': 1, 'service_type': 1, 'room_ids': [home_id, room_1001], 'subscribe': 'test'},
     14001, 1])
add_ticket_cmd.append(
    [add_ticket, '添加安装工单,subscribe字段缺失', 'post', {'home_id': home_id, 'service_target': 1, 'service_type': 1, 'room_ids': [home_id, room_1001]}, 14001, 1])
add_ticket_cmd.append([add_ticket, '添加安装工单,name字段缺失', 'post', {'home_id': home_id, 'service_target': 1, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                               'subscribe': {'date': before_ms, 'time': 100, 'phone': '18566260535'}}, 14001, 1])
add_ticket_cmd.append([add_ticket, '添加安装工单,phone字段缺失', 'post', {'home_id': home_id, 'service_target': 1, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                                'subscribe': {'date': before_ms, 'time': 100, 'name': '李飞超'}}, 14001, 1])
add_ticket_cmd.append([add_ticket, '添加安装工单,phone格式错误', 'post', {'home_id': home_id, 'service_target': 1, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                                'subscribe': {'date': before_ms, 'time': 100, 'name': '李飞超', 'phone': '110666600QQ'}}, 14001,
                       1])
add_ticket_cmd.append([add_ticket, '添加安装工单,note字段正确', 'post', {'home_id': home_id, 'service_target': 1, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                               'subscribe': {'date': before_ms, 'time': 100, 'name': '李飞超', 'phone': '18566260535',
                                                                             'note': 'test_note'}}, '', 0])
add_ticket_cmd.append([add_ticket, '添加安装工单,预约工单,date+time', 'post', {'home_id': home_id, 'service_target': 1, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                                     'subscribe': {'name': '李飞超', 'phone': '18566260535', 'date': after_ms, 'time': 100}}, 0,
                       ''])
add_ticket_cmd.append([add_ticket, '添加安装工单,预约工单,只有date', 'post', {'home_id': home_id, 'service_target': 1, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                                  'subscribe': {'name': '李飞超', 'phone': '18566260535', 'date': after_ms}}, 14001, 1])
add_ticket_cmd.append([add_ticket, '添加安装工单,预约工单,只有time', 'post', {'home_id': home_id, 'service_target': 1, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                                  'subscribe': {'name': '李飞超', 'phone': '18566260535', 'time': 100}}, 14001, 1])
add_ticket_cmd.append([add_ticket, '添加安装工单,预约工单,date小于今天', 'post', {'home_id': home_id, 'service_target': 1, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                                    'subscribe': {'name': '李飞超', 'phone': '18566260535', 'date': 0, 'time': 100}}, 14001, 1])
add_ticket_cmd.append([add_ticket, '添加安装工单,预约工单,date类型错误', 'post', {'home_id': home_id, 'service_target': 1, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                                    'subscribe': {'name': '李飞超', 'phone': '18566260535', 'date': 'test', 'time': 100}}, 14001,
                       1])
add_ticket_cmd.append([add_ticket, '添加安装工单,预约工单,预约上午', 'post', {'home_id': home_id, 'service_target': 1, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                                'subscribe': {'name': '李飞超', 'phone': '18566260535', 'date': after_ms, 'time': 101}}, '', 0])
add_ticket_cmd.append([add_ticket, '添加安装工单,预约工单,预约下午', 'post', {'home_id': home_id, 'service_target': 1, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                                'subscribe': {'name': '李飞超', 'phone': '18566260535', 'date': after_ms, 'time': 102}}, '', 0])
add_ticket_cmd.append([add_ticket, '添加安装工单,预约工单,time范围错误', 'post', {'home_id': home_id, 'service_target': 1, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                                    'subscribe': {'name': '李飞超', 'phone': '18566260535', 'date': after_ms, 'time': 105}}, 14001,
                       1])
add_ticket_cmd.append([add_ticket, '添加安装工单,预约工单,time类型错误', 'post', {'home_id': home_id, 'service_target': 1, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                                    'subscribe': {'name': '李飞超', 'phone': '18566260535', 'date': after_ms, 'time': 'test'}},
                       14001, 1])
add_ticket_cmd.append([add_ticket, '添加维修工单,网关', 'post', {'home_id': home_id, 'service_target': 7, 'service_type': 2, 'room_ids': [home_id, room_1001],
                                                         'subscribe': {'name': '李飞超', 'phone': '18566260535', 'note': 'test', 'time': 100}}, '', 0])
add_ticket_cmd.append([add_ticket, '添加维修工单,门锁', 'post', {'home_id': home_id, 'service_target': 2, 'service_type': 2, 'room_ids': [home_id, room_1001],
                                                         'subscribe': {'name': '李飞超', 'phone': '18566260535', 'note': 'test', 'time': 100}}, '', 0])
add_ticket_cmd.append([add_ticket, '添加维修工单,电表', 'post', {'home_id': home_id, 'service_target': 3, 'service_type': 2, 'room_ids': [home_id, room_1001],
                                                         'subscribe': {'name': '李飞超', 'phone': '18566260535', 'note': 'test', 'time': 100}}, '', 0])
# write_print_list_dic(add_ticket_cmd)

# 获取工单信息
empty_file('get_ticket_by_id_cmd')
get_ticket_by_id_cmd = []
get_ticket_by_id_cmd.append([get_ticket_by_id, '获取工单信息,安装工单', 'get', {'ticket_id': install_ticket}, '', 0])
get_ticket_by_id_cmd.append([get_ticket_by_id, '获取工单信息,维修工单', 'get', {'ticket_id': fix_ticket}, '', 0])
get_ticket_by_id_cmd.append([get_ticket_by_id, '获取工单信息,ticket_id错误', 'get', {'ticket_id': 'test'}, 15006, 1])
get_ticket_by_id_cmd.append([get_ticket_by_id, '获取工单信息,ticket_id字段缺失', 'get', {}, 14001, 1])
# write_print_list_dic(get_ticket_by_id_cmd)

# 获取房源下所有工单
empty_file('get_ticket_by_home_cmd')
get_ticket_by_home_cmd = []
get_ticket_by_home_cmd.append([get_ticket_by_home, '获取房源下所有工单,安装工单', 'get', {'home_id': home_id, 'service_type': 1}, '', 0])
get_ticket_by_home_cmd.append([get_ticket_by_home, '获取房源下所有工单,维修工单', 'get', {'home_id': home_id, 'service_type': 2}, '', 0])
get_ticket_by_home_cmd.append([get_ticket_by_home, '获取房源下所有工单,service_type范围错误', 'get', {'home_id': home_id, 'service_type': 0}, 14001, 1])
get_ticket_by_home_cmd.append([get_ticket_by_home, '获取房源下所有工单,service_type类型错误', 'get', {'home_id': home_id, 'service_type': 'test'}, 14001, 1])
get_ticket_by_home_cmd.append([get_ticket_by_home, '获取房源下所有工单,service_type字段缺失', 'get', {'home_id': home_id}, 14001, 1])
get_ticket_by_home_cmd.append([get_ticket_by_home, '获取房源下所有工单,home_id不存在', 'get', {'home_id': 'test', 'service_type': 1}, 15004, 1])
get_ticket_by_home_cmd.append([get_ticket_by_home, '获取房源下所有工单,home_id字段缺失', 'get', {'service_type': 1}, 14001, 1])
# write_print_list_dic(get_ticket_by_home_cmd)

# 更新工单状态
empty_file('update_ticket_state_cmd')
update_ticket_state_cmd = []
update_ticket_state_cmd.append([update_ticket_state, '更新工单状态,安装工单,待处理', 'post', {'ticket_id': install_ticket, 'ticket_state': 1}, 0, 0])
update_ticket_state_cmd.append([update_ticket_state, '更新工单状态,安装工单,待分配', 'post', {'ticket_id': install_ticket, 'ticket_state': 2}, 0, 0])
update_ticket_state_cmd.append([update_ticket_state, '更新工单状态,安装工单,已分配', 'post', {'ticket_id': install_ticket, 'ticket_state': 3}, 0, 0])
update_ticket_state_cmd.append([update_ticket_state, '更新工单状态,安装工单,已完成', 'post', {'ticket_id': install_ticket, 'ticket_state': 4}, 0, 0])
update_ticket_state_cmd.append([update_ticket_state, '更新工单状态,安装工单,已关闭', 'post', {'ticket_id': 'ISEM1903291452323', 'ticket_state': 5}, 0, 0])
update_ticket_state_cmd.append([update_ticket_state, '更新工单状态,维修工单,待处理', 'post', {'ticket_id': fix_ticket, 'ticket_state': 1}, 0, 0])
update_ticket_state_cmd.append([update_ticket_state, '更新工单状态,维修工单,待分配', 'post', {'ticket_id': fix_ticket, 'ticket_state': 2}, 0, 0])
update_ticket_state_cmd.append([update_ticket_state, '更新工单状态,维修工单,已分配', 'post', {'ticket_id': fix_ticket, 'ticket_state': 3}, 0, 0])
update_ticket_state_cmd.append([update_ticket_state, '更新工单状态,维修工单,已完成', 'post', {'ticket_id': fix_ticket, 'ticket_state': 4}, 0, 0])
update_ticket_state_cmd.append([update_ticket_state, '更新工单状态,维修工单,已关闭', 'post', {'ticket_id': fix_ticket, 'ticket_state': 5}, 0, 0])
update_ticket_state_cmd.append([update_ticket_state, '更新工单状态,ticket_state范围错误', 'post', {'ticket_id': install_ticket, 'ticket_state': 6}, 14001, 1])
update_ticket_state_cmd.append([update_ticket_state, '更新工单状态,ticket_state类型错误', 'post', {'ticket_id': install_ticket, 'ticket_state': 'test'}, 14001, 1])
update_ticket_state_cmd.append([update_ticket_state, '更新工单状态,ticket_state字段缺失', 'post', {'ticket_id': install_ticket}, 14001, 1])
update_ticket_state_cmd.append([update_ticket_state, '更新工单状态,ticket_id不存在', 'post', {'ticket_id': 'test', 'ticket_state': 1}, 15006, 1])
update_ticket_state_cmd.append([update_ticket_state, '更新工单状态,ticket_id字段缺失', 'post', {'ticket_state': 1}, 14001, 1])
# write_print_list_dic(update_ticket_state_cmd)

# 更新工单信息
empty_file('update_ticket_cmd')
update_ticket_cmd = []
update_ticket_cmd.append([update_ticket, '更新工单信息,安装工单', 'post',
                          {'ticket_id': install_ticket, 'room_ids': [home_id, room_1002, room_1001],
                           'subscribe': {'name': get_string(5), 'phone': '18566260535', 'note': 'test'}}, 0,
                          0])
update_ticket_cmd.append([update_ticket, '更新工单信息,维修工单', 'post',
                          {'ticket_id': fix_ticket, 'room_ids': [home_id, room_1002, room_1001],
                           'subscribe': {'name': get_string(5), 'phone': '18566260535', 'note': 'test'}}, 0, 0])
update_ticket_cmd.append(
    [update_ticket, '更新工单信息,room_ids类型错误', 'post',
     {'ticket_id': install_ticket, 'room_ids': home_id, 'subscribe': {'name': '李飞超', 'phone': '18566260535', 'note': 'test'}},
     14001, 1])
update_ticket_cmd.append([update_ticket, '更新工单信息,room_ids不存在', 'post',
                          {'ticket_id': install_ticket, 'room_ids': ['test', '123'], 'subscribe': {'name': '李飞超', 'phone': '18566260535', 'note': 'test'}}, 15006,
                          1])
update_ticket_cmd.append(
    [update_ticket, '更新工单信息,room_ids字段缺失', 'post', {'ticket_id': install_ticket, 'subscribe': {'name': '李飞超', 'phone': '18566260535', 'note': 'test'}}, 14001, 1])
update_ticket_cmd.append(
    [update_ticket, '更新工单信息,subscribe类型错误', 'post', {'ticket_id': install_ticket, 'room_ids': [home_id, room_1002, room_1001], 'subscribe': 'test'}, 14001, 1])
update_ticket_cmd.append([update_ticket, '更新工单信息,subscribe字段缺失', 'post', {'ticket_id': install_ticket, 'room_ids': [home_id, room_1002, room_1001]}, 14001, 1])
update_ticket_cmd.append(
    [update_ticket, '更新工单信息,name字段缺失', 'post', {'ticket_id': install_ticket, 'room_ids': [home_id, room_1002, room_1001], 'subscribe': {'phone': '18566260535'}},
     14001, 1])
update_ticket_cmd.append([update_ticket, '更新工单信息,phone格式错误', 'post',
                          {'ticket_id': install_ticket, 'room_ids': [home_id, room_1002, room_1001], 'subscribe': {'name': '李飞超', 'phone': '110666600WW'}},
                          14001, 1])
update_ticket_cmd.append([update_ticket, '更新工单信息,note正确', 'post', {'ticket_id': install_ticket, 'room_ids': [home_id, room_1002, room_1001],
                                                                   'subscribe': {'name': '李飞超', 'phone': '110666600WW', 'note': 'update_note'}}, 0, 0])
# write_print_list_dic(update_ticket_cmd)

# 删除工单
empty_file('delete_ticket_cmd')
delete_ticket_class = GetDataList(right_delete_ticket, wrong_delete_ticket, [], delete_ticket, 'post')
delete_ticket_cmd = delete_ticket_class.get_all_http_cmd([0], [14001, 15006])
# write_print_list_dic(delete_ticket_cmd)

