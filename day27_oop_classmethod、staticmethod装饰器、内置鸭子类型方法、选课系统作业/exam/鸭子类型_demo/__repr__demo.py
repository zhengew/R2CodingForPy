# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: __repr__demo.py
# @datatime: 2023/4/11 22:41

"""
目标：理解常见鸭子类型(魔术方法)
5.__repr__  打印对象
类中同时实现了__str__ 和 __repr__方法：
1. print(对象)、%s 拼接对象、str(对象)，执行 __str__方法
2. %r 拼接对象、 repr(对象)， 执行 __repr__方法
"""

class A(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return "%s" % self.width
    def __repr__(self):
        return "%s" % self.height

if __name__ == '__main__':
    a = A(width=3, height=5)
    print(a) # 3
    print("%s" % a) # 3
    print(str(a)) # 3

    print("%r" % a) # 5
    print(repr(a)) # 5