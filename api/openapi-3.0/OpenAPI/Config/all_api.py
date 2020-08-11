# 3.0
access_token = 'access_token'
# 房源管理
add_home = 'add_home'
update_home = 'update_home'
del_home = 'del_home'
get_home_info = 'get_home_info'
find_home_device = 'find_home_device'
find_home_devices = 'find_home_devices'
search_home_info = 'search_home_info'
count_home_info = 'count_home_info'
add_rooms = 'add_rooms'
update_room = 'update_room'
del_room = 'del_room'

# 设备通用管理
get_device_uuid = 'get_device_uuid'
get_device_info = 'get_device_info'         # super
search_device_op_log = 'search_device_op_log'
count_device_op_log = 'count_device_op_log'
refresh_devices_lqi = 'refresh_devices_lqi'
device_count_exceptions = 'device_count_exceptions'
device_fetch_exceptions = 'device_fetch_exceptions'
device_count_exceptions_old = 'device_count_exceptions_old'
device_fetch_exceptions_old = 'device_fetch_exceptions_old'

# 网关管理
get_center_info = 'get_center_info'
get_center_info_arr = 'get_center_info_arr'

# 门锁管理
get_lock_info = 'get_lock_info'
fetch_passwords = 'fetch_passwords'
get_default_password_plaintext = 'get_default_password_plaintext'
get_dynamic_password_plaintext = 'get_dynamic_password_plaintext'
add_password = 'add_password'
add_password_without_center = 'add_password_without_center'
update_password = 'update_password'
update_password_without_center = 'update_password_without_center'
delete_password = 'delete_password'
frozen_password = 'frozen_password'
unfrozen_password = 'unfrozen_password'
get_lock_events = 'get_lock_events'
count_lock_events = 'count_lock_events'

# 采集器管理
get_elecollector_info_arr = 'get_elecollector_info_arr'

# 电表管理
get_elemeter_info = 'get_elemeter_info'
elemeter_update_overdraft = 'elemeter_update_overdraft'
elemeter_reset_by_collector = 'elemeter_reset_by_collector'
# elemeter_reset_by_collector = '/v2/elemeter_reset_by_collector'
elemeter_update_max_capacity = 'elemeter_update_max_capacity'
elemeter_read = 'elemeter_read'
# elemeter_read = '/v2/elemeter_read'
elemeter_fetch_power_consumption = 'elemeter_fetch_power_consumption'
elemeter_count_power_history = 'elemeter_count_power_history'
elemeter_fetch_power_history = 'elemeter_fetch_power_history'
elemeter_fetch_power_history_with_pool = 'elemeter_fetch_power_history_with_pool'
# elemeter_fetch_power_history_with_pool = '/v2/elemeter_fetch_power_history_with_pool'
elemeter_switch_on = 'elemeter_switch_on'
elemeter_switch_off = 'elemeter_switch_off'
elemeter_force_open = 'elemeter_force_open'
elemeter_syn_data = 'elemeter_syn_data'
set_room_pay_type = 'set_room_pay_type'
elemeter_charge = 'elemeter_charge'             # super
# elemeter_charge = '/v2/elemeter_charge'
elemeter_charge_fees = 'elemeter_charge_fees'     # super
# elemeter_charge_fees = '/v2/elemeter_charge_fees'
elemeter_charge_query = 'elemeter_charge_query'     # super
# elemeter_charge_query = '/v2/elemeter_charge_query'
elemeter_count_charge_history = 'elemeter_count_charge_history'
elemeter_fetch_charge_history = 'elemeter_fetch_charge_history'
# elemeter_fetch_charge_history = '/v2/elemeter_fetch_charge_history'
elemeter_charge_reset = 'elemeter_charge_reset'
# elemeter_charge_reset = '/v2/elemeter_charge_reset'
elemeter_set_eleprice = 'elemeter_set_eleprice'
elemeter_set_eleprice_by_home = 'elemeter_set_eleprice_by_home'
elemeter_set_eleprice_way = 'elemeter_set_eleprice_way'
elemeter_get_price_and_way = 'elemeter_get_price_and_way'

