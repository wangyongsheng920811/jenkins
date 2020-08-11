from OpenAPI.Data.final_data.water_data import *

'''
绑定水表采集器（add_water_gateway）未实现 #
解绑水表采集器（del_water_gateway）未实现 #
替换水表采集器（replace_water_gateway）未实现 #
绑定水表（add_watermeter）未实现 #
解绑水表（del_watermeter）未实现 #
获取添加水表的状态（add_watermeter_status）未实现 #
设置房间水表付费模式（update_room_water_pay_type）未实现
设置房间水表透支额度（update_watermeter_overdraft）未实现
向水表充值（watermeter_charge）未实现
水表剩余水量清零（watermeter_charge_reset）未实现
获取水表充值记录条数（count_watermeter_charge_record）未实现
获取水表充值记录（watermeter_charge_records）未实现

获取水表采集器信息（get_water_gateway_info）#
获取水表信息（get_watermeter_info） #
获取水表读数（read_watermeter） #
查询获取水表读数进度（read_watermeter_status） #
获取水表抄表记录条数（count_meter_record） #
获取水表抄表记录（get_meter_record） #
'''


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
        # empty_log('http.log')
        # empty_log('http_20.log')
        pass

    # 所有测试执行之后
    @classmethod
    def tearDownClass(cls):
        pass

    # # 绑定水表网关
    # @ddt.data(
    #     *(get_cases(add_water_gateway_cmd))
    # )
    # def test_01_add_water_gateway(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 解绑水表网关
    # @ddt.data(
    #     *(get_cases(del_water_gateway_cmd))
    # )
    # def test_02_del_water_gateway(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 替换水表网关
    # @ddt.data(
    #     *(get_cases(replace_water_gateway_cmd))
    # )
    # def test_03_replace_water_gateway(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 绑定水表
    # @ddt.data(
    #     *(get_cases(add_watermeter_cmd))
    # )
    # def test_04_add_watermeter(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取添加水表状态
    # @ddt.data(
    #     *(get_cases(add_watermeter_status_cmd))
    # )
    # def test_05_add_watermeter_status(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 解绑水表
    # @ddt.data(
    #     *(get_cases(del_watermeter_cmd))
    # )
    # def test_06_del_watermeter(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # 获取水表采集器信息  ##
    @ddt.data(
        *(get_cases(get_water_gateway_info_cmd))
    )
    @ddt.unpack
    def test_07_get_water_gateway_info(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('info', ret)
        elif do == 1:
            self.assertEqual(int(check), ret['ErrNo'])
        return

    # 获取水表信息  ##
    @ddt.data(
        *(get_cases(get_watermeter_info_cmd))
    )
    @ddt.unpack
    def test_08_get_watermeter_info(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('info', ret)
        elif do == 1:
            self.assertEqual(int(check), ret['ErrNo'])
        return

    # 获取水表读数  ##
    @ddt.data(
        *(get_cases(read_watermeter_cmd))
    )
    @ddt.unpack
    def test_09_read_watermeter(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(int(check), ret['ErrNo'])
        return

    # 查询获取水表读数进度  ##
    @ddt.data(
        *(get_cases(read_watermeter_status_cmd))
    )
    @ddt.unpack
    def test_10_read_watermeter_status(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('reading', ret)
        elif do == 1:
            self.assertEqual(int(check), ret['ErrNo'])
        return

    # # 设置房间水表付费模式
    # @ddt.data(
    #     *(get_cases(update_room_water_pay_type_cmd))
    #     )
    # @ddt.unpack
    # def test_11_update_room_water_pay_type(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 设置房间水表透支额度
    # @ddt.data(
    #     *(get_cases(update_watermeter_overdraft_cmd))
    #     )
    # @ddt.unpack
    # def test_12_update_watermeter_overdraft(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 向水表充值
    # @ddt.data(
    #     *(get_cases(watermeter_charge_cmd))
    #     )
    # @ddt.unpack
    # def test_13_watermeter_charge(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 水表剩余水量清零
    # @ddt.data(
    #     *(get_cases(watermeter_charge_reset_cmd))
    #     )
    # @ddt.unpack
    # def test_14_watermeter_charge_reset(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取水表充值记录条数
    # @ddt.data(
    #     *(get_cases(count_watermeter_charge_record_cmd))
    #     )
    # @ddt.unpack
    # def test_15_count_watermeter_charge_record(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取水表充值记录
    # @ddt.data(
    #     *(get_cases(watermeter_charge_records_cmd))
    #     )
    # @ddt.unpack
    # def test_16_watermeter_charge_records(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # 获取水表抄表记录条数  ##
    @ddt.data(
        *(get_cases(count_meter_record_cmd))
    )
    @ddt.unpack
    def test_17_count_meter_record(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('count', ret)
        elif do == 1:
            self.assertEqual(int(check), ret['ErrNo'])
        return

    # 获取水表抄表记录  ##
    @ddt.data(
        *(get_cases(get_meter_record_cmd))
    )
    @ddt.unpack
    def test_18_get_meter_record(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('records', ret)
        elif do == 1:
            self.assertEqual(int(check), ret['ErrNo'])
        return


if __name__ == "__main__":
    unittest.main()
