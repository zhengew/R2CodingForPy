# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 经典类多继承.py
# @datatime: 2023/4/5 09:42
"""
目标：理解pyton2经典类多继承的内存图
"""
class A:
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

