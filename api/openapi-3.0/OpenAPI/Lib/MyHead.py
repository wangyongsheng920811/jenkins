import sys, os, smtplib, unittest, time, ddt, requests, json, copy, random, string, datetime, inspect, random, math, re
# from selenium import webdriver
from HTMLTestRunner_PY3 import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders
from email.utils import parseaddr, formataddr
from OpenAPI.Config.all_api import *
from OpenAPI.Config.api_config import *
from OpenAPI.Config.device_home_config import *

path = os.path.split(os.path.realpath(__file__))[0]
param_path = os.path.join(path + '/../../Param/')
log_path = os.path.join(path + '/../RunCase/')
test_case_path = os.path.join(path + '/../TestCase')
test_case_new_path = os.path.join(path + '/../TestCase/news')
test_case_scenario = os.path.join(path + '/../TestCase/TestScenario')
report_path = os.path.join(path + '/../RunCase/Report.html')
key_path = os.path.join(path + '/../Config/')
# 失败重试次数
retrytimes = 0


# 操作执行用例编号
# flag=0为读取用例编号
# flag=1为写入用例编号（默认）
# case_num 为写入时的用例编号
# 执行用例等级
# 0 执行所有用例
# 1 .. n 执行第n个用例
# success 执行所有成功用例
# fail 执行所有失败用例
def get_case_grade(flag='r', case_num=0):
    if flag == 'r':
        try:
            with open(log_path+'case_grade', 'r') as fl:
                case_flag = fl.read()
        except:
            case_flag = '1'
        if case_flag == 'success' or case_flag == 'fail':
            return case_flag
        return int(case_flag)
    elif flag == 'w':
        with open(log_path+'case_grade', 'w') as fl:
            fl.write(str(case_num))
        return True
    elif flag == 'd':
        os.remove(log_path+'case_grade')
        return True
    else:
        return False


# 获取需要运行的用例
def get_cases(inputcmd=[], grade_in=None):
    if not grade_in:
        grade = get_case_grade()
    else:
        grade = grade_in
    # print(grade)
    if isinstance(grade, int):
        if grade == 0:
            return inputcmd
        else:
            if len(inputcmd) < grade or grade < 0:
                return False
            else:
                return inputcmd[(grade-1):grade]
    elif grade == 'success':
        rightcmd = []
        for tmp in inputcmd:
            if "-S-" in tmp[1]:
                rightcmd.append(tmp)
            else:
                continue
        return rightcmd
    elif grade == 'fail':
        wrongcmd = []
        for tmp in inputcmd:
            if "-F-" in tmp[1]:
                wrongcmd.append(tmp)
            else:
                continue
        return wrongcmd
    else:
        return False


# 生成的命令写入文件
def write_file(content, way='a', path_name='add_home', ifprint=False):
    file_path = param_path + path_name
    with open(file_path, way) as fl:
        for i in range(len(content)):
            fl.write(str(content[i]))
            if ifprint:
                print(i+1, '\t', content[i])
            fl.write('\n')
        # for tmp in content:
        #     fl.write(str(tmp))
        #     if ifprint:
        #         print(tmp)
        #     fl.write('\n')
    return


# 清空文件
def empty_file(path_name='add_home'):
    with open(param_path + path_name, 'w') as fl:
        fl.write("")
    return


# 打印并写log到文件
def write_print(content, isprint=True, name='http.log'):
    content = content.replace('\u2006', '')
    with open(log_path+name, 'a') as fl:
        fl.write(content)
    if isprint:
        print(content, end='')
    return


# 获取变量名
def get_variable_name(variable):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is variable]


# 格式化参数，适配form-data格式发送
def change_form_data(content={'client_id': client_id, 'client_secret': client_secret}):
    for tmp_key in content.keys():
        content[tmp_key] = (None, content[tmp_key])
    return content


# 格式化打印字典
def formatdic(dic={'a': 1}):
    if isinstance(dic, dict):
        dic_str = json.dumps(dic, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)
        return dic_str
    else:
        raise Exception('wrong input %s' % dic)


# 打印字典、列表
def write_print_list_dic(var, name='', ele=0):
    if name == '':
        try:
            if '/' in var[0][0]:
                name_tmp = var[0][0].split('/')[-1]
            else:
                name_tmp = var[0][0]
            name_ = name_tmp+'_cmd'
        except:
            name_ = 'var'
    else:
        name_ = name
    if name_ != 'var':
        empty_file(name_)
    print('**********  '+name_+'  **********')
    if ele != 0:
        ret_json = json.dumps(var[ele], sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False)
        print(ret_json)
        return
    if isinstance(var, list) or isinstance(var, dict):
        write_file(var, 'a', name_, True)
    else:
        write_file(var, 'a', name_, True)
    return


# 生成随机6位数,返回字符串
def get_numbers(length=6):
    str_tmp = ""
    while len(str_tmp) < length:
        # ch = random.randint(0, 9)
        # str_tmp += str(ch)
        ch = chr(random.randrange(ord('0'), ord('9') + 1))
        str_tmp += ch
        # 第一位不能为0，为0则重新开始生成
        if str_tmp[0] == '0':
            str_tmp = ""
    return int(str_tmp)


# 获取当前时间
def get_time(content=None, stamp=False):
    time_result = None
    # 不传，获取当前时间
    if not content:
        now = datetime.datetime.now()
        time_result = now.strftime("%Y-%m-%d %H:%M:%S")
        # 是否打印当前时间的时间戳
        if stamp:
            now_stamp = int(time.time())
            time_result += '\n' + str(now_stamp) + '\n' + str(now_stamp * 1000)
    # 传入整型，如果是毫秒（13位）先转成秒（10位）再转换成时间
    elif isinstance(content, int):
        if int(math.log10(content)+1) == 13:
            content = int(content/1000)
        dateArray = datetime.datetime.utcfromtimestamp(int(content)+28800)
        time_result = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    # 传入时间，转变为时间戳（时间格式为 2019-04-10 10:10:20）
    elif isinstance(content, str):
        time_result = str(int(datetime.datetime.strptime(content, "%Y-%m-%d %H:%M:%S").timestamp()))
        # # 转为时间数组
        # timeArray = time.strptime(content, "%Y-%m-%d %H:%M:%S")
        # # 转为时间戳
        # time_result = str(int(time.mktime(timeArray)))
        time_result = time_result + '\n' + str(int(time_result) * 1000)
    else:
        AssertionError('wrong input param: ', content)
    return time_result


# 生成随机长度字符串
def get_string(length):
    return ''.join(random.sample(string.ascii_letters + string.digits, length))


# 字典中的值相加
def get_sum(amount):
    left_amount = 0
    if isinstance(amount, dict):
        for tmp in amount:
            if isinstance(amount[tmp], int) or isinstance(amount[tmp], float):
                left_amount += amount[tmp]
    elif isinstance(amount, list):
        for tmp in amount:
            left_amount += tmp
    return round(left_amount, 2)


# print(get_time(1555558485087, stamp=True))


