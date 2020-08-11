import sys, os

# 添加系统路径
sys.path.append(os.path.split(os.path.realpath(__file__))[0] + '/../../')
sys.path.append(os.path.split(os.path.realpath(__file__))[0] + '/../../../Test')
from API_CG.lib.global_var import *

set_value('environment', sys.argv[-1])  # 从执行语句中获取environment并设置为全局变量
from API_CG.lib.common_func import *  # 导入common_func(根据environment的值初始化config)

if __name__ == '__main__':
    file_names = sys.argv[1:]  # 从执行语句中获取装载测试用例的脚本名(支持正则表达式)
    # file_names = ['checklist_*']  # 调试时指定执行脚本名称
    print_write('执行参数:\t', sys.argv, '\n测试环境:\t', config.saas3_api)
    get_run(file_names=file_names)  # 将所有测试用例添加到测试套件中并执行
