# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 多继承乌龟模型.py
# @datatime: 2023/4/5 11:03
"""
目标:理解新式类中多继承 深度优先
经典乌龟模型
"""
class A(object):
    def func(self): pass
    def func2(self, obj): print(obj.mro())
class B(A):
    def func(self): pass
class C(A):
    def func(self): pass
class D(B):
    def func(self): pass
class E(C):
    def func(self): pass
class F(D, E):
    def func(self): pass

if __name__ == '__main__':
    f = F()
    f.func2(obj=F)
    # [<class '__main__.F'>,
    # <class '__main__.D'>,
    # <class '__main__.B'>,
    # <class '__main__.E'>,
    # <class '__main__.C'>,
    # <class '__main__.A'>,
    # <class 'object'>]
