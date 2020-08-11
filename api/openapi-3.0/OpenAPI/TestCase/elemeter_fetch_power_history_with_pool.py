from OpenAPI.Data.final_data.elemeter_data import *
from OpenAPI.Data.final_data.new_add_data import *
from OpenAPI.Lib.connect_server import *
from OpenAPI.Lib.saas_api import run_case as run_case_saasapi


serial_no = []
trade_num = []
amount = {'consume_amount': 0, 'total_amount': 0, 'pooling_amount': 0, 'charge_pooling_amount': 0}
charge_amount = []
left_amount = amount['total_amount'] - amount['consume_amount'] + amount['charge_pooling_amount'] - amount['pooling_amount']

room_id_saas = '1680272836'
elemeter_A1_id = '1466764174'


@ddt.ddt
class test_case(unittest.TestCase):
    # 每个测试用例执行之后做操作
    def tearDown(self):
        time.sleep(1)
        pass

    # 每个测试用例执行之前做操作
    def setUp(self):
        pass

    # 所有测试执行之前
    @classmethod
    def setUpClass(cls):
        empty_log()
        pass

    # 所有测试执行之后
    @classmethod
    def tearDownClass(cls):
        pass

    # # 获取电表当前用电量
    # @ddt.data(
    #     *(get_cases(elemeter_read_cmd))
    # )
    # @ddt.unpack
    # def test_01_elemeter_read(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('serviceid', ret)
    #         # self.assertEqual(CheckCallback(way='service', serviceid=ret['serviceid'], looptime=30), True)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     # time.sleep(30)
    #     return

    # # 查询剩余电量    /v2/elemeter_fetch_power_history_with_pool
    # @ddt.data(
    #     *(get_cases(elemeter_fetch_power_history_with_pool_cmd))
    # )
    # @ddt.unpack
    # def test_02_elemeter_fetch_power_history_with_pool(self, url, name, method, param, check, do=0):
    #     global amount
    #     if 'count' in param:
    #         param['count'] = 10
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('history', ret)
    #         for one_charge in ret['history']:
    #             if one_charge['time'] > now_ms:
    #                 if param['uuid'] == elemeter_A4_uuid:
    #                     for tmp in one_charge['consume_amounts']:
    #                         amount['consume_amount'] += float(one_charge['consume_amounts'][tmp])
    #                     amount['consume_amount'] = 0 - round(amount['consume_amount'], 2)
    #                 else:
    #                     amount['consume_amount'] = 0 - one_charge['consume_amount']
    #                 amount['total_amount'] = one_charge['total_amount']
    #                 amount['pooling_amount'] = 0 - one_charge['pooling_amount']
    #                 amount['charge_pooling_amount'] = one_charge['charge_pooling_amount']
    #                 print('amount', amount)
    #                 print('left_amount', get_sum(amount))
    #                 break
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取电表电量记录  /antapi/v1/amount_record
    # @ddt.data(
    #     *(get_cases(amount_record_cmd))
    # )
    # @ddt.unpack
    # def test_02_amount_record(self, url, name, method, param, check, do=0):
    #     global amount
    #     if 'count' in param:
    #         param['count'] = 5
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('history', ret)
    #         for one_charge in ret['history']:
    #             if one_charge['time'] > now_ms:
    #                 if param['uuid'] == elemeter_A4_uuid:
    #                     for tmp in one_charge['consume_amounts']:
    #                         amount['consume_amount'] += float(one_charge['consume_amounts'][tmp])
    #                     amount['consume_amount'] = 0 - round(amount['consume_amount'], 2)
    #                 else:
    #                     amount['consume_amount'] = 0 - one_charge['consume_amount']
    #                 amount['total_amount'] = one_charge['total_amount']
    #                 amount['pooling_amount'] = 0 - one_charge['pooling_amount']
    #                 amount['charge_pooling_amount'] = one_charge['charge_pooling_amount']
    #                 print('amount', amount)
    #                 print('left_amount', get_sum(amount))
    #                 break
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # # 获取房间电量值   /v2/room_elemeter_amount
    # @ddt.data(
    #     *(get_cases(room_elemeter_amount_cmd))
    # )
    # @ddt.unpack
    # def test_02_room_elemeter_amount(self, url, name, method, param, check, do=0):
    #     global amount
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('total_amount', ret)
    #         amount['consume_amount'] = 0 - ret['consume_amount']
    #         amount['total_amount'] = ret['total_amount']
    #         amount['pooling_amount'] = 0 - ret['pooling_amount']
    #         amount['charge_pooling_amount'] = ret['charge_pooling_amount']
    #         print('amount', amount)
    #         print('left_amount', get_sum(amount))
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # # 获取最新剩余电量    /v2/elemeter_last_power_history_with_pool
    # @ddt.data(
    #     *(get_cases(elemeter_last_power_history_with_pool_cmd))
    # )
    # @ddt.unpack
    # def test_02_elemeter_last_power_history_with_pool(self, url, name, method, param, check, do=0):
    #     global amount
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('history', ret)
    #         if param['uuid'] == elemeter_A4_uuid:
    #             for tmp in ret['history']['consume_amounts']:
    #                 amount['consume_amount'] += float(ret['history']['consume_amounts'][tmp])
    #             amount['consume_amount'] = 0 - round(amount['consume_amount'], 2)
    #         else:
    #             amount['consume_amount'] = 0 - ret['history']['consume_amount']
    #         amount['consume_amount'] = 0 - ret['history']['consume_amount']
    #         amount['total_amount'] = ret['history']['total_amount']
    #         amount['pooling_amount'] = 0 - ret['history']['pooling_amount']
    #         amount['charge_pooling_amount'] = ret['history']['charge_pooling_amount']
    #         print('amount', amount)
    #         print('left_amount', get_sum(amount))
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # # 获取房间电量值
    # @ddt.data(
    #     *(get_cases(get_room_amount_cmd))
    # )
    # @ddt.unpack
    # def test_02_get_room_amount(self, url, name, method, param, check, do=0):
    #     global amount
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('left_amount', ret)
    #         amount['consume_amount'] = 0 - ret['consume_amount']
    #         amount['total_amount'] = ret['total_amount']
    #         amount['pooling_amount'] = 0 - ret['pooling_amount']
    #         amount['charge_pooling_amount'] = ret['charge_pooling_amount']
    #         print('amount', amount)
    #         print('left_amount', get_sum(amount))
    #         self.assertEqual(get_sum(amount), ret['left_amount'])
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # # 获取房间剩余电量
    # @ddt.data(
    #     ['/v3/rooms/' + room_id_saas, '查询剩余电量-SaaSAPI', 'get', 0, {}]
    # )
    # @ddt.unpack
    # def test_02_get_amount_saasapi(self, url, name, method, param, check, do=0):
    #     global amount
    #     ret = run_case_saasapi(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('result', ret)
    #         amount['consume_amount'] = 0 - float(ret['result']['electric_read'])
    #         amount['total_amount'] = float(ret['result']['electric_amount'])
    #         amount['pooling_amount'] = 0 - float(ret['result']['pool_read'])
    #         amount['charge_pooling_amount'] = float(ret['result']['pool_amount'])
    #         print('amount', amount)
    #         print('left_amount', get_sum(amount))
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # # 充电量
    # @ddt.data(
    #     *(get_cases(elemeter_charge_cmd))
    # )
    # @ddt.unpack
    # def test_03_elemeter_charge(self, url, name, method, param, check, do=0):
    #     global serial_no, trade_num, charge_amount
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('serial_no', ret)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     charge_amount.append(param['amount'])
    #     serial_no.append(ret['serial_no'])
    #     trade_num.append(param['trade_num'])
    #     return
    #
    # # 电量充值(含公摊)
    # @ddt.data(
    #     *(get_cases(elemeter_charge_with_pool_cmd))
    # )
    # @ddt.unpack
    # def test_03_elemeter_charge_with_pool(self, url, name, method, param, check, do=0):
    #     global serial_no, trade_num, charge_amount
    #     if ('trade_num' in param and '-F-' not in name) or ('trade_num' not in name and '-F-' in name):
    #         param['trade_num'] = get_string(3)
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('serial_no', ret)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     charge_amount.append(param['amount'])
    #     serial_no.append(ret['serial_no'])
    #     trade_num.append(param['trade_num'])
    #     return

    # # 充电量 saas
    # @ddt.data(
    #     ['/v3/rooms/' + room_id_saas + '/elemeters/charge', '充电量-SaaSAPI', 'post', {'amount': 1.1}, 0]
    # )
    # @ddt.unpack
    # def test_03_charge_saasapi(self, url, name, method, param, check, do=0):
    #     global serial_no, trade_num, charge_amount
    #     ret = run_case_saasapi(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('ok', ret['result'])
    #     elif do == 1:
    #         self.assertEqual(check, ret['err_code'])
    #     charge_amount.append(param['amount'])
    #     return

    # # 充电费（不含公摊）
    # @ddt.data(
    #     *(get_cases(elemeter_charge_fees_cmd))
    # )
    # @ddt.unpack
    # def test_04_elemeter_charge_fees(self, url, name, method, param, check, do=0):
    #     global serial_no, trade_num, charge_amount
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('serial_no', ret)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     charge_amount.append(param['fees'])
    #     serial_no.append(ret['serial_no'])
    #     trade_num.append(param['trade_num'])
    #     return
    #
    # # 充电费(含公摊)
    # @ddt.data(
    #     *(get_cases(elemeter_charge_fees_with_pool_cmd))
    # )
    # @ddt.unpack
    # def test_05_elemeter_charge_fees_with_pool(self, url, name, method, param, check, do=0):
    #     global serial_no, trade_num, charge_amount
    #     if ('trade_num' in param and '-F-' not in name) or ('trade_num' not in name and '-F-' in name):
    #         param['trade_num'] = get_string(3)
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('serial_no', ret)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     charge_amount.append(param['fees'])
    #     serial_no.append(ret['serial_no'])
    #     trade_num.append(param['trade_num'])
    #     return
    # #
    # # 查询电表充值结果
    # @ddt.data(
    #     *(get_cases(elemeter_charge_query_cmd))
    # )
    # @ddt.unpack
    # def test_06_elemeter_charge_query(self, url, name, method, param, check, do=0):
    #     global serial_no, trade_num
    #     for i in range(len(serial_no)):
    #         if 'serial_no' in param and '-F-' not in name:
    #             param['serial_no'] = serial_no[i]
    #         if 'trade_num' in param and '-F-' not in name:
    #             param['trade_num'] = trade_num[i]
    #         ret = run_case(url, name, method, param)
    #         if do == 0:
    #             self.assertIn('charge_stage', ret)
    #         elif do == 1:
    #             self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取电表充值记录
    # @ddt.data(
    #     *(get_cases(elemeter_fetch_charge_history_cmd))
    # )
    # @ddt.unpack
    # def test_07_elemeter_fetch_charge_history(self, url, name, method, param, check, do=0):
    #     global charge_amount
    #     if 'count' in param:
    #         param['count'] = 30
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('history', ret)
    #         for one_charge in ret['history']:
    #             if one_charge['time'] > now_ms:
    #                 self.assertIn(float(one_charge['amount']), charge_amount)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # # 查询电表充值记录 saas
    # @ddt.data(
    #     ['/v3/rooms/' + room_id_saas + '/elemeter/charge_list', '查询充值结果-SaaSAPI', 'get', {'limit': 3, 'startTime': before_ms, 'endTime': after_ms}, 0]
    # )
    # @ddt.unpack
    # def test_07_get_charge_history_saasapi(self, url, name, method, param, check, do=0):
    #     global charge_amount
    #     ret = run_case_saasapi(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('history', ret)
    #         for one_charge in ret['history']:
    #             if one_charge['time'] > now_ms:
    #                 self.assertIn(float(one_charge['amount']), charge_amount)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # # 获取电表当前用电量
    # @ddt.data(
    #     *(get_cases(elemeter_read_cmd))
    # )
    # @ddt.unpack
    # def test_08_elemeter_read(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('serviceid', ret)
    #         self.assertEqual(CheckCallback(way='service', serviceid=ret['serviceid'], looptime=30), True)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     # time.sleep(30)
    #     return

    # # 查询剩余电量  /v2/elemeter_fetch_power_history_with_pool
    # @ddt.data(
    #     *(get_cases(elemeter_fetch_power_history_with_pool_cmd))
    # )
    # @ddt.unpack
    # def test_09_elemeter_fetch_power_history_with_pool(self, url, name, method, param, check, do=0):
    #     global amount, charge_amount
    #     if 'count' in param:
    #         param['count'] = 10
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('history', ret)
    #         old_left_amount = get_sum(amount)
    #         print('left_amount_old', old_left_amount)
    #         for one_charge in ret['history']:
    #             if one_charge['time'] > now_ms:
    #                 if param['uuid'] == elemeter_A4_uuid:
    #                     for tmp in one_charge['consume_amounts']:
    #                         amount['consume_amount'] += float(one_charge['consume_amounts'][tmp])
    #                     amount['consume_amount'] = 0 - round(amount['consume_amount'], 2)
    #                 else:
    #                     amount['consume_amount'] = 0 - one_charge['consume_amount']
    #                 amount['total_amount'] = one_charge['total_amount']
    #                 amount['pooling_amount'] = 0 - one_charge['pooling_amount']
    #                 amount['charge_pooling_amount'] = one_charge['charge_pooling_amount']
    #                 print('amount', amount)
    #                 print('left_amount_new', get_sum(amount))
    #                 self.assertEqual(old_left_amount, get_sum(amount) - get_sum(charge_amount))
    #                 break
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # # 获取电表电量记录  /antapi/v1/amount_record
    # @ddt.data(
    #     *(get_cases(amount_record_cmd))
    # )
    # @ddt.unpack
    # def test_09_amount_record(self, url, name, method, param, check, do=0):
    #     global amount, charge_amount
    #     if 'count' in param:
    #         param['count'] = 3
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('history', ret)
    #         old_left_amount = get_sum(amount)
    #         print('left_amount_old', old_left_amount)
    #         for one_charge in ret['history']:
    #             if one_charge['time'] > now_ms:
    #                 if param['uuid'] == elemeter_A4_uuid:
    #                     for tmp in one_charge['consume_amounts']:
    #                         amount['consume_amount'] += float(one_charge['consume_amounts'][tmp])
    #                     amount['consume_amount'] = 0 - round(amount['consume_amount'], 2)
    #                 else:
    #                     amount['consume_amount'] = 0 - one_charge['consume_amount']
    #                 amount['total_amount'] = one_charge['total_amount']
    #                 amount['pooling_amount'] = 0 - one_charge['pooling_amount']
    #                 amount['charge_pooling_amount'] = one_charge['charge_pooling_amount']
    #                 print('amount', amount)
    #                 print('left_amount', get_sum(amount))
    #                 self.assertEqual(old_left_amount, get_sum(amount) - get_sum(charge_amount))
    #                 break
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取房间电量值   /v2/room_elemeter_amount
    # @ddt.data(
    #     *(get_cases(room_elemeter_amount_cmd))
    # )
    # @ddt.unpack
    # def test_09_room_elemeter_amount(self, url, name, method, param, check, do=0):
    #     global amount, charge_amount
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('total_amount', ret)
    #         old_left_amount = get_sum(amount)
    #         print('left_amount_old', old_left_amount)
    #         amount['consume_amount'] = 0 - ret['consume_amount']
    #         amount['total_amount'] = ret['total_amount']
    #         amount['pooling_amount'] = 0 - ret['pooling_amount']
    #         amount['charge_pooling_amount'] = ret['charge_pooling_amount']
    #         print('amount', amount)
    #         print('left_amount', get_sum(amount))
    #         self.assertEqual(old_left_amount, get_sum(amount) - get_sum(charge_amount))
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # # 获取最新剩余电量    /v2/elemeter_last_power_history_with_pool
    # @ddt.data(
    #     *(get_cases(elemeter_last_power_history_with_pool_cmd))
    # )
    # @ddt.unpack
    # def test_09_elemeter_last_power_history_with_pool(self, url, name, method, param, check, do=0):
    #     global amount, charge_amount
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('history', ret)
    #         old_left_amount = get_sum(amount)
    #         print('left_amount_old', old_left_amount)
    #         if param['uuid'] == elemeter_A4_uuid:
    #             for tmp in ret['history']['consume_amounts']:
    #                 amount['consume_amount'] += float(ret['history']['consume_amounts'][tmp])
    #             amount['consume_amount'] = 0 - round(amount['consume_amount'], 2)
    #         else:
    #             amount['consume_amount'] = 0 - ret['history']['consume_amount']
    #         amount['total_amount'] = ret['history']['total_amount']
    #         amount['pooling_amount'] = 0 - ret['history']['pooling_amount']
    #         amount['charge_pooling_amount'] = ret['history']['charge_pooling_amount']
    #         print('amount', amount)
    #         print('left_amount', get_sum(amount))
    #         self.assertEqual(old_left_amount, get_sum(amount) - get_sum(charge_amount))
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # # 获取房间电量值
    # @ddt.data(
    #     *(get_cases(get_room_amount_cmd))
    # )
    # @ddt.unpack
    # def test_09_get_room_amount(self, url, name, method, param, check, do=0):
    #     global amount, charge_amount
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('left_amount', ret)
    #         old_left_amount = get_sum(amount)
    #         print('left_amount_old', old_left_amount)
    #         amount['consume_amount'] = 0 - ret['consume_amount']
    #         amount['total_amount'] = ret['total_amount']
    #         amount['pooling_amount'] = 0 - ret['pooling_amount']
    #         amount['charge_pooling_amount'] = ret['charge_pooling_amount']
    #         print('amount', amount)
    #         print('left_amount', get_sum(amount))
    #         self.assertEqual(get_sum(amount), ret['left_amount'])
    #         self.assertEqual(old_left_amount, get_sum(amount) - get_sum(charge_amount))
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # # 获取房间剩余电量
    # @ddt.data(
    #     ['/v3/rooms/' + room_id_saas, '查询剩余电量-SaaSAPI', 'get', 0, {}]
    # )
    # @ddt.unpack
    # def test_09_get_amount_saasapi(self, url, name, method, param, check, do=0):
    #     global amount
    #     ret = run_case_saasapi(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('result', ret)
    #         old_left_amount = get_sum(amount)
    #         print('left_amount_old', old_left_amount)
    #         amount['consume_amount'] = 0 - float(ret['result']['electric_read'])
    #         amount['total_amount'] = float(ret['result']['electric_amount'])
    #         amount['pooling_amount'] = 0 - float(ret['result']['pool_read'])
    #         amount['charge_pooling_amount'] = float(ret['result']['pool_amount'])
    #         print('amount', amount)
    #         print('left_amount', get_sum(amount))
    #         self.assertEqual(old_left_amount, get_sum(amount) - get_sum(charge_amount))
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # # 电表剩余电量清零
    # @ddt.data(
    #     *(get_cases(elemeter_charge_reset_cmd))
    # )
    # @ddt.unpack
    # def test_10_elemeter_charge_reset(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('serviceid', ret)
    #         # self.assertEqual(CheckCallback(way='service', serviceid=ret['serviceid'], looptime=30), True)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # # 剩余电量清零 saas
    # @ddt.data(
    #     ['/v3/rooms/' + room_id_saas + '/elemeters/left/reset', '剩余电量清零-SaaSAPI', 'post', {}, 0]
    # )
    # @ddt.unpack
    # def test_10_reset_left_amount_saasapi(self, url, name, method, param, check, do=0):
    #     global amount
    #     ret = run_case_saasapi(url, name, method, param)
    #     if do == 0:
    #         self.assertEqual(1, ret['result']['status'])
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # # 电表清零
    # @ddt.data(
    #     *(get_cases(elemeter_reset_by_collector_cmd))
    # )
    # @ddt.unpack
    # def test_10_elemeter_reset_by_collector(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('serviceid', ret)
    #         self.assertEqual(CheckCallback(way='service', serviceid=ret['serviceid'], looptime=30), True)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # # 电表清零 saas
    # @ddt.data(
    #     ['/v3/rooms/' + room_id_saas + '/elemeters/' + elemeter_A1_id + '/reset', '电表清零-SaaSAPI', 'post', {}, 0]
    # )
    # @ddt.unpack
    # def test_10_elemeter_reset_saasapi(self, url, name, method, param, check, do=0):
    #     global amount
    #     ret = run_case_saasapi(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('result', ret)
    #         self.assertEqual(CheckCallback(way='service', serviceid=ret['result']['serviceid'], looptime=30), True)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取电表充值记录
    # @ddt.data(
    #     *(get_cases(elemeter_fetch_charge_history_cmd))
    # )
    # @ddt.unpack
    # def test_11_elemeter_fetch_charge_history(self, url, name, method, param, check, do=0):
    #     global amount, charge_amount
    #     if 'count' in param:
    #         param['count'] = 5
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('history', ret)
    #         for one_charge in ret['history']:
    #             if one_charge['time'] > now_ms:
    #                 self.assertIn(float(one_charge['amount']), charge_amount)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取电表当前用电量
    # @ddt.data(
    #     *(get_cases(elemeter_read_cmd))
    # )
    # @ddt.unpack
    # def test_12_elemeter_read(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('serviceid', ret)
    #         self.assertEqual(CheckCallback(way='service', serviceid=ret['serviceid'], looptime=30), True)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     # time.sleep(30)
    #     return
    #
    # 查询剩余电量    /v2/elemeter_fetch_power_history_with_pool
    @ddt.data(
        *(get_cases(elemeter_fetch_power_history_with_pool_cmd))
    )
    @ddt.unpack
    def test_13_elemeter_fetch_power_history_with_pool(self, url, name, method, param, check, do=0):
        global amount, charge_amount
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('history', ret)
            old_left_amount = get_sum(amount)
            print('left_amount_old', old_left_amount)
            amount['total_amount'] = abs(amount['consume_amount'])
            amount['charge_pooling_amount'] = abs(amount['pooling_amount'])
            reset_amount = get_sum(amount)
            print('reset_amount', reset_amount)
            for one_charge in ret['history']:
                if one_charge['time'] > now_ms:
                    if param['uuid'] == elemeter_A4_uuid:
                        for tmp in one_charge['consume_amounts']:
                            amount['consume_amount'] += float(one_charge['consume_amounts'][tmp])
                        amount['consume_amount'] = 0 - round(amount['consume_amount'], 2)
                    else:
                        amount['consume_amount'] = 0 - one_charge['consume_amount']
                    amount['total_amount'] = one_charge['total_amount']
                    amount['pooling_amount'] = 0 - one_charge['pooling_amount']
                    amount['charge_pooling_amount'] = one_charge['charge_pooling_amount']
                    print('amount', amount)
                    print('left_amount', get_sum(amount))
                    self.assertEqual(reset_amount, get_sum(amount))
                    break
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # # 获取电表电量记录  /antapi/v1/amount_record
    # @ddt.data(
    #     *(get_cases(amount_record_cmd))
    # )
    # @ddt.unpack
    # def test_13_amount_record(self, url, name, method, param, check, do=0):
    #     global amount, charge_amount
    #     if 'count' in param:
    #         param['count'] = 3
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('history', ret)
    #         old_left_amount = get_sum(amount)
    #         print('left_amount_old', old_left_amount)
    #         amount['total_amount'] = abs(amount['consume_amount'])
    #         amount['charge_pooling_amount'] = abs(amount['pooling_amount'])
    #         reset_amount = get_sum(amount)
    #         print('reset_amount', reset_amount)
    #         for one_charge in ret['history']:
    #             if one_charge['time'] > now_ms:
    #                 if param['uuid'] == elemeter_A4_uuid:
    #                     for tmp in one_charge['consume_amounts']:
    #                         amount['consume_amount'] += float(one_charge['consume_amounts'][tmp])
    #                     amount['consume_amount'] = 0 - round(amount['consume_amount'], 2)
    #                 else:
    #                     amount['consume_amount'] = 0 - one_charge['consume_amount']
    #                 amount['total_amount'] = one_charge['total_amount']
    #                 amount['pooling_amount'] = 0 - one_charge['pooling_amount']
    #                 amount['charge_pooling_amount'] = one_charge['charge_pooling_amount']
    #                 print('amount', amount)
    #                 print('left_amount', get_sum(amount))
    #                 self.assertEqual(reset_amount, get_sum(amount))
    #                 break
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取房间电量值   /v2/room_elemeter_amount
    # @ddt.data(
    #     *(get_cases(room_elemeter_amount_cmd))
    # )
    # @ddt.unpack
    # def test_13_room_elemeter_amount(self, url, name, method, param, check, do=0):
    #     global amount, charge_amount
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('total_amount', ret)
    #         old_left_amount = get_sum(amount)
    #         print('left_amount_old', old_left_amount)
    #         amount['consume_amount'] = 0 - ret['consume_amount']
    #         amount['total_amount'] = ret['total_amount']
    #         amount['pooling_amount'] = 0 - ret['pooling_amount']
    #         amount['charge_pooling_amount'] = ret['charge_pooling_amount']
    #         print('amount', amount)
    #         print('left_amount', get_sum(amount))
    #         self.assertEqual(old_left_amount - get_sum(charge_amount), get_sum(amount))
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # # 获取最新剩余电量    /v2/elemeter_last_power_history_with_pool
    # @ddt.data(
    #     *(get_cases(elemeter_last_power_history_with_pool_cmd))
    # )
    # @ddt.unpack
    # def test_13_elemeter_last_power_history_with_pool(self, url, name, method, param, check, do=0):
    #     global amount, charge_amount
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('history', ret)
    #         old_left_amount = get_sum(amount)
    #         print('left_amount_old', old_left_amount)
    #         if param['uuid'] == elemeter_A4_uuid:
    #             for tmp in ret['history']['consume_amounts']:
    #                 amount['consume_amount'] += float(ret['history']['consume_amounts'][tmp])
    #             amount['consume_amount'] = 0 - round(amount['consume_amount'], 2)
    #         else:
    #             amount['consume_amount'] = 0 - ret['history']['consume_amount']
    #         amount['total_amount'] = ret['history']['total_amount']
    #         amount['pooling_amount'] = 0 - ret['history']['pooling_amount']
    #         amount['charge_pooling_amount'] = ret['history']['charge_pooling_amount']
    #         print('amount', amount)
    #         print('left_amount', get_sum(amount))
    #         self.assertEqual(old_left_amount - get_sum(charge_amount), get_sum(amount))
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取房间电量值
    # @ddt.data(
    #     *(get_cases(get_room_amount_cmd))
    # )
    # @ddt.unpack
    # def test_13_get_room_amount(self, url, name, method, param, check, do=0):
    #     global amount, charge_amount
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('left_amount', ret)
    #         old_left_amount = get_sum(amount)
    #         print('left_amount_old', old_left_amount)
    #         amount['consume_amount'] = 0 - ret['consume_amount']
    #         amount['total_amount'] = ret['total_amount']
    #         amount['pooling_amount'] = 0 - ret['pooling_amount']
    #         amount['charge_pooling_amount'] = ret['charge_pooling_amount']
    #         print('amount', amount)
    #         print('left_amount', get_sum(amount))
    #         self.assertEqual(get_sum(amount), ret['left_amount'])
    #         self.assertEqual(old_left_amount - get_sum(charge_amount), get_sum(amount))
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # # 获取房间剩余电量
    # @ddt.data(
    #     ['/v3/rooms/' + room_id_saas, '查询剩余电量-SaaSAPI', 'get', 0, {}]
    # )
    # @ddt.unpack
    # def test_13_get_amount_saasapi(self, url, name, method, param, check, do=0):
    #     global amount, charge_amount
    #     ret = run_case_saasapi(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('result', ret)
    #         old_left_amount = get_sum(amount)
    #         print('left_amount_old', old_left_amount)
    #         amount['consume_amount'] = 0 - float(ret['result']['electric_read'])
    #         amount['total_amount'] = float(ret['result']['electric_amount'])
    #         amount['pooling_amount'] = 0 - float(ret['result']['pool_read'])
    #         amount['charge_pooling_amount'] = float(ret['result']['pool_amount'])
    #         print('amount', amount)
    #         print('left_amount', get_sum(amount))
    #         self.assertEqual(old_left_amount - get_sum(charge_amount), get_sum(amount))
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return


if __name__ == '__main__':
    unittest.main()
