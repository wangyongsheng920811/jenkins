#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import json
import pika


class Event(object):
    """ 事件消息：来自设备的上行事件消息（门锁电量、门锁打开事件、门锁低电异常、门锁离线等）"""
    lock_uuid = 'f9183e99a1ffa53b955ffb9e9880f5ec'
    center_uuid = 'e9f94c4b9902ae350b554e890718ad55'
    elemeter_uuid = '3320e79de87067ce88e40724e5728ead'

    # 门锁低电报警
    batteryAlarm = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "batteryAlarm",
        "detail": {"battery_level": 9}
    }

    # 门锁电量恢复
    clearBatteryAlarm = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "clearBatteryAlarm",
        "detail": {"battery_level": 19}
    }

    # 门锁防撬报警
    brokenAlarm = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "brokenAlarm"
    }

    # 门锁电池电量同步
    batteryAsync = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "batteryAsync",
        "detail": {"battery": 99}
    }

    # 门锁指纹被撬报警
    fpBrokenAlarm = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "fpBrokenAlarm"
    }

    # 门锁密码连续错误次数大于5次
    wrongPwdAlarm = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "wrongPwdAlarm"
    }

    # 门锁指纹连续错误大于15次
    wrongFpAlarm = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "wrongFpAlarm"
    }

    # 硬件故障（RTC）
    hwRTCAlarm = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "hwRTCAlarm"
    }

    # 硬件故障（LED）
    hwLEDAlarm = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "hwLEDAlarm"
    }

    # 硬件故障（Fp）
    hwFpAlarm = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "hwFpAlarm"
    }

    # 硬件故障（Touch）
    hwTouchAlarm = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "hwTouchAlarm"
    }

    # 设备时间有误
    rtcError = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "rtcError"
    }

    #    password : {password：混淆后的密码值, id:密码id}
    pwdAddLocal = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "pwdAddLocal",
        "detail": {"password": {"password": "AAAAAA", "id": 2}}
    }

    # 门锁本地清空蓝牙钥匙事件
    bleReset = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "bleReset"
    }

    # 门锁本地删除密码事件 password：{id ： //密码id}
    pwdDelLocal = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "pwdDelLocal",
        "detail": {"password": {"id": 2}}
    }

    # 门锁本地修改密码值事件 password : {password：混淆后的密码值, id:密码id}
    pwdUpdateLocal = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "pwdUpdateLocal",
        "detail": {"password": {"password": "AAAAAA", "id": 2}}
    }

    """
    门锁开锁事件
    {"source_name", //密码名字
    "eventid"://开门事件类型,
    "source"://开门源类型,
    "sourceid"://密码id,
    "audio_played": //是否播放了语音留言}
    或
    {"eventid": 21,
    "stream": [] }
    """
    lockerOpenAlarm = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "lockerOpenAlarm",
        "detail": {"source_name": "卫斯理", "eventid": 1, "source": 2, "sourceid": 1006, "notify": 1, "audio_played": 0}
    }
    # 或者
    # lockerOpenAlarm = {
    #     "uuid": "e20ca5453c280a472b2b783a4d6db7e6",
    #     "time": int(time.time()*1000),
    #     "event": "lockerOpenAlarm",
    #     "detail": {"eventid": 21, "stream": [2, 2, 2]}
    # }

    # 门锁开门历史同步消息
    lockOpenHistoryAlarm = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "lockOpenHistoryAlarm",
        "detail": {
            "events": [{
                "userid": "100001",
                "uuid": "acebb0aec8ae19c4e745959b39794325",
                "time": 1518060588000,
                "lock_time": 1518060588000,
                "eventid": 1,
                "source": 2,
                "sourceid": 1002,
                "source_name": "H70370.侯倩",
                "audio_played": 0}]}
    }

    # 网关离线 subdevices：网关下子设备列表
    centerOfflineAlarm = {
        "uuid": center_uuid,
        "time": int(time.time() * 1000),
        "event": "centerOfflineAlarm",
        "detail": {"subdevices": [lock_uuid]}
    }

    # 网关子设备离线 subdevices：如果设备类型为采集器，则会有subdevices，表示采集器下的电表列表；如果是其他设备类型，则没有该字段
    # 如果无采集器，则uuid为子设备uuid同时没有detail字段或detail字段为空字典，如果有采集器则uuid为采集器的uuid，同时subdevices对应采集器子设备列表
    lockOfflineAlarm = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "lockOfflineAlarm",
        # "detail": {"subdevices": [lock_uuid]}
    }

    # 网关恢复在线
    clearCenterOfflineAlarm = {
        "uuid": center_uuid,
        "time": int(time.time() * 1000),
        "event": "clearCenterOfflineAlarm",
    }

    # 网关子设备恢复在线 subdevices：如果设备类型为采集器，则会有subdevices，表示采集器下的电表列表；如果是其他设备类型，则没有该字段
    clearLockOfflineAlarm = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "clearLockOfflineAlarm",
        # "detail": {"subdevices": [lock_uuid]}
        # "detail": {lock_uuid}
    }

    # 门锁被重置事件
    lockerReset = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "lockerReset",
        "detail": {"parent": "0e5ef1d27de3312ee638731928b9e5ec"}
    }

    # 电表上传用电量
    elemeterPowerAsync = {
        "uuid": elemeter_uuid,
        "time": int(time.time() * 1000),
        "event": "elemeterPowerAsync",
        "detail": {
            "consume_amount": 2.34,
            "consume_amount_time": 1518058800000,
            "group_amounts": [{"devid": "180111050071", "amount": 3.53},
                              {"devid": "180111060302", "amount": 47.52},
                              {"devid": "180111050063", "amount": 2.34}]}
    }

    # 电表上传用电历史
    elemeterPowerHisAsync = {
        "uuid": elemeter_uuid,
        "time": int(time.time() * 1000),
        "event": "elemeterPowerHisAsync",
        "detail": {"powers": [{"sn": "171105024756", "time": 1518062400000, "amount": 6.16}]}
    }

    # 电表事件消息（485通讯错误等）
    """
    histories表示电表的事件历史,eventid取值：
    1 超功率，回调当前capacity，类似于elemeterOvercomeCapacity事件
    2 超电量，回调当前amount，类似于事件elemeterOvercomeAmount
    3 本地合闸，类似于事件elemeterLocalClose
    4 已废弃
    5 电表远程主动跳闸，类似于事件elemeterRemoteOpen
    6 电表远程主动合闸，类似于事件elemeterRemoteClose
    7 超电流，回调当前current，类似于事件elemeterOvercomeCurrent
    8 电表离线，类似于事件elemeterTransError
    9 电表恢复在线，类似于事件 elemeterTransNormal
    10 电表超电量报警），回调当前amount，类似于事件elemeterOvercomeAmountWarn
    """
    elemeterHistory = {
        "uuid": elemeter_uuid,
        "time": int(time.time() * 1000),
        "event": "elemeterHistory",
        "histories": [{"uuid": "2aa7d8e65e7db0e1e53adc60858b0e6f",
                       "time": 1518048000000,
                       "eventid": 2,
                       "devid": "161109003000",
                       "amount": 690.45,
                       "_id": "5a7bc02ca23f917cbe53e3ec"}]
    }

    # 超电量异常（超电量且电表发生了跳闸）amount 电表实际用电量
    elemeterOvercomeAmount = {
        "uuid": elemeter_uuid,
        "time": int(time.time() * 1000),
        "event": "elemeterOvercomeAmount",
        "detail": {"amount": 800.14}
    }

    # 超功率异常（超功率且发生了跳闸） capacity 功率值
    elemeterOvercomeCapacity = {
        "uuid": elemeter_uuid,
        "time": int(time.time() * 1000),
        "event": "elemeterOvercomeCapacity",
        "detail": {"capacity": 5.0158}
    }

    # 电表超电量告警（超电量但未跳闸）amount 电表实际用电量
    elemeterOvercomeAmountWarn = {
        "uuid": elemeter_uuid,
        "time": int(time.time() * 1000),
        "event": "elemeterOvercomeAmountWarn",
        "detail": {"amount": 91.3}
    }

    # 电表本地获取当前度数出现异常
    elemeterWrongAmountWarn = {
        "uuid": elemeter_uuid,
        "time": int(time.time() * 1000),
        "event": "elemeterWrongAmountWarn",
        "detail": {"amount": 362.72}
    }

    # 超电流异常（超电流且发生了跳闸）current 电流值
    elemeterOvercomeCurrent = {
        "uuid": elemeter_uuid,
        "time": int(time.time() * 1000),
        "event": "elemeterOvercomeCurrent",
        "detail": {"current": 17.812}
    }

    # 门锁本地清空所有租客授权码
    clearRenterAuthenCode = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "clearRenterAuthenCode"
    }

    # 门锁本地清空所有租客及管理员授权码
    clearAllCommonAuthenCode = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "clearAllCommonAuthenCode"
    }

    # 电表本地合闸
    elemeterLocalClose = {
        "uuid": elemeter_uuid,
        "time": int(time.time() * 1000),
        "event": "elemeterLocalClose",
        "detail": {}
    }

    # 电表485通讯异常
    elemeterTransError = {
        "uuid": elemeter_uuid,
        "time": int(time.time() * 1000),
        "event": "elemeterTransError",
        "detail": {}
    }

    # 电表485通讯恢复正常
    elemeterTransNormal = {
        "uuid": elemeter_uuid,
        "time": int(time.time() * 1000),
        "event": "elemeterTransNormal",
        "detail": {}
    }

    # 电表跳闸
    elemeterRemoteOpen = {
        "uuid": elemeter_uuid,
        "time": int(time.time() * 1000),
        "event": "elemeterRemoteOpen",
        "detail": {}
    }

    # 电表合闸
    elemeterRemoteClose = {
        "uuid": elemeter_uuid,
        "time": int(time.time() * 1000),
        "event": "elemeterRemoteClose",
        "detail": {}
    }

    # 电表充值耗时过长 serial_no 充值流水号列表
    elemeterSynFailed = {
        "uuid": elemeter_uuid,
        "time": int(time.time() * 1000),
        "event": "elemeterSynFailed",
        "detail": {"serial_no": ["18020811530612577"]}
    }

    # 电表充值成功 serial_no 充值流水号列表, data为充值成功时写入到电表的数据
    elemeterSynSucceed = {
        "uuid": elemeter_uuid,
        "time": int(time.time() * 1000),
        "event": "elemeterSynSucceed",
        "detail": {"serial_no": ["18020812062166336"],
                   "data": {"control_switch": "1",
                            "overdraft": "10",
                            "power_total": "104.92",
                            "amount": "114.92"}}
    }

    # 门磁状态事件 state //open 表示门磁打开close门磁关闭
    doorSensorOpen = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "doorSensorOpen",
        "detail": {"state": "open"}
    }

    # 语音留言下载成功 file_id 语音文件id, is_success 下载是否成功
    voiceDownloadFinish = {
        "uuid": lock_uuid,
        "time": int(time.time() * 1000),
        "event": "voiceDownloadFinish",
        "detail": {"is_success": 1, "file_id": "a9fc891e517df275e90f7d023e77f202"}
    }


