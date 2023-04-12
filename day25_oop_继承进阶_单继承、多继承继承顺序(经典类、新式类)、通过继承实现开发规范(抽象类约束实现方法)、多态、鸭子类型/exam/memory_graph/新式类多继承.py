# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 新式类多继承.py
# @datatime: 2023/4/5 10:13

"""
目标: 理解新式类多继承内存图: 广度优先
"""
class A(object):
    def func(self): pass
    def func2(self): print(A.__name__)
class B(A):
    def func(self): pass
class C(A):
    def func(self): pass
class D(B, C):
    def func(self): pass

d = D()
d.func2() # A