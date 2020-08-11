from OpenAPI.Lib.MyHead import *
from OpenAPI.Lib.run_case import *


# 删除租客
def del_all_tenant(tenant_room=[room_1001, room_1002, room_1003]):
    ret_b = False
    if isinstance(tenant_room, str):
        del_tenant_cmd = [delete_tenant, 'delete_tenant_init', 'post', {'room_id': tenant_room}]
        ret = run_case(del_tenant_cmd[0], del_tenant_cmd[1], del_tenant_cmd[2], del_tenant_cmd[3], False)
        if ret['ErrNo'] == 0 or ret['ErrNo'] == 15904:
            ret_b = True
    elif isinstance(tenant_room, list):
        for room_id in tenant_room:
            del_tenant_cmd = [delete_tenant, 'delete_tenant_init', 'post', {'room_id': room_id}]
            ret = run_case(del_tenant_cmd[0], del_tenant_cmd[1], del_tenant_cmd[2], del_tenant_cmd[3], False)
            if ret['ErrNo'] == 0 or ret['ErrNo'] == 15904:
                ret_b = True
            if not ret_b:
                break
    # print(ret)
    if ret_b:
        print('删除租客完成')
        return True
    else:
        print('删除租客失败')
        return False


# 房间添加租客，如果有租客，返回
def add_tenant_init(tenant_room=room_1001):
    add_tenant_cmd = [add_tenant, 'add_tenant_init', 'post', {'room_id': tenant_room, 'tenant_name': get_string(5), 'tenant_phone': phonenumber, 'start_time': now_ms, 'end_time': after_ms}]
    get_room_tenant_cmd = [get_tenant_by_roomid, 'get_tenant_by_roomid_init', 'get', {'room_id': tenant_room}]
    ret_get_room_tenant = run_case(get_room_tenant_cmd[0], get_room_tenant_cmd[1], get_room_tenant_cmd[2], get_room_tenant_cmd[3], False)
    if 'tenant_phone' in ret_get_room_tenant:
        return True
    else:
        ret_add_tenant = run_case(add_tenant_cmd[0], add_tenant_cmd[1], add_tenant_cmd[2], add_tenant_cmd[3], False)
        if 'tenant_phone' in ret_add_tenant:
            return True
        else:
            return False


# add_tenant_init()
# del_all_tenant()
