from OpenAPI.Data.final_data.ticket_data import *

# openapi/工单管理接口
'''
添加工单(add_ticket)
更新工单状态(update_ticket_state)
获取工单信息(get_ticket_by_id)
获取房源下所有工单(get_ticket_by_home)
更新工单信息(update_ticket)
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

    # 添加工单(add_ticket)
    @ddt.data(
        *(get_cases(add_ticket_cmd))
    )
    @ddt.unpack
    def test_01_add_ticket(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('ticket_id', ret)
        if do == 1:
            self.assertEqual(int(check), ret['ErrNo'])
        return

    # 获取工单信息(get_ticket_by_id)
    @ddt.data(
        *(get_cases(get_ticket_by_id_cmd))
    )
    @ddt.unpack
    def test_02_get_ticket_by_id(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('ticket_info', ret)
        if do == 1:
            self.assertEqual(int(check), ret['ErrNo'])
        return

    # 获取房源下所有工单(get_ticket_by_home)
    @ddt.data(
        *(get_cases(get_ticket_by_home_cmd))
    )
    @ddt.unpack
    def test_03_get_ticket_by_home(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        if do == 0:
            self.assertIn('home_ticket_list', ret)
        if do == 1:
            self.assertEqual(int(check), ret['ErrNo'])
        return

    # 更新工单状态(update_ticket_state)
    @ddt.data(
        *(get_cases(update_ticket_state_cmd))
    )
    @ddt.unpack
    def test_04_update_ticket_state(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(int(check), ret['ErrNo'])
        return

    # 更新工单信息(update_ticket)
    @ddt.data(
        *(get_cases(update_ticket_cmd))
    )
    @ddt.unpack
    def test_05_update_ticket(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(int(check), ret['ErrNo'])
        return

    # 删除工单
    @ddt.data(
        *(get_cases(delete_ticket_cmd))
    )
    @ddt.unpack
    def test_06_delete_ticket(self, url, name, method, param, check, do=0):
        if 'ticket_id' in param and '-F-' not in name:
            param['ticket_id'] = get_ticket_id('install')
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return


if __name__ == "__main__":
    unittest.main()
