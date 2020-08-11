from OpenAPI.Data.source_data.source_antapi_data import *
from OpenAPI.Lib.get_data_list import *
from OpenAPI.Lib.run_case import *

'''
兼容支付宝分账接口
antapi/v1/lock/info
antapi/v1/lock/password_id
antapi/v1/tenant/info
antapi/v1/tenant/home
antapi/v1/tenant/place_transaction
antapi/v1/elemeter/info
antapi/v1/elemeter/amount_record
antapi/v1/elemeter/charge_record
antapi/v1/watermeter/info
antapi/v1/watermeter/amount_record
'''
# 获取门锁信息
empty_file('antapi_get_lock_info_cmd')
antapi_get_lock_info_class = GetDataList(right_antapi_get_lock_info, wrong_antapi_get_lock_info, [], antapi_get_lock_info, 'get')
antapi_get_lock_info_cmd = antapi_get_lock_info_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(antapi_get_lock_info_cmd)

# 获取租客密码id
empty_file('antapi_get_lock_passwordid_cmd')
antapi_get_lock_info_class = GetDataList(right_antapi_get_lock_passwordid, wrong_antapi_get_lock_passwordid, [], antapi_get_lock_passwordid, 'get')
antapi_get_lock_passwordid_cmd = antapi_get_lock_info_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(antapi_get_lock_passwordid_cmd)

# 获取租客信息
empty_file('antapi_get_tenant_info_cmd')
antapi_get_tenant_info_class = GetDataList(right_antapi_get_tenant_info, wrong_antapi_get_tenant_info, [], antapi_get_tenant_info, 'get')
antapi_get_tenant_info_cmd = antapi_get_tenant_info_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(antapi_get_tenant_info_cmd)

# 获取租客房源信息
empty_file('antapi_get_tenant_home_cmd')
antapi_get_tenant_home_class = GetDataList(right_antapi_get_tenant_home, wrong_antapi_get_tenant_home, [], antapi_get_tenant_home, 'get')
antapi_get_tenant_home_cmd = antapi_get_tenant_home_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(antapi_get_tenant_home_cmd)

# 发起支付
empty_file('antapi_tenant_place_transaction_cmd')
antapi_tenant_place_transaction_class = GetDataList(right_antapi_tenant_place_transaction, wrong_antapi_tenant_place_transaction, [], antapi_tenant_place_transaction, 'get')
antapi_tenant_place_transaction_cmd = antapi_tenant_place_transaction_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(antapi_tenant_place_transaction_cmd)

# 获取电表信息
empty_file('antapi_get_elemeter_info_cmd')
antapi_get_elemeter_info_class = GetDataList(right_antapi_get_elemeter_info, wrong_antapi_get_elemeter_info, [], antapi_get_elemeter_info, 'get')
antapi_get_elemeter_info_cmd = antapi_get_elemeter_info_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(antapi_get_elemeter_info_cmd)

# 获取电表电量记录
empty_file('antapi_get_elemeter_amount_record_cmd')
antapi_get_elemeter_amount_record_class = GetDataList(right_antapi_get_elemeter_amount_record, wrong_antapi_get_elemeter_amount_record, [], antapi_get_elemeter_amount_record, 'get')
antapi_get_elemeter_amount_record_cmd = antapi_get_elemeter_amount_record_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(antapi_get_elemeter_amount_record_cmd)

# 获取电表充值记录
empty_file('antapi_get_elemeter_charge_record_cmd')
antapi_get_elemeter_charge_record_class = GetDataList(right_antapi_get_elemeter_charge_record, wrong_antapi_get_elemeter_charge_record, [], antapi_get_elemeter_charge_record, 'get')
antapi_get_elemeter_charge_record_cmd = antapi_get_elemeter_charge_record_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(antapi_get_elemeter_charge_record_cmd)

# 获取水表基本信息
empty_file('antapi_get_watermeter_info_cmd')
antapi_get_watermeter_info_class = GetDataList(right_antapi_get_watermeter_info, wrong_antapi_get_watermeter_info, [], antapi_get_watermeter_info, 'get')
antapi_get_watermeter_info_cmd = antapi_get_watermeter_info_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(antapi_get_watermeter_info_cmd)

# 获取水表水量记录
empty_file('antapi_get_watermeter_amount_record_cmd')
antapi_get_watermeter_amount_record_class = GetDataList(right_antapi_get_watermeter_amount_record, wrong_antapi_get_watermeter_amount_record, [], antapi_get_watermeter_amount_record, 'get')
antapi_get_watermeter_amount_record_cmd = antapi_get_watermeter_amount_record_class.get_all_http_cmd([0], [14001])
# write_print_list_dic(antapi_get_watermeter_amount_record_cmd)
