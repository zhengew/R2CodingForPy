# -*- coding: utf-8 -*-
# @author: erwei.zheng
# @file: 1.被property装饰的方法不能有参数.py
# @datatime: 2023/4/8 09:43

"""
目标：理解@property装饰器
1.被装饰的方法，不能有参数
"""
from math import pi
class Circle(object):
    def __init__(self, r):
        self.r = r

    @property
    def area(self, num):
        return pi * self.r**2

if __name__ == '__main__':
    c = Circle(10)
    print(c.area)

    # TypeError: Circle.area() missing 1 required positional argument: 'num'
