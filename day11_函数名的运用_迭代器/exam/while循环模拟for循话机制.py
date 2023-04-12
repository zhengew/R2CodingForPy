# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/11 17:32
# 文件名称: while循环模拟for循话机制.py

l1 = [1, 2 ,3, 4, 5 ,6]
obj = l1.__iter__()
while True:
    try:
        print(obj.__next__(), end=" ")
    except StopIteration:
        break

# 1 2 3 4 5 6