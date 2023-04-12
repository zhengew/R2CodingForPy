# -*- coding:utf-8 -*-
# 开发人员: erwei.zheng
# 开发时间: 2023/3/5 15:33
# 文件名称: 4.列表元素修改.py

l1 = ['test1', 'test2', 'test3', 'test4']

# 1.根据索引位置改
l1[-1] = "test5"
print(l1) # ['test1', 'test2', 'test3', 'test5']

# 2.按照切片改值(可迭代对象迭代着追加)
l2 = l1.copy()
print(l2) # ['test1', 'test2', 'test3', 'test5']
l2[1:len(l2)-1] = "123456"
print(l2) # ['test1', '1', '2', '3', '4', '5', '6', 'test5']

# 3.按照切片步长改（必须一一对应）
l3 = l1.copy() # ['test1', 'test2', 'test3', 'test5']
print(l3)

l3[1::2] = "AB"
print(l3) # ['test1', 'A', 'test3', 'B']
