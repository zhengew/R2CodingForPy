# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 多继承中super通过mro顺序找当前类的父类.py
# @datatime: 2023/4/7 21:05

"""
目标: 理解super在多继承中的用法
在多继承中，super是按照mro顺序找当前类的下一个父类
在多继承中，通过 类名.mro()
"""

class A(object):
    def func(self):
        print('in func_A')
class B(A):
    def func(self):
        super().func()
        print('in func_B')

class C(A):
    def func(self):
        super(C, self).func()
        print('in func_C')

class D(B, C):
    def func(self):
        super().func()
        print('in func_D')

if __name__ == '__main__':
    d = D()
    d.func()
    print(D.mro())
"""
in func_A
in func_C
in func_B
in func_D
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
"""