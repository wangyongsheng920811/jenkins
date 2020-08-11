# -*- coding: utf-8 -*-
import requests
import json
import time
from sys import argv


class Dd_Robot(object):
    """docstring for Dd_Robot"""

    def __init__(self, hook):
        super(Dd_Robot, self).__init__()
        self.hook = hook
        self.header = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
        }

    def notify_text(self, content, atMobiles, isAtAll=False):
        self.message = {
            'msgtype': 'text',
            'text': {'content': content},
            'at': {'atMobiles': [atMobiles], 'isAtAll': isAtAll}}
        if atMobiles != '18640573589':
            self.post_robot()

    def post_robot(self):
        print(self.hook)
        print(self.message)
        message = json.dumps(self.message).encode('utf-8')
        res = requests.post(self.hook, data=message, headers=self.header)
        if res.status_code == 200:
            print('send message to dingding robot success!')
        else:
            print('send message to dingding robot failed!,status_code is %s' % res.status_code)


if __name__ == '__main__':
    job_name = argv[1]
    user_name = argv[2]
    job_url = argv[3]
    job_result = argv[4]
    build_time = argv[5]
    build_branch = argv[6]
    changes = argv[7].replace('JENKINS', '\n')
    if len(build_time) == 13 and build_time.isdecimal():
        build_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(build_time) / 1000))
    # hook = r'https://oapi.dingtalk.com/robot/send?access_token=f1ec1988f8f5ba09dce87923e8a3a558730c3881ee5fa01b5bb26f499d0ef983' saas测试部门群
    hook = r'https://oapi.dingtalk.com/robot/send?access_token=78334506e004db8ed3129324c0877326ca3c342b87b62f4bb34daa03aeec0fd1'  # SaaS测试内部群
    user_mobiles = {
        'wangyongsheng': '18640573589',
        'yaosheng': '15989486910',
        'liuyue': '18376711496',
        'xingzhiyuan': '15220203835',
        'zhanghongmei': '17620381365',
        'lifeichao': '18566260535',
        'WeiqiYao': '18620726218',
        '李暾': '18806642362',
        'CC': '13267153508',
        '张婉莹': '13924677550',
        '谢冰': '13750427073',
		'xuyanhui': '13603084097'
    }
    # content = '''
    # 工程名：%s
    # 代码分支: %s
    # 启动时间：%s
    # 运行结果：%s
    # 本次变更：
    # %s

    # 打开以下链接可查看本次构建的详细信息：
    # %s

    # 打开以下链接可查看本次构建的Eslint静态检查报告：
    # %s

    # 打开以下链接可查看本次构建的测试报告：
    # %s
    # ''' %(job_name, build_branch, build_time, job_result, changes, job_url, job_url+'Eslint_20Report', job_url+'Test_20Report')

    content = '''
    工程名：%s
    代码分支: %s
    启动时间：%s
    运行结果：%s
    本次变更：
    %s

    打开以下链接可查看本次构建的详细信息：
    %s

    ''' % (job_name, build_branch, build_time, job_result, changes, job_url)

    if job_name == 'test-pipeline':
        content = '''
    工程名：%s
    代码分支: %s
    启动时间：%s
    运行结果：%s
    本次变更：
    %s

    打开以下链接可查看本次构建的详细信息：
    %s

    打开以下链接可查看本次构建的SaaSAPI测试报告：
    %s

    打开以下链接可查看本次构建的OpenApi测试报告：
    %s
        ''' % (job_name, build_branch, build_time, job_result, changes, job_url, job_url + 'SaaSAPI_20Test_20Report', job_url + 'OpenAPI_20Test_20Report')
    if job_name == 'pre-saas-db-schema-migration-pipeline':
        content = '''
    工程名：%s
    代码分支: %s
    启动时间：%s
    运行结果：%s
    本次数据库变更：
    %s

    打开以下链接可查看本次构建的详细信息：
    %s

        ''' % (job_name, build_branch, build_time, job_result, changes, job_url)

    if job_name in 'pre-performance-test-pipeline':
        content = '''
    工程名：%s
    代码分支: %s
    启动时间：%s
    运行结果：%s
    本次变更：
    %s

    打开以下链接可查看本次构建的详细信息：
    %s
    打开以下链接可查看本次构建的SaaSAPI测试报告：
    %s
    打开以下链接可查看本次构建的OpenApi测试报告：
    %s
        ''' % (job_name, build_branch, build_time, job_result, changes, job_url, job_url + 'SaaSAPI_20PerformanceTest_20Report', job_url + 'OpenAPI_20PerformanceTest_20Report')

    if 'docker' in job_name and 'queue' not in job_name:
        port = argv[8]
        web_url = 'http://qa-ci.dding.net:' + port
        content = '''
    工程名：%s
    代码分支: %s
    启动时间：%s
    运行结果：%s
    本次变更：
    %s

    打开以下链接可查看本次构建的详细信息：
    %s
    前端访问地址为：
    %s
        ''' % (job_name, build_branch, build_time, job_result, changes, job_url, web_url)
    if 'docker-queue-service-pipeline' in job_name:
        content = '''
    工程名：%s
    代码分支: %s
    启动时间：%s
    运行结果：%s
    本次变更：
    %s

    打开以下链接可查看本次构建的详细信息：
    %s
        ''' % (job_name, build_branch, build_time, job_result, changes, job_url)
        print(job_name)
        print(build_branch)
        print(build_time)
        print(job_result)
        print(changes)
        print(job_url)
    print(content)
    atMobiles = user_mobiles.get(user_name)
    if user_name == 'saasdev':
        hook = 'https://oapi.dingtalk.com/robot/send?access_token=2c91c11f83860d23326b46564ccb9f4b6ba45171de23b82420dbaba6069ec109'
        atMobiles = '13544164082'
    robot = Dd_Robot(hook)
    robot.notify_text(content, atMobiles)
