from OpenAPI.Data.source_data.source_wanke_boyu_data import *
from OpenAPI.Lib.get_data_list import *
from OpenAPI.Lib.run_case import *

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
