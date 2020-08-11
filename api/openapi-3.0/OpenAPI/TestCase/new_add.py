from OpenAPI.Data.final_data.new_add_data import *


@ddt.ddt
class test_case(unittest.TestCase):
    # 每个测试用例执行之后做操作
    def tearDown(self):
        pass

    # 每个测试用例执行之前做操作
    def setUp(self):
        pass

    # 所有测试执行之前
    @classmethod
    def setUpClass(cls):
        pass

    # 所有测试执行之后
    @classmethod
    def tearDownClass(cls):
        pass

    # # 获取商户设置
    # @ddt.data(
    #     *(get_cases(get_client_setting_cmd))
    # )
    # @ddt.unpack
    # def test_01_get_client_setting(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param, way='raw')
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取公摊设置
    # @ddt.data(
    #     *(get_cases(get_home_setting_cmd))
    # )
    # @ddt.unpack
    # def test_02_get_home_setting(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取采集器信息
    # @ddt.data(
    #     *(get_cases(get_elecollector_info_cmd))
    # )
    # @ddt.unpack
    # def test_03_get_elecollector_info(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 工单测试
    # @ddt.data(
    #     *(get_cases(new_cmd))
    # )
    # @ddt.unpack
    # def test_04_add_new(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取房间下工单
    # @ddt.data(
    #     *(get_cases(get_ticket_by_room_cmd))
    # )
    # @ddt.unpack
    # def test_06_get_ticket_by_room(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取房间安装状态
    # @ddt.data(
    #     *(get_cases(find_home_state_cmd))
    # )
    # @ddt.unpack
    # def test_07_find_home_state(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 添加房间
    # @ddt.data(
    #     *(get_cases(add_room_cmd))
    # )
    # @ddt.unpack
    # def test_08_add_room(self, url, name, method, param, check, do=0):
    #     if 'room_id' in param and '-F-' not in name:
    #         param['room_id'] = get_string(5)
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return

    # 电费充值(含公摊)
    @ddt.data(
        *(get_cases(elemeter_charge_fees_with_pool_cmd))
    )
    @ddt.unpack
    def test_09_elemeter_charge_fees_with_pool(self, url, name, method, param, check, do=0):
        if ('trade_num' in param and '-F-' not in name)  or ('trade_num' not in name and '-F-' in name):
            param['trade_num'] = get_string(3)
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('serial_no', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # # 获取房间电量值
    # @ddt.data(
    #     *(get_cases(room_elemeter_amount_cmd))
    # )
    # @ddt.unpack
    # def test_10_room_elemeter_amount(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn(check, ret)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取房间电量值
    # @ddt.data(
    #     *(get_cases(get_room_amount_cmd))
    # )
    # @ddt.unpack
    # def test_11_get_room_amount(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn(check, ret)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 电量充值(含公摊)
    # @ddt.data(
    #     *(get_cases(elemeter_charge_with_pool_cmd))
    # )
    # @ddt.unpack
    # def test_12_elemeter_charge_with_pool(self, url, name, method, param, check, do=0):
    #     if ('trade_num' in param and '-F-' not in name) or ('trade_num' not in name and '-F-' in name):
    #         param['trade_num'] = get_string(3)
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('serial_no', ret)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 小程序授权和回调地址设置
    # @ddt.data(
    #     *(get_cases(client_setting_by_3rd_cmd))
    # )
    # @ddt.unpack
    # def test_16_client_setting_by_3rd(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取最新剩余电量
    # @ddt.data(
    #     *(get_cases(elemeter_last_power_history_with_pool_cmd))
    # )
    # @ddt.unpack
    # def test_17_elemeter_last_power_history_with_pool(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return


if __name__ == '__main__':
    unittest.main()



