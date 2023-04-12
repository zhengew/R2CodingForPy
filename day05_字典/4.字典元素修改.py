# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/5 19:24
# 文件名称: 4.字典元素修改.py

"""
目标：字典修改
方式一：通过key改
"""

dict1 = {"name": "test", "age": 20}

# 1.通过键修改对应value
dict1["age"] = 21
print(dict1) # {'name': 'test', 'age': 21}

# 2.update方法，迭代追加
dict1.update([("name", "alex"), ("age", 25)])
print(dict1) # {'name': 'alex', 'age': 25}

dict3 = {"name": "lucy", "age": 19}
dict1.update(dict3)
print(dict1) # {'name': 'lucy', 'age': 19}

