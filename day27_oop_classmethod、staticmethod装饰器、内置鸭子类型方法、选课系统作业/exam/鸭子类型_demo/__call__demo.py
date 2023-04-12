# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: __call__demo.py
# @datatime: 2023/4/11 21:02

"""
目标：理解常见鸭子类型(魔术方法)
1.__call__  判断一个对象是否可调用
"""
class A(object):
    def __call__(self, *args, **kwargs):
        print('in A')
class B(object):
    pass

if __name__ == '__main__':
    a1 = A()
    print(callable(a1)) # True
    A()() # in A

    b1 = B()
    print(callable(b1)) # False