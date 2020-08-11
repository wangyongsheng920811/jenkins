from OpenAPI.Data.final_data.wanke_buyu_data import *


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

    # 采集房源下的同类型设备读数
    @ddt.data(
        *(get_cases(meter_records_by_homeid_cmd))
    )
    @ddt.unpack
    def test_01_meter_records_by_homeid(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param, iftoken=False)
        if do == 0:
            self.assertIn('result', ret)
        elif do == 1:
            self.assertEqual(check, ret['errcode'])
        return

    # 实时采集电表读数
    @ddt.data(
        *(get_cases(realtime_query_cmd))
    )
    @ddt.unpack
    def test_02_realtime_query(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param, iftoken=False)
        if do == 0:
            self.assertIn('result', ret)
        elif do == 1:
            self.assertEqual(check, ret['errcode'])
        return

    # 跳合闸开关
    @ddt.data(
        *(get_cases(elemeter_control_cmd))
    )
    @ddt.unpack
    def test_03_elemeter_control(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param, iftoken=False)
        self.assertEqual(check, ret['errcode'])
        time.sleep(5)
        return


if __name__ == '__main__':
    unittest.main()



