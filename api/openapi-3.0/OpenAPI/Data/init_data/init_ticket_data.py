from OpenAPI.Lib.MyHead import *
from OpenAPI.Lib.run_case import *


# 关闭所有预约和售后工单
# 保留测试用的一个安装、一个维修
def del_ticket_init():
    all_ticket = {}
    ticket_tmp = {}
    ticket_1 = []
    ticket_2 = []
    # 更新指定工单状态为关闭
    update_ticket_state_cmd = [delete_ticket, 'delete_ticket-init', 'post', {'ticket_id': 'xxxx'}]
    # 获取所有安装工单
    get_ticket_1_by_home_cmd = [get_ticket_by_home, 'get_ticket_by_home-init', 'get', {'home_id': home_id, 'service_type': 1}]
    ret_get_ticket_1_by_home = run_case(get_ticket_1_by_home_cmd[0], get_ticket_1_by_home_cmd[1], get_ticket_1_by_home_cmd[2], get_ticket_1_by_home_cmd[3], False)

    # 获取所有售后工单
    get_ticket_1_by_home_cmd[3]['service_type'] = 2
    ret_get_ticket_2_by_home = run_case(get_ticket_1_by_home_cmd[0], get_ticket_1_by_home_cmd[1], get_ticket_1_by_home_cmd[2], get_ticket_1_by_home_cmd[3], False)

    # 格式化所有工单和状态
    for tmp in ret_get_ticket_1_by_home['home_ticket_list']:
        # 如果是测试用安装工单，跳过
        if tmp['ticket_id'] == install_ticket:
            continue
        ticket_tmp[tmp['ticket_id']] = tmp['ticket_state']
        ticket_1.append(ticket_tmp)
        ticket_tmp = {}
    for tmps in ret_get_ticket_2_by_home['home_ticket_list']:
        # 如果是测试用维修工单，跳过
        if tmps['ticket_id'] == fix_ticket:
            continue
        ticket_tmp[tmps['ticket_id']] = tmps['ticket_state']
        ticket_2.append(ticket_tmp)
        ticket_tmp = {}
    all_ticket.update({'install_ticket': ticket_1, 'fix_ticket': ticket_2})
    print(all_ticket)
    # 更新所有工单状态为关闭
    for ticket_tmp in all_ticket.keys():
        for ticket_tmp_2 in all_ticket[ticket_tmp]:
            for ticket_id_tmp in ticket_tmp_2.keys():
                if ticket_tmp_2[ticket_id_tmp] == 5:
                    continue
                else:
                    update_ticket_state_cmd[3]['ticket_id'] = ticket_id_tmp
                    run_case(update_ticket_state_cmd[0], update_ticket_state_cmd[1], update_ticket_state_cmd[2], update_ticket_state_cmd[3], False)
    return


