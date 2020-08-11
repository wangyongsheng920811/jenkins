from OpenAPI.Data.final_data.tenant_data import *


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
        # 删除所有租客(只清空1001房间的租客)
        del_all_tenant(room_1001)
        pass

    # 所有测试执行之后
    @classmethod
    def tearDownClass(cls):
        pass

    # 添加租客
    @ddt.data(
        *(get_cases(add_tenant_cmd))
    )
    @ddt.unpack
    def test_01_add_tenant(self, url, name, method, param, check, do=0):
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        if '-S-' in name:
            del_all_tenant(room_1001)
        return

    # 更新租客
    @ddt.data(
        *(get_cases(update_tenant_cmd))
    )
    @ddt.unpack
    def test_02_update_tenant(self, url, name, method, param, check, do=0):
        add_tenant_init()
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return

    # 根据房源id获取租客列表
    @ddt.data(
        *(get_cases(list_tenants_by_homeid_cmd))
    )
    @ddt.unpack
    def test_03_list_tenants_by_homeid(self, url, name, method, param, check, do=0):
        add_tenant_init()
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return

    # 根据room_id获取租客信息
    @ddt.data(
        *(get_cases(get_tenant_by_roomid_cmd))
    )
    @ddt.unpack
    def test_04_get_tenant_by_roomid(self, url, name, method, param, check, do=0):
        add_tenant_init()
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return

    # 删除租客
    @ddt.data(
        *(get_cases(delete_tenant_cmd))
    )
    @ddt.unpack
    def test_05_delete_tenant(self, url, name, method, param, check, do=0):
        add_tenant_init()
        ret = run_case(url, name, method, param)
        self.assertEqual(check, ret['ErrNo'])
        return


if __name__ == '__main__':
    unittest.main()



