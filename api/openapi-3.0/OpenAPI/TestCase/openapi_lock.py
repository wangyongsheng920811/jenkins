from OpenAPI.Data.final_data.lock_data import *
from OpenAPI.Data.init_data.init_lock_data import *
from OpenAPI.Lib.aes import *
from OpenAPI.Lib.connect_server import *


@ddt.ddt
class test_case(unittest.TestCase):
    # 每个测试用例执行之后操作
    def tearDown(self):
        pass

    # 每个测试用例执行之前操作
    def setUp(self):
        global retrytimes
        retrytimes = 0
        pass

    # 所有测试执行之前
    @classmethod
    def setUpClass(cls):
        # 清空无效密码
        empty_lock_password(True)
        pass

    # 所有测试执行之后
    @classmethod
    def tearDownClass(cls):
        pass

    # 获取门锁状态信息
    @ddt.data(
        *(get_cases(get_lock_info_cmd))
    )
    @ddt.unpack
    def test_01_get_lock_info(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('device_id', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 获取门锁中已添加的密码信息
    @ddt.data(
        *(get_cases(fetch_passwords_cmd))
    )
    @ddt.unpack
    def test_02_fetch_passwords(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('passwords', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 获取超级管理员密码
    @ddt.data(
        *(get_cases(get_default_password_plaintext_cmd))
    )
    @ddt.unpack
    def test_03_get_default_password_plaintext(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('password', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 获取动态密码
    @ddt.data(
        *(get_cases(get_dynamic_password_plaintext_cmd))
    )
    @ddt.unpack
    def test_04_get_dynamic_password_plaintext(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('password', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 添加在线密码
    @ddt.data(
        *(get_cases(add_password_cmd))
    )
    @ddt.unpack
    def test_05_add_password(self, url, name, method, param, check, do=0):
        if 'password' in param and '-F-' not in name:
            param['password'] = str(get_numbers(6))
        if 'encrypted_password' in param and '-F-' not in name:
            if 'linux' in sys.platform:
                param['encrypted_password'] = ''
            else:
                param['encrypted_password'] = get_key_by_web(pwd=get_numbers(6), token_b_16=access_token_r[:16])
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('serviceid', ret)
            self.assertEqual(CheckCallback(way='service', serviceid=ret['serviceid'], looptime=30), True)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 添加激活码密码
    @ddt.data(
        *(get_cases(add_password_without_center_cmd))
    )
    @ddt.unpack
    def test_06_add_password_without_center(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('id', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 修改密码
    @ddt.data(
        *(get_cases(update_password_cmd))
    )
    @ddt.unpack
    def test_07_update_password(self, url, name, method, param, check, do=0):
        if 'password_id' in param and '-F-' not in name:
            param['password_id'] = int(get_password_id('center'))
        if 'encrypted_password' in param and '-F-' not in name:
            if 'linux' in sys.platform:
                param['encrypted_password'] = ''
            else:
                param['encrypted_password'] = get_key_by_web(pwd=get_numbers(6), token_b_16=access_token_r[:16])
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('serviceid', ret)
            self.assertEqual(CheckCallback(way='service', serviceid=ret['serviceid'], looptime=30), True)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # # 修改激活码密码
    # @ddt.data(
    #     *(get_cases(update_password_without_center_cmd))
    # )
    # @ddt.unpack
    # def test_08_update_password_without_center(self, url, name, method, param, check, do=0):
    #     if 'password_id' in param and '-F-' not in name:
    #         param['password_id'] = int(get_password_id('without_center'))
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('id', ret)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # # 删除密码
    # @ddt.data(
    #     *(get_cases(delete_password_cmd))
    # )
    # @ddt.unpack
    # def test_09_delete_password(self, url, name, method, param, check, do=0):
    #     if 'password_id' in param and '-F-' not in name:
    #         param['password_id'] = int(get_password_id('center'))
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('serviceid', ret)
    #         self.assertEqual(CheckCallback(way='service', serviceid=ret['serviceid'], looptime=30), True)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # # 冻结密码
    # @ddt.data(
    #     *(get_cases(frozen_password_cmd))
    # )
    # @ddt.unpack
    # def test_10_frozen_password(self, url, name, method, param, check, do=0):
    #     if 'password_id' in param and '-F-' not in name:
    #         param['password_id'] = int(get_password_id('center'))
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('serviceid', ret)
    #         self.assertEqual(CheckCallback(way='service', serviceid=ret['serviceid'], looptime=30), True)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # # 解冻密码
    # @ddt.data(
    #     *get_cases(unfrozen_password_cmd)
    # )
    # @ddt.unpack
    # def test_11_unfrozen_password(self, url, name, method, param, check, do=0):
    #     if 'password_id' in param and '-F-' not in name:
    #         param['password_id'] = int(get_password_id('frozen_center'))
    #     ret = run_case(url, name, method, param)
    #     if do == 0:
    #         self.assertIn('serviceid', ret)
    #         self.assertEqual(CheckCallback(way='service', serviceid=ret['serviceid'], looptime=30), True)
    #     elif do == 1:
    #         self.assertEqual(check, ret['ErrNo'])
    #     return

    # 获取开锁记录
    @ddt.data(
        *(get_cases(get_lock_events_cmd))
    )
    @ddt.unpack
    def test_12_get_lock_events(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('lock_events', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return

    # 统计门锁开门记录数量
    @ddt.data(
        *(get_cases(count_lock_events_cmd))
    )
    @ddt.unpack
    def test_13_count_lock_events(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('count', ret)
        elif do == 1:
            self.assertEqual(check, ret['ErrNo'])
        return


if __name__ == '__main__':
    unittest.main()
