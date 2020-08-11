#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : WangYongsheng
import requests


class Common(object):
    '''Hyperloop 测试公共方法'''
    host = None
    token = None

    @classmethod
    def init(cls, section):
        '''启动时初始化，根据conf.ini获取对应环境地址、用户名和密码并登录，获取token'''
        from configparser import ConfigParser
        if 'prod' in section:
            cls.section = 'prod'
        else:
            cls.section = 'qa'
        reader = ConfigParser()
        reader.read('conf/conf.ini')
        d = {key: value for key, value in reader.items(cls.section)}
        cls.host = d.get('host')
        payload = {
            'phone': d.get('user_name'),
            'password': d.get('password'),
            'from': '2'
        }
        res = requests.post(url=cls.host + d.get('login_path'), json=payload)
        try:
            cls.token = res.json().get('data').get('token')
        except Exception as e:
            print('无法获取token')
        # cls.token = '34c5faf74025e4a46d9f4183afdc0ac45aabc950c7b9748b45078afb2af4d36f597811e19e2f0e1289d149632bc029d5'

    @classmethod
    def request(cls, payload):
        '''请求方法，根据对应用例json数据里的method字段发起对应请求'''
        url = cls.host + payload.get('path')
        data = payload.get('params')
        headers = {'x-access-token': cls.token, 'from': '2'}
        print('\n')
        print('url:', url)
        print('method:', payload.get('method'))
        print('headers:', headers)
        print('data:', data)
        return getattr(requests, payload.get('method'))(url=url, params=data, json=data, headers=headers)

    @classmethod
    def check(cls, test_cls, datas):
        '''公用检测方法，检测请求结果响应码和响应数据是否和json一致
           检测用例json数据中是否有path、method、check_res_code和check_res_data字段'''
        test_cls.assertIn('path', datas)
        test_cls.assertIn('method', datas)
        test_cls.assertIn(datas.get('method'), ['get', 'post', 'put', 'delete'])
        test_cls.assertIn('check_res_code', datas)
        test_cls.assertIn('check_res_data', datas)
        res = cls.request(datas)
        check_res_code = datas.get('check_res_code')
        check_res_data = datas.get('check_res_data')
        try:
            print('response:', res.json())
        except Exception as e:
            print('response响应码:', res.status_code)
        print('check_res_code:', check_res_code)
        print('check_res_data:', check_res_data)
        print('\n')
        test_cls.assertEqual(res.json().get('code'), check_res_code, msg=res.json())
        if check_res_data:
            if check_res_data.startswith('res.json()'):
                test_cls.assertTrue(eval(check_res_data), msg=check_res_data)
            else:
                print('check_res_data格式错误')
        return res

    @staticmethod
    def random_list(l):
        '''返回列表中随机个元素'''
        import random
        return random.sample(l, random.randint(1, len(l)))

    @staticmethod
    def format_time():
        '''返回当前时间字符串，如20190723161620'''
        import time
        return str(time.strftime("%Y%m%d%H%M%S", time.localtime()))

    @staticmethod
    def dd_robot(success_count, failure_count, error_count):
        hook = r'https://oapi.dingtalk.com/robot/send?access_token=dc7c20ebd64bb47c4d9e70577f2b7e443b53fca7b7aa4235dfb6a1a78186f022'
        report_url = 'http://qa-ci.dding.net:8081/jenkins/view/5.0/job/hyperloop-auto-test-pipeline/Hyperloop_20Test_20Report'
        content = '''
            接口自动化:  成功: {},  失败: {},  错误: {}
            点击查看详情
            {}
            '''.format(success_count, failure_count, error_count, report_url)
        atMobiles = '18640573589'
        message = {
            'msgtype': 'text',
            'text': {'content': content},
            'at': {'atMobiles': [atMobiles], 'isAtAll': False}
        }
        requests.post(url=hook, json=message)
