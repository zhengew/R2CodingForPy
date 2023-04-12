# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/5 21:36
# 文件名称: 1.id == is 区别.py

"""
id : 内存地址
is : 比较内存地址
== : 值比较
"""
import copy

name1 = [1, 2, 3]
name2 = [1, 2, 3]

print(id(name1)) # 4528831296
print(id(name2)) # 4528831296

print(name1 == name2) # True
print(name1 is name2) # False

# 浅拷贝
name3 = name1.copy()
print(name3 is name1) # False
print(id(name3), id(name1)) # 4495838592 4497632512

# 深拷贝
name4 = copy.deepcopy(name1)
print(name1 == name4) # True
print(name4 is name1) # False