# 水表管理
add_water_gateway = 'add_water_gateway'         # super
del_water_gateway = 'del_water_gateway'         # super
replace_water_gateway = 'replace_water_gateway'         # super
add_watermeter = 'add_watermeter'                   # super
del_watermeter = 'del_watermeter'                   # super
add_watermeter_status = 'add_watermeter_status'         # super
get_water_gateway_info = 'get_water_gateway_info'
get_watermeter_info = 'get_watermeter_info'
read_watermeter = 'read_watermeter'
read_watermeter_status = 'read_watermeter_status'
update_room_water_pay_type = 'update_room_water_pay_type'
update_watermeter_overdraft = 'update_watermeter_overdraft'
watermeter_charge = 'watermeter_charge'
watermeter_charge_reset = 'watermeter_charge_reset'
count_watermeter_charge_record = 'count_watermeter_charge_record'
watermeter_charge_records = 'watermeter_charge_records'
count_meter_record = 'count_meter_record'
get_meter_record = 'get_meter_record'

# 蓝牙授权接口
blu_auth_room = '/openapi/v2/auth_room'     # 添加授权房间
blu_unauth_room = '/openapi/v2/unauth_room'     # 接触授权房间
blu_app_token = '/openapi/v2/app_token'     # 获取蓝牙sdk请求token

# 蓝牙relation
blu_relation_list = '/appapi/v1/relation/list'  # 获取蓝牙授权列表
blu_relation_operations_unbind_slave = '/appapi/v1/relation/operations/unbind_slave'    # 解绑slave的授权
blu_relation_authened_devices = '/appapi/v1/relation/authened_devices'  # 获取授权过的设备
blu_relation_operations_authen_accept = '/appapi/v1/relation/operations/authen_accept'
blu_relation_operations_authen_refuse = '/appapi/v1/relation/operations/authen_refuse'
blu_relation_slave_nickname = '/appapi/v1/relation/slave_nickname'

# 蓝牙password
blu_password_operations_synchronize = '/appapi/v1/password/operations/synchronize'  # 同步密码列表

# 蓝牙history
blu_history_operations_synchronization_begin = '/appapi/v1/history/operations/synchronization_begin'    # 获取设备最近上报事件的序列号(时间戳)
blu_history_operations_synchronize = '/appapi/v1/history/operations/synchronize'    # 上报设备历史记录
blu_history_operations_synchronization_end = '/appapi/v1/history/operations/synchronization_end'    # 上报设备最近上报事件的序列号(时间戳)
blu_history_count = '/appapi/v1/history/count'  # 获取设备一段时间内操作记录条数
blu_history = '/appapi/v1/history'  # 获取一段时间内门锁的开锁记录

# 蓝牙device
blu_device_battery = '/appapi/v1/device/battery'    # 无网关类型门锁同步设备电量
blu_device_lock_reset = '/appapi/v1/device/lock/reset'  # 重置无网关门锁？
blu_device_ota_info = '/appapi/v1/device/ota_info'  # 检测无网关类型门锁是否需要ota升级
blu_device_lock_infos = '/appapi/v1/device/lock_infos'  # 批量获取锁信息？
blu_device_ota_file = '/appapi/v1/device/ota_file'  #
blu_device_lock_versions = '/appapi/v1/device/lock/versions'    # 无网关门锁向服务器同步设备版本号
blu_device_gatewayless_lock = '/appapi/v1/device/gatewayless_lock'  # 无网关门锁注册
blu_device_gatewayless_lock_register_state = '/appapi/v1/device/gatewayless_lock/register_state'    # 上报无网关门锁绑定状态
blu_device_lock_geo_autounlock = '/appapi/v1/device/geo_autounlock'    # 设置蓝牙自动开始模式
blu_device_geo_info = '/appapi/v1/device/geo_info'  # 上报设备地理信息

# 蓝牙bluetooth
blu_bluetooth_connection_log = '/appapi/v1/bluetooth/connection_log'    # 错误日志记录接口

# 蓝牙ble
blu_ble_config = '/appapi/v1/ble/config'    # 配置获取
blu_ble_dark_bind_state = '/appapi/v1/ble/dark_bind_state'  # 获取暗绑定状态
blu_ble_trans_secret = '/appapi/v1/ble/trans_secret'    # 获取密匙
blu_ble_token_with_mac = '/appapi/v1/ble/token_with_mac'    # 获取token 和 mac
blu_ble_token = '/appapi/v1/ble/token'  # 获取token
blu_ble_operations_reset_token = '/appapi/v1/ble/operations/reset_token'    # 重置蓝牙钥匙
blu_ble_operations_reset_tokens = '/appapi/v1/ble/operations/reset_tokens'  # 批量重置蓝牙钥匙
blu_ble_used_state = '/appapi/v1/ble/used_state'    # 修改蓝牙钥匙的使用情况
blu_ble_used_states = '/appapi/v1/ble/used_states'  # 批量修改蓝牙钥匙的使用情况
blu_ble_operations_synchronize = '/appapi/v1/ble/operations/synchronize'    # 蓝牙授权列表同步
blu_ble_encode_cmd = '/appapi/v1/ble/encode_cmd'    # 获取蓝牙管理二进制命令
blu_ble_decode_raw_data = '/appapi/v1/ble/decode_raw_data'  # 获取蓝牙管理二进制命令

