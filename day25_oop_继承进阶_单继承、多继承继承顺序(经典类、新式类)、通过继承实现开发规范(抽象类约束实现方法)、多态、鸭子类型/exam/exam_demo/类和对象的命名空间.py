# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 类和对象的命名空间.py
# @datatime: 2023/4/5 20:12

"""
目标:掌握类和对象的命名空间
"""

# 例1
# class A:
#     def func(self):print('a')
# class B(A):pass
# b = B()
# b.func()   # a  自己没有用父类的

# 例2
# class A:
#     def func(self):print('a')
# class B(A):
#     def func(self):
#         A.func(self)
#         print('b')
# b = B()
# b.func()     # a,b  先执行B.func,调用了A.func打印a,然后回到B.func打印b

# 例3
# class A:
#     def func(self):print('a')
# class B(A):
#     def func(self):
#         print('b')
#         A.func(self)
# b = B()
# b.func()     # b,a

# 例4
# class A:
#     lst = []
#     def func(self):
#         self.lst.append(1)
# class B(A):
#     lst = []
#     def func(self):
#         self.lst.append(2)
# b = B()
# b.func()
# print(A.lst)   # []
# print(B.lst)   #  [2]

# 例5
# class A:
#     lst = []
#     def func(self):
#         self.lst.append(1)
# class B(A):
#     def func(self):
#         self.lst.append(2)
# b = B()
# b.func()
# print(A.lst)   # [2]
# print(B.lst)   # [2]

# 例6
class A:
    lst = []
    def __init__(self):
        self.lst = []
    def func(self):
        self.lst.append(1)
class B(A):
    def __init__(self):
        self.lst= []
    def func(self):
        self.lst.append(2)
b = B()
b.func()
print(A.lst)  # []
print(B.lst)  # []
