#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import csv
import time
import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

def csv_to_table(file):
    with open(file, 'r', encoding="utf-8") as f:
        datas = list(csv.reader(f))
        table = ''
        for i in datas:
            table += '<tr>'
            for j in i:
                table += '<td>' + j + '</td>'
            table += '</tr>'
        return table

def json_to_js(server_name):
    print(server_name)
    instance_id = ''
    if 'saasapi' in server_name:
        instance_id = 'i-bp1cxjakqgruiklj6r42'
    if 'openapi' in server_name:
        instance_id = 'i-bp1hqj94tqd6rehk40wa'
    instance_str = {"instanceId": instance_id}
    end_time = time.time() + 15
    start_time = end_time - 60 * 10 -15
    end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))
    start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))
    client = AcsClient("LTAIS2gayXtUpGes", "2dz2N0LVTKA8cvP38YhKJf44N77nq3", "cn-hangzhou")
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('metrics.aliyuncs.com')
    request.set_method('POST')
    request.set_version('2018-03-08')
    request.set_action_name('QueryMetricData')
    request.add_query_param('Metric', 'cpu_total')
    request.add_query_param('Project', 'acs_ecs_dashboard')
    request.add_query_param('StartTime', start_time)
    request.add_query_param('EndTime', end_time)
    request.add_query_param('Dimensions', str(instance_str))
    time.sleep(30)
    response = client.do_action(request)
    cpu_data = json.loads(response.decode('utf-8')).get('Datapoints')
    cpu_data = json.loads(cpu_data)
    request.add_query_param('Metric', 'memory_usedutilization')
    response = client.do_action(request)
    memory_data = json.loads(response.decode('utf-8')).get('Datapoints')
    memory_data = json.loads(memory_data)

    times = [i.get('timestamp') for i in cpu_data]
    times = [time.strftime('%H:%M:%S', time.localtime(i/1000)) for i in times]
    cpu_list = [i.get('Average') for i in cpu_data]
    memory_list = [i.get('Average') for i in memory_data]

    js_str = """
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: %s},
        yAxis: {type: 'value'},
        series: [{name:'CPU使用率', type:'line', data:%s},
        {name:'内存使用率', type:'line', data:%s},
        """ % (times, cpu_list, memory_list)
    
    return js_str

def write_html(table, js_str):
    html = """
        <!DOCTYPE html>
        <html style="height: 100%">
            <head>
                <meta charset="utf-8">
                <style type="text/css">
                    #cpu{margin: auto;}
                    #locust{margin:60px 0}
                </style>
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
                <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/echarts.min.js"></script>
                <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts-gl/echarts-gl.min.js"></script>
                <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts-stat/ecStat.min.js"></script>
                <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/extension/dataTool.min.js"></script>
                <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/china.js"></script>
                <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/map/js/world.js"></script>
                <script type="text/javascript" src="https://api.map.baidu.com/api?v=2.0&ak=ZUONbpqGBsYGXNIYHicvbAbM"></script>
                <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/echarts/extension/bmap.min.js"></script>
                <script type="text/javascript" src="http://echarts.baidu.com/gallery/vendors/simplex.js"></script>
            </head>
            <body style="height: 90%; width:90%;margin: auto">
                <div id="locust" >
                    <table class="table table-hover"> """ + table + """
                    </table>
                </div>
                <div id="cpu" style="height: 60%"></div>
                <script type="text/javascript" charset="utf-8">
                    function create(dom)
                        {
                            var myChart = echarts.init(dom);
                            window.onresize = myChart.resize;
                            var app = {};
                            option = null;
                            option = {
                                title: {text: 'CPU和内存使用率'},
                                tooltip: {trigger: 'axis'},
                                legend: {data:['CPU使用率','内存使用率']},
                                grid: {left: '3%', right: '4%', bottom: '3%', containLabel: true},
                                toolbox: {feature: {saveAsImage: {}}},
                                """ + js_str + """
                            ]};;
                    if (option && typeof option === "object") {myChart.setOption(option, true);}}
                    var dom1 = document.getElementById("cpu");
                    create(dom1)
               </script>
           </body>
        </html> """
    with open('Report.html', 'w', encoding="utf-8") as f:
        f.write(html)

table = csv_to_table('report_requests.csv')
js_str = json_to_js(sys.argv[1])
write_html(table, js_str)