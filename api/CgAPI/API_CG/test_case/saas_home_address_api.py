from API_CG.lib.saas_api_prepare import *


# 房源模块
@ddt.ddt
class Run_setting(unittest.TestCase):

    # 获取省份接口
    @ddt.data(
        ['/v3/provinces', 'get', '获取省份列表', {}, '0'],
    )
    @ddt.unpack
    def test_01(self, url, method, title, param, check_str, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 获取城市接口
    @ddt.data(
        ['/v3/cities', 'get', '获取城市列表,province_id正确', {'province_id': province['id']},
         'res["err_code"]==0 and len(res["result"])>0'],
        ['/v3/cities', 'get', '获取城市列表,province_id字段缺失', {}, 'res["err_code"]==0 and len(res["result"])>100'],
        ['/v3/cities', 'get', '获取城市列表,province_id类型错误', {'province_id': 'test'}, '400000'],
        ['/v3/cities', 'get', '获取城市列表,province_id为空', {'province_id': None},
         'res["err_code"]==0 and len(res["result"])>100'],
        ['/v3/cities', 'get', '获取城市列表,province_id不存在', {'province_id': 12345678}, '0'],
    )
    @ddt.unpack
    def test_02(self, url, method, title, param, check_str, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 获取区域接口
    @ddt.data(
        ['/v3/districts', 'get', '获取区域列表,city_id字段缺失', {'city_id': city['id']}, '0'],
        ['/v3/districts', 'get', '获取区域列表,city_id字段缺失', {}, '400000'],
        ['/v3/districts', 'get', '获取区域列表,city_id类型错误', {'city_id': 'test'}, '400000'],
        ['/v3/districts', 'get', '获取区域列表,city_id为空', {'city_id': None}, '400000'],
        ['/v3/districts', 'get', '获取区域列表,city_id不存在', {'city_id': 12345678}, '0'],
    )
    @ddt.unpack
    def test_03(self, url, method, title, param, check_str, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 新建房源
    @ddt.data(
        ['/v3/homes', 'post', '新建房源', {
            'home_name': home_name_root + '01',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'alias': '别名1',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '0'],
        ['/v3/homes', 'post', '新建房源,home_name重复', {
            'home_name': home['name'],
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'alias': '别名2',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '400044'],
        ['/v3/homes', 'post', '新建房源,home_name为空', {
            'home_name': None,
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'alias': '别名3',
            'number': ' 门牌号 ',
            'street': '测试街道'
        }, '400000'],
        ['/v3/homes', 'post', '新建房源,home_name类型错误', {
            'home_name': 12345,
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'alias': '别名4',
            'number': ' 门牌号 ',
            'street': '测试街道'
        }, '400000'],
        ['/v3/homes', 'post', '新建房源,home_name为空字符串', {
            'home_name': '',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'alias': '别名5',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '400000'],
        ['/v3/homes', 'post', '新建房源,home_name为空格', {
            'home_name': ' ',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'alias': '别名6',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '400000'],
        ['/v3/homes', 'post', '新建房源,home_name字段缺失', {
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'alias': '别名7',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '400000'],
        ['/v3/homes', 'post', '新建房源,home_type=0', {
            'home_name': home_name_root + '08',
            'branch_id': branch['id'],
            'home_type': 0,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '400000'],
        ['/v3/homes', 'post', '新建房源,home_type=1', {
            'home_name': home_name_root + '09',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '0'],
        ['/v3/homes', 'post', '新建房源,home_type=2', {
            'home_name': home_name_root + '10',
            'branch_id': branch['id'],
            'home_type': 2,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '0'],
        ['/v3/homes', 'post', '新建房源,home_type=3', {
            'home_name': home_name_root + '11',
            'branch_id': branch['id'],
            'home_type': 3,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '400000'],
        ['/v3/homes', 'post', '新建房源,home_type类型错误', {
            'home_name': home_name_root + '12',
            'branch_id': branch['id'],
            'home_type': 'test',
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '400000'],
        ['/v3/homes', 'post', '新建房源,home_type为空', {
            'home_name': home_name_root + '13',
            'branch_id': branch['id'],
            'home_type': None,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '0'],
        ['/v3/homes', 'post', '新建房源,home_type字段缺失', {
            'home_name': home_name_root + '14',
            'branch_id': branch['id'],
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '0'],
        ['/v3/homes', 'post', '新建房源,street为空', {
            'home_name': home_name_root + '15',
            'branch_id': branch['id'],
            'home_type': 1,
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': ''}, '400000'],
        ['/v3/homes', 'post', '新建房源,street类型错误', {
            'home_name': home_name_root + '16',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': 12345,
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': 12345}, '400000'],
        ['/v3/homes', 'post', '新建房源,street字段缺失', {
            'home_name': home_name_root + '17',
            'branch_id': branch['id'],
            'home_type': 1,
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',}, '400000'],
        ['/v3/homes', 'post', '新建房源,block为空', {
            'home_name': home_name_root + '18',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': '',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '400000'],
        ['/v3/homes', 'post', '新建房源,block类型错误', {
            'home_name': home_name_root + '17',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': 12345,
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '400000'],
        ['/v3/homes', 'post', '新建房源,block字段缺失', {
            'home_name': home_name_root + '17',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '400000'],
        ['/v3/homes', 'post', '新建房源,district不正确', {
            'home_name': home_name_root + '18',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': '接口测试区',
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'
        }, '400084'],
        ['/v3/homes', 'post', '新建房源,district类型错误', {
            'home_name': home_name_root + '19',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': 1234,
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'
        }, '400000'],
        ['/v3/homes', 'post', '新建房源,district为空', {
            'home_name': home_name_root + '20',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': None,
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'
        }, '400000'],
        ['/v3/homes', 'post', '新建房源,district字段缺失', {
            'home_name': home_name_root + '21',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'
        }, '400000'],
        ['/v3/homes', 'post', '新建房源,city不正确', {
            'home_name': home_name_root + '22',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': '接口测市',
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'
        }, '400083'],
        ['/v3/homes', 'post', '新建房源,city类型错误', {
            'home_name': home_name_root + '23',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': 1234,
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'
        }, '400000'],
        ['/v3/homes', 'post', '新建房源,city为空', {
            'home_name': home_name_root + '24',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': None,
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'
        }, '400000'],
        ['/v3/homes', 'post', '新建房源,city字段缺失', {
            'home_name': home_name_root + '25',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 '
        }, '400000'],
        ['/v3/homes', 'post', '新建房源,province不正确', {
            'home_name': home_name_root + '26',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': '测试省',
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'
        }, '400082'],
        ['/v3/homes', 'post', '新建房源,province类型错误', {
            'home_name': home_name_root + '27',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': 1234,
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'
        }, '400000'],
        ['/v3/homes', 'post', '新建房源,province为空', {
            'home_name': home_name_root + '28',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': None,
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'
        }, '400000'],
        ['/v3/homes', 'post', '新建房源,province字段缺失', {
            'home_name': home_name_root + '29',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            # 'province': None,
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'
        }, '400000'],
        ['/v3/homes', 'post', '新建房源,市/区不匹配', {
            'home_name': home_name_root + '30',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': '南山区',
            'city': '广州市',
            'province': '广东省',
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'
        }, '400084'],
        ['/v3/homes', 'post', '新建房源,省/市不匹配', {
            'home_name': home_name_root + '31',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': '南山区',
            'city': '深圳市',
            'province': '湖南省',
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'
        }, '400083'],
        ['/v3/homes', 'post', '新建房源,country不是中国', {
            'home_name': home_name_root + '32',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '日本',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '400081'],
        ['/v3/homes', 'post', '新建房源,country类型错误', {
            'home_name': home_name_root + '33',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': 1234,
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '400000'],
        ['/v3/homes', 'post', '新建房源,country为空', {
            'home_name': home_name_root + '34',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': None,
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '0'],
        ['/v3/homes', 'post', '新建房源,country不传', {
            'home_name': home_name_root + '35',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '0'],
        ['/v3/homes', 'post', '新建房源,description类型错误', {
            'home_name': home_name_root + '36',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': 123,
            'number': ' 门牌号 ',
            'street': '测试街道'}, '400000'],
        ['/v3/homes', 'post', '新建房源,description为空', {
            'home_name': home_name_root + '37',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': None,
            'number': ' 门牌号 ',
            'street': '测试街道'}, '0'],
        ['/v3/homes', 'post', '新建房源,description为空字符串', {
            'home_name': home_name_root + '38',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '0'],
        ['/v3/homes', 'post', '新建房源,description不传', {
            'home_name': home_name_root + '39',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            # 'description': '',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '0'],
        ['/v3/homes', 'post', '新建房源,number类型错误', {
            'home_name': home_name_root + '40',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': 1234,
            'street': '测试街道'}, '400000'],
        ['/v3/homes', 'post', '新建房源,number为空', {
            'home_name': home_name_root + '41',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': None,
            'street': '测试街道'}, '400000'],
        ['/v3/homes', 'post', '新建房源,number不传', {
            'home_name': home_name_root + '41',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'street': '测试街道'}, '400000'],
        ['/v3/homes', 'post', '新建房源,alias重复', {
            'home_name': home_name_root + '42',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'alias': home['alias'],
            'number': ' 门牌号 ',
            'description': '描述',
            'street': '测试街道'}, '400044'],
        ['/v3/homes', 'post', '新建房源,alias不传', {
            'home_name': home_name_root + '43',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            # 'alias': '别名999',
            'number': ' 门牌号 ',
            'description': '描述',
            'street': '测试街道'}, '0'],
        ['/v3/homes', 'post', '新建房源,alias类型错误', {
            'home_name': home_name_root + '44',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'alias': 1234,
            'number': ' 门牌号 ',
            'description': '描述',
            'street': '测试街道'}, '400000'],
        ['/v3/homes', 'post', '新建房源,alias为空', {
            'home_name': home_name_root + '45',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'alias': None,
            'number': ' 门牌号 ',
            'description': '描述',
            'street': '测试街道'}, '0'],
        ['/v3/homes', 'post', '新建房源,alias为空字符串', {
            'home_name': home_name_root + '46',
            'branch_id': branch['id'],
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'alias': '',
            'number': ' 门牌号 ',
            'description': '描述',
            'street': '测试街道'}, '0'],
        ['/v3/homes', 'post', '新建房源,branch_id参数缺失', {
            'home_name': home_name_root + '47',
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '0'],
        ['/v3/homes', 'post', '新建房源,branch_id类型错误', {
            'home_name': home_name_root + '48',
            'branch_id': 'test',
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '400000'],
        ['/v3/homes', 'post', '新建房源,branch_id类型错误', {
            'home_name': home_name_root + '49',
            'branch_id': 32222.5,
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '400000'],
        ['/v3/homes', 'post', '新建房源,branch_id不存在', {
            'home_name': home_name_root + '50',
            'branch_id': 12345,
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '400121'],
        ['/v3/homes', 'post', '新建房源,branch_id为空字符串', {
            'home_name': home_name_root + '51',
            'branch_id': '',
            'home_type': 1,
            'address': ' 测试地址 ',
            'block': ' 测试小区 ',
            'district': district['name'],
            'city': city['name'],
            'province': province['name'],
            'country': '中国',
            'description': '描述',
            'number': ' 门牌号 ',
            'street': '测试街道'}, '400000'],
    )
    @ddt.unpack
    def test_04(self, url, method, title, param, check_str, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 获取房源详情
    @ddt.data(
        ['/v3/homes/' + str(home['home_id']), 'get', '获取房源详情', {}, '0'],
        ['/v3/homes/1234', 'get', '获取房源详情,home_id不正确', {}, '403004'],
        ['/v3/homes/test', 'get', '获取房源详情,home_id类型错误', {}, '400000'],
    )
    @ddt.unpack
    def test_05(self, url, method, title, param, check_str, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 获取房源楼层
    @ddt.data(
        ['/v3/homes/' + str(home['home_id']) + '/floors', 'get', '获取房源楼层,分散式房源', {}, '0'],
        ['/v3/homes/' + str(home_update['home_id']) + '/floors', 'get', '获取房源楼层,集中式房源', {}, '0'],
        ['/v3/homes/test/floors', 'get', '获取房源楼层,home_id类型错误', {}, '400000'],
        ['/v3/homes/12345/floors', 'get', '获取房源楼层,home_id不正确', {}, '403004'],
    )
    @ddt.unpack
    def test_06(self, url, method, title, param, check_str, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 修改房源详情
    @ddt.data(
        ['/v3/homes/' + str(home_update['home_id']), 'put', '更新房源,无参数,不修改', {}, '0'],
        ['/v3/homes/' + str(home_update['home_id']), 'put', '更新房源,home_name正确', {'home_name': home_update['name']+'_updated'}, '0'],
        ['/v3/homes/' + str(home_update['home_id']), 'get', '更新后检查', {}, 'res["result"]["home_name"]=="' + home_update['name'] + '_updated"'],
        ['/v3/homes/' + str(home_update['home_id']), 'put', '更新房源,home_name类型错误', {'home_name': 1234}, '400000'],
        ['/v3/homes/' + str(home_update['home_id']), 'put', '更新房源,home_name为空', {'home_name': None}, '0'],
        ['/v3/homes/' + str(home_update['home_id']), 'put', '更新房源,home_name空格', {'home_name': ' '}, '400000'],
        ['/v3/homes/' + str(home_update['home_id']), 'put', '更新房源,home_name重复', {'home_name': home['name']}, '400044'],
        ['/v3/homes/' + str(home_update['home_id']), 'put', '更新房源,alias正确', {'alias': '别名998'}, '0'],
        ['/v3/homes/' + str(home_update['home_id']), 'get', '更新后检查', {}, 'res["result"]["alias"]=="别名998"'],
        ['/v3/homes/' + str(home_update['home_id']), 'put', '更新房源,alias类型错误', {'alias': 1234}, '400000'],
        ['/v3/homes/' + str(home_update['home_id']), 'put', '更新房源,alias为空', {'alias': None}, '0'],
        ['/v3/homes/' + str(home_update['home_id']), 'put', '更新房源,alias重复', {'alias': home['alias']}, '400044'],
        ['/v3/homes/' + str(home_update['home_id']), 'put', '更新房源,home_type', {'home_type': 2}, ''],
        ['/v3/homes/' + str(home_update['home_id']), 'get', '更新后检查', {}, 'res["result"]["home_type"]==1'],
        ['/v3/homes/' + str(home_update['home_id']), 'put', '更新房源,description', {'description': 'T'}, '0'],
        ['/v3/homes/' + str(home_update['home_id']), 'get', '更新后检查', {}, 'res["result"]["description"]=="T"'],
        ['/v3/homes/' + str(home_update['home_id']), 'put', '更新房源,description为空', {'description': None}, '0'],
        ['/v3/homes/' + str(home_update['home_id']), 'put', '更新房源,description为空字符串', {'description': ''}, '0'],
        ['/v3/homes/' + str(home_update['home_id']), 'put', '更新房源,description类型错误', {'description': 1234}, '400000'],
    )
    @ddt.unpack
    def test_07(self, url, method, title, param, check_str, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 获取房源设置
    @ddt.data(
        ['/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'get', '获取房源设置', {}, '0'],
        ['/v3/homes/test/elemeter_setting', 'get', '获取房源设置,home_id类型错误', {}, '400000'],
        ['/v3/homes/12345/elemeter_setting', 'get', '获取房源设置,home_id不存在', {}, '403004'],
    )
    @ddt.unpack
    def test_08(self, url, method, title, param, check_str, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 获取房源公摊设置
    @ddt.data(
        ['/v3/homes/' + str(home['home_id']) + '/pool_setting', 'get', '获取房源设置', {}, '0'],
        ['/v3/homes/test/pool_setting', 'get', '获取房源设置,home_id类型错误', {}, '400000'],
        ['/v3/homes/12345/pool_setting', 'get', '获取房源设置,home_id不存在', {}, '403004'],
    )
    @ddt.unpack
    def test_09(self, url, method, title, param, check_str, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 更改房源设置
    @ddt.data(
        ['更改房源设置overdraft_amount参数正确:1', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 1, 'pay_type': 1}, '0', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'put'],
        ['更改房源设置overdraft_amount参数正确:99', {'overdraft_amount': 99, 'low_warn': 3, 'ele_price': 1, 'pay_type': 1}, '0', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting',
         'put'],
        ['更改房源设置overdraft_amount参数缺失', {'low_warn': 3, 'ele_price': 1, 'pay_type': 1}, '403001', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'put'],
        ['更改房源设置overdraft_amount参数错误:-1', {'overdraft_amount': -1, 'low_warn': 3, 'ele_price': 1, 'pay_type': 1}, '400000', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting',
         'put'],
        ['更改房源设置overdraft_amount类型错误', {'overdraft_amount': 'test', 'low_warn': 3, 'ele_price': 1, 'pay_type': 1}, '400000', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting',
         'put'],
        ['更改房源设置low_warn参数正确:1', {'overdraft_amount': 1, 'low_warn': 1, 'ele_price': 1, 'pay_type': 1}, '0', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'put'],
        ['更改房源设置low_warn参数正确:99', {'overdraft_amount': 1, 'low_warn': 99, 'ele_price': 1, 'pay_type': 1}, '0', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'put'],
        ['更改房源设置low_warn参数缺失', {'overdraft_amount': 1, 'ele_price': 1, 'pay_type': 1}, '403001', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'put'],
        ['更改房源设置low_warn参数错误:0', {'overdraft_amount': 1, 'low_warn': 0, 'ele_price': 1, 'pay_type': 1}, '403001', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'put'],
        ['更改房源设置low_warn参数错误:-1', {'overdraft_amount': 1, 'low_warn': -1, 'ele_price': 1, 'pay_type': 1}, '400000', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'put'],
        ['更改房源设置low_warn类型错误', {'overdraft_amount': 1, 'low_warn': 'test', 'ele_price': 1, 'pay_type': 1}, '400000', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'put'],
        ['更改房源设置ele_price参数正确:0.1', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 0.1, 'pay_type': 1}, '0', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'put'],
        ['更改房源设置ele_price参数正确:5', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 5, 'pay_type': 1}, '0', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'put'],
        ['更改房源设置ele_price参数缺失', {'overdraft_amount': 1, 'low_warn': 3, 'pay_type': 1}, '0', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'put'],
        ['更改房源设置ele_price参数错误:0', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 0, 'pay_type': 1}, '400000', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'put'],
        ['更改房源设置ele_price参数错误:6', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 6, 'pay_type': 1}, '400000', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'put'],
        ['更改房源设置ele_price类型错误', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 'test', 'pay_type': 1}, '400000', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'put'],
        ['更改房源设置pay_type参数缺失', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 1}, '403001', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'put'],
        ['更改房源设置pay_type参数错误:1.1', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 1, 'pay_type': 1.1}, '400000', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'put'],
        ['更改房源设置pay_type类型错误', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 1, 'pay_type': 'test'}, '400000', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'put'],
        ['更改房源设置pay_type范围错误', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 1, 'pay_type': 0}, '400000', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'put'],
        ['更改房源设置pay_type最大值', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 1, 'pay_type': 2}, '0', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'put'],
        ['更改房源设置pay_type范围错误', {'overdraft_amount': 1, 'low_warn': 3, 'ele_price': 1, 'pay_type': 3}, '400000', '/v3/homes/' + str(home['home_id']) + '/elemeter_setting', 'put'],
    )
    @ddt.unpack
    def test_10(self, title, param, check_str, url, method, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 更改房源公摊设置
    @ddt.data(
        ['更改房源公摊设置pool_area_type参数正确:1', {'pool_area_type': 1, 'use_pool': True, 'pool_type': 1}, '0', '/v3/homes/' + str(home['home_id']) + '/pool_setting', 'put'],
        ['更改房源公摊设置pool_area_type参数缺失', {'use_pool': True, 'pool_type': 1}, '0', '/v3/homes/' + str(home['home_id']) + '/pool_setting', 'put'],
        ['更改房源公摊设置pool_area_type参数错误:1.1', {'pool_area_type': 1.1, 'use_pool': True, 'pool_type': 1}, '400000', '/v3/homes/' + str(home['home_id']) + '/pool_setting', 'put'],
        ['更改房源公摊设置pool_area_type类型错误', {'pool_area_type': 'test', 'use_pool': True, 'pool_type': 1}, '400000', '/v3/homes/' + str(home['home_id']) + '/pool_setting', 'put'],
        ['更改房源公摊设置pool_area_type范围错误', {'pool_area_type': 0, 'use_pool': True, 'pool_type': 1}, '400000', '/v3/homes/' + str(home['home_id']) + '/pool_setting', 'put'],
        ['更改房源公摊设置pool_area_type最大值', {'pool_area_type': 2, 'use_pool': True, 'pool_type': 1}, '0', '/v3/homes/' + str(home['home_id']) + '/pool_setting', 'put'],
        ['更改房源公摊设置pool_area_type范围错误', {'pool_area_type': 3, 'use_pool': True, 'pool_type': 1}, '400000', '/v3/homes/' + str(home['home_id']) + '/pool_setting', 'put'],
        ['更改房源公摊设置use_pool参数正确:False', {'pool_area_type': 1, 'use_pool': False, 'pool_type': 1}, '0', '/v3/homes/' + str(home['home_id']) + '/pool_setting', 'put'],
        ['更改房源公摊设置use_pool参数缺失', {'pool_area_type': 1, 'pool_type': 1}, '0', '/v3/homes/' + str(home['home_id']) + '/pool_setting', 'put'],
        ['更改房源公摊设置use_pool类型错误', {'pool_area_type': 1, 'use_pool': 'test', 'pool_type': 1}, '400000', '/v3/homes/' + str(home['home_id']) + '/pool_setting', 'put'],
        ['更改房源公摊设置pool_type参数缺失', {'pool_area_type': 1, 'use_pool': True}, '0', '/v3/homes/' + str(home['home_id']) + '/pool_setting', 'put'],
        ['更改房源公摊设置pool_type参数错误:1.1', {'pool_area_type': 1, 'use_pool': True, 'pool_type': 1.1}, '400000', '/v3/homes/' + str(home['home_id']) + '/pool_setting', 'put'],
        ['更改房源公摊设置pool_type类型错误', {'pool_area_type': 1, 'use_pool': True, 'pool_type': 'test'}, '400000', '/v3/homes/' + str(home['home_id']) + '/pool_setting', 'put'],
        ['更改房源公摊设置pool_type范围错误', {'pool_area_type': 1, 'use_pool': True, 'pool_type': 0}, '400000', '/v3/homes/' + str(home['home_id']) + '/pool_setting', 'put'],
        # ['更改房源公摊设置pool_type最大值', {'pool_area_type': 1, 'use_pool': True, 'pool_type': 2}, '0', '/v3/homes/' + str(home['home_id']) + '/pool_setting', 'put'],
        ['更改房源公摊设置pool_type范围错误', {'pool_area_type': 1, 'use_pool': True, 'pool_type': 3}, '400000', '/v3/homes/' + str(home['home_id']) + '/pool_setting', 'put'],
    )
    @ddt.unpack
    def test_11(self, title, param, check_str, url, method, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')

    # 获取房源设备列表
    @ddt.data(
        ['获取房源设备列表device_type参数正确:1', {'device_type': 1}, '0', '/v3/homes/' + str(home['home_id']) + '/devices', 'get'],
        ['获取房源设备列表device_type参数正确:2', {'device_type': 2}, '0', '/v3/homes/' + str(home['home_id']) + '/devices', 'get'],
        ['获取房源设备列表device_type参数正确:3', {'device_type': 3}, '0', '/v3/homes/' + str(home['home_id']) + '/devices', 'get'],
        ['获取房源设备列表device_type参数正确:4', {'device_type': 4}, '0', '/v3/homes/' + str(home['home_id']) + '/devices', 'get'],
        ['获取房源设备列表device_type参数正确:5', {'device_type': 5}, '0', '/v3/homes/' + str(home['home_id']) + '/devices', 'get'],
        ['获取房源设备列表device_type参数正确:6', {'device_type': 6}, '0', '/v3/homes/' + str(home['home_id']) + '/devices', 'get'],
        ['获取房源设备列表device_type参数缺失', {}, '0', '/v3/homes/' + str(home['home_id']) + '/devices', 'get'],
        ['获取房源设备列表device_type参数错误:999', {'device_type': 999}, '400000', '/v3/homes/' + str(home['home_id']) + '/devices', 'get'],
        ['获取房源设备列表device_type参数错误:9', {'device_type': 9}, '400000', '/v3/homes/' + str(home['home_id']) + '/devices', 'get'],
        ['获取房源设备列表device_type类型错误', {'device_type': 'test'}, '400000', '/v3/homes/' + str(home['home_id']) + '/devices', 'get'],
        ['获取房源设备列表device_type范围错误', {'device_type': 0}, '400000', '/v3/homes/' + str(home['home_id']) + '/devices', 'get'],
        ['获取房源设备列表device_type最大值', {'device_type': 7}, '0', '/v3/homes/' + str(home['home_id']) + '/devices', 'get'],
        ['获取房源设备列表device_type范围错误', {'device_type': 8}, '400000', '/v3/homes/' + str(home['home_id']) + '/devices', 'get'],
    )
    @ddt.unpack
    def test_12(self, title, param, check_str, url, method, t=0):
        print_write('\n----', title, '---------------')
        res = get_response(url=url, do=method, param=param, headers=headers_fe, address=config.saas3_api, print_resp=1)
        assert check_res(res=res, check_str=check_str)
        print_write('----Pass---------------------\n')



if __name__ == "__main__":
    unittest.main()
