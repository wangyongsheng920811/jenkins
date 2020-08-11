#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
from locust import task
from locust import TaskSet
from locust import HttpLocust


class WebsiteTasks(TaskSet):

    def web_get(self, url, param={}):
        with self.client.get(url, name=url, params=param, headers=self.locust.header, catch_response=True) as response:
            if response.status_code == 200 and '"err_code":0' in response.text:
                response.success()
            elif response.url != None:
                response.failure(response.text)

    @task(1)
    def get_tickets_info(self):
        param = {
            'offset': 0,
            'limit': 10,
            'state': 0,
            'device_type': 0
        }
        
        self.web_get('v3/tickets/1', param)

    @task(1)
    def get_homes_info(self):
        param = {
            'offset': 0,
            'limit': 20
        }
        
        self.web_get('v3/homes', param)

    @task(1)
    def get_locks_info(self):
        self.web_get('v3/rooms/1482758146/locks/1822635935')

    @task(1)
    def get_reports(self):
        url = 'v3/reports/elemeter_readed_amount/action_export'
        with self.client.get(url, headers=self.locust.header, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(response.status_code)


class WebsiteUser(HttpLocust):
    host = 'https://pre-api.dding.net/'

    login_header = {'Origin': 'http://local.dding.cn', 'Content-Type': 'application/json;charset=UTF-8'}
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
               'Accept': 'application/json, text/plain, */*',
               'Content-Type': 'application/json; charset=UTF-8',
               'Connection': 'keep-alive',
               }
    login_url = 'https://passport.dding.net/login'
    login_param = {"name": "15989486910", "pass": "qwert12345", "from": 2}

    response = requests.post(url=login_url, data=json.dumps(login_param), headers=login_header)
    if response.status_code == 200 and 'access_token' in response.headers.get('set-cookie'):
        header.update({'Cookie': response.headers.get('set-cookie')})
    else:
        print(response.status_code)
        print(response.headers)
        print(response.text)

    task_set = WebsiteTasks
    # min_wait = 0
    # max_wait = 0