class Service(object):
    lock_uuid = '8d1166e0ee4b26c9a0afbcec88ac155b'
    center_uuid = 'e9f94c4b9902ae350b554e890718ad55'
    elemeter_uuid = '3320e79de87067ce88e40724e5728ead'
    lock_sn = 'lkjl0012180300726739'
    """ 服务消息：设备对业务层调用的执行结果（添加密码结果消息、修改密码结果消息、电表充值结果等） """
    # 删除指纹
    Fingerprint_Delete_Service = {
        "uuid": "1f97a01fcbb7a4250b8a3deb95005466",
        "service": "Fingerprint_Delete_Service",
        "serviceid": 69587,
        "result": {"ErrNo": 1000},
        "userData": "{\"id\":0,\"userid\":\"13372721120\",\"nickname\":\"Loock Touch\",\"uuid\":\"1f97a01fcbb7a4250b8a3deb95005466\",\"master\":\"13372721120\"}"
    }

    # 添加子设备
    AddSubdevice_Service = {
        "uuid": center_uuid,
        "service": "AddSubdevice_Service",
        "serviceid": "53291549",
        "username": "102243",
        "result": {
            "devid": lock_sn,
            "uuid": lock_uuid,
            "ErrNo": 1000}
    }

    # 蓝牙钥匙修改
    BLE_Add_Service = {
        "uuid": "4469985154876443db3da0b98290882a",
        "service": "BLE_Add_Service",
        "serviceid": 69334,
        "username": "18721111400",
        "result": {"ErrNo": 1000}
    }

    # 删除蓝牙钥匙
    BLE_Delete_Service = {
        "uuid": "0112f6467349bce95a0f73a2cd0071f6",
        "service": "BLE_Delete_Service",
        "serviceid": 69332,
        "username": "15700164546",
        "result": {"ErrNo": 5101}
    }

    # 绑定
    Bind_Service = {
        "uuid": lock_uuid,
        "service": "Bind_Service",
        "serviceid": 53291891,
        "username": "101439",
        "result": {"ErrNo": 1000}
    }

    # 门锁、采集器更新种子
    PwdSeed_Service = {
        "uuid": "e3961666a105990948f322f58294bac4",
        "service": "PwdSeed_Service",
        "serviceid": "53221482",
        "username": "user",
        "result": {"ErrNo": 5101}
    }

    # 添加密码 {"id":1015,"passwordid":"密码id","ErrNo":1000}
    Password_Add_Service = {
        "uuid": "8d1166e0ee4b26c9a0afbcec88ac155b",
        "service": "Password_Add_Service",
        "serviceid": 53292148,
        "username": "900001",
        "result": {"id": 1015, "passwordid": "1015", "ErrNo": 1000}
    }

    # 删除密码
    Password_Delete_Service = {
        "uuid": "fbb87008d0f1fb9071a6f1207e7ee96c",
        "service": "Password_Delete_Service",
        "serviceid": 53292147,
        "username": "900001",
        "result": {"id": 1001, "passwordid": "1001", "ErrNo": 1000}
    }

    # 修改密码
    Password_Update_Service = {
        "uuid": "3555c7c9324644aa3e4131de0dfe58c9",
        "service": "Password_Update_Service",
        "serviceid": 53292379,
        "username": "900001",
        "result": {"id": 1031, "passwordid": "1031", "ErrNo": 1000}
    }

    # 冻结密码
    Password_Frozen_Service = {
        "uuid": "33cc6cab393f08ce6cbecd504c18e9b6",
        "service": "Password_Frozen_Service",
        "serviceid": 53292382,
        "username": "102232",
        "result": {"id": 1005, "passwordid": "1005", "ErrNo": 1000}
    }

    # 解冻密码
    Password_Unfrozen_Service = {
        "uuid": "abb9ef021015768dad406c04ce6aef64",
        "service": "Password_Unfrozen_Service",
        "serviceid": 53291110,
        "username": "100492",
        "result": {"id": 1001, "passwordid": "1001", "ErrNo": 1000}
    }

    # 采集器电表透传消息 {"ErrNo":操作结果,"consume_amount":用电量}
    Elemeter_Passthrough_Service = {
        "uuid": "dda7f39a0ad4ef274167e183027e55a9",
        "service": "Elemeter_Passthrough_Service",
        "serviceid": 53292320,
        "username": "100027",
        "result": {"ErrNo": 1000, "consume_amount": 657.09},
        "userData": "{\"home_id\": \"59c358aaf31fbe2ed70eae0d\", \"room_id\": \"59c364adc4ac521f1cbbe3cf\", \"operation_type\": 5}"
    }

    # 采集器电表非透传消息
    Elemeter_Control_Service = {
        "uuid": "56fe8435213a0b577fa15a95c29164c5",
        "service": "Elemeter_Control_Service",
        "serviceid": 53292435,
        "username": "100027",
        "result": {"ErrNo": 1000},
        "userData": "{\"home_id\": \"15083961511415310\", \"room_id\": \"fj15083661511415951\", \"operation_type\": 6}"
    }

    # 采集器电表数据同步 {"ErrNo":1000,"control_switch":跳合闸,"current":额定电流,"capacity":额定功率,"amount":充值度数}
    Elemeter_Syn_Service = {
        "uuid": "681251df853e27c35becd9971fcc29f3",
        "service": "Elemeter_Syn_Service",
        "serviceid": 53292666,
        "result": {"ErrNo": 1000, "control_switch": "1", "current": "38", "capacity": "8.36", "amount": "0"},
        "userData": "{\"uuid\": \"681251df853e27c35becd9971fcc29f3\", \"sn\": \"170808020133\", \"control_switch\": 1, \"overdraft\": 0, \"power_total\": 0, \"current\": 38, \"capacity\": 8.36, \"amount\": 0}"
    }

    # zigbee电表充值
    Zmeter_Charge_Service = {
        "uuid": "50040f014cbba9ed2d60a2ca5c47286c",
        "service": "Zmeter_Charge_Service",
        "serviceid": 53286679,
        "username": "100184",
        "result": {"ErrNo": 1000},
        "userData": "{\"home_id\": \"59b0def50bd13153a34a0a71\", \"room_id\": \"59b0e03e0bd13153a34a0b3c\", \"amount\": 50, \"total_amount\": 368.63, \"operation_type\": 1, \"serial_no\": \"18020814111636750\", \"switch_state\": 1}"
    }

    # zigbee电表清零
    Zmeter_Reset_Service = {
        "uuid": "93c7fdb8409eeafda13f8d4b43dcacf1",
        "service": "Zmeter_Reset_Service",
        "serviceid": 53280821,
        "username": "100082",
        "result": {"ErrNo": 1000},
        "userData": "{\"home_id\": \"5a7945b592123d4671c50571\", \"room_id\": \"5a7945b692123d4671c50578\", \"operation_type\": 3}"
    }

    # zigbee电表修改功率
    Zmeter_Capacity_Service = {
        "uuid": "3c87a4bb297b9084d2d745631e184acb",
        "service": "Zmeter_Capacity_Service",
        "serviceid": 53279478,
        "username": "100082",
        "result": {"ErrNo": 1000},
        "userData": "{\"home_id\": \"5a7945b592123d4671c50571\", \"room_id\": \"5a7945b692123d4671c50576\", \"capacity\": \"14.52\", \"operation_type\": 4}"
    }

    # zigbee电表跳闸
    Zmeter_Open_Service = {
        "uuid": "f080858d530f723b4393ff92c52ffb7f",
        "service": "Zmeter_Open_Service",
        "serviceid": 53293188,
        "username": "101289",
        "result": {"ErrNo": 1000},
        "userData": "{\"home_id\": \"5a0667fa64e8a07affd39ac2\", \"room_id\": \"5a0667fa74c33d0400ae5ccb\", \"operation_type\": 6}"
    }

    # zigbee电表合闸
    Zmeter_Close_Service = {
        "uuid": "f714c1b79e1a7d2beb0e40721e0b859d",
        "service": "Zmeter_Close_Service",
        "serviceid": 53283964,
        "username": "101561",
        "result": {"ErrNo": 1000},
        "userData": "{\"home_id\": \"5a58852db224871d87aa99cb\", \"room_id\": \"5a58852db224871d87aa99cc\", \"operation_type\": 7}"
    }

    # zigbee电表修改最大电流
    Zmeter_Current_Service = {
        "uuid": "a5897fd9aa2f9756101cdf0dd87400cd",
        "service": "Zmeter_Current_Service",
        "serviceid": 53256596,
        "username": "102198",
        "result": {"ErrNo": 1000},
        "userData": "{\"home_id\": \"5a77c8fce59d5a04629c989d\", \"room_id\": \"5a77c8fce59d5a04629c98a1\", \"current\": 66, \"operation_type\": 9}"
    }

    # zigbee电表抄表 {"ErrNo":操作结果,"consume_amount":用电量}
    Zmeter_Read_Service = {
        "uuid": "c7b178ebb24b172cc147f68862d08bfa",
        "service": "Zmeter_Read_Service",
        "serviceid": 53289427,
        "username": "100027",
        "result": {"ErrNo": 1000, "consume_amount": 369.4},
        "userData": "{\"home_id\": \"5a3b55bd0e0fbd1e694d1d1f\", \"room_id\": \"5a3ba2d22bdf8669e9153b83\", \"operation_type\": 5}"
    }

    # zigbee电表数据同步 "ErrNo":1000,"amount":充值度数,"current":额定电流,"room_id":房间号,"capacity":额定功率,"control_switch":开合闸
    Zmeter_Syn_Service = {
        "uuid": "4ff032c7c09d3fa25a45945bffa7555a",
        "service": "Zmeter_Syn_Service",
        "serviceid": 53290180,
        "username": "account",
        "result": {"ErrNo": 1000,
                    "amount": 0,
                    "current": 17,
                    "room_id": None,
                    "capacity": 3,
                    "control_switch": 1}
    }


