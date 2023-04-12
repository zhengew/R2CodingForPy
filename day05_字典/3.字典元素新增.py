# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/5 17:14
# 文件名称: 3.字典元素新增.py

"""
字典元素新增：
方式一：通过key - value 新增， 有则改之，无则加勉
方式二：setdefault 有则不改，无则增加，有返回值
"""

dict1 = dict()
# 1.通过键值对形式增加
dict1["name"] = "lucy"
print(dict1) # {'name': 'lucy'}
dict1["age"] = 18
print(dict1) # {'name': 'lucy', 'age': 18}

dict1["name"] = "alex"
print(dict1) # {'name': 'alex', 'age': 18}

# 2.setdefaut 改值
dict2 = dict1.copy()
print(dict2) # {'name': 'alex', 'age': 18}
dict2.setdefault("sex", "女")
print(dict2) # {'name': 'alex', 'age': 18, 'sex': '女'}

old_value = dict2.setdefault("age", 20)
print(old_value)
print(dict2)

phone = dict2.setdefault("phone", "None")
print(phone)
print(dict2)