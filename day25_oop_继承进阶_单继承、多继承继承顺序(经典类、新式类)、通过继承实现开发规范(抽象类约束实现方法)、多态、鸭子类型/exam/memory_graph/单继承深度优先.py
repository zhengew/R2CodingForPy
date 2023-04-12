# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 单继承广度优先.py
# @datatime: 2023/4/5 09:20

# 单继承 深度优先
class A(object):
    def func(self): pass
    def func2(self):pass
class B(A):
    def func(self): pass
class C(B):
    def func(self): pass
class D(C):
    def func(self): pass

if __name__ == '__main__':
    d = D()
    d.func2() # 深度优先
