from OpenAPI.Data.final_data.elemeter_data import *
from OpenAPI.Lib.connect_server import *


serial_no = ''
trade_num = ''


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
        # empty_log()
        pass

    # 所有测试执行之后
    @classmethod
    def tearDownClass(cls):
        pass

    # 获取电表基本信息  ##
    @ddt.data(
        *(get_cases(get_elemeter_info_cmd))
    )
    @ddt.unpack
    def test_01_get_elemeter_info(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('versions', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 设置电表透支额度  ##
    @ddt.data(
        *(get_cases(elemeter_update_overdraft_cmd))
    )
    @ddt.unpack
    def test_02_elemeter_update_overdraft(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('serviceid', ret)
            self.assertEqual(CheckCallback(way='service', serviceid=ret['serviceid'], looptime=30), True)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 电表清零  ##
    @ddt.data(
        *(get_cases(elemeter_reset_by_collector_cmd))
    )
    @ddt.unpack
    def test_03_elemeter_reset_by_collector(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('serviceid', ret)
            self.assertEqual(CheckCallback(way='service', serviceid=ret['serviceid'], looptime=30), True)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 设置电表最大功率  ##
    @ddt.data(
        *(get_cases(elemeter_update_max_capacity_cmd))
    )
    @ddt.unpack
    def test_04_elemeter_update_max_capacity(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('serviceid', ret)
            self.assertEqual(CheckCallback(way='service', serviceid=ret['serviceid'], looptime=30), True)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 获取电表当前用电量 ##
    @ddt.data(
        *(get_cases(elemeter_read_cmd))
    )
    @ddt.unpack
    def test_05_elemeter_read(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('serviceid', ret)
            self.assertEqual(CheckCallback(way='service', serviceid=ret['serviceid'], looptime=30), True)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 获取电表历史用电量  ##
    @ddt.data(
        *(get_cases(elemeter_fetch_power_consumption_cmd))
    )
    @ddt.unpack
    def test_06_elemeter_fetch_power_consumption(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('consumption', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # # 获取房间用电记录个数  ##
    # @ddt.data(
    #     *(get_cases(elemeter_count_power_history_cmd))
    # )
    # @ddt.unpack
    # def test_07_elemeter_count_power_history(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('count', ret)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # 获取电表用电记录  ##
    @ddt.data(
        *(get_cases(elemeter_fetch_power_history_cmd))
    )
    @ddt.unpack
    def test_08_elemeter_fetch_power_history(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('history', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 获取含公摊的电表用电记录  ##
    @ddt.data(
        *(get_cases(elemeter_fetch_power_history_with_pool_cmd))
    )
    @ddt.unpack
    def test_09_elemeter_fetch_power_history_with_pool(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('history', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 电表跳闸  ##
    @ddt.data(
        *(get_cases(elemeter_switch_off_cmd))
    )
    @ddt.unpack
    def test_10_elemeter_switch_off(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('serviceid', ret)
            self.assertEqual(CheckCallback(way='service', serviceid=ret['serviceid'], looptime=30), True)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 设置房间强制跳闸状态  ##
    @ddt.data(
        *(get_cases(elemeter_force_open_cmd))
    )
    @ddt.unpack
    def test_11_elemeter_force_open(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return

    # 发起电表同步
    @ddt.data(
        *(get_cases(elemeter_syn_data_cmd))
    )
    @ddt.unpack
    def test_12_elemeter_syn_data(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('serviceid', ret)
            self.assertEqual(CheckCallback(way='service', serviceid=ret['serviceid'], looptime=30), True)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 设置房间付费模式
    @ddt.data(
        *(get_cases(set_room_pay_type_cmd))
    )
    @ddt.unpack
    def test_13_set_room_pay_type(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return

    # 电表合闸  ##
    @ddt.data(
        *(get_cases(elemeter_switch_on_cmd))
    )
    @ddt.unpack
    def test_14_elemeter_switch_on(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('serviceid', ret)
            self.assertEqual(CheckCallback(way='service', serviceid=ret['serviceid'], looptime=30), True)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 向电表内充电
    @ddt.data(
        *(get_cases(elemeter_charge_cmd))
    )
    @ddt.unpack
    def test_15_elemeter_charge(self, url, name, method, param, check, do=0):
        global serial_no, trade_num
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('serial_no', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        if not serial_no:
            serial_no = ret['serial_no']
        if not trade_num:
            trade_num = param['trade_num']
        return

    # 向电表内充值
    @ddt.data(
        *(get_cases(elemeter_charge_fees_cmd))
    )
    @ddt.unpack
    def test_16_elemeter_charge_fees(self, url, name, method, param, check, do=0):
        global serial_no, trade_num
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('serial_no', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        if not serial_no:
            serial_no = ret['serial_no']
        if not trade_num:
            trade_num = param['trade_num']
        return

    # 查询电表充值结果
    @ddt.data(
        *(get_cases(elemeter_charge_query_cmd))
    )
    @ddt.unpack
    def test_17_elemeter_charge_query(self, url, name, method, param, check, do=0):
        if 'serial_no' in param and '-F-' not in name:
            param['serial_no'] = serial_no
        if 'trade_num' in param and '-F-' not in name:
            param['trade_num'] = trade_num
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('charge_stage', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 获取电表充值记录个数  ##
    @ddt.data(
        *(get_cases(elemeter_count_charge_history_cmd))
    )
    @ddt.unpack
    def test_18_elemeter_count_charge_history(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('count', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 获取电表充值记录  ##
    @ddt.data(
        *(get_cases(elemeter_fetch_charge_history_cmd))
    )
    @ddt.unpack
    def test_19_elemeter_fetch_charge_history(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('history', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 电表剩余电量清零  ##
    @ddt.data(
        *(get_cases(elemeter_charge_reset_cmd))
    )
    @ddt.unpack
    def test_20_elemeter_charge_reset(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('serviceid', ret)
            self.assertEqual(CheckCallback(way='service', serviceid=ret['serviceid'], looptime=30), True)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 获取房间电价及使用的计价方式（elemeter_get_price_and_way）
    @ddt.data(
        *(get_cases(elemeter_get_price_and_way_cmd))
    )
    @ddt.unpack
    def test_21_elemeter_get_price_and_way(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('eleprice_way', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 设置房源电价（elemeter_set_eleprice_by_home）
    @ddt.data(
        *(get_cases(elemeter_set_eleprice_by_home_cmd))
    )
    @ddt.unpack
    def test_22_elemeter_set_eleprice_by_home(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(int(check), ret['ErrNo'])
        return

    # 设置商户或房间电价（elemeter_set_eleprice）  ##
    @ddt.data(
        *(get_cases(elemeter_set_eleprice_cmd))
    )
    @ddt.unpack
    def test_23_elemeter_set_eleprice(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(int(check), ret['ErrNo'])
        return

    # 设置电价计算方式
    @ddt.data(
        *(get_cases(elemeter_set_eleprice_way_cmd))
    )
    @ddt.unpack
    def test_24_elemeter_set_eleprice_way(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(int(check), ret['ErrNo'])
        return

    # 获取房间电量值
    @ddt.data(
        *(get_cases(room_elemeter_amount_cmd))
    )
    @ddt.unpack
    def test_25_room_elemeter_amount(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('total_amount', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return


if __name__ == '__main__':
    unittest.main()