# 获取ticket_id
def get_ticket_id(ticket='fix', ticket_state=1):
    all_install_ticket_id = []
    all_fix_ticket_id = []
    # 获取所有安装工单
    get_ticket_1_by_home_cmd = [get_ticket_by_home, 'get_ticket_by_home-init', 'get', {'home_id': home_id, 'service_type': 1}]
    update_ticket_state_cmd = [update_ticket_state, 'update_ticket_state-init', 'post', {'ticket_id': 'xxx', 'ticket_state': ticket_state}]
    ret_get_ticket_1_by_home = run_case(get_ticket_1_by_home_cmd[0], get_ticket_1_by_home_cmd[1], get_ticket_1_by_home_cmd[2], get_ticket_1_by_home_cmd[3], False)
    for tmp in ret_get_ticket_1_by_home['home_ticket_list']:
        if tmp['ticket_id'] == install_ticket:
            continue
        all_install_ticket_id.append({'ticket_id': tmp['ticket_id'], 'ticket_state': tmp['ticket_state']})
    # all_install_ticket_id_json = json.dumps(all_install_ticket_id, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)
    # print(all_install_ticket_id_json)

    # 获取所有售后工单
    get_ticket_1_by_home_cmd[3]['service_type'] = 2
    ret_get_ticket_2_by_home = run_case(get_ticket_1_by_home_cmd[0], get_ticket_1_by_home_cmd[1], get_ticket_1_by_home_cmd[2], get_ticket_1_by_home_cmd[3], False)
    for tmp2 in ret_get_ticket_2_by_home['home_ticket_list']:
        if tmp2['ticket_id'] == fix_ticket:
            continue
        all_fix_ticket_id.append({'ticket_id': tmp2['ticket_id'], 'ticket_state': tmp2['ticket_state']})
    # all_fix_ticket_id_json = json.dumps(all_fix_ticket_id, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)
    # print(all_fix_ticket_id_json)

    # 增加工单
    add_ticket_1_cmd = [add_ticket, 'add_ticket-init', 'post', {'home_id': home_id, 'service_target': 2, 'service_type': 1, 'room_ids': [home_id, room_1001],
                                                                'subscribe': {'date': now_ms, 'time': 100, 'name': 'lifc_test', 'phone': '18566260535',
                                                                              'note': 'test'}}]
    if ticket == 'install':
        if len(all_install_ticket_id) == 0:
            ret_add_ticket_1 = run_case(add_ticket_1_cmd[0], add_ticket_1_cmd[1], add_ticket_1_cmd[2], add_ticket_1_cmd[3], False)
            update_ticket_state_cmd[3]['ticket_state'] = ticket_state
            update_ticket_state_cmd[3]['ticket_id'] = ret_add_ticket_1['ticket_id']
            update_ticket_1 = run_case(update_ticket_state_cmd[0], update_ticket_state_cmd[1], update_ticket_state_cmd[2], update_ticket_state_cmd[3], False)
            if ret_add_ticket_1['ticket_id'] != None:
                return ret_add_ticket_1['ticket_id']
        else:
            for tmp_install in all_install_ticket_id:
                if tmp_install['ticket_state'] == ticket_state:
                    return tmp_install['ticket_id']
            update_ticket_state_cmd[3]['ticket_state'] = ticket_state
            update_ticket_state_cmd[3]['ticket_id'] = all_install_ticket_id[0]['ticket_id']
            update_ticket_1 = run_case(update_ticket_state_cmd[0], update_ticket_state_cmd[1], update_ticket_state_cmd[2], update_ticket_state_cmd[3], False)
            return all_install_ticket_id[0]['ticket_id']
    elif ticket == 'fix':
        if len(all_fix_ticket_id) == 0:
            add_ticket_1_cmd[3]['service_type'] = 2
            ret_add_ticket_2 = run_case(add_ticket_1_cmd[0], add_ticket_1_cmd[1], add_ticket_1_cmd[2], add_ticket_1_cmd[3], False)
            update_ticket_state_cmd[3]['ticket_state'] = ticket_state
            update_ticket_state_cmd[3]['ticket_id'] = ret_add_ticket_2['ticket_id']
            update_ticket_1 = run_case(update_ticket_state_cmd[0], update_ticket_state_cmd[1], update_ticket_state_cmd[2], update_ticket_state_cmd[3], False)
            if ret_add_ticket_2['ticket_id'] != None:
                return ret_add_ticket_2['ticket_id']
        else:
            for tmp_fix in all_fix_ticket_id:
                if tmp_fix['ticket_state'] == ticket_state:
                    return tmp_fix['ticket_id']
            update_ticket_state_cmd[3]['ticket_state'] = ticket_state
            update_ticket_state_cmd[3]['ticket_id'] = all_fix_ticket_id[0]['ticket_id']
            update_ticket_1 = run_case(update_ticket_state_cmd[0], update_ticket_state_cmd[1], update_ticket_state_cmd[2], update_ticket_state_cmd[3], False)
            return all_fix_ticket_id[0]['ticket_id']
    else:
        raise AssertionError('错误的ticket: %s' % ticket)
    return


# del_ticket_init()
# tickets = del_ticket_init()
# if install_ticket in tickets['install_ticket']:
#     print(1)
# if fix_ticket in tickets['fix_ticket']:
#     print(2)
# print(tickets)
# print(get_ticket_id('install', 5))
