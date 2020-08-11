from OpenAPI.Data.final_data.gateway_data import *

# finished


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

    # 获取网关信息
    @ddt.data(
        *(get_cases(get_center_info_cmd))
    )
    @ddt.unpack
    def test_01_get_center_info(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return

    # 获取房源下所有网关信息
    @ddt.data(
        *(get_cases(get_center_info_arr_cmd))
    )
    @ddt.unpack
    def test_02_get_device_info(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return


if __name__ == '__main__':
    unittest.main()
