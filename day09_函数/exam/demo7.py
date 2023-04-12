# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/8 07:36
# 文件名称: demo7.py

# 8.写函数，此函数只接收一个参数且此参数必须是列表数据类型，此函数完成的功能是返回给调用者一个字典，
# 此字典的键值对为此列表的索引及对应的元素。例如传入的列表为：[11,22,33] 返回的字典为 {0:11,1:22,2:33}。

def func(data: list):
    result = dict()
    if type(data) == list:
        for k, v in enumerate(data):
            result[k] = v
    return result


print(func([11, 22, 33, 44]))
