from OpenAPI.Data.final_data.home_data import *


# finished


@ddt.ddt
class test_case(unittest.TestCase):
    def tearDown(self):
        # 每个测试用例执行之后做操作
        pass

    def setUp(self):
        # 每个测试用例执行之前做操作
        pass

    # 所有测试执行之前
    @classmethod
    def setUpClass(cls):
        # 初始化房源测试接口
        init_home_date()
        pass

    # 所有测试执行之后
    @classmethod
    def tearDownClass(cls):
        # search_all_home()
        pass

    # 新增房源
    @ddt.data(
        *(get_cases(add_home_cmd))
    )
    @ddt.unpack
    def test_01_add_home(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('home_id', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 更新房源
    @ddt.data(
        *(get_cases(update_home_cmd))
    )
    @ddt.unpack
    def test_02_update_home(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return

    # 删除房源
    @ddt.data(
        *(get_cases(del_home_cmd))
    )
    @ddt.unpack
    def test_03_del_home(self, url, name, method, param, check, do=0):
        if 'home_id' in param and '-F-' not in name:
            param['home_id'] = get_id('home_id')
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return

    # 查询房源
    @ddt.data(
        *(get_cases(search_home_info_cmd))
    )
    @ddt.unpack
    def test_04_search_home_info(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('home_list', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 查询满足条件房源数量
    @ddt.data(
        *(get_cases(count_home_info_cmd))
    )
    @ddt.unpack
    def test_05_count_home_info(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('count', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 向房源增加房间
    @ddt.data(
        *(get_cases(add_rooms_cmd))
    )
    @ddt.unpack
    def test_06_add_rooms(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return

    # 更新房间信息
    @ddt.data(
        *(get_cases(update_room_cmd))
    )
    @ddt.unpack
    def test_07_update_room(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return

    # 删除房间
    @ddt.data(
        *(get_cases(del_room_cmd))
    )
    @ddt.unpack
    def test_08_del_room(self, url, name, method, param, check, do=0):
        if 'room_id' in param and '-F-' not in name:
            param['room_id'] = get_id('room_id')
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return

    # 查询房源内设备信息
    @ddt.data(
        *(get_cases(find_home_device_cmd))
    )
    @ddt.unpack
    def test_09_find_home_device(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('result', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 查询一组房源的设备信息
    @ddt.data(
        *(get_cases(find_home_devices_cmd))
    )
    @ddt.unpack
    def test_10_find_home_devices(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('result', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 查询房源信息
    @ddt.data(
        *(get_cases(get_home_info_cmd))
    )
    @ddt.unpack
    def test_11_get_home_info(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('result', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return


if __name__ == '__main__':
    unittest.main()
