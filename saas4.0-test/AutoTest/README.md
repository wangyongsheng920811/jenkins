## case

- 按模块创建目录，存放测试用例py文件
- 测试用例文件名必须为test_*.py

## common

- 存放公共方法等
- common.py 公共方法
- HTMLTestRunner_PY3.py html格式测试报告工具
- my_ddt.py 重写的ddt数据驱动

## conf

- 配置信息
- conf.ini 不同环境地址以及账号密码等

## data

- 测试用例数据，json格式

- 必须与case目录结构相同且文件名相同，如case里登陆用例路径为case/login/test_login.py，则该用例的测试数据为data/login/test_login.json

- 在json文件中:

  - 第一级key值必须和对应的测试用例方法同名且必须一一对应
  - 必填字段：
    - path 接口地址
    - method 请求方法
    - check_res_code 响应码
    - check_res_data 响应数据
  - 最里层json为实际case数据

  

  

- 通用用例场景及用法：以角色模块为例，当所有用例都是只检测响应码或响应字段时，则只写一个case，对应的case和data如下：

  ```python
  @ddt
  class Setting(unittest.TestCase):
      '''设置管理-角色权限'''
  
      @file_data(common_test=1)
      def test_common(self, payload):
          '''通用测试'''
          Common.check(self, payload)
  
  ```

  ```json
  {
      "test_001_permissions_list": {
          "path": "/v1/auth/permissions",
          
          "test_common": {
              "desc": "显示权限列表接口可用性",
              "method": "get",
              "check_res_code": "00",
              "check_res_data": null
          }
      },
      
      "test_002_get_all_roles": {
          "path": "/v1/auth/roles/all",
          
          "test_common": {
              "desc": "获取商户所有角色",
              "method": "get",
              "check_res_code": "00",
              "check_res_data": null
          }
      },
      
      "test_003_permissions_by_id": {
          "path": "/v1/auth/roles/8c662a6f-18a9-4894-b68d-c6ff71ee2b3a/permissions",
          
          "test_common": {
              "desc": "根据id查询角色超管对应权限",
              "method": "get",
              "check_res_code": "00",
              "check_res_data": null
          }
      },
      
      "test_004_add_role": {
          "path": "/v1/auth/roles",
          
          "test_common_1": {
              "desc": "新增未有角色",
              "method": "post",
              "params": {
                  "name": "AutoTest",
                  "roleIds": [],
                  "permissionIds": []
              },
              "check_res_code": "00",
              "check_res_data": "res.json().get('data').get('id') != None"
          },
          
          "test_common_2": {
              "desc": "新增已有角色",
              "method": "post",
              "params": {
                  "name": "AutoTest",
                  "roleIds": [],
                  "permissionIds": []
              },
              "check_res_code": "51404",
              "check_res_data": "res.json().get('message') == '角色名重复'"
          }
      }
  }
  ```

  

## run.py

- 启动入口
- python run.py 或python run.py test 代表线下环境
- python run.py prod 代表线上环境