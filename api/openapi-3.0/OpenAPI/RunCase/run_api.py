import sys, os, copy
paths = os.path.split(os.path.realpath(__file__))[0]
params_file_path = os.path.join(paths + '/../RunCase/')
os.chdir(paths)
sys.path.append('../../../openapi-3.0')
sys.path.append('../../../Test')
if 'win' in sys.platform:
    cases = ['case_grade=1', 'openapi=3.0', 'onoffline=on', 'platform=openapi', 'custom=self', 'openapi_*.py']
elif 'linux' in sys.platform:
    cases = sys.argv[1:]
else:
    cases = []
print("param : %s" % cases)
cases_ = copy.deepcopy(cases)

# 写入参数
with open(params_file_path+'param.cfg', 'w') as fl:
    flag_openapi = False
    flag_onoffline = False
    flag_platform = False
    flag_custom = False
    for tmp in cases_:
        if tmp.find("openapi=") != -1:
            fl.write(tmp+'\n')
            flag_openapi = True
            cases.remove(tmp)
            continue
        if tmp.find("onoffline=") != -1:
            fl.write(tmp+'\n')
            flag_onoffline = True
            cases.remove(tmp)
            continue
        if tmp.find("platform=") != -1:
            fl.write(tmp+'\n')
            flag_platform = True
            cases.remove(tmp)
        if tmp.find("custom=") != -1:
            fl.write(tmp+'\n')
            flag_custom = True
            cases.remove(tmp)
# 读取参数
# with open(params_file_path+'param.cfg', 'r') as fl:
#     content = fl.read()
# 判断文件中参数是否合法
if not flag_openapi:
    with open(params_file_path+'param.cfg', 'a') as fl:
        fl.write("openapi=3.0\n")
if not flag_onoffline:
    with open(params_file_path + 'param.cfg', 'a') as fl:
        fl.write('onoffline=off\n')
if not flag_platform:
    with open(params_file_path + 'param.cfg', 'a') as fl:
        fl.write('platform=openapi\n')
if not flag_custom:
    with open(params_file_path + 'param.cfg', 'a') as fl:
        fl.write('custom=self\n')
# 展示配置文件
with open(params_file_path+'param.cfg', 'r') as fl:
    param_config = fl.read()
    print(param_config)

# 获取当前线上线下环境    生成报告时用到
if param_config.find('onoffline=on') != -1:
    onoff_config = ' 线上 '
elif param_config.find('onoffline=off') != -1:
    onoff_config = ' 线下 '
elif param_config.find('onoffline=qa-off') != -1:
    onoff_config = ' 线下-qa '
else:
    onoff_config = ' 线下 '

from OpenAPI.Lib.send_email import *
from OpenAPI.Lib.add_case import *
from OpenAPI.Lib.run_case import *
from OpenAPI.RunCase.init import *


def get_run_and_email(cases=[]):
    # 初始化参数
    # 默认只执行第一条用例
    case_grade = 1
    for tmp in cases_:
        if tmp.find("case_grade=") != -1:
            case_grade = tmp.split("case_grade=")[-1]
            cases.remove(tmp)

    # 写入执get_case_grade行用例的编号
    get_case_grade(flag='w', case_num=case_grade)

    # 清空log文件
    empty_log('http.log')
    print("cases: %s" % cases)

    # 如果cases不为空执行用例
    if cases != []:
        # 执行和生成报告
        fl = open(report_path, 'wb')
        runner = HTMLTestRunner(stream=fl, verbosity=2,
                                title='云丁 SaaS ' + param_config[
                                                   param_config.find('openapi=') + 8:param_config.find('openapi=') + 11] + onoff_config + ' OpenAPI 自动化测试报告',
                                description='测试人：李飞超').run(find_case(cases))
        fl.close()
        # 发送报告
        send_mail()
    # 清除配置文件
    operate_param_file(operate='d')
    get_case_grade(flag='d')
    return


get_run_and_email(cases)

