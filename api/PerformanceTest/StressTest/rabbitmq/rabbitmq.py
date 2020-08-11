#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import json
import pika
from locust import task
from locust import events
from locust import Locust
from locust import TaskSet
from locust import HttpLocust

class AmqpClient(object):
    """rewrite self.client for rabbitmq"""
    def connection(self, config):
        credentials = pika.PlainCredentials(config.get('user'), config.get('pass'))
        connection = pika.BlockingConnection(pika.ConnectionParameters(config.get('host'),config.get('port'),config.get('vhost'),credentials, heartbeat=config.get('heartbeat'), socket_timeout=config.get('timeout'), client_properties={'connection_name': 'default',}))
        AmqpClient.channel = connection.channel()

    def queue_declare(self, queue, durable):
        self.channel.queue_declare(queue=queue, durable=durable)

    def basic_publish(self, exchange, routing_key, body):
        try:
            start_time = int(time.time())
            res = self.channel.basic_publish(exchange=exchange, routing_key=routing_key, body=json.dumps(body), properties=pika.BasicProperties(content_type='application/json', content_encoding='utf8'))
            total_time = int((time.time() - start_time) * 1000)
            if res != True:
                raise Exception
            events.request_success.fire(request_type='amqp', name='/amqp', response_time=total_time, response_length=0)
        except Exception as e:
            total_time = int((time.time() - start_time) * 1000)
            events.request_failure.fire(request_type='amqp', name='/amqp', response_time=total_time, exception=e)


class AmqpLocust(Locust):
    def __init__(self, *args, **kwargs):
        super(AmqpLocust, self).__init__(*args, **kwargs)
        self.client = AmqpClient()


class WebsiteTasks(TaskSet):
    def setup(self):
        # 测试环境
        # config = {
        # 'user': 'dingding',
        # 'pass': '12345Yunding',
        # 'host': 'dev-factory.dding.net',
        # 'port': 5672,
        # 'timeout': 20 * 1000,
        # 'vhost': '/',
        # 'heartbeat': 10,
        # 'retryLimit': 10,
        # 'replyQueue': False
        # }
        # self.client.connection(config)
        # self.client.queue_declare('test', True)

        # 预发布环境
        config = {
        'user': 'yunding',
        'pass': 'jkjkfsdfs',
        'host': '192.168.1.217',
        'port': 5672,
        'timeout': 20 * 1000,
        'vhost': '/yunding',
        'heartbeat': 10,
        'retryLimit': 10,
        'replyQueue': False
        }
        self.client.connection(config)
        self.client.queue_declare('event_queue_3', True)

    @task(1)
    def event_queue(self):
        # body = {"uuid":"2fd016d7e40896ac9e278864fb50778d","time":1545186667296,"event":"lockerOpenAlarm","detail":{"source_name":"动态密码","eventid":1,"source":2,"sourceid":2015,"notify":1,"audio_played":0}}

        # 门锁本地清空蓝牙钥匙事件
        body = {"uuid":"2fd016d7e40896ac9e278864fb50778d","time":1545186667296,"event":"bleReset"}
        self.client.basic_publish(exchange='event_exchange', routing_key='event_3', body=body)


class WebsiteUser(AmqpLocust):
    host = 'https://www.baidu.com'
    task_set = WebsiteTasks
    # min_wait = 0
    # max_wait = 0
