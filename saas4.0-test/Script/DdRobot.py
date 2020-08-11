# -*- coding: utf-8 -*-
import requests
import json
import time
from sys import argv


class Dd_Robot(object):
    """4.0机器人"""

    def __init__(self, hook):
        super(Dd_Robot, self).__init__()
        self.hook = hook
        self.header = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
        }

    def notify_text(self, content, atMobiles, isAtAll=False):
        self.message = {'msgtype': 'text',
                        'text': {'content': content},
                        'at': {'atMobiles': [atMobiles],
                               'isAtAll': isAtAll
                               }
                        }
        if atMobiles != '18640573589':
            self.post_robot()

    def notify_link(self, content, title, messageUrl):
        self.message = {'msgtype': 'link',
                        'link': {'text': content,
                                 'title': title,
                                 'picUrl': '',
                                 'messageUrl': messageUrl}
                        }
        self.post_robot()

    def post_robot(self):
        print(self.hook)
        print(self.message)
        message = json.dumps(self.message).encode('utf-8')
        res = requests.post(self.hook, data=message, headers=self.header)
        if res.status_code == 200:
            print('send message to dingding robot success!')
        else:
            print('send message to dingding robot failed!,status_code is %s' %
                  res.status_code)


if __name__ == '__main__':
    job_name = argv[1]
    user_name = argv[2]
    job_url = argv[3]
    job_result = argv[4]
    build_time = argv[5]
    build_branch = argv[6]
    changes = argv[7].replace('JENKINS', '\n')
    if len(build_time) == 13 and build_time.isdecimal():
        build_time = time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(int(build_time) / 1000))
    hook = r'https://oapi.dingtalk.com/robot/send?access_token=dc7c20ebd64bb47c4d9e70577f2b7e443b53fca7b7aa4235dfb6a1a78186f022'  # Jenkins通知群
    user_mobiles = {
        'wangyongsheng': '18640573589',
        'zhengdai': '13121343660',
        'liuyue': '18376711496',
        'xingzhiyuan': '15220203835',
        'luwenhao': '15980816144',
        '刘一航': '13676085975',
        '胡涛': '18617153027',
        'huangsiyun': '18814382648',
        '王玉龙': '17688713579',
        'gaochugang': '15766389355',
        'wangweiwei': '13049343752',
        'yeweihan': '13610224699',
        'zhouchong': '13249856847',
        '周翀': '13249856847',
        'herui': '13128896272',
        '何锐': '13128896272',
        'qiuting': '18702696853',
        'yangxiong': '18575585029',
        'yehaochang': '13143458523',
        '叶浩昌': '13143458523',
        'liudongdong': '15339223629',
        'chenminqi': '17620351910',
        'leidongxing': '18811512897',
        'sunyakun': '13670035252',
        'zouweiqiang': '17870563823',
        '邹伟强': '17870563823',
        'zhangzhengxiang': '15001957936',
        'wenxinhua': '18820177954',
        'luojinming': '15900593609',
        '罗金明': '15900593609'
    }
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
    if job_result == 'pre_build':
        content = '重启  %s  ------  by %s' % (job_name, user_name)
        print(content)
        robot = Dd_Robot(hook)
        robot.notify_text(content, '')
    else:
        print(content)
        atMobiles = user_mobiles.get(user_name)
        robot = Dd_Robot(hook)
        robot.notify_text(content, atMobiles)
