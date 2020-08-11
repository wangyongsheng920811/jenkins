#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import requests
from locust import task
from locust import TaskSet
from locust import HttpLocust


class WebsiteTasks(TaskSet):

    def web_post(self, path, payload={}):
        params = {
            'userid': self.locust.user_id,
            'gcid': self.locust.gcid,
            'token': self.locust.token
        }
        params.update(payload)
        with self.client.post(self.locust.host + path, name=path, json=params, catch_response=True) as response:
            if response.status_code == 200 and response.json().get('status').get('code') == '200':
                response.success()
            else:
                response.failure(response.text)

    @task(1)
    def dingding_call_back(self):
        '''openapi回调'''
        path = '/v2/device/dingDing/dingDingCallback'

        installer_submit_payload = {"home_id": "5c383d2d7b3d8530984b2914", "room_id": "", "uuid": "", "detail": {"sp_state": 1, "origin_state": 11, "to_state": 3, "public_auth": True}, "time": 0, "center_uuid": None, "elecollector_uuid": None, "ticket_id": "RPMR1908051715173", "nickname": "", "manufactory": None, "event": "installerSubmit", "sign": "52b96e951a912b1f33748a91645ea871"}

        watermeter_amount_async_payload = {"event": "watermeterAmountAsync", "uuid": "4307b2223cb917ff7c52d51d348b03ad", "time": 1565061013011, "detail": {"amount": 16}, "center_uuid": "4708d915e47f56041ca9a1de93539334", "home_id": " 5bf25d7db028e37078dfb573", "room_id": "5bf25d7db028e37078dfb57c", "nickname": "", "manufactory": "ym", "meter_type": 1, "sign": "ecdd4caae962d68afa5bde1372677678"}

        elemeter_power_async_payload = {"event": "elemeterPowerAsync", "uuid": "e23a1f49e9f0f4a054b192e5c091b381", "time": 1565061072730, "detail": {"consume_amount": 1.35, "consume_amount_time": 1565060400000, "left_amount": -1.35}, "center_uuid": "96ccf8ecf571b5b1dcac3dc1d30fb834", "elecollector_uuid": "a5ab0f483981ba63f4e1459b85072df7", "home_id": "5cda8caae5d91a5ccb94184d", "room_id": "5cda8caa2e7d2919b072bde8", "nickname": "", "manufactory": None, "sign": "9e40f6aa3bee416277ad3efe75295314"}

        payloads = [installer_submit_payload, watermeter_amount_async_payload, elemeter_power_async_payload]
        payload = random.sample(payloads, 1)[0]
        with self.client.post(self.locust.host + path, name=path, json=payload, catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(response.text)

    @task(1)
    def dingding_call_back_result(self):
        '''openapi回调门锁密码'''
        path = '/v2/device/dingDing/dingDingCallBackresult'

        add_pwd_payload = {"service": "Password_Add_Service", "uuid": "4c96dd9c685ce67243f8dea46b58294d", "result": {"id": 1002, "passwordid": "1002", "ErrNo": 1000}, "serviceid": "565948071", "home_id": "5cb6d2dd6a2c0c66eca5d926", "room_id": "5cb6d2dec89fe603886f9799", "sign": "7cd67fb0ae11a93193abb00aa9d93acc"}

        update_pwd_payload = {"service": "Password_Update_Service", "uuid": "4c96dd9c685ce67243f8dea46b58294d", "result": {"id": 1002, "passwordid": "1002", "ErrNo": 1000}, "serviceid": "565951589", "home_id": "5cb6d2dd6a2c0c66eca5d926", "room_id": "5cb6d2dec89fe603886f9799", "sign": "1c6a7f27cd63e5e30cfdaeaecb936e09"}

        payloads = [add_pwd_payload, update_pwd_payload]
        payload = random.sample(payloads, 1)[0]
        self.web_post(path, payload)

    @task(1)
    def get_list_by_mark(self):
        '''获取字典列表'''
        path = '/v2/sys/zi_dian/get_list_by_mark'
        marks = ['6ae4d789-4d0b-476d-ab0b-7411614f269d', '31841886-28ec-45dc-aaec-67c40f7a73fe']
        payload = {
            'params': {
                'mark': random.sample(marks, 1)[0],
                'currentObj': {
                    '0': {'0': {}},
                    'context': {'0': {}},
                    'length': 1
                }
            }
        }
        self.web_post(path, payload)

    @task(1)
    def get_alipay_entrance_v2(self):
        '''安心住租客账单'''
        path = '/v2/alipay/aliPayMentController/alipay/entrance'
        paylist = {"timestamp": 1565008960860, "signature": "NWR6FTnrOsPT1ggLEzN4iC8kwguTqpwuijW4Xz0F/yUl6n9H9y4Z3ccDaUIub2lNNhIp0RBnLE7Arc8BF1R+fi/RnNewQlWmvC+QPEKfx50ohVwWrj/w5ct/a4fccdLH0y1WYD8mqy9iUwVfUC32yf9EhGat6vglAfrLnYnl8mGkNsIN/AFQPNqkTAt26F4QdvKhGgoGN5WIWMXW00rvWGhmpN1NrVWS4qIJA09XEHHXqBLCIlfiryr6LzmAbWtBxMRg++5y7VVg3ESDi1EQSOp9ft/5EZ4NnmlV7OZEUxmnJfjrXjN6itjLjiFQGzX1i0T7fozJcH6ZrXIQGyUWXQ==", "traceId": "6c04a67442184529a606225b2caf29df", "accessToken": "W9CXskaMuAQwld61O0vyRBRyiuRa-8UObOWoIcSQjcE=", "payload": [{"operationType": "1900000010005", "operationAttrValues": {"externalHouseId": "00e60c3c91de44d88c72238a34332f4c", "userInfo": {"antUserId": "392f5fb5269c48caabafe6aa3a72e291"}, "billStatus": 1, "bizId": "6A1CFFB3FB143E4911B96A07E2CC7F874931"}}]}
        pay = {"timestamp": 1564591519649, "signature": "NWR6FTnrOsPT1ggLEzN4iC8kwguTqpwuijW4Xz0F/yUl6n9H9y4Z3ccDaUIub2lNNhIp0RBnLE7Arc8BF1R+fi/RnNewQlWmvC+QPEKfx50ohVwWrj/w5ct/a4fccdLH0y1WYD8mqy9iUwVfUC32yf9EhGat6vglAfrLnYnl8mGkNsIN/AFQPNqkTAt26F4QdvKhGgoGN5WIWMXW00rvWGhmpN1NrVWS4qIJA09XEHHXqBLCIlfiryr6LzmAbWtBxMRg++5y7VVg3ESDi1EQSOp9ft/5EZ4NnmlV7OZEUxmnJfjrXjN6itjLjiFQGzX1i0T7fozJcH6ZrXIQGyUWXQ==", "traceId": "6c04a67442184529a606225b2caf29df", "accessToken": "W9CXskaMuAQwld61O0vyRBRyiuRa-8UObOWoIcSQjcE=", "payload": [{"operationType": "1900000010006", "operationAttrValues": {"billList": [{"billId": "18befe8c9c8840209694c08f0603fdb9", "feeIdList": ["0f7b6684b249441dab5b0ef5d43fa3b4"]}], "payAmount": "630.00", "antUserId": "392f5fb5269c48caabafe6aa3a72e291", "alipayUserId": "2088822973722066"}}]}
        payloads = [paylist, pay]
        payload = random.sample(payloads, 1)[0]
        with self.client.post(self.locust.host + path, name=path, json=payload, catch_response=True) as response:
            if response.status_code == 200 and response.json().get('statusCode') == 200:
                response.success()
            else:
                response.failure(response.text)

    @task(0)
    def get_department_list(self):
        '''获取部门列表'''
        path = '/v2/sys/department/get_list'
        self.web_post(path)

    @task(0)
    def get_chengzu_list(self):
        '''查看合同详情'''
        path = '/v2/compact/chengzu/get_by_id'
        payload = {
            'id': 'FC7D73E3RA30294E05R9A142E360EB7407E8',
            'isGetChengZuRen': 1
        }
        self.web_post(path, payload)

    @task(0)
    def get_part_house(self):
        '''查看合租房间详情'''
        path = '/v2/house/part_house/get_by_id'
        payload = {
            'id': '1a4a878664e94660961c4d5e8f4acf3f'
        }
        self.web_post(path, payload)

    @task(0)
    def get_compact_list(self):
        '''查看财务房屋账单'''
        path = '/v2/balance/table_balance_sheet/get_compact_list'
        payload = {
            'bigType': 2,
            'pageNo': '1',
            'pageSize': '10',
            'searchtype': '2',
        }
        self.web_post(path, payload)

    @task(0)
    def get_lock_info(self):
        '''查看门锁信息'''
        path = '/v2/lockmanage/lock_util/selislock'
        payload = {
            'params': {
                'house_id': '812f00c535e041e68e74b1911a6dd10a',
                'parent_house_id': '812f00c535e041e68e74b1911a6dd10a'
            }
        }
        self.web_post(path, payload)


class WebsiteUser(HttpLocust):
    host = 'http://yc-fin.dding.net'
    login_path = '/v2/jjr_user_login/pc_login_new'
    gcid = '2892537'
    login_payload = {
        'gcid': gcid,
        'params': {
            'accountName': 'admin',
            'accountPwd': '123123ss',
        }
    }
    res = requests.post(url=host + login_path, json=login_payload)
    token = res.json().get('result').get('token')
    user_id = res.json().get('result').get('id')
    header = {
        'userid': user_id,
        'gcid': gcid,
        'token': token
    }
    task_set = WebsiteTasks