class Rabbitmq(object):
    def __init__(self, config):
        print('connection ... ')
        self.exchange = config.get('exchange')
        self.routing_key = config.get('routing_key')
        credentials = pika.PlainCredentials(
            config.get('user'), config.get('pass'))
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(config.get('host'), config.get('port'), config.get(
            'vhost'), credentials, heartbeat=config.get('heartbeat'), socket_timeout=config.get('timeout'), client_properties={'connection_name': 'default', }))
        self.channel = self.connection.channel()

    def __del__(self):
        print('close ... ')
        self.connection.close()

    def basic_publish(self, message):
        print('send message to rabbitmq, event:%s ' % message.get('event'))
        properties = pika.BasicProperties(
            # app_id='online.message.parser',
            # type='event_space',
            # message_id='',
            # reply_to='',
            # correlation_id='',
            # headers='',
            content_type='application/json',
            content_encoding='utf8',
            delivery_mode=2)
        self.channel.basic_publish(exchange=self.exchange,
                                   routing_key=self.routing_key,
                                   body=json.dumps(
                                       message, ensure_ascii=False),
                                   properties=properties)


class Config(object):
    # 测试环境队列服务器配置
    dev_config = {
        'user': 'dingding',
        'pass': '12345Yunding',
        'host': 'dev-factory.dding.net',
        'port': 5672,
        'timeout': 20 * 1000,
        'vhost': '/',
        'heartbeat': 10,
        'retryLimit': 10,
        'replyQueue': False,
        'exchange': 'event_queue_space',
        'routing_key': 'event_space',
    }

    # 预发布环境服务器配置，运行时需要和此服务器在同一网段
    pre_config = {
        'user': 'yunding',
        'pass': 'jkjkfsdfs',
        'host': '192.168.1.217',
        'port': 5672,
        'timeout': 20 * 1000,
        'vhost': '/yunding',
        'heartbeat': 10,
        'retryLimit': 10,
        'replyQueue': False,
        'exchange': 'event_exchange',
        'routing_key': 'event_3',
    }


