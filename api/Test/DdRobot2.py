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

    def notify_text(self, content):
        self.message = {'msgtype':'text',
                        'text':{'content':content},
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
            print('send message to dingding robot failed!,status_code is %s' %res.status_code)


if __name__ == '__main__':
    content = argv[1]
    user = argv[2]
    content = content + '------by: ' + user
    hook = r'https://oapi.dingtalk.com/robot/send?access_token=80b60e2c7f205a8a12c032fe65357071f7db0a02c00411537b57176bf709cda4' # 4.0精简群
    print(content)
    robot = Dd_Robot(hook)
    robot.notify_text(content)