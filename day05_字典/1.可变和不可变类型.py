# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/5 16:45
# 文件名称: 1.可变和不可变类型.py

"""
1.可变类型(不可哈希)：list dict set
2.不可变类型(可哈希): int str tuple boolean

hash(）: 获取hash值

3.字典中的key必须是不可变类型
"""
# print(hash([1, 2])) # TypeError: unhashable type: 'list'
# print(hash({"name": "lucy"})) # TypeError: unhashable type: 'dict'
# print(hash({1, 2, 3})) # TypeError: unhashable type: 'set'

print(hash("test1")) # -4192470874109376107

dict1 = dict(((1,"query()"), (2,"update()")))
print(dict1) # {1: 'query()', 2: 'update()'}