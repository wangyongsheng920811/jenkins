from OpenAPI.Data.final_data.device_data import *


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

    # 根据设备SN查询UUID
    @ddt.data(
        *(get_cases(get_device_uuid_cmd))
    )
    @ddt.unpack
    def test_01_get_device_uuid(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('result', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 获取设备信息
    @ddt.data(
        *(get_cases(get_device_info_cmd))
    )
    @ddt.unpack
    def test_02_get_device_info(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('result', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 查询设备操作记录
    @ddt.data(
        *(get_cases(search_device_op_log_cmd)),

    )
    @ddt.unpack
    def test_03_search_device_op_log(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('op_list', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 查询设备操作记录数量
    @ddt.data(
        *(get_cases(count_device_op_log_cmd))
    )
    @ddt.unpack
    def test_04_count_device_op_log(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('count', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 刷新设备信号强度
    @ddt.data(
        *(get_cases(refresh_devices_lqi_cmd))
    )
    @ddt.unpack
    def test_05_refresh_devices_lqi(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return

    # 获取设备历史异常记录数量
    @ddt.data(
        *(get_cases(device_count_exceptions_cmd))
    )
    @ddt.unpack
    def test_06_device_count_exceptions(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('count', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 获取设备历史异常记录
    @ddt.data(
        *(get_cases(device_fetch_exceptions_cmd))
    )
    @ddt.unpack
    def test_07_device_fetch_exceptions(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('device_exceptions', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 获取设备历史异常记录数量-三个月前
    @ddt.data(
        *(get_cases(device_count_exceptions_old_cmd))
    )
    @ddt.unpack
    def test_08_device_count_exceptions_old(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('count', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 获取设备历史异常记录-三个月前
    @ddt.data(
        *(get_cases(device_fetch_exceptions_old_cmd))
    )
    @ddt.unpack
    def test_09_device_fetch_exceptions_old(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('device_exceptions', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return


if __name__ == '__main__':
    unittest.main()
