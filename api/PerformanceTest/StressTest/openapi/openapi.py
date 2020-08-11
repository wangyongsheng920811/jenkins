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
            if response.status_code == 200 and '"ErrNo":0' in response.text:
                response.success()
            elif response.url != None:
                response.failure(response.text)

    @task(200)
    def get_lock_info(self):
        param = {
            'home_id': '5a4519a50d40aa312c428972',
            'room_id': '5a4519a50d40aa312c428972',
            'uuid': '2fd016d7e40896ac9e278864fb50778d',
            'access_token': self.locust.token
        }
        self.web_get('v2/get_lock_info', param)

    @task(80)
    def get_elemeter_info(self):
        param = {
            "access_token": self.locust.token, 
            "home_id": "5a4519a50d40aa312c428972", 
            "room_id": "5a4519a50d40aa312c428972", 
            "uuid": "cb42c3eda70b7746fa13d279f9efffb7"
        }
        self.web_get('v2/get_elemeter_info', param)

    @task(80)
    def get_lock_events(self):
        param = {
            "access_token": self.locust.token, 
            "home_id": "5a4519a50d40aa312c428972",
            "room_id": "5a4519a50d40aa312c428972",
            "uuid": "2fd016d7e40896ac9e278864fb50778d",
            "start_time": 1543990082,
            "end_time": 1544076482,
            "count": 20,
            "offset": 0
        }
        self.web_get('v2/get_lock_events', param)

    @task(80)
    def elemeter_fetch_power_history(self):
        param = {
            "access_token": self.locust.token, 
            "home_id": "5a4519a50d40aa312c428972",
            "room_id": "5a4519a50d40aa312c428972",
            "uuid": "cb42c3eda70b7746fa13d279f9efffb7",
            "start_time": 1543486181,
            "end_time": 1543572581,
            "count": 20,
            "offset": 0,
        }
        self.web_get('v2/elemeter_fetch_power_history', param)

    @task(60)
    def get_center_info(self):
        param = {
            "access_token": self.locust.token, 
            "home_id": "5a4519a50d40aa312c428972",
            "uuid": "6f469ccc408fc9247830ed4308b4b5ad"
        }
        self.web_get('v2/get_center_info', param)

    @task(80)
    def fetch_passwords(self):
        param = {
            "access_token": self.locust.token, 
            "home_id": "5a4519a50d40aa312c428972",
            "room_id": "5a4519a50d40aa312c428972",
            "uuid": "2fd016d7e40896ac9e278864fb50778d"
        }
        self.web_get('v2/fetch_passwords', param)


class WebsiteUser(HttpLocust):
    host = 'https://pre-openapi-saas3.dding.net/'
    token_url = host + 'v2/access_token'
    header = {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json; charset=UTF-8',
            'Connection': 'keep-alive',
            'User-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3486.0 Safari/537.36"}
    payload = {
        'client_id': '48db710db57c3d8a00e56ca3',
        'client_secret': '67a427131625749c29e97797a8f43c5c'}
    res = requests.post(token_url, data=json.dumps(payload), headers=header)
    if res.status_code == 200 and 'access_token' in res.text:
        token = res.json()['access_token']

    task_set = WebsiteTasks
    # min_wait = 0
    # max_wait = 0
