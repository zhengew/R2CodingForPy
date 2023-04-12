# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/5 20:08
# 文件名称: 7.字典的其他操作.py

"""
目标：字典的其他操作
1.直接用变量接收字典的key,拆包
2.keys(), values(), items() 获取的假列表，可以通过list强转成列表
3.循话遍历时拆包
4.字典循环时默认遍历的key
"""

# 1. items() 获取的值拆包
dict1 = {"name": "alex", "age": 18}
k1, k2 = dict1
print(k1, k2) # name age

# 2. list强制转换
key_list = list(dict1.keys())
print(type(key_list)) # <class 'list'>
print(key_list) # ['name', 'age']

value_List = list(dict1.values())
print(value_List) # ['alex', 18]

key_value_list = list(dict1.items())
print(key_value_list) # [('name', 'alex'), ('age', 18)]

# 3.循话遍历时拆包
for k, v in dict1.items(): # Key:age, Value:18
    print(f"Key:{k}, Value:{v}")

# 4.字典循环时默认遍历的key
for key in dict1:
    print(key)