# 蓝牙app
blu_app_crypt_secret = '/appapi/v1/crypt_secret'    # 获取密匙
blu_app_server_time = '/appapi/v1/server_time'  # 获取服务器时间
blu_app_cellphone_identifier = '/appapi/v1/cellphone_identifier'    # 获取identifier
blu_app_auth_room_count = '/appapi/v1/auth_room/count'  # 获取授权房间数目
blu_app_auth_room = '/appapi/v1/auth_room'

# 工单管理
add_ticket = 'add_ticket'
update_ticket_state = 'update_ticket_state'
get_ticket_by_id = 'get_ticket_by_id'
get_ticket_by_home = 'get_ticket_by_home'
update_ticket = 'update_ticket'

# internalapi
# 获取商户是否存在
check_is_client = '/internalapi/v1/check_is_client'
# 平台取消权限接口
unauth_observer = '/internalapi/v1/unauth_observer'
# 平台验证权限接口
auth_observer = '/internalapi/v1/auth_observer'

# 兼容支付宝分账接口
antapi_get_lock_info = '/antapi/v1/lock/info'
antapi_get_lock_passwordid = '/antapi/v1/lock/password_id'
antapi_get_tenant_info = '/antapi/v1/tenant/info'
antapi_get_tenant_home = '/antapi/v1/tenant/home'
antapi_tenant_place_transaction = '/antapi/v1/tenant/place_transaction'
antapi_get_elemeter_info = '/antapi/v1/elemeter/info'
antapi_get_elemeter_amount_record = '/antapi/v1/elemeter/amount_record'
antapi_get_elemeter_charge_record = '/antapi/v1/elemeter/charge_record'
antapi_get_watermeter_info = '/antapi/v1/watermeter/info'
antapi_get_watermeter_amount_record = '/antapi/v1/watermeter/amount_record'

# new_add
# # 获取商户设置    在公摊里已经有
# get_client_setting = 'get_client_setting'
# # 获取公摊设置    在公摊里已经有
# get_home_setting = 'get_home_setting'
# 获取采集器信息
get_elecollector_info = 'get_elecollector_info'
# 删除工单
delete_ticket = 'delete_ticket'
# 获取房间下工单
get_ticket_by_room = 'get_ticket_by_room'
# 获取房间安装状态
find_home_state = 'find_home_state'
# 添加房间
add_room = 'add_room'
# 电费充值(含公摊)
elemeter_charge_fees_with_pool = 'elemeter_charge_fees_with_pool'
# elemeter_charge_fees_with_pool = '/v2/elemeter_charge_fees_with_pool'
# 获取房间电量值
room_elemeter_amount = 'room_elemeter_amount'
# room_elemeter_amount = '/v2/room_elemeter_amount'
# 获取房间电量值
get_room_amount = '/pms/v1/get_room_amount'
# 电量充值(含公摊)
elemeter_charge_with_pool = 'elemeter_charge_with_pool'
# elemeter_charge_with_pool = '/pms/v1/elemeter_charge_with_pool'
# 采集房源下的同类型设备读数
meter_records_by_homeid = '/wanke/boyu/meter_records_by_homeid'
# 实时采集电表读数
realtime_query = '/wanke/boyu/realtime_query'
# 跳合闸开关
elemeter_control = '/wanke/boyu/elemeter_control'
# 获取电表电量记录
amount_record = '/antapi/v1/elemeter/amount_record'
# 小程序授权和回调地址设置
client_setting_by_3rd = 'client_setting_by_3rd'
# 获取最新剩余电量（针对麻雀公寓新增的接口）
elemeter_last_power_history_with_pool = 'elemeter_last_power_history_with_pool'
# elemeter_last_power_history_with_pool = '/v2/elemeter_last_power_history_with_pool'

