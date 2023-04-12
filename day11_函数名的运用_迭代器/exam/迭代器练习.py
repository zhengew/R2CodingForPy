# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/11 16:53
# 文件名称: 迭代器练习.py

with open('file1', mode='w', encoding='utf-8') as f1:
    print('__iter__' in dir(f1) and '__next__' in dir(f1)) # True


s = 'abdefg'
print('__next__' in dir(s)) # False

l1 = [11, 22, 33, 44, 55]
obj = l1.__iter__()
try:
    print(obj.__next__())
    print(obj.__next__())
    print(obj.__next__())
    print(obj.__next__())
    print(obj.__next__())
    print(obj.__next__())
except Exception:
    print("StopIteration")
