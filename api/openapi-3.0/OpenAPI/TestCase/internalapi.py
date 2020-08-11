from OpenAPI.Data.final_data.internalapi_data import *


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

    # 获取商户是否存在
    @ddt.data(
        *(get_cases(check_is_client_cmd))
    )
    @ddt.unpack
    def test_01_check_is_client(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param, iftoken=False)
        self.assertEqual(check, ret['ErrNo'])
        return

    # 平台验证权限接口
    @ddt.data(
        *(get_cases(auth_observer_cmd))
    )
    @ddt.unpack
    def test_02_auth_observer(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param, iftoken=False)
        self.assertEqual(check, ret['ErrNo'])
        return

    # 平台取消权限接口
    @ddt.data(
        *(get_cases(unauth_observer_cmd))
    )
    @ddt.unpack
    def test_03_unauth_observer(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param, iftoken=False)
        self.assertEqual(check, ret['ErrNo'])
        return


if __name__ == '__main__':
    unittest.main()



