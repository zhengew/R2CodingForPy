# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/5 19:49
# 文件名称: 6.字典元素查询.py

"""
目标：字典元素查询
1.通过key查询
2.get(key, defaultValue)  通过key查询，返回key对应的value;若key不存在，则返回None或default参数

3.keys() 获取所有的key, 格式为dict_keys([key1, key2, ...])
4.values() 获取所有的value, 格式为 dict_values([value1, value2, ...])
5.items() 获取所有的键追对，格式为 dict_items([(key1, value1), (key2, value2), ...])
"""

dict1 = {'name': 'test1', 'age': 18}

# 1.通过key查询
name = dict1["name"]
print(name) # test1

# 2.get(key)  通过key查询value,可设置默认返回值
value = dict1.get("age")
print(value) # 18

none_key = dict1.get("sex")
print(none_key) # None

default_value = dict1.get("sex", "Key不存在")
print(default_value) # None

# 3.keys
dict2 = dict1.copy()
print(dict2.keys()) # dict_keys(['name', 'age'])
for i in dict2.keys():
    print(i + " ", end="") # name age
print()
print("".center(50, "*"))

# 4.values
dict3 = dict1.copy()
print(dict3.values()) # dict_values(['test1', 18])
print(list(dict3.values())) # ['test1', 18]

print("items()".center(50, "*"))
# 5.items
dict4 = dict1.copy()
print(dict4.items()) # dict_items([('name', 'test1'), ('age', 18)])
for key, value in dict4.items():
    print(key, value)

