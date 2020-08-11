from OpenAPI.Data.final_data.antapi_data import *


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

    # # 获取门锁信息
    # @ddt.data(
    #     *(get_cases(antapi_get_lock_info_cmd))
    # )
    # @ddt.unpack
    # def test_01_antapi_get_lock_info(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param, way='raw')
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取租客密码id
    # @ddt.data(
    #     *(get_cases(antapi_get_lock_passwordid_cmd))
    # )
    # @ddt.unpack
    # def test_02_antapi_get_lock_passwordid(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取租客信息
    # @ddt.data(
    #     *(get_cases(antapi_get_tenant_info_cmd))
    # )
    # @ddt.unpack
    # def test_03_antapi_get_tenant_info(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取租客房源信息
    # @ddt.data(
    #     *(get_cases(antapi_get_tenant_home_cmd))
    # )
    # @ddt.unpack
    # def test_05_antapi_get_tenant_home(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 发起支付
    # @ddt.data(
    #     *(get_cases(antapi_tenant_place_transaction_cmd))
    # )
    # @ddt.unpack
    # def test_05_antapi_tenant_place_transaction(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param, way='raw')
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取电表信息
    # @ddt.data(
    #     *(get_cases(antapi_get_elemeter_info_cmd))
    # )
    # @ddt.unpack
    # def test_06_antapi_get_elemeter_info(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取电表电量记录
    # @ddt.data(
    #     *(get_cases(antapi_get_elemeter_amount_record_cmd))
    # )
    # @ddt.unpack
    # def test_07_antapi_get_elemeter_amount_record(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # 获取电表充值记录
    @ddt.data(
        *(get_cases(antapi_get_elemeter_charge_record_cmd))
    )
    @ddt.unpack
    def test_08_antapi_get_elemeter_charge_record(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return

    # # 获取水表基本信息
    # @ddt.data(
    #     *(get_cases(antapi_get_watermeter_info_cmd))
    # )
    # @ddt.unpack
    # def test_09_antapi_get_watermeter_info(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return
    #
    # # 获取水表水量记录
    # @ddt.data(
    #     *(get_cases(antapi_get_watermeter_amount_record_cmd))
    # )
    # @ddt.unpack
    # def test_10_antapi_get_watermeter_amount_record(self, url, name, method, param, check, do=0):
    #     ret = run_case(url, name, method, param)
    #     self.assertEqual(check, ret['ErrNo'])
    #     return


if __name__ == '__main__':
    unittest.main()



