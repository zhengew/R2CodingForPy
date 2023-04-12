
# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/5 16:54
# 文件名称: 2.字段创建方式.py

"""
目标：学习创建字典的方式
"""
# 1.空字典
dictNull = dict()
print(type(dictNull)) # <class 'dict'>
print(dictNull) # {}

# 2.静态初始
# 方式一
dict1 = {1:"query", 2:"update", 3:"delete"}
print(dict1) # {1: 'query', 2: 'update', 3: 'delete'}

# 方式二
dict2 = dict(((1, "query"), (2, "update"), (3, "delete")))
print(dict2) # {1: 'query', 2: 'update', 3: 'delete'}

# 方式三 没什么用，=号左边还必须是字符串
dict3 = dict(one=1, two=2, three = 3)
print(dict3) # {'one': 1, 'two': 2, 'three': 3}

# 方式四
dict4 = dict({1:"query", 2:"update", 3:"delete"})
print(dict4) # {1: 'query', 2: 'update', 3: 'delete'}

# 方式五 zip拆包
dict5 = dict(zip([1, 2, 3], ["query", "update", "delete"])) # {1: 'query', 2: 'update', 3: 'delete'}
print(dict5)

# 方式六 字典推导式, 利用列表遍历及元组的拆包
dict6 = {k : v for k, v in [(1, "query"), (2, "update"), (3, "delete")]}
print(dict6)

# 方式七 fromkeys
didt7 = dict.fromkeys("123", "初始值")
print(didt7) # {'1': '初始值', '2': '初始值', '3': '初始值'}



