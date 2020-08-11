from OpenAPI.Data.final_data.pooling_data import *


@ddt.ddt
class test_case(unittest.TestCase):

    # 每个测试用例执行之前做操作
    def setUp(self):
        pass

    # 每个测试用例执行之后做操作
    def tearDown(self):
        pass

    # 所有测试执行之前
    @classmethod
    def setUpClass(cls):
        pass

    # 所有测试执行之后
    @classmethod
    def tearDownClass(cls):
        pass

    # 获取房源公摊设置
    @ddt.data(
        *(get_cases(get_home_setting_cmd))
    )
    @ddt.unpack
    def test_01_get_home_setting(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return

    # 获取商户设置公摊配置
    @ddt.data(
        *(get_cases(get_client_setting_cmd))
    )
    @ddt.unpack
    def test_02_get_client_setting(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return

    # 控制商户公摊状态开启关闭
    @ddt.data(
        *(get_cases(switch_client_pooling_state_cmd))
    )
    @ddt.unpack
    def test_03_switch_client_pooling_state(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return

    # 设置商户公摊模式
    @ddt.data(
        *(get_cases(set_client_pooling_area_cmd))
    )
    @ddt.unpack
    def test_04_set_client_pooling_area(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return

    # 控制房源公摊状态开启关闭
    @ddt.data(
        *(get_cases(switch_home_pooling_state_cmd))
    )
    @ddt.unpack
    def test_05_switch_home_pooling_state(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param, way='raw')
        self.assertEqual(check, ret['ErrNo'])
        return

    # 设置房源公摊模式
    @ddt.data(
        *(get_cases(set_home_pooling_area_cmd))
    )
    @ddt.unpack
    def test_06_set_home_pooling_area(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return

    # 设置房源权重
    @ddt.data(
        *(get_cases(update_pooling_weight_cmd))
    )
    @ddt.unpack
    def test_07_update_pooling_weight(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return

    # 获取房源权重
    @ddt.data(
        *(get_cases(get_pooling_weight_cmd))
    )
    @ddt.unpack
    def test_08_get_pooling_weight(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return


if __name__ == '__main__':
    unittest.main()



