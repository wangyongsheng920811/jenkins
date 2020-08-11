from OpenAPI.Lib.MyHead import *


class GetDataList(object):
    def __init__(self, right_data, wrong_data, random_flag, data_name, send_way, iswrite=False):
        self.right_data = right_data    # 正确的用例
        self.wrong_data = wrong_data    # 错误的用例
        self.random_flag = random_flag  # 需要随机处理的字段
        self.data_name = data_name+'-'+operate_param_file(flag='platform')  # 用例名称
        self.API_name = data_name   # 接口名称
        self.send_way = send_way    # 接口发送方式
        self.iswrite = iswrite      # 是否打印log
        self.dispensable_list = []
        self.option_dict = {}
        # # 非必须元素
        # if len(self.right_data) > 1:
        #     if 'dispensable' in self.right_data[len(self.right_data) - 1]:
        #         self.dispensable_list = copy.deepcopy(self.right_data[len(self.right_data) - 1]['dispensable'])
        #         del self.right_data[len(self.right_data) - 1]
        #     else:
        #         self.dispensable_list = []
        # else:
        #     self.dispensable_list = []
        if len(self.right_data) > 1:
            right_data_tmp = copy.deepcopy(self.right_data)
            for i in range(len(right_data_tmp)):
                # 非必须元素
                if 'dispensable' in right_data_tmp[i].keys() and not self.dispensable_list:
                    self.dispensable_list = copy.deepcopy(right_data_tmp[i]['dispensable'])
                    del self.right_data[self.right_data.index(right_data_tmp[i])]
                    continue
                # 可选参数
                if 'option' in right_data_tmp[i].keys() and not self.option_dict:
                    self.option_dict = copy.deepcopy(right_data_tmp[i]['option'])
                    del self.right_data[self.right_data.index(right_data_tmp[i])]
                    continue
        else:
            self.dispensable_list = []
            self.option_dict = {}

    # 获取正确的参数列表
    def get_right_data_list(self):
        right_data_tmp = copy.deepcopy(self.right_data)
        data_list = []
        for dict_tmp in right_data_tmp:
            data_list.append([self.data_name + '-S-全部参数', dict_tmp])
            dict_tmp_tmp2 = copy.deepcopy(dict_tmp)
            if self.option_dict:
                for option_element in self.option_dict.keys():
                    for option_element_ele in self.option_dict[option_element]:
                        dict_tmp_tmp3 = copy.deepcopy(dict_tmp)
                        dict_tmp_tmp3[option_element] = option_element_ele
                        data_list.append([self.data_name + '-S-' + str(option_element) + '=' + str(option_element_ele), dict_tmp_tmp3])
            if self.dispensable_list:
                for element in self.dispensable_list:
                    dict_tmp_tmp = copy.deepcopy(dict_tmp)
                    # 删除一个非必须元素
                    del dict_tmp_tmp[element]
                    if len(self.dispensable_list) != 1:
                        data_list.append([self.data_name + '-S-缺失' + str(element), dict_tmp_tmp])
                    # 删除所有非必须元素
                    del dict_tmp_tmp2[element]
                if (('uuid' in dict_tmp and 'home_id' in dict_tmp and 'room_id' in dict_tmp) and (
                        'uuid' not in self.dispensable_list or 'room_id' not in self.dispensable_list or 'home_id' not in self.dispensable_list) and dict_tmp_tmp2) or (
                        'uuid' not in dict_tmp and 'home_id' not in dict_tmp and 'room_id' not in dict_tmp):
                    data_list.append([self.data_name + '-S-缺失全部非必须', dict_tmp_tmp2])
        if self.random_flag:
            for i in range(len(data_list)):
                for tmp_flag in self.random_flag:
                    if tmp_flag in data_list[i][1].keys():
                        data_list[i][1][tmp_flag] += "_right_" + get_string(4) + "_" + str(i)
        if self.iswrite:
            write_file(data_list, 'w', self.data_name + "_right")
        return data_list

    # 针对包含home/room/uuid的接口
    def get_hru_data_list(self):
        flag_list = ['home_id', 'room_id', 'uuid']
        right_data_tmp = copy.deepcopy(self.right_data[0])
        wrong_data_tmp = copy.deepcopy(self.wrong_data)
        # 如果正确列表里没有home_id、room_id和uuid，直接返回空列表
        if not ('home_id' in right_data_tmp and 'room_id' in right_data_tmp and 'uuid' in right_data_tmp):
            return []
        data_list = []
        # 去除错误参数里除了home_id、room_id、uuid之外的参数
        for element in right_data_tmp:
            if element not in flag_list:
                del wrong_data_tmp[element]
        # 全部都正确的情况
        data_list.append([self.data_name, right_data_tmp])
        # 遍历所有正确元素 3元素情况
        for element_right in right_data_tmp:
            # 如果非home_id、room_id、uuid，跳过
            if element_right not in flag_list:
                continue
            # 遍历所有错误元素
            for element_wrong in wrong_data_tmp:
                # 如果错误元素与当前正确元素相同，跳过
                if element_right == element_wrong:
                    continue
                # 遍历当前错误元素的所有可能值
                for wrong_ele_tmp in wrong_data_tmp[element_wrong]:
                    riht_dict_tmp = copy.deepcopy(right_data_tmp)
                    riht_dict_tmp[element_wrong] = wrong_ele_tmp
                    if [self.data_name, riht_dict_tmp] not in data_list:
                        data_list.append([self.data_name, riht_dict_tmp])
        # 遍历所有正确元素 2元素情况
        for element_right in right_data_tmp:
            # 如果非home_id、room_id、uuid，跳过
            if element_right not in flag_list:
                continue
            for element_wrong in wrong_data_tmp:
                # 如果错误元素与当前正确元素相同，跳过
                if element_right == element_wrong:
                    continue
                # 去除当前错误元素的情况
                right_dict = copy.deepcopy(right_data_tmp)
                del right_dict[element_wrong]
                if [self.data_name, right_dict] not in data_list:
                    data_list.append([self.data_name, right_dict])
                right_dict2 = copy.deepcopy(right_dict)
                for element_right2 in right_dict2:
                    if element_right == element_right2:
                        continue
                    for element_wrong2 in wrong_data_tmp:
                        if element_wrong2 == element_right or element_wrong2 == element_wrong:
                            continue
                        # 遍历当前错误元素的所有可能值
                        for wrong_ele_tmp2 in wrong_data_tmp[element_wrong2]:
                            right_dict_tmp2 = copy.deepcopy(right_dict2)
                            right_dict_tmp2[element_wrong2] = wrong_ele_tmp2
                            if [self.data_name, right_dict_tmp2] not in data_list:
                                data_list.append([self.data_name, right_dict_tmp2])
        # 遍历所有正确元素 1元素情况
        for element_right in right_data_tmp:
            # 如果非home_id、room_id、uuid，跳过
            if element_right not in flag_list:
                continue
            right_dict3 = copy.deepcopy(right_data_tmp)
            for element_wrong in wrong_data_tmp:
                # 如果错误元素与当前正确元素不相同，删除，否则保留
                if element_wrong != element_right:
                    del right_dict3[element_wrong]
            if [self.data_name, right_dict3] not in data_list:
                data_list.append([self.data_name, right_dict3])
            # 遍历当前错误元素的所有可能值
            for wrong_ele_tmp3 in wrong_data_tmp[element_right]:
                right_dict_tmp3 = copy.deepcopy(right_dict3)
                right_dict_tmp3[element_right] = wrong_ele_tmp3
                if [self.data_name, right_dict_tmp3] not in data_list:
                    data_list.append([self.data_name, right_dict_tmp3])
        return data_list

    # 判断包含home/room/uuid的用例的正确与否，修改用例名称
    def check_hru(self, data_list=[]):
        for one_case in data_list:
            if not ('home_id' in self.right_data[0] and 'room_id' in self.right_data[0] and 'uuid' in self.right_data[0]):
                return []
            # 存在uuid的情况，只要uuid正确，结果就正确
            if 'uuid' in one_case[1]:
                if self.right_data[0]['uuid'] == one_case[1]['uuid']:
                    one_case[0] += '-S-hru-uuid正确'
                else:
                    one_case[0] += '-F-hru-错误元素uuid=' + str(one_case[1]['uuid'])
                continue
            # 只有home_id和room_id的情况，两者都正确，结果才正确
            if 'home_id' in one_case[1] and 'room_id' in one_case[1]:
                if self.right_data[0]['home_id'] == one_case[1]['home_id'] and self.right_data[0]['room_id'] == one_case[1]['room_id']:
                    one_case[0] += '-S-hru-只有正确的home_id+room_id'
                else:
                    one_case[0] += '-F-hru-错误元素home_id=' + str(one_case[1]['home_id']) + ',' + 'room_id=' + str(one_case[1]['room_id'])
                continue
            # 只有一个元素的情况
            one_case_copy = copy.deepcopy(one_case[1])
            for element in one_case[1]:
                if element not in ['home_id', 'room_id', 'uuid']:
                    del one_case_copy[element]
            if len(one_case_copy) == 1:
                for tmp in one_case_copy:
                    if self.right_data[0][tmp] == one_case[1][tmp]:
                        one_case[0] += '-S-hru-只存在正确的' + tmp
                    else:
                        one_case[0] += '-F-hru-只存在错误的' + tmp + '=' + str(one_case[1][tmp])
        return data_list

    # 获取错误的参数列表
    def get_wrong_data_list(self):
        right_data_tmp = copy.deepcopy(self.right_data)
        data_list = []
        for dict_tmp in right_data_tmp:
            # 缺少某一个必要元素
            for element in dict_tmp:
                if element in self.dispensable_list:
                    continue
                dict_tmp_tmp = copy.deepcopy(dict_tmp)
                del dict_tmp_tmp[element]
                data_list.append([self.data_name + '-F-缺失' + str(element), dict_tmp_tmp])
            # 其中某个元素错误
            for wrong_element in self.wrong_data:
                for element in self.wrong_data[wrong_element]:
                    dict_tmp_tmp = copy.deepcopy(dict_tmp)
                    dict_tmp_tmp[wrong_element] = element
                    data_list.append([self.data_name + '-F-错误元素' + wrong_element + '=' + str(element), dict_tmp_tmp])
        if self.random_flag:
            for i in range(len(data_list)):
                for tmp_flag in self.random_flag:
                    if tmp_flag in data_list[i][1].keys():
                        if tmp_flag in self.wrong_data.keys():
                            if data_list[i][1][tmp_flag] in self.wrong_data[tmp_flag]:
                                continue
                        data_list[i][1][tmp_flag] += "_wrong_" + get_string(4) + "_" + str(i)
        if self.iswrite:
            write_file(data_list, 'w', self.data_name + "_wrong")
        return data_list

    # 获取http指令
    def get_http_cmd(self, name, method, param, check=[], do=-1):
        do_ = 0
        http_cmd = []
        if len(param) > len(check):
            for k in range(len(param)):
                if '-S-' in param[k][0]:
                    for j in range(len(param)-len(check)):
                        check.append(check[0])
                elif '-F-' in param[k][0]:
                    for j in range(len(param)-len(check)):
                        check.append(14001)
        for i in range(len(param)):
            if do == -1:
                if '-S-' in param[i][0]:
                    do_ = 0
                elif '-F-' in param[i][0]:
                    do_ = 1
            else:
                do_ = do
            if len(check) != 1:
                one_http_cmd = [name, param[i][0], method, param[i][1], check[i], do_]
            else:
                one_http_cmd = [name, param[i][0], method, param[i][1], check[0], do_]
            http_cmd.append(one_http_cmd)

        if self.iswrite:
            write_file(http_cmd, 'a', self.data_name + "_cmd")
        return http_cmd

    # 获取所有http指令
    def get_all_http_cmd(self, check_right=[], check_wrong=[]):
        right_case = self.get_right_data_list()
        wrong_case = self.get_wrong_data_list()
        hru_case = self.check_hru(self.get_hru_data_list())
        all_http_cmd = []
        # 存在home_id、room_id、uuid的情况,去重
        if hru_case:
            hru_case_copy = copy.deepcopy(hru_case)
            for i in range(len(hru_case_copy)):
                for one_right_case in right_case:
                    if hru_case_copy[i][1] == one_right_case[1]:
                        del hru_case[hru_case.index(hru_case_copy[i])]
                        break
                for one_wrong_case in wrong_case:
                    if hru_case_copy[i][1] == one_wrong_case[1]:
                        del hru_case[hru_case.index(hru_case_copy[i])]
                        break
            for tmp in hru_case:
                if '-S-' in tmp[0]:
                    right_case.append(tmp)
                    continue
                if '-F-' in tmp[0]:
                    wrong_case.append(tmp)
        for one_right_http_cmd in self.get_http_cmd(self.API_name, self.send_way, right_case, check_right):
            all_http_cmd.append(one_right_http_cmd)
        for one_wrong_http_cmd in self.get_http_cmd(self.API_name, self.send_way, wrong_case, check_wrong):
            all_http_cmd.append(one_wrong_http_cmd)
        return all_http_cmd


# right_list = [{'home_id': 'home_id_xxx', 'room_id': 'room_id_xxx', 'uuid': 'uuid_xxx', 'other': 'other_xxx'}, {'dispensable': ['home_id', 'room_id', 'uuid']},
#               {'option': {'other': ['xxoo']}}]
# wrong_list = {'home_id': [True], 'room_id': [True], 'uuid': [True], 'other': ['xxx', True]}

# right_list = [{'a': 'a', 'b': 'b', 'c': 'c'}, {'dispensable': ['a', 'b']}, {'option': {'a': [1]}}]
# wrong_list = {'a': [True], 'b': [True], 'c': [True], 'd': ['xxx', True]}
#
# test_class = GetDataList(right_list, wrong_list, [], 'hru_test', 'get')
# for tmp in test_class.get_all_http_cmd([0], [14001]):
#     print(tmp)