if __name__ == '__main__':
    rabbit = Rabbitmq(Config.dev_config)
    # lock_uuid = sys.argv[1]
    # center_uuid = sys.argv[2]
    # elemeter_uuid = sys.argv[3]
    # event_name = sys.argv[4]
    # e = Event()

    # e.lock_uuid = lock_uuid
    # # print(Event.lock_uuid)
    # e.center_uuid = center_uuid
    # e.elemeter_uuid = elemeter_uuid
    # print(getattr(e, 'lock_uuid'))
    # print(e.batteryAlarm)
    # rabbit.basic_publish(getattr(Event, event_name))
    # rabbit.basic_publish(Event.batteryAlarm)  # 低电提醒
    # rabbit.basic_publish(Event.clearBatteryAlarm) #取消低电提醒
    # rabbit.basic_publish(Event.brokenAlarm) #防撬报警
    # rabbit.basic_publish(Event.batteryAsync) #电池电量同步

    # rabbit.basic_publish(Event.fpBrokenAlarm) #指纹被撬报警
    # rabbit.basic_publish(Event.wrongPwdAlarm) #密码连续错误次数大于5次
    # rabbit.basic_publish(Event.wrongFpAlarm) #指纹连续错误大于15次

    # rabbit.basic_publish(Event.hwRTCAlarm) #硬件故障（RTC）
    # rabbit.basic_publish(Event.hwLEDAlarm) #硬件故障（LED）
    # rabbit.basic_publish(Event.hwFpAlarm) #硬件故障（Fp）
    # rabbit.basic_publish(Event.hwTouchAlarm) #硬件故障（Touch）

    # rabbit.basic_publish(Event.rtcError) #设备时间有误
    # rabbit.basic_publish(Event.pwdAddLocal) #门锁本地添加密码事件
    # rabbit.basic_publish(Event.bleReset) #门锁本地清空蓝牙钥匙事件
    # rabbit.basic_publish(Event.pwdDelLocal) #门锁本地删除密码事件
    # rabbit.basic_publish(Event.pwdUpdateLocal) #门锁本地修改密码值事件
    # rabbit.basic_publish(Event.lockerOpenAlarm) #门锁开锁事件
    # rabbit.basic_publish(Event.lockOpenHistoryAlarm) #门锁开门历史同步消息

    # rabbit.basic_publish(Event.centerOfflineAlarm) #网关离线
    # rabbit.basic_publish(Event.lockOfflineAlarm) #网关子设备离线
    # rabbit.basic_publish(Event.clearCenterOfflineAlarm) #网关恢复在线
    # rabbit.basic_publish(Event.clearLockOfflineAlarm) #网关子设备恢复在线

    # rabbit.basic_publish(Event.elemeterPowerAsync) #电表上传用电量
    # rabbit.basic_publish(Event.elemeterPowerHisAsync) #电表上传用电历史
    # rabbit.basic_publish(Event.elemeterHistory) #电表事件消息（485通讯错误等）
    # rabbit.basic_publish(Event.elemeterOvercomeAmount) #超电量异常（超电量且电表发生了跳闸）
    # rabbit.basic_publish(Event.elemeterOvercomeCapacity) #超过率异常（超功率且发生了跳闸）
    # rabbit.basic_publish(Event.elemeterOvercomeAmountWarn) #电表超电量告警（超电量但未跳闸）
    # rabbit.basic_publish(Event.elemeterWrongAmountWarn) #电表本地获取当前度数出现异常
    # rabbit.basic_publish(Event.elemeterOvercomeCurrent) #超电量异常（超电流且发生了跳闸）

    # rabbit.basic_publish(Event.clearRenterAuthenCode) #门锁本地清空所有租客授权码
    # rabbit.basic_publish(Event.clearAllCommonAuthenCode) #门锁本地清空所有租客及管理员授权码

    # rabbit.basic_publish(Event.elemeterLocalClose) #电表本地合闸
    # rabbit.basic_publish(Event.elemeterTransError) #电表485通讯异常
    # rabbit.basic_publish(Event.elemeterTransNormal) #电表485通讯恢复正常
    # rabbit.basic_publish(Event.elemeterRemoteOpen) #电表跳闸
    # rabbit.basic_publish(Event.elemeterRemoteClose) #电表合闸
    # rabbit.basic_publish(Event.elemeterSynFailed) #电表充值耗时过长
    # rabbit.basic_publish(Event.elemeterSynSucceed) #电表充值成功
    # rabbit.basic_publish(Event.doorSensorOpen) #门磁状态事件
    # rabbit.basic_publish(Event.voiceDownloadFinish) #语音留言下载成功
    # rabbit.basic_publish(Service.Bind_Service) #语音留言下载成功