# pooling
# 获取房源公摊设置
get_home_setting = 'get_home_setting'
# 获取商户设置公摊配置
get_client_setting = 'get_client_setting'
# 控制商户公摊状态开启关闭
switch_client_pooling_state = 'switch_client_pooling_state'
# 设置商户公摊模式
set_client_pooling_area = 'set_client_pooling_area'
# 控制房源公摊状态开启关闭
switch_home_pooling_state = 'switch_home_pooling_state'
# 设置房源公摊模式
set_home_pooling_area = 'set_home_pooling_area'
# 设置房源权重
update_pooling_weight = 'update_pooling_weight'
# 获取房源权重
get_pooling_weight = 'get_pooling_weight'

# tenant
# 添加租客
add_tenant = 'add_tenant'
# 更新租客
update_tenant = 'update_tenant'
# 根据房源id获取租客列表
list_tenants_by_homeid = 'list_tenants_by_homeid'
# 根据room_id获取租客信息
get_tenant_by_roomid = 'get_tenant_by_roomid'
# 删除租客
delete_tenant = 'delete_tenant'

# 事件
batteryAlarm = 'batteryAlarm'                           # 门锁低电量事件
clearBattryAlarm = 'clearBattryAlarm'                   # 门锁解除低电量事件
brokenAlarm = 'brokenAlarm'                             # 门锁被破坏事件
wrongPwdAlarm = 'wrongPwdAlarm'                         # 密码连续输入错误事件
lockerOpenAlarm = 'lockerOpenAlarm'                     # 开锁事件
lockOfflineAlarm = 'lockOfflineAlarm'                   # 设备离线事件
clearLockOfflineAlarm = 'clearLockOfflineAlarm'         # 设备解除离线事件
centerOfflineAlarm = 'centerOfflineAlarm'               # 网关离线事件
clearCenterOfflineAlarm = 'clearCenterOfflineAlarm'     # 网关解除离线事件
batteryAsync = 'batteryAsync'                           # 电量更新事件
installSubmit = 'installSubmit'                         # 房源设备安装完成事件
deviceInstall = 'deviceInstall'                         # 设备绑定事件
deviceUninstall = 'deviceUninstall'                     # 设备解绑事件
elemeterPowerAsync = 'elemeterPowerAsync'               # 电表电量同步事件
elemeterHistory = 'elemeterHistory'                     # 电表历史异常记录上传事件
elemeterOvercomeAmount = 'elemeterOvercomeAmount'       # 电表欠费事件
elemeterOvercomeCapacity = 'elemeterOvercomeCapacity'   # 电表超功率事件
elemeterLocalClose = 'elemeterLocalClose'               # 电表本地合闸事件
elemeterTransError = 'elemeterTransError'               # 电表通讯错误事件
elemeterPowerHisAsync = 'elemeterPowerHisAsync'         # 电表电量历史记录上传事件
deviceReplace = 'deviceReplace'                         # 水表采集器替换事件
waterGatewayOfflineAlarm = 'waterGatewayOfflineAlarm'   # 水表采集器离线事件
waterGatewayOnlineAlarm = 'waterGatewayOnlineAlarm'     # 水表采集器在线事件
watermeterAmountAsync = 'watermeterAmountAsync'         # 水表读数更新事件
watermeterOvercomeAmount = 'watermeterOvercomeAmount'   # 超水量事件

# 回调
Password_Add_Service = 'Password_Add_Service'           # 门锁密码添加回调
Password_Delete_Service = 'Password_Delete_Service'     # 门锁密码删除回调
Password_Update_Service = 'Password_Update_Service'     # 门锁密码更新回调
Password_Frozen_Service = 'Password_Frozen_Service'     # 门锁密码冻结回调
Password_Unfrozen_Service = 'Password_Unfrozen_Service'  # 门锁密码解冻回调
Elemeter_Control_Service = 'Elemeter_Control_Service'   # 电表操作回调
Elemeter_Passthrough_Service = 'Elemeter_Passthrough_Service'   # 电表电量获取回调
Elemeter_Syn_Service = 'Elemeter_Syn_Service'           # 电表同步回调
Zmeter_Charge_Service = 'Zmeter_Charge_Service'         # 电表充值回调
Zmeter_Reset_Service = 'Zmeter_Reset_Service'           # 电表清零回调
Zmeter_Capacity_Service = 'Zmeter_Capacity_Service'     # 电表修改功率回调
Zmeter_Open_Service = 'Zmeter_Open_Service'             # 电表跳闸回调
Zmeter_Close_Service = 'Zmeter_Close_Service'           # 电表合闸回调
Zmeter_Read_Service = 'Zmeter_Read_Service'             # 电表抄表回调
Zmeter_Syn_Service = 'Zmeter_Syn_Service'               # 电表同步回调